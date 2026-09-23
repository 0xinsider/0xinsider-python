"""Typed errors for the 0xinsider Developer API V1 error envelope."""

from __future__ import annotations

from typing import Any

from ._response import ApiResponse


class OxinsiderError(Exception):
    """Base class for every error this package raises."""


class OxinsiderConnectionError(OxinsiderError):
    """The request did not produce an HTTP response (DNS, TLS, timeout, reset)."""


class OxinsiderApiError(OxinsiderError):
    """A non-2xx response.

    ``code`` is the stable V1 class (``bad_request``, ``invalid_api_key``,
    ``subscription_required``, ``forbidden``, ``not_found``, ``account_locked``,
    ``rate_limited``, ``rate_limit_unavailable``, ``internal_error``). ``reason`` is
    the additive, specific cause when the API sends one: branch on it first.
    A 408 transport timeout has an empty body, so ``code`` is ``None`` there.

    ``response`` is the failed response itself (#16175): ``status``, ``headers``
    and the parsed ``data``, with the same ``rate_limit``, ``monthly_quota``,
    ``request_id`` and ``retry_after`` accessors a success has, so a 429 can be
    handled from the window the API described rather than from a guess. It is
    ``None`` only for an error built without one.
    """

    def __init__(
        self,
        status: int,
        message: str,
        *,
        code: str | None = None,
        reason: str | None = None,
        param: str | None = None,
        retry_at: str | None = None,
        retry_after: float | None = None,
        request_id: str | None = None,
        body: Any = None,
        response: ApiResponse[Any] | None = None,
    ) -> None:
        super().__init__(f"{status} {code or 'error'}: {message}")
        self.status = status
        self.message = message
        self.code = code
        self.reason = reason
        self.param = param
        self.retry_at = retry_at
        self.retry_after = retry_after
        self.request_id = request_id
        self.body = body
        self.response = response


class BadRequestError(OxinsiderApiError):
    """400: a request parameter is invalid (see ``param``)."""


class AuthenticationError(OxinsiderApiError):
    """401: the credential is missing, invalid, expired or revoked."""


class SubscriptionRequiredError(OxinsiderApiError):
    """402: the account needs an active Pro subscription for this operation."""


class PermissionDeniedError(OxinsiderApiError):
    """403: the credential cannot use this operation (for OAuth, a missing scope)."""


class NotFoundError(OxinsiderApiError):
    """404: the resource does not exist, or is not released yet (see ``reason``)."""


class RateLimitedError(OxinsiderApiError):
    """429: a rate limit was exceeded. Wait ``retry_after`` seconds before retrying."""


class ServerError(OxinsiderApiError):
    """5xx: the API failed. 503 responses carry ``retry_after`` when retrying is safe."""


_BY_STATUS: dict[int, type[OxinsiderApiError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    402: SubscriptionRequiredError,
    403: PermissionDeniedError,
    404: NotFoundError,
    429: RateLimitedError,
}


def error_class_for(status: int) -> type[OxinsiderApiError]:
    if status >= 500:
        return ServerError
    return _BY_STATUS.get(status, OxinsiderApiError)


class StreamClosedError(OxinsiderError):
    """``AsyncClient.stream`` ended on a documented ``event: error`` frame, not a disconnect.

    ``GET /api/v1/stream`` ends the body with this frame instead of a plain
    close when the credential backing an open stream is revoked, rotated,
    de-scoped or otherwise refused while the stream is open, or when the
    credential store itself stops answering
    (``backend/docs/internal-api/028-public-v1-stream-sse.md``). ``code`` and
    ``message`` are the frame's own ``error`` object; ``retry`` is the frame's
    own verdict on whether reconnecting is worth it -- ``False`` for a
    permanently refused credential, ``True`` for a transient one
    (``database_unavailable``, with ``retry_at`` naming when to try again).
    ``AsyncClient.stream`` stops reconnecting and raises this when ``retry`` is
    ``False``; it backs off and reconnects on its own when ``retry`` is ``True``.
    """

    def __init__(
        self,
        *,
        code: str | None,
        message: str,
        retry: bool,
        retry_at: str | None = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(f"stream closed ({code or 'error'}): {message}")
        self.code = code
        self.message = message
        self.retry = retry
        self.retry_at = retry_at
        self.request_id = request_id
