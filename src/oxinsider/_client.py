"""The 0xinsider Developer API client."""

from __future__ import annotations

import os
from collections.abc import Iterator, Mapping
from typing import Any
from urllib.parse import quote

import httpx

from ._download import Download, DownloadError
from ._errors import OxinsiderApiError, OxinsiderConnectionError, error_class_for
from ._operations import OPERATIONS, OperationsMixin
from ._pagination import PaginationProgress
from ._pagination import paginate as _walk_items
from ._pagination import paginate_pages as _walk_pages
from ._policy import assert_credential_destination, is_trusted_destination
from ._version import __version__

PRODUCTION_BASE_URL = "https://api.0xinsider.com"
SANDBOX_BASE_URL = "https://0xinsider.com/sandbox"
API_KEY_ENV = "OXINSIDER_API_KEY"

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
    ) -> Any:
        """Send one request and return the decoded body.

        A JSON response returns the decoded object. A 304 for ``if_none_match``
        returns ``{"object": "not_modified", "data": None}``. A non-JSON response
        (Markdown, CSV) returns the text. With ``stream=True`` the open
        ``httpx.Response`` is returned for the caller to iterate and close, which
        is how the SSE stream (``GET /api/v1/stream``) is read.
        """
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
            return {**NOT_MODIFIED, "etag": response.headers.get("etag")}
        if not response.is_success:
            raise self._error(response)
        if response.status_code == 204 or not response.content:
            return None
        if "json" in response.headers.get("content-type", ""):
            return response.json()
        return response.text

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
        )
