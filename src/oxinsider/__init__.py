"""Official Python client for the 0xinsider Developer API.

https://0xinsider.com/developers

Every operation's request and response shapes live in ``oxinsider.types``,
generated from the same OpenAPI document as the methods themselves.
"""

from . import types
from ._client import API_KEY_ENV, NOT_MODIFIED, PRODUCTION_BASE_URL, SANDBOX_BASE_URL, Client
from ._download import DEFAULT_MAX_READ_BYTES, Download, DownloadError, SavedDownload
from ._errors import (
    AuthenticationError,
    BadRequestError,
    NotFoundError,
    OxinsiderApiError,
    OxinsiderConnectionError,
    OxinsiderError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
    SubscriptionRequiredError,
)
from ._operations import OPENAPI_VERSION, OPERATIONS
from ._pagination import (
    CURSOR_HISTORY_LIMIT,
    PaginationError,
    PaginationProgress,
    pagination_checkpoint,
)
from ._policy import InsecureTransportError
from ._response import ApiResponse, Budget
from ._provenance import APP_COMMIT, OPENAPI_SHA256, OPERATION_COUNT
from ._version import __version__
from .types import NotModifiedResponse

__all__ = [
    "API_KEY_ENV",
    "APP_COMMIT",
    "CURSOR_HISTORY_LIMIT",
    "DEFAULT_MAX_READ_BYTES",
    "NOT_MODIFIED",
    "OPENAPI_SHA256",
    "OPENAPI_VERSION",
    "OPERATIONS",
    "OPERATION_COUNT",
    "PRODUCTION_BASE_URL",
    "SANDBOX_BASE_URL",
    "ApiResponse",
    "AuthenticationError",
    "BadRequestError",
    "Budget",
    "Client",
    "Download",
    "DownloadError",
    "InsecureTransportError",
    "NotFoundError",
    "NotModifiedResponse",
    "OxinsiderApiError",
    "OxinsiderConnectionError",
    "OxinsiderError",
    "PaginationError",
    "PaginationProgress",
    "PermissionDeniedError",
    "RateLimitedError",
    "SavedDownload",
    "ServerError",
    "SubscriptionRequiredError",
    "__version__",
    "pagination_checkpoint",
    "types",
]
