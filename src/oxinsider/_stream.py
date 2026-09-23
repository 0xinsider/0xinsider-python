"""Resumable Server-Sent Events reading for ``AsyncClient.stream``.

``GET /api/v1/stream`` (``backend/docs/internal-api/028-public-v1-stream-sse.md``)
resumes from a ``Last-Event-ID`` header (or the ``?last_event_id=``/``?seq=``
query fallback): present and numeric, it replays the retained window before
going live; absent or non-numeric attaches live with no replay. Every frame,
replayed or live, carries its sequence as the SSE ``id:`` field. A finite
``200 text/event-stream`` body is a disconnect to recover from, never a
documented end of the collection (``.claude/rules/api-contracts.md``): the
server holds the body open with a keep-alive comment every five seconds and
otherwise only stops it for a shutdown or a credential re-check failure, both
recoverable by reconnecting with the last ``id:`` seen.

This module is the reconnect loop: it decodes ``text/event-stream`` frames
per the WHATWG parsing rules (comments, multi-line ``data:``, the persisting
``id:``/``retry:`` buffers), and on every disconnect calls back into the
caller-supplied ``open_response`` with the last ``id:`` observed, waiting a
bounded, exponentially growing delay between attempts (the server's own
``retry:`` field, when it sent one, overrides the computed delay for that one
reconnect). ``AsyncClient.stream`` supplies ``open_response`` and is the
public entry point; nothing here talks to a real connection or the API base
URL directly, which is what keeps it testable against any opener.
"""

from __future__ import annotations

import asyncio
import json
from collections.abc import AsyncIterator, Awaitable, Callable
from dataclasses import dataclass
from typing import Any

import httpx

from ._errors import OxinsiderConnectionError, StreamClosedError

#: A reconnect's starting delay, in seconds, absent a server ``retry:`` field.
#: Matches an ``EventSource``'s own 3 s default reconnection time.
DEFAULT_BACKOFF_INITIAL = 3.0

#: The delay never grows past this, in seconds, however many attempts fail in a row.
DEFAULT_BACKOFF_MAX = 30.0


@dataclass(frozen=True)
class ServerSentEvent:
    """One decoded ``text/event-stream`` frame.

    ``event`` is ``"message"`` when the frame sent none. ``data`` is the
    joined ``data:`` lines exactly as sent (newline-joined, undecoded);
    ``json()`` parses it for the routes that document a JSON payload. ``id``
    is the current last-event-id buffer at dispatch, per the WHATWG rules: a
    frame that carries no ``id:`` of its own still reports the most recent one
    seen, which is what makes it safe to always read as "resume from here."
    """

    event: str
    data: str
    id: str | None = None

    def json(self) -> Any:
        return json.loads(self.data)


class _SseDecoder:
    """Buffers ``text/event-stream`` lines into ``ServerSentEvent``s.

    One instance per connection attempt: ``last_id`` and
    ``reconnection_delay_ms`` are the WHATWG "last event ID buffer" and
    "reconnection time", which persist across frames within a connection and
    are read by the reconnect loop after the connection drops.
    """

    def __init__(self) -> None:
        self._event = "message"
        self._data: list[str] = []
        self.last_id: str | None = None
        self.reconnection_delay_ms: int | None = None

    def push(self, line: str) -> ServerSentEvent | None:
        line = line.rstrip("\r")
        if line == "":
            return self._dispatch()
        if line.startswith(":"):
            return None  # a comment, including the periodic keep-alive ping
        field, sep, value = line.partition(":")
        if sep and value.startswith(" "):
            value = value[1:]
        if field == "event":
            self._event = value or "message"
        elif field == "data":
            self._data.append(value)
        elif field == "id":
            if "\x00" not in value:  # a NUL in the field aborts setting it, per spec
                self.last_id = value
        elif field == "retry":
            if value.isdigit():
                self.reconnection_delay_ms = int(value)
        # An unrecognized field name is ignored, per spec.
        return None

    def _dispatch(self) -> ServerSentEvent | None:
        event_type, self._event = self._event, "message"
        if not self._data:
            return None
        data = "\n".join(self._data)
        self._data = []
        return ServerSentEvent(event=event_type, data=data, id=self.last_id)


