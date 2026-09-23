"""One default decision over a response's ``data_quality`` block.

Hand-written, kept outside the generated files (0xinsider/0xinsider#16965).

``data_quality`` says how old each part of a body is; it does not say whether
that is old enough to act on, because the tolerance belongs to the caller.
``assess_data_quality`` applies one. It is a pure function over the response
and makes no request. The TypeScript SDK (``assessDataQuality``) and the Go SDK
(``AssessDataQuality``) carry the same rule under the same name.

The rule:

- A group passes only when its ``status`` is ``fresh``, it carries ``as_of``,
  and that clock is within ``max_age`` of ``now``. ``fresh`` alone means
  tracked and clocked, not current enough for you.
- ``untracked`` groups are left out of the verdict: 0xinsider does not track
  them for this subject by design. They are listed in ``untracked`` so a caller
  that needs one can refuse the body.
- Every other status fails: ``unknown`` (served, but this read cannot date it;
  never treat missing as recent), ``partial``, ``unavailable``, and any status
  this release does not recognize.
- A body with nothing to judge (every group ``untracked``) is not ok.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any
from collections.abc import Iterable, Mapping

__all__ = ["DataQualityAssessment", "DataQualityFailure", "assess_data_quality"]

_FRACTION = re.compile(r"\.(\d{6})\d+")


@dataclass(frozen=True)
class DataQualityFailure:
    group: str
    #: The group's status, or ``missing`` when a requested group is absent.
    status: str
    #: The server's reason when it gave one, otherwise why this helper failed it.
    reason: str
    as_of: str | None = None
    #: How far ``as_of`` sits before ``now``, when the group carries a clock.
    age: timedelta | None = None


@dataclass(frozen=True)
class DataQualityAssessment:
    #: True when at least one group was judged and every judged group is fresh
    #: and within ``max_age``.
    ok: bool
    #: Every judged group that did not pass, in response order.
    failing: list[DataQualityFailure] = field(default_factory=list)
    #: Groups left out of the verdict because they are ``untracked``.
    untracked: list[str] = field(default_factory=list)
    #: The oldest ``as_of`` among the judged groups that carry one.
    oldest_as_of: str | None = None
    #: Age of ``oldest_as_of`` at ``now``.
    oldest_age: timedelta | None = None


def _parse_instant(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    text = value.strip()
    if text.endswith(("Z", "z")):
        text = text[:-1] + "+00:00"
    # Python before 3.11 accepts at most six fractional digits.
    text = _FRACTION.sub(r".\1", text)
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed


def assess_data_quality(
    quality: Mapping[str, Any],
    *,
    max_age: timedelta,
    groups: Iterable[str] | None = None,
    now: datetime | None = None,
) -> DataQualityAssessment:
    """Judge a ``data_quality`` block against your own tolerance.

    ``quality`` is the block itself or any mapping that carries it under
    ``data_quality`` (a trader's ``data``, a list page).

    ``groups`` limits the verdict to the named groups; a named group the body
    does not carry fails as ``missing``, so a renamed group cannot pass
    silently.

    Example::

        trader = client.get_trader("0xabc...")
        verdict = oxinsider.assess_data_quality(trader["data"], max_age=timedelta(minutes=15))
        if not verdict.ok:
            for failure in verdict.failing:
                print(failure.group, failure.status, failure.reason)
    """
    block = quality.get("data_quality", quality) if isinstance(quality, Mapping) else quality
    if not isinstance(block, Mapping):
        raise TypeError("assess_data_quality: expected a data_quality mapping")
    if max_age < timedelta(0):
        raise ValueError("assess_data_quality: max_age must not be negative")
    at = now if now is not None else datetime.now(timezone.utc)
    if at.tzinfo is None:
        raise ValueError("assess_data_quality: now must be timezone-aware")

    entries = [entry for entry in block.get("field_groups") or [] if isinstance(entry, Mapping)]
    by_name = {entry.get("group"): entry for entry in entries}
    names = list(groups) if groups is not None else [entry.get("group") for entry in entries]

    failing: list[DataQualityFailure] = []
    untracked: list[str] = []
    judged: list[Mapping[str, Any]] = []
    for name in names:
        entry = by_name.get(name)
        if entry is None:
            failing.append(
                DataQualityFailure(group=str(name), status="missing", reason="the response carries no such group")
            )
            continue
        if entry.get("status") == "untracked":
            untracked.append(str(name))
            continue
        judged.append(entry)

    oldest: datetime | None = None
    oldest_as_of: str | None = None
    for entry in judged:
        status = str(entry.get("status"))
        as_of = entry.get("as_of")
        clock = _parse_instant(as_of)
        age = at - clock if clock is not None else None
        if clock is not None and (oldest is None or clock < oldest):
            oldest, oldest_as_of = clock, as_of
        common = {"group": str(entry.get("group")), "status": status, "as_of": as_of, "age": age}
        if status != "fresh":
            failing.append(DataQualityFailure(reason=entry.get("reason") or f"status is {status}", **common))
        elif age is None:
            failing.append(DataQualityFailure(reason="fresh but carries no as_of, so no age can be measured", **common))
        elif age > max_age:
            failing.append(DataQualityFailure(reason=f"older than max_age ({max_age})", **common))

    return DataQualityAssessment(
        ok=not failing and bool(judged),
        failing=failing,
        untracked=untracked,
        oldest_as_of=oldest_as_of,
        oldest_age=(at - oldest) if oldest is not None else None,
    )
