"""Progress-checked cursor pagination over the V1 list envelope.

Every cursor-paginated operation answers ``{"object": "list", "data": [...],
"has_more": <bool>, "next_cursor": "<str>"}`` (``ApiList`` in the API: ``object``,
``data``, ``has_more`` and ``meta`` are required, ``next_cursor`` is a string or
omitted). The walk here is a consumer of that protocol rather than a loop that
trusts whatever came back (#16191):

- A page is validated BEFORE it is handed to the caller. A response that is not
  a list envelope, or whose ``data`` is not a list, raises ``PaginationError``
  instead of finishing the walk with nothing. Before #16191 it returned as if
  the collection were an exhausted empty one, so paginating a route that answers
  a different envelope -- ``GET /api/v1/whale-trades/{id}/counterparties/executions``
  takes a ``cursor`` and answers ``object: "counterparty_analysis"`` with an
  object ``data`` -- gave zero items and no error.
- ``has_more: true`` with no usable ``next_cursor`` raises ``PaginationError``
  (``missing_cursor``). The server's own cursor builders refuse to emit that
  page, so a client seeing one is looking at a malformed response, not at the
  end of the collection.
- A ``next_cursor`` this walk already requested raises ``PaginationError``
  (``repeated_cursor``) BEFORE the duplicate request, so a self-referential or
  cyclic cursor cannot spend metered requests indefinitely. The last
  ``CURSOR_HISTORY_LIMIT`` cursors are remembered, which bounds the memory of a
  long walk; a cycle longer than that is not detected.
- ``has_more: false`` ends the walk normally whatever ``next_cursor`` says, and
  a valid empty terminal page is still a success.
- ``max_pages`` and ``max_items`` are validated before any request, and reaching
  one is a caller's choice rather than exhaustion:
  ``PaginationProgress.stopped_by`` tells the two apart and keeps the
  continuation.

Wherever a walk stops -- exhaustion, a caller bound, an early ``break``, an API
error, an expired cursor -- the last safe checkpoint survives it. Pass a
``PaginationProgress`` as ``progress=`` and read it afterwards, or recover it
from the error with ``pagination_checkpoint(error)``. Resuming from
``checkpoint.cursor`` refetches the page the walk stopped on; resuming from
``checkpoint.next_cursor`` continues past it.

The filters are captured once and reused unchanged for every page: only
``cursor`` moves, so neither a later page nor a recovery can quietly run a
different query than the one the caller asked for.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass, replace
from typing import Any

from ._errors import OxinsiderError

#: How many requested cursors one walk remembers for the repeat check. A cycle
#: longer than this is not detected; the bound keeps a long walk's memory flat
#: instead of growing it with every page.
CURSOR_HISTORY_LIMIT = 1024

#: ``PaginationProgress.stopped_by`` values.
STOP_EXHAUSTED = "exhausted"
STOP_MAX_PAGES = "max_pages"
STOP_MAX_ITEMS = "max_items"
STOP_NOT_MODIFIED = "not_modified"


@dataclass
class PaginationProgress:
    """Where a walk got to, updated as it goes.

    Pass one as ``progress=`` and read it after the loop, or recover it from a
    failure with ``pagination_checkpoint(error)``.

    ``cursor`` is what the most recent page was requested with (``None`` for the
    first page): pass it back as ``cursor=`` to refetch that page and carry on
    without losing an item. ``next_cursor`` is what that page offered next: pass
    that instead to continue past a page you have fully consumed. ``stopped_by``
    is set only when the walk ended on its own terms -- ``"exhausted"`` (the
    server said there is no more), ``"max_pages"`` or ``"max_items"`` (your
    bound, and ``next_cursor`` continues the walk), ``"not_modified"`` (a
    conditional read matched). It stays ``None`` when the walk was interrupted
    by an error or abandoned early, which is what tells a partial walk from a
    complete one.
    """

    pages_fetched: int = 0
    items_yielded: int = 0
    cursor: str | None = None
    next_cursor: str | None = None
    stopped_by: str | None = None


# Where the checkpoint of a failed walk is kept. It is an attribute on the
# error rather than a weak-keyed map, because CPython refuses a weak reference
# to a built-in exception instance (measured 2026-09-22 on 3.9.6 and 3.12.11:
# ``weakref.ref(ValueError())`` raises ``TypeError``, while a custom subclass
# is fine), so a map would have turned an ordinary ``TypeError`` out of a
# caller's method into a different error and hidden the original.
_CHECKPOINT_ATTR = "_oxinsider_pagination_checkpoint"


def pagination_checkpoint(error: BaseException) -> PaginationProgress | None:
    """The checkpoint of an error raised out of ``paginate`` or ``paginate_pages``.

    ``None`` for an error that did not come out of a walk. The snapshot is the
    walk's state at the failing page, so a rate limit, an expired cursor (the
    API's own ``BadRequestError``) or a dropped connection can be retried from
    ``checkpoint.cursor`` instead of starting again at page one::

        try:
            for trade in client.paginate("list_whale_trades", min_grade="A"):
                handle(trade)
        except oxinsider.OxinsiderError as error:
            resume = oxinsider.pagination_checkpoint(error)
            if resume is not None:
                client.paginate("list_whale_trades", min_grade="A", cursor=resume.cursor)
    """
    found = getattr(error, _CHECKPOINT_ATTR, None)
    return found if isinstance(found, PaginationProgress) else None


class PaginationError(OxinsiderError):
    """A list response broke the cursor protocol; the walk stopped before spending another request.

    ``reason`` is one of:

    - ``invalid_envelope``: the response is not a cursor-paginated list. It is
      not a JSON object, or it carries no boolean ``has_more``. Paginating an
      operation that answers a different envelope lands here.
    - ``invalid_data``: ``data`` is not a list, so the page has no items to
      yield and cannot be counted as an empty one either.
    - ``missing_cursor``: ``has_more`` is true but ``next_cursor`` is absent,
      null or empty, so there is no way to continue.
    - ``repeated_cursor``: ``next_cursor`` repeats a cursor this walk already
      requested. Raised before the duplicate request goes out.

    ``page`` is the response as received, so its contents are still available.
    ``checkpoint`` is where the walk stopped, and ``request_id`` is the failing
    page's ``meta.request_id`` when it carried one -- quote it when reporting a
    route whose cursor is broken.
    """

    def __init__(
        self,
        reason: str,
        message: str,
        *,
        method_name: str,
        page: Any,
        checkpoint: PaginationProgress,
        request_id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.reason = reason
        self.method_name = method_name
        self.page = page
        self.checkpoint = checkpoint
        self.request_id = request_id
        self.cursor = checkpoint.cursor
        self.next_cursor = checkpoint.next_cursor
        self.pages_fetched = checkpoint.pages_fetched
        self.items_yielded = checkpoint.items_yielded


def _bound(value: int | None, name: str) -> int | None:
    """A caller bound: ``None`` for no cap, otherwise a positive integer.

    Checked before any request, so ``0``, a negative, a float, a bool or a
    string fails without spending one.
    """
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer or None, got {value!r}")
    return value


def _request_id(page: Any) -> str | None:
    meta = page.get("meta") if isinstance(page, Mapping) else None
    value = meta.get("request_id") if isinstance(meta, Mapping) else None
    return value if isinstance(value, str) else None


def _context(method_name: str, state: PaginationProgress, page: Any) -> str:
    request_id = _request_id(page)
    where = f"{method_name} page {state.pages_fetched + 1}"
    return f"{where} (request {request_id})" if request_id else where


def _protocol_error(
    reason: str,
    message: str,
    *,
    method_name: str,
    page: Any,
    state: PaginationProgress,
) -> PaginationError:
    error = PaginationError(
        reason,
        message,
        method_name=method_name,
        page=page,
        checkpoint=replace(state),
        request_id=_request_id(page),
    )
    _record(error, error.checkpoint)
    return error


def _record(error: BaseException, checkpoint: PaginationProgress) -> None:
    """Attach the checkpoint to an error on its way out of a walk.

    An exception type that refuses attributes (``__slots__`` and no instance
    dict) is left exactly as it is: the error itself is re-raised unchanged
    either way, and a caller that passed ``progress=`` already holds the same
    state, so nothing is lost and nothing is hidden.
    """
    if getattr(error, _CHECKPOINT_ATTR, None) is not None:
        return
    try:
        setattr(error, _CHECKPOINT_ATTR, checkpoint)
    except (AttributeError, TypeError):
        return


def _remember(seen: set, order: deque, cursor: str) -> None:
    if cursor in seen:
        return
    seen.add(cursor)
    order.append(cursor)
    if len(order) > CURSOR_HISTORY_LIMIT:
        seen.discard(order.popleft())


def paginate_pages(
    method: Callable[..., Any],
    method_name: str,
    *,
    filters: Mapping[str, Any],
    cursor: str | None = None,
    max_pages: int | None = None,
    max_items: int | None = None,
    progress: PaginationProgress | None = None,
) -> Iterator[Any]:
    """Yield whole validated list pages, following ``next_cursor`` to exhaustion.

    ``Client.paginate_pages`` is the public entry point; the module docstring
    says what each page is checked against.
    """
    page_cap = _bound(max_pages, "max_pages")
    item_cap = _bound(max_items, "max_items")
    state = progress if progress is not None else PaginationProgress()
    # Captured once: every page after the first differs from it only by the
    # cursor, so no page can quietly run different filters than the one before.
    query = dict(filters)
    seen: set = set()
    order: deque = deque()

    while True:
        if cursor is not None:
            _remember(seen, order, cursor)
        state.cursor = cursor
        try:
            page = method(cursor=cursor, **query)
        except BaseException as error:
            # Record where the walk got to and re-raise the original error
            # unchanged, so an ``except RateLimitedError`` still works and the
            # caller can resume from ``pagination_checkpoint(error)``.
            _record(error, replace(state))
            raise

        if isinstance(page, Mapping) and page.get("object") == "not_modified":
            # A conditional read that matched: nothing changed, so there is
            # nothing to page through. Not an error and not an empty collection.
            state.next_cursor = None
            state.stopped_by = STOP_NOT_MODIFIED
            return

        if not isinstance(page, Mapping) or not isinstance(page.get("has_more"), bool):
            raise _protocol_error(
                "invalid_envelope",
                f"{_context(method_name, state, page)} is not a cursor-paginated list envelope: expected an "
                f"object with a boolean has_more, got {type(page).__name__}"
                + (f" with object={page.get('object')!r}" if isinstance(page, Mapping) else ""),
                method_name=method_name,
                page=page,
                state=state,
            )

        data = page.get("data")
        if not isinstance(data, list):
            raise _protocol_error(
                "invalid_data",
                f"{_context(method_name, state, page)} carries data of type {type(data).__name__}, not a list; "
                "that is a malformed page, not an exhausted collection",
                method_name=method_name,
                page=page,
                state=state,
            )

        has_more = page["has_more"]
        raw_next = page.get("next_cursor")
        state.next_cursor = raw_next if isinstance(raw_next, str) and raw_next else None

        if has_more:
            if state.next_cursor is None:
                raise _protocol_error(
                    "missing_cursor",
                    f"{_context(method_name, state, page)} says has_more but carries no usable next_cursor "
                    f"({raw_next!r}); the walk cannot continue safely",
                    method_name=method_name,
                    page=page,
                    state=state,
                )
            if state.next_cursor in seen:
                raise _protocol_error(
                    "repeated_cursor",
                    f"{_context(method_name, state, page)} offers next_cursor {state.next_cursor!r}, which this "
                    "walk already requested; stopping before the duplicate request",
                    method_name=method_name,
                    page=page,
                    state=state,
                )

        state.pages_fetched += 1
        state.items_yielded += len(data)
        yield page

        if not has_more:
            state.stopped_by = STOP_EXHAUSTED
            return
        if page_cap is not None and state.pages_fetched >= page_cap:
            state.stopped_by = STOP_MAX_PAGES
            return
        if item_cap is not None and state.items_yielded >= item_cap:
            state.stopped_by = STOP_MAX_ITEMS
            return
        cursor = state.next_cursor


def paginate(
    method: Callable[..., Any],
    method_name: str,
    *,
    filters: Mapping[str, Any],
    cursor: str | None = None,
    max_pages: int | None = None,
    max_items: int | None = None,
    progress: PaginationProgress | None = None,
) -> Iterator[Any]:
    """Yield individual ``data[]`` items across pages. ``Client.paginate`` is the public entry point."""
    item_cap = _bound(max_items, "max_items")
    state = progress if progress is not None else PaginationProgress()
    pages = paginate_pages(
        method,
        method_name,
        filters=filters,
        cursor=cursor,
        max_pages=max_pages,
        progress=state,
    )
    delivered = 0
    try:
        for page in pages:
            for item in page["data"]:
                if item_cap is not None and delivered >= item_cap:
                    # Stopped inside a page: ``cursor`` still points at that
                    # page, so resuming there re-reads the items already
                    # delivered rather than skipping the rest of the page.
                    state.items_yielded = delivered
                    state.stopped_by = STOP_MAX_ITEMS
                    return
                yield item
                delivered += 1
            state.items_yielded = delivered
    finally:
        pages.close()