def _delay(attempt: int, initial: float, maximum: float) -> float:
    """Exponential backoff from ``initial``, doubling per attempt, capped at ``maximum``."""
    return min(initial * (2 ** (attempt - 1)), maximum)


def _terminal_error(event: ServerSentEvent) -> StreamClosedError | None:
    """Decode a documented ``event: error`` frame into a ``StreamClosedError``.

    ``None`` for anything else -- a different event type, or an ``error``
    frame whose body is not the documented ``{"error": {...}, "retry": ...}``
    shape -- so an undocumented frame is surfaced to the caller as data
    instead of silently ending the walk.
    """
    if event.event != "error":
        return None
    try:
        payload = json.loads(event.data)
    except ValueError:
        return None
    if not isinstance(payload, dict):
        return None
    body = payload.get("error")
    if not isinstance(body, dict):
        return None
    return StreamClosedError(
        code=body.get("code"),
        message=body.get("message") or "stream closed with an error",
        retry=bool(payload.get("retry", True)),
        retry_at=body.get("retry_at"),
        request_id=body.get("request_id"),
    )


async def stream_events(
    open_response: Callable[[str | None], Awaitable[httpx.Response]],
    *,
    last_event_id: str | None = None,
    max_retries: int | None = None,
    backoff_initial: float = DEFAULT_BACKOFF_INITIAL,
    backoff_max: float = DEFAULT_BACKOFF_MAX,
) -> AsyncIterator[ServerSentEvent]:
    """Read one logical SSE stream to exhaustion, reconnecting after every disconnect.

    ``open_response`` opens a fresh streaming ``httpx.Response`` given the
    ``id`` to resume from (``None`` for a cold start); it is called again,
    with the last ``id`` this walk observed, every time the connection drops,
    whichever end dropped it. Backoff between reconnects is exponential from
    ``backoff_initial``, capped at ``backoff_max`` seconds, or the server's
    own ``retry:`` field for that one attempt when it sent one; it resets
    after a connection opens successfully, so one blip in an otherwise
    long-lived stream does not creep the delay towards the cap forever.

    ``max_retries`` bounds consecutive failed *reconnect* attempts (``None``,
    the default, retries forever, matching a browser ``EventSource``);
    exceeding it re-raises the error the last attempt failed with, or returns
    quietly if every attempt so far had opened fine and only the walk's own
    bound was reached with no error in hand. A ``StreamClosedError`` whose
    ``retry`` is ``False`` (a permanently refused credential) is raised
    immediately and never counts against ``max_retries``, since reconnecting
    would not help.

    ``asyncio.CancelledError`` is never caught here: the open response is
    always released in a ``finally`` and the cancellation propagates to the
    caller uninterrupted.
    """
    attempt = 0
    last_error: BaseException | None = None
    while True:
        try:
            response = await open_response(last_event_id)
        except (httpx.HTTPError, OxinsiderConnectionError) as error:
            attempt += 1
            last_error = error
            if max_retries is not None and attempt > max_retries:
                raise
            await asyncio.sleep(_delay(attempt, backoff_initial, backoff_max))
            continue

        attempt = 0  # the connection opened: a future drop starts backoff fresh
        last_error = None
        decoder = _SseDecoder()
        try:
            async for line in response.aiter_lines():
                event = decoder.push(line)
                if decoder.last_id is not None:
                    last_event_id = decoder.last_id
                if event is None:
                    continue
                terminal = _terminal_error(event)
                yield event
                if terminal is not None:
                    if not terminal.retry:
                        raise terminal
                    last_error = terminal
                    break
        except httpx.HTTPError as error:
            last_error = error
        finally:
            await response.aclose()

        attempt += 1
        if max_retries is not None and attempt > max_retries:
            if last_error is not None:
                raise last_error
            return
        delay = (
            decoder.reconnection_delay_ms / 1000
            if decoder.reconnection_delay_ms is not None
            else _delay(attempt, backoff_initial, backoff_max)
        )
        await asyncio.sleep(delay)
