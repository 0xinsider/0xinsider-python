"""Official Python client for the 0xinsider Developer API.

https://0xinsider.com/developers

Every operation's request and response shapes live in ``oxinsider.types``,
generated from the same OpenAPI document as the methods themselves.
"""

from . import types
from ._data_quality import DataQualityAssessment, DataQualityFailure, assess_data_quality
from ._client import (
    API_KEY_ENV,
    DEFAULT_MAX_CONCURRENCY,
    NOT_MODIFIED,
    PRODUCTION_BASE_URL,
    SANDBOX_BASE_URL,
    AsyncClient,
    Client,
)
from ._download import DEFAULT_MAX_READ_BYTES, AsyncDownload, Download, DownloadError, SavedDownload
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
    StreamClosedError,
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
from ._stream import DEFAULT_BACKOFF_INITIAL, DEFAULT_BACKOFF_MAX, ServerSentEvent
from ._version import __version__
from .types import NotModifiedResponse

__all__ = [
    "assess_data_quality",
    "API_KEY_ENV",
    "APP_COMMIT",
    "CURSOR_HISTORY_LIMIT",
    "DEFAULT_BACKOFF_INITIAL",
    "DEFAULT_BACKOFF_MAX",
    "DEFAULT_MAX_CONCURRENCY",
    "DEFAULT_MAX_READ_BYTES",
    "NOT_MODIFIED",
    "OPENAPI_SHA256",
    "OPENAPI_VERSION",
    "OPERATIONS",
    "OPERATION_COUNT",
    "PRODUCTION_BASE_URL",
    "SANDBOX_BASE_URL",
    "ApiResponse",
    "AsyncClient",
    "AsyncDownload",
    "AuthenticationError",
    "BadRequestError",
    "Budget",
    "Client",
    "DataQualityAssessment",
    "DataQualityFailure",
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
    "ServerSentEvent",
    "StreamClosedError",
    "SubscriptionRequiredError",
    "__version__",
    "pagination_checkpoint",
    "types",
]
