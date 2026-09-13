"""The 0xinsider Developer API client."""

from __future__ import annotations

import os
from collections.abc import Iterator, Mapping
from typing import Any
from urllib.parse import quote

import httpx

from ._errors import OxinsiderApiError, OxinsiderConnectionError, error_class_for
from ._operations import OPERATIONS, OperationsMixin
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
        request_headers = {
            "Accept": "application/json",
            "User-Agent": f"0xinsider-python/{__version__}",
        }
        if self.api_key:
            request_headers["Authorization"] = f"Bearer {self.api_key}"
        if if_none_match:
            request_headers["If-None-Match"] = if_none_match
        if idempotency_key:
            request_headers["Idempotency-Key"] = idempotency_key
        request_headers.update(headers or {})
        request = self._http.build_request(
            method.upper(),
            f"{self.base_url}{path}",
            params=_clean_query(query),
            json=body,
            headers=request_headers,
        )
        try:
            response = self._http.send(request, stream=stream)
        except httpx.HTTPError as error:
            raise OxinsiderConnectionError(f"{method.upper()} {path} failed: {error}") from error
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

    def paginate(self, method_name: str, **kwargs: Any) -> Iterator[Any]:
        """Yield every item of a cursor-paginated list, following ``next_cursor``.

        ``client.paginate("list_whale_trades", min_grade="A", limit=100)``
        """
        method = getattr(self, method_name)
        cursor = kwargs.pop("cursor", None)
        while True:
            page = method(cursor=cursor, **kwargs)
            data = page.get("data") if isinstance(page, dict) else None
            if isinstance(data, list):
                yield from data
            next_cursor = page.get("next_cursor") if isinstance(page, dict) else None
            if not (isinstance(page, dict) and page.get("has_more") and next_cursor):
                return
            cursor = next_cursor

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
        path = operation.path
        for name, value in path_params.items():
            path = path.replace("{" + name + "}", quote(str(value), safe="@"))
        return self.request(
            operation.method,
            path,
            query=query,
            body=body,
            if_none_match=if_none_match,
            idempotency_key=idempotency_key,
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
