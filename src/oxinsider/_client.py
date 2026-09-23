"""The 0xinsider Developer API client."""

from __future__ import annotations

import asyncio
import os
from collections.abc import AsyncIterator, Iterator, Mapping
from typing import Any
from urllib.parse import quote

import httpx

from ._download import AsyncDownload, Download, DownloadError
from ._errors import OxinsiderApiError, OxinsiderConnectionError, error_class_for
from ._operations import (
    OPERATIONS,
    AsyncOperationsMixin,
    AsyncResponseOperationsMixin,
    OperationsMixin,
    ResponseOperationsMixin,
)
from ._pagination import PaginationProgress
from ._pagination import apaginate as _awalk_items
from ._pagination import apaginate_pages as _awalk_pages
from ._pagination import paginate as _walk_items
from ._pagination import paginate_pages as _walk_pages
from ._policy import assert_credential_destination, is_trusted_destination
from ._response import ApiResponse
from ._stream import DEFAULT_BACKOFF_INITIAL, DEFAULT_BACKOFF_MAX, ServerSentEvent
from ._stream import stream_events as _stream_events
from ._version import __version__

PRODUCTION_BASE_URL = "https://api.0xinsider.com"
SANDBOX_BASE_URL = "https://0xinsider.com/sandbox"
API_KEY_ENV = "OXINSIDER_API_KEY"

#: ``AsyncClient``'s default ``max_concurrency``: how many requests it holds in
#: flight at once via its internal semaphore. Bounded and caller-configurable
#: rather than unlimited, so an ``asyncio.gather`` over many reads cannot open
#: more connections than the API (or the caller's own downstream) can take.
DEFAULT_MAX_CONCURRENCY = 10

NOT_MODIFIED: dict[str, Any] = {"object": "not_modified", "data": None}


def _clean_query(query: Mapping[str, Any] | None) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for key, value in (query or {}).items():
        if value is None:
            continue
        values = value if isinstance(value, (list, tuple)) else [value]
        for item in values:
            if isinstance(item, bool):
                pairs.append((key, "true" if item else "false"))
            else:
                pairs.append((key, str(item)))
    return pairs


def _retry_after(response: httpx.Response) -> float | None:
    raw = response.headers.get("retry-after")
    if raw is None:
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def _operation_path(operation_id: str, path_params: Mapping[str, str]) -> str:
    """``Client._operation_path``'s module-level twin, shared with ``AsyncClient``."""
    path = OPERATIONS[operation_id].path
    for name, value in path_params.items():
        path = path.replace("{" + name + "}", quote(str(value), safe="@"))
    return path


def _error_from_response(response: httpx.Response) -> OxinsiderApiError:
    """``Client._error``'s module-level twin, shared with ``AsyncClient``."""
    payload: Any = None
    error: dict[str, Any] = {}
    meta: dict[str, Any] = {}
    if response.content:
        try:
            payload = response.json()
        except ValueError:
            payload = response.text
    if isinstance(payload, dict):
        error = payload.get("error") if isinstance(payload.get("error"), dict) else {}
        meta = payload.get("meta") if isinstance(payload.get("meta"), dict) else {}
    message = error.get("message") or response.reason_phrase or "request failed"
    cls = error_class_for(response.status_code)
    return cls(
        response.status_code,
        message,
        code=error.get("code"),
        reason=error.get("reason"),
        param=error.get("param"),
        retry_at=error.get("retry_at"),
        retry_after=_retry_after(response),
        request_id=meta.get("request_id") or response.headers.get("x-request-id"),
        body=payload,
        response=ApiResponse(data=payload, status=response.status_code, headers=response.headers),
    )


def _bound_concurrency(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"max_concurrency must be a positive integer, got {value!r}")
    return value


