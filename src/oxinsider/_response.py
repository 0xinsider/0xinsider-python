"""The response beside the decoded body: status, headers, ETag and budgets.

Every operation method returns the decoded body, and that is the contract this
package keeps (#16175). What it used to discard is everything else the API
said: the `ETag` that makes the next read conditional, the request id to quote
in a bug report, and the rate-limit, monthly-quota and cost headers that let a
client see its own budget before it runs out of it.

``client.with_response.<method>(...)`` calls the same operation and returns an
``ApiResponse``: ``.data`` is exactly what the plain method returns, and
``.status`` and ``.headers`` are the rest of the answer.
``client.request(..., raw=True)`` does the same for a hand-built call.

Everything here is read from the response as received. A header the API did not
send reads ``None``, never ``0`` and never an invented default: "no quota
information on this response" and "no quota left" are different facts, and a
budget you cannot see is not a budget of zero. A header that is present but not
a number reads ``None`` too, rather than raising in the middle of a caller's
read.

The header inventory is the API's own ``Access-Control-Expose-Headers`` list
(measured 2026-09-22 on ``GET https://api.0xinsider.com/api/v1/health``), which
is what the API publishes for a browser to read.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

import httpx

BodyT = TypeVar("BodyT")


def _int(headers: httpx.Headers, name: str) -> int | None:
    raw = headers.get(name)
    if raw is None:
        return None
    try:
        return int(raw.strip())
    except ValueError:
        return None


def _float(headers: httpx.Headers, name: str) -> float | None:
    raw = headers.get(name)
    if raw is None:
        return None
    try:
        return float(raw.strip())
    except ValueError:
        return None


@dataclass(frozen=True)
class Budget:
    """One budget window as the API reported it, or ``None`` per field where it said nothing.

    ``limit`` and ``remaining`` are request counts. ``reset_at`` is a UNIX
    epoch second; ``reset_after`` is seconds from now and only the per-minute
    window publishes it (``RateLimit-Reset``), so it is ``None`` on the monthly
    quota and on the batch window. ``remaining`` of ``0`` is a real zero; a
    window the response did not describe is a ``None`` field, and a window it
    did not mention at all is a ``None`` budget.
    """

    limit: int | None = None
    remaining: int | None = None
    reset_at: int | None = None
    reset_after: float | None = None


def _budget(
    headers: httpx.Headers,
    *,
    limit: str,
    remaining: str,
    reset_at: str,
    reset_after: str | None = None,
) -> Budget | None:
    names = [limit, remaining, reset_at] + ([reset_after] if reset_after else [])
    if not any(name in headers for name in names):
        return None
    return Budget(
        limit=_int(headers, limit),
        remaining=_int(headers, remaining),
        reset_at=_int(headers, reset_at),
        reset_after=_float(headers, reset_after) if reset_after else None,
    )


@dataclass(frozen=True)
class ApiResponse(Generic[BodyT]):
    """A successful response: the decoded body, and everything else the API said.

    ``data`` carries the operation's own response type (``oxinsider.types``),
    so ``client.with_response.get_trader(...).data["data"]["grade"]`` is typed
    the same as the plain call. It is exactly what the plain operation method returns -- the decoded
    JSON for a JSON route, the text for a Markdown one, ``None`` for a ``204``
    or an empty body, and ``{"object": "not_modified", "data": None, "etag":
    ...}`` for a ``304`` answered to ``if_none_match``. ``headers`` is
    case-insensitive.
    """

    data: BodyT
    status: int
    headers: httpx.Headers

    @property
    def etag(self) -> str | None:
        """The representation's validator, to send back as ``if_none_match``.

        Present on a ``200`` from a route that supports conditional reads, and
        on the ``304`` that answers one.
        """
        return self.headers.get("etag")

    @property
    def not_modified(self) -> bool:
        """``True`` for the ``304`` answered to a conditional read: keep your cached body."""
        return self.status == 304

    @property
    def request_id(self) -> str | None:
        """``X-Request-Id``, the same id as ``meta.request_id`` in the body. Quote it in a report."""
        return self.headers.get("x-request-id")

    @property
    def retry_after(self) -> float | None:
        """``Retry-After`` in seconds, when the API asked you to wait. ``None`` when it did not."""
        return _float(self.headers, "retry-after")

    @property
    def rate_limit(self) -> Budget | None:
        """The per-minute request window, or ``None`` when the response carried none.

        ``reset_after`` is the seconds-from-now form (``RateLimit-Reset``) and
        ``reset_at`` the epoch form (``X-RateLimit-Reset``).
        """
        return _budget(
            self.headers,
            limit="x-ratelimit-limit",
            remaining="x-ratelimit-remaining",
            reset_at="x-ratelimit-reset",
            reset_after="ratelimit-reset",
        )

    @property
    def monthly_quota(self) -> Budget | None:
        """The calendar-month request quota, on an authenticated response. ``reset_after`` is always ``None``."""
        return _budget(
            self.headers,
            limit="x-monthly-quota-limit",
            remaining="x-monthly-quota-remaining",
            reset_at="x-monthly-quota-reset",
        )

    @property
    def batch_rate_limit(self) -> Budget | None:
        """The batch routes' per-ITEM window, which a batch call spends `request_cost` of."""
        return _budget(
            self.headers,
            limit="x-batch-ratelimit-limit",
            remaining="x-batch-ratelimit-remaining",
            reset_at="x-batch-ratelimit-reset",
        )

    @property
    def request_cost(self) -> int | None:
        """``X-Request-Cost``: how many batch items this call charged. ``None`` off the batch routes."""
        return _int(self.headers, "x-request-cost")

    @property
    def server_timing_ms(self) -> float | None:
        """The API's own processing time from ``Server-Timing: api;dur=...``, in milliseconds.

        It is the server's time, not the round trip: the network and your own
        decoding are not in it.
        """
        raw = self.headers.get("server-timing")
        if not raw:
            return None
        for part in raw.split(","):
            fields = part.strip().split(";")
            if fields[0].strip() != "api":
                continue
            for field in fields[1:]:
                name, _, value = field.partition("=")
                if name.strip() == "dur":
                    try:
                        return float(value.strip().strip('"'))
                    except ValueError:
                        return None
        return None

    @property
    def usage_accounting(self) -> str | None:
        """``X-Usage-Accounting``: how this request was recorded against your usage ledger."""
        return self.headers.get("x-usage-accounting")

    @property
    def deprecation(self) -> str | None:
        """``Deprecation``, when the API is retiring what you called. ``Link`` carries the successor."""
        return self.headers.get("deprecation")

    @property
    def sandbox(self) -> bool:
        """``True`` when the sandbox answered: example data, never production data."""
        return self.headers.get("x-oxi-sandbox") is not None

    @property
    def content_type(self) -> str | None:
        return self.headers.get("content-type")

    def header(self, name: str, default: str | None = None) -> str | None:
        """Any other response header, by name, case-insensitively."""
        return self.headers.get(name, default)