class Client(OperationsMixin):
    """A synchronous client for https://api.0xinsider.com.

    The API key comes from ``api_key`` or the ``OXINSIDER_API_KEY`` environment
    variable. Data operations need a key (or an OAuth access token) and an active
    Pro subscription; discovery, health and platforms do not.

    Use ``Client.sandbox()`` to build against the zero-credential sandbox, which
    answers every documented operation with example data and never touches
    production data.

    A credential is only ever sent over ``https://``, or over ``http://`` to a
    loopback host (``localhost``, ``127.0.0.1``, ``[::1]``). A ``base_url`` that
    would send the key anywhere else raises ``InsecureTransportError`` here,
    before any request; a keyless client may still call the public operations
    on such a base. Redirects are never followed automatically.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str = PRODUCTION_BASE_URL,
        timeout: float = 30.0,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.api_key = api_key if api_key is not None else os.environ.get(API_KEY_ENV)
        self.base_url = base_url.rstrip("/")
        self._owns_http = http_client is None
        self._http = http_client or httpx.Client(timeout=timeout)
        if self.api_key or self._http.auth is not None:
            assert_credential_destination(httpx.URL(self.base_url))

    @classmethod
    def sandbox(cls, *, timeout: float = 30.0) -> Client:
        """A client for https://0xinsider.com/sandbox: no credential, example data only."""
        return cls(api_key="", base_url=SANDBOX_BASE_URL, timeout=timeout)

    def close(self) -> None:
        if self._owns_http:
            self._http.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        if_none_match: str | None = None,
        idempotency_key: str | None = None,
        headers: Mapping[str, str] | None = None,
        stream: bool = False,
        raw: bool = False,
    ) -> Any:
        """Send one request and return the decoded body.

        A JSON response returns the decoded object. A 304 for ``if_none_match``
        returns ``{"object": "not_modified", "data": None}``. A non-JSON response
        (Markdown, CSV) returns the text. With ``stream=True`` the open
        ``httpx.Response`` is returned for the caller to iterate and close, which
        is how the SSE stream (``GET /api/v1/stream``) is read.

        With ``raw=True`` the same call returns an ``ApiResponse`` instead: the
        identical body as ``.data``, plus ``.status``, ``.headers`` and the
        ``etag``, ``request_id``, ``rate_limit``, ``monthly_quota`` and
        ``retry_after`` accessors. It changes nothing about the request that
        goes out, and an error status still raises. ``stream=True`` already
        hands back the open response with its own headers, so the two cannot be
        combined.
        """
        if raw and stream:
            raise ValueError("raw=True and stream=True cannot be combined: a stream returns the open response")
        request = self._build_api_request(
            method,
            path,
            query=query,
            body=body,
            if_none_match=if_none_match,
            idempotency_key=idempotency_key,
            headers=headers,
        )
        response = self._send(request, stream=stream)
        if stream and response.is_success:
            return response
        if stream:
            response.read()
        if response.status_code == 304:
            decoded: Any = {**NOT_MODIFIED, "etag": response.headers.get("etag")}
        elif not response.is_success:
            raise self._error(response)
        elif response.status_code == 204 or not response.content:
            decoded = None
        elif "json" in response.headers.get("content-type", ""):
            decoded = response.json()
        else:
            decoded = response.text
        if raw:
            return ApiResponse(data=decoded, status=response.status_code, headers=response.headers)
        return decoded

    @property
    def with_response(self) -> _ResponseClient:
        """Every operation, returning an ``ApiResponse`` instead of the body alone.

        ``client.with_response.get_trader("swisstony")`` sends exactly the
        request ``client.get_trader("swisstony")`` sends and answers with the
        same body under ``.data``, plus the status, the headers, the ``etag``
        for the next conditional read, the ``request_id``, and the
        ``rate_limit`` and ``monthly_quota`` budgets. The body-only methods are
        unchanged.

        A redirect-only operation (``download_trader_export``,
        ``redirect_api_openapi_spec``) already returns a ``Download`` carrying
        the file's own headers, so it is unchanged here too.
        """
        client = getattr(self, "_with_response", None)
        if client is None:
            client = _ResponseClient(self)
            self._with_response = client
        return client

    def _build_api_request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        if_none_match: str | None = None,
        idempotency_key: str | None = None,
        headers: Mapping[str, str] | None = None,
        accept: str = "application/json",
    ) -> httpx.Request:
        request_headers = {
            "Accept": accept,
            "User-Agent": f"0xinsider-python/{__version__}",
        }
        if self.api_key:
            request_headers["Authorization"] = f"Bearer {self.api_key}"
        if if_none_match:
            request_headers["If-None-Match"] = if_none_match
        if idempotency_key:
            request_headers["Idempotency-Key"] = idempotency_key
        request_headers.update(headers or {})
        return self._http.build_request(
            method.upper(),
            f"{self.base_url}{path}",
            params=_clean_query(query),
            json=body,
            headers=request_headers,
        )

    def _send(self, request: httpx.Request, *, stream: bool) -> httpx.Response:
        """Send one request to the API origin. Redirects are never followed here:
        the two documented ones (the OpenAPI document and a finished export) are
        handled by ``download``, which keeps the credential on the API origin.

        The destination is checked again on the final request, so a credential
        that arrived through ``headers=``, a later ``client.api_key = ...``, or an
        ``auth=`` on a supplied ``httpx.Client`` cannot travel over plain HTTP to
        a host that is not loopback either."""
        if request.headers.get("Authorization") or self._http.auth is not None:
            assert_credential_destination(request.url)
        try:
            return self._http.send(request, stream=stream, follow_redirects=False)
        except httpx.HTTPError as error:
            raise OxinsiderConnectionError(f"{request.method} {request.url.path} failed: {error}") from error

    def download(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Download:
        """Call a redirect-only operation and open the file it points at.

        The API request carries the credential; the redirect's ``Location`` is
        fetched with a fresh request that carries none, so the bearer never
        reaches the file host. Only ``https://`` locations are followed (``http://``
        for a loopback host); one hop only. The API's own errors raise the usual
        typed ``OxinsiderApiError`` (a 400 while an export job is not ``ready``,
        a 404 for an unknown job); a redirect or transfer fault raises
        ``DownloadError``. The returned ``Download`` streams the bytes: iterate,
        ``save`` or ``read`` it, and close it.
        """
        request = self._build_api_request(method, path, query=query, headers=headers, accept="*/*")
        response = self._send(request, stream=True)
        if not response.is_redirect:
            response.read()
            if response.is_success:
                raise DownloadError(
                    f"{request.method} {path} answered {response.status_code} instead of a redirect to the file",
                    reason="not_redirected",
                    status=response.status_code,
                )
            raise self._error(response)
        location_header = response.headers.get("location")
        response.close()
        if not location_header:
            raise DownloadError(
                f"{request.method} {path} redirected without a Location header",
                reason="missing_location",
                status=response.status_code,
            )
        location = request.url.join(location_header)
        host = f"{location.scheme}://{location.netloc.decode('ascii')}"
        if not is_trusted_destination(location):
            raise DownloadError(
                f"refusing to fetch the file from {host}: only https:// (or http:// on a loopback host) is followed",
                reason="insecure_location",
                host=host,
            )
        file_request = self._http.build_request(
            "GET",
            location,
            headers={"Accept": "*/*", "User-Agent": f"0xinsider-python/{__version__}"},
        )
        # A user-supplied httpx.Client may carry default headers; the credential
        # and cookies stay on the API origin whatever the client was built with.
        file_request.headers.pop("Authorization", None)
        file_request.headers.pop("Cookie", None)
        try:
            file_response = self._http.send(file_request, stream=True, auth=None, follow_redirects=False)
        except httpx.HTTPError as error:
            raise DownloadError(
                f"fetching the file from {host} failed: {error}",
                reason="interrupted",
                host=host,
            ) from error
        if file_response.is_redirect:
            file_response.close()
            raise DownloadError(
                f"{host} answered {file_response.status_code} with another redirect; only one hop is followed",
                reason="unexpected_redirect",
                host=host,
                status=file_response.status_code,
            )
        if not file_response.is_success:
            file_response.close()
            raise DownloadError(
                f"{host} answered {file_response.status_code} for the file"
                + (
                    "; the download location has expired, call the download operation again for a fresh one"
                    if file_response.status_code == 403
                    else ""
                ),
                reason="unavailable",
                host=host,
                status=file_response.status_code,
            )
        return Download(file_response, location=location)

    def paginate(
        self,
        method_name: str,
        *,
        max_pages: int | None = None,
        max_items: int | None = None,
        progress: PaginationProgress | None = None,
        **kwargs: Any,
    ) -> Iterator[Any]:
        """Yield every item of a cursor-paginated list, following ``next_cursor``.

        ``client.paginate("list_whale_trades", min_grade="A", limit=100)``

        The filters are sent unchanged on every page; only the cursor moves.
        ``cursor=`` starts the walk part way through, which is how an
        interrupted one is resumed.

        A page that breaks the list protocol raises ``PaginationError`` before
        it is yielded and before another request: a response that is not a list
        envelope, ``data`` that is not a list, ``has_more`` with no usable
        ``next_cursor``, or a ``next_cursor`` this walk already requested. An
        exhausted collection and a valid empty page still end the walk quietly.

        ``max_pages`` caps requests and ``max_items`` caps items; each is a
        positive integer or ``None``, checked before the first request. Pass a
        ``PaginationProgress`` as ``progress=`` to read afterwards where the
        walk got to and why it stopped, and see ``pagination_checkpoint`` to
        recover the same from a failure.
        """
        cursor = kwargs.pop("cursor", None)
        return _walk_items(
            getattr(self, method_name),
            method_name,
            filters=kwargs,
            cursor=cursor,
            max_pages=max_pages,
            max_items=max_items,
            progress=progress,
        )

    def paginate_pages(
        self,
        method_name: str,
        *,
        max_pages: int | None = None,
        max_items: int | None = None,
        progress: PaginationProgress | None = None,
        **kwargs: Any,
    ) -> Iterator[Any]:
        """Yield whole list pages instead of items, with the same checks as ``paginate``.

        Use it when you need the envelope rather than only the items: ``total``,
        ``has_more``, ``next_cursor``, or ``meta`` for the request ID and the
        request's cost.

        ``max_items`` stops the walk after the first page that reaches it; a
        page is never cut in half here.
        """
        cursor = kwargs.pop("cursor", None)
        return _walk_pages(
            getattr(self, method_name),
            method_name,
            filters=kwargs,
            cursor=cursor,
            max_pages=max_pages,
            max_items=max_items,
            progress=progress,
        )

    @staticmethod
    def _operation_path(operation_id: str, path_params: Mapping[str, str]) -> str:
        path = OPERATIONS[operation_id].path
        for name, value in path_params.items():
            path = path.replace("{" + name + "}", quote(str(value), safe="@"))
        return path

    def _download(
        self,
        operation_id: str,
        *,
        path_params: Mapping[str, str],
        query: Mapping[str, Any],
    ) -> Download:
        operation = OPERATIONS[operation_id]
        return self.download(operation.method, self._operation_path(operation_id, path_params), query=query)

    def _call(
        self,
        operation_id: str,
        *,
        path_params: Mapping[str, str],
        query: Mapping[str, Any],
        body: Any = None,
        if_none_match: str | None = None,
        idempotency_key: str | None = None,
        raw: bool = False,
    ) -> Any:
        operation = OPERATIONS[operation_id]
        path = self._operation_path(operation_id, path_params)
        return self.request(
            operation.method,
            path,
            query=query,
            body=body,
            if_none_match=if_none_match,
            idempotency_key=idempotency_key,
            headers={"Accept": operation.accept},
            raw=raw,
        )

    @staticmethod
    def _error(response: httpx.Response) -> OxinsiderApiError:
        payload: Any = None
        error: dict[str, Any] = {}
        meta: dict[str, Any] = {}
        if response.content:
            try:
                payload = response.json()
            except ValueError:
                payload = response.text
        if isinstance(payload, dict):
            error = payload.get("error") if isinstance(payload.get("error"), dict) else {}
            meta = payload.get("meta") if isinstance(payload.get("meta"), dict) else {}
        message = error.get("message") or response.reason_phrase or "request failed"
        cls = error_class_for(response.status_code)
        return cls(
            response.status_code,
            message,
            code=error.get("code"),
            reason=error.get("reason"),
            param=error.get("param"),
            retry_at=error.get("retry_at"),
            retry_after=_retry_after(response),
            request_id=meta.get("request_id") or response.headers.get("x-request-id"),
            body=payload,
            response=ApiResponse(data=payload, status=response.status_code, headers=response.headers),
        )


class _ResponseClient(ResponseOperationsMixin):
    """The operation methods of one ``Client``, answering with ``ApiResponse``.

    Reached as ``client.with_response``; it holds no state of its own and sends
    the same requests the client does.
    """

    def __init__(self, client: Client) -> None:
        self._client = client

    def request(self, method: str, path: str, **kwargs: Any) -> ApiResponse[Any]:
        """``Client.request`` with ``raw=True``."""
        return self._client.request(method, path, raw=True, **kwargs)

    def _call(self, operation_id: str, **kwargs: Any) -> ApiResponse[Any]:
        return self._client._call(operation_id, raw=True, **kwargs)

    def _download(self, operation_id: str, **kwargs: Any) -> Download:
        # A redirect-only operation already answers with the file's own headers.
        return self._client._download(operation_id, **kwargs)


class AsyncClient(AsyncOperationsMixin):
    """An async client for https://api.0xinsider.com, built on ``httpx.AsyncClient``.

    The same operations as ``Client``, as coroutines: same method names, same
    argument names, the same ``oxinsider.types`` shapes and the same errors --
    ``AsyncOperationsMixin`` is generated from the identical operation table,
    so a route's contract cannot drift between the two clients. Only the
    transport changes: every method here awaits ``httpx.AsyncClient`` instead
    of blocking the event loop on the synchronous one.

    ``max_concurrency`` (default ``DEFAULT_MAX_CONCURRENCY``, 10) bounds how
    many requests this client holds in flight at once, through an internal
    ``asyncio.Semaphore`` acquired only around the send itself -- a ``stream()``
    walk's open connection is not held under it once its headers arrive, so
    one long-lived stream does not starve ordinary calls sharing the client.
    Raise it for a bulk workflow that fans many independent reads out with
    ``asyncio.gather``; lower it to stay further under the API's own
    per-minute budget. It is concurrency, not a rate limit: pair it with the
    ``rate_limit`` budget on ``with_response`` or a ``RateLimitedError``'s
    ``retry_after`` for that.

    Cancelling a call -- ``asyncio.CancelledError``, an ``asyncio.wait_for``
    timeout, a task group cancelling its members -- is never caught here: it
    propagates to the caller, and the in-flight ``httpx`` request and any open
    stream response are released as part of that unwind (every request and
    ``stream()`` iteration closes its response in a ``finally``). ``aclose()``
    closes the underlying ``httpx.AsyncClient`` only when this client built it
    itself; one passed in as ``http_client=`` remains the caller's to close,
    exactly like ``Client``.

    Use ``AsyncClient.sandbox()`` for the zero-credential sandbox, same as
    ``Client.sandbox()``.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str = PRODUCTION_BASE_URL,
        timeout: float = 30.0,
        http_client: httpx.AsyncClient | None = None,
        max_concurrency: int = DEFAULT_MAX_CONCURRENCY,
    ) -> None:
        self.api_key = api_key if api_key is not None else os.environ.get(API_KEY_ENV)
        self.base_url = base_url.rstrip("/")
        self.max_concurrency = _bound_concurrency(max_concurrency)
        self._owns_http = http_client is None
        self._http = http_client or httpx.AsyncClient(timeout=timeout)
        self._semaphore = asyncio.Semaphore(self.max_concurrency)
        if self.api_key or self._http.auth is not None:
            assert_credential_destination(httpx.URL(self.base_url))

    @classmethod
    def sandbox(cls, *, timeout: float = 30.0, max_concurrency: int = DEFAULT_MAX_CONCURRENCY) -> AsyncClient:
        """An async client for https://0xinsider.com/sandbox: no credential, example data only."""
        return cls(api_key="", base_url=SANDBOX_BASE_URL, timeout=timeout, max_concurrency=max_concurrency)

    async def aclose(self) -> None:
        if self._owns_http:
            await self._http.aclose()

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *_exc: object) -> None:
        await self.aclose()

    async def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        if_none_match: str | None = None,
        idempotency_key: str | None = None,
        headers: Mapping[str, str] | None = None,
        stream: bool = False,
        raw: bool = False,
    ) -> Any:
        """``Client.request``'s async counterpart: send one request, return the decoded body.

        With ``stream=True`` the open ``httpx.Response`` is returned for the
        caller to read with ``aiter_lines()``/``aiter_bytes()`` and close (or
        use it as an async context manager); use ``stream()`` instead for a
        resumable SSE walk over ``GET /api/v1/stream`` that reconnects for
        you. Otherwise this is ``Client.request``'s exact contract: ``raw=True``
        answers an ``ApiResponse``, a 304 for ``if_none_match`` decodes to the
        not-modified sentinel, and the two options refuse to combine.
        """
        if raw and stream:
            raise ValueError("raw=True and stream=True cannot be combined: a stream returns the open response")
        request = self._build_api_request(
            method,
            path,
            query=query,
            body=body,
            if_none_match=if_none_match,
            idempotency_key=idempotency_key,
            headers=headers,
        )
        response = await self._send(request, stream=stream)
        if stream and response.is_success:
            return response
        if stream:
            await response.aread()
        if response.status_code == 304:
            decoded: Any = {**NOT_MODIFIED, "etag": response.headers.get("etag")}
        elif not response.is_success:
            raise _error_from_response(response)
        elif response.status_code == 204 or not response.content:
            decoded = None
        elif "json" in response.headers.get("content-type", ""):
            decoded = response.json()
        else:
            decoded = response.text
        if raw:
            return ApiResponse(data=decoded, status=response.status_code, headers=response.headers)
        return decoded

    @property
    def with_response(self) -> _AsyncResponseClient:
        """Every operation, returning an ``ApiResponse`` instead of the body alone. See ``Client.with_response``."""
        client = getattr(self, "_with_response", None)
        if client is None:
            client = _AsyncResponseClient(self)
            self._with_response = client
        return client

    def _build_api_request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        if_none_match: str | None = None,
        idempotency_key: str | None = None,
        headers: Mapping[str, str] | None = None,
        accept: str = "application/json",
    ) -> httpx.Request:
        request_headers = {
            "Accept": accept,
            "User-Agent": f"0xinsider-python/{__version__}",
        }
        if self.api_key:
            request_headers["Authorization"] = f"Bearer {self.api_key}"
        if if_none_match:
            request_headers["If-None-Match"] = if_none_match
        if idempotency_key:
            request_headers["Idempotency-Key"] = idempotency_key
        request_headers.update(headers or {})
        return self._http.build_request(
            method.upper(),
            f"{self.base_url}{path}",
            params=_clean_query(query),
            json=body,
            headers=request_headers,
        )

    async def _send(self, request: httpx.Request, *, stream: bool) -> httpx.Response:
        """Send one request, bounded by ``max_concurrency``.

        The semaphore is held only around ``AsyncClient.send`` itself, which
        returns as soon as the response headers arrive -- a streamed body is
        read afterwards, outside it, so an open stream does not hold a
        concurrency slot for its whole lifetime. Redirects are never followed
        here, matching ``Client._send``.
        """
        if request.headers.get("Authorization") or self._http.auth is not None:
            assert_credential_destination(request.url)
        try:
            async with self._semaphore:
                return await self._http.send(request, stream=stream, follow_redirects=False)
        except httpx.HTTPError as error:
            raise OxinsiderConnectionError(f"{request.method} {request.url.path} failed: {error}") from error

    async def download(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> AsyncDownload:
        """``Client.download``'s async counterpart; returns an ``AsyncDownload``."""
        request = self._build_api_request(method, path, query=query, headers=headers, accept="*/*")
        response = await self._send(request, stream=True)
        if not response.is_redirect:
            await response.aread()
            if response.is_success:
                raise DownloadError(
                    f"{request.method} {path} answered {response.status_code} instead of a redirect to the file",
                    reason="not_redirected",
                    status=response.status_code,
                )
            raise _error_from_response(response)
        location_header = response.headers.get("location")
        await response.aclose()
        if not location_header:
            raise DownloadError(
                f"{request.method} {path} redirected without a Location header",
                reason="missing_location",
                status=response.status_code,
            )
        location = request.url.join(location_header)
        host = f"{location.scheme}://{location.netloc.decode('ascii')}"
        if not is_trusted_destination(location):
            raise DownloadError(
                f"refusing to fetch the file from {host}: only https:// (or http:// on a loopback host) is followed",
                reason="insecure_location",
                host=host,
            )
        file_request = self._http.build_request(
            "GET",
            location,
            headers={"Accept": "*/*", "User-Agent": f"0xinsider-python/{__version__}"},
        )
        # A user-supplied httpx.AsyncClient may carry default headers; the
        # credential and cookies stay on the API origin whatever it was built with.
        file_request.headers.pop("Authorization", None)
        file_request.headers.pop("Cookie", None)
        try:
            file_response = await self._http.send(file_request, stream=True, auth=None, follow_redirects=False)
        except httpx.HTTPError as error:
            raise DownloadError(
                f"fetching the file from {host} failed: {error}",
                reason="interrupted",
                host=host,
            ) from error
        if file_response.is_redirect:
            await file_response.aclose()
            raise DownloadError(
                f"{host} answered {file_response.status_code} with another redirect; only one hop is followed",
                reason="unexpected_redirect",
                host=host,
                status=file_response.status_code,
            )
        if not file_response.is_success:
            await file_response.aclose()
            raise DownloadError(
                f"{host} answered {file_response.status_code} for the file"
                + (
                    "; the download location has expired, call the download operation again for a fresh one"
                    if file_response.status_code == 403
                    else ""
                ),
                reason="unavailable",
                host=host,
                status=file_response.status_code,
            )
        return AsyncDownload(file_response, location=location)

    async def paginate(
        self,
        method_name: str,
        *,
        max_pages: int | None = None,
        max_items: int | None = None,
        progress: PaginationProgress | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[Any]:
        """``Client.paginate``'s async counterpart: ``async for item in client.paginate(...)``."""
        cursor = kwargs.pop("cursor", None)
        async for item in _awalk_items(
            getattr(self, method_name),
            method_name,
            filters=kwargs,
            cursor=cursor,
            max_pages=max_pages,
            max_items=max_items,
            progress=progress,
        ):
            yield item

    async def paginate_pages(
        self,
        method_name: str,
        *,
        max_pages: int | None = None,
        max_items: int | None = None,
        progress: PaginationProgress | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[Any]:
        """``Client.paginate_pages``'s async counterpart."""
        cursor = kwargs.pop("cursor", None)
        async for page in _awalk_pages(
            getattr(self, method_name),
            method_name,
            filters=kwargs,
            cursor=cursor,
            max_pages=max_pages,
            max_items=max_items,
            progress=progress,
        ):
            yield page

    async def stream(
        self,
        path: str = "/api/v1/stream",
        *,
        query: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        last_event_id: str | None = None,
        max_retries: int | None = None,
        backoff_initial: float = DEFAULT_BACKOFF_INITIAL,
        backoff_max: float = DEFAULT_BACKOFF_MAX,
    ) -> AsyncIterator[ServerSentEvent]:
        """Read a Server-Sent Events endpoint, reconnecting for you after every disconnect.

        ``path`` defaults to ``GET /api/v1/stream``, the one documented SSE
        route. Resume is automatic: every reconnect sends ``Last-Event-ID``
        set to the ``id`` of the last frame this walk saw (or ``last_event_id``
        on the very first connection, to continue a walk started in an earlier
        process) -- the same header the stream's own resume contract reads
        (``backend/docs/internal-api/028-public-v1-stream-sse.md``), so a
        disconnect never skips or repeats a frame this walk already delivered.

        Backoff between reconnects is exponential from ``backoff_initial``
        (3 s, matching a browser ``EventSource``'s own default), capped at
        ``backoff_max`` (30 s) -- or the server's own ``retry:`` field for
        that one attempt, when the stream sent one -- and resets after a
        connection opens successfully, so one blip in an otherwise long-lived
        stream does not creep the delay towards the cap. ``max_retries``
        bounds consecutive failed reconnects (``None``, the default, retries
        forever, matching a browser ``EventSource``). A terminal
        ``event: error`` frame whose payload says the credential was
        permanently refused (``"retry": false``) raises ``StreamClosedError``
        immediately instead of reconnecting; one that says ``"retry": true``
        (a transient store outage) backs off and reconnects like any other
        disconnect.

        Cancellation (``asyncio.CancelledError``, breaking out of the
        surrounding ``async for``) closes the open connection and propagates
        uninterrupted -- nothing here catches it::

            async with oxinsider.AsyncClient() as client:
                async for event in client.stream(query={"min_size": "10000"}):
                    if event.event == "resync":
                        refetch_from_rest()
                        continue
                    handle(event.json())
        """

        async def open_response(resume_from: str | None) -> httpx.Response:
            request_headers = dict(headers or {})
            if resume_from is not None:
                request_headers["Last-Event-ID"] = resume_from
            return await self.request("GET", path, query=query, headers=request_headers, stream=True)

        async for event in _stream_events(
            open_response,
            last_event_id=last_event_id,
            max_retries=max_retries,
            backoff_initial=backoff_initial,
            backoff_max=backoff_max,
        ):
            yield event

    async def _call(
        self,
        operation_id: str,
        *,
        path_params: Mapping[str, str],
        query: Mapping[str, Any],
        body: Any = None,
        if_none_match: str | None = None,
        idempotency_key: str | None = None,
        raw: bool = False,
    ) -> Any:
        operation = OPERATIONS[operation_id]
        path = _operation_path(operation_id, path_params)
        return await self.request(
            operation.method,
            path,
            query=query,
            body=body,
            if_none_match=if_none_match,
            idempotency_key=idempotency_key,
            headers={"Accept": operation.accept},
            raw=raw,
        )

    async def _download(
        self,
        operation_id: str,
        *,
        path_params: Mapping[str, str],
        query: Mapping[str, Any],
    ) -> AsyncDownload:
        operation = OPERATIONS[operation_id]
        return await self.download(operation.method, _operation_path(operation_id, path_params), query=query)


class _AsyncResponseClient(AsyncResponseOperationsMixin):
    """The operation methods of one ``AsyncClient``, answering with ``ApiResponse``.

    Reached as ``async_client.with_response``; it holds no state of its own
    and sends the same requests the client does.
    """

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def request(self, method: str, path: str, **kwargs: Any) -> ApiResponse[Any]:
        """``AsyncClient.request`` with ``raw=True``."""
        return await self._client.request(method, path, raw=True, **kwargs)

    async def _call(self, operation_id: str, **kwargs: Any) -> ApiResponse[Any]:
        return await self._client._call(operation_id, raw=True, **kwargs)

    async def _download(self, operation_id: str, **kwargs: Any) -> AsyncDownload:
        # A redirect-only operation already answers with the file's own headers.
        return await self._client._download(operation_id, **kwargs)
