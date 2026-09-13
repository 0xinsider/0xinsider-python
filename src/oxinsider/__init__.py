"""Official Python client for the 0xinsider Developer API.

https://0xinsider.com/developers
"""

from ._client import API_KEY_ENV, NOT_MODIFIED, PRODUCTION_BASE_URL, SANDBOX_BASE_URL, Client
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
from ._version import __version__

__all__ = [
    "API_KEY_ENV",
    "NOT_MODIFIED",
    "OPENAPI_VERSION",
    "OPERATIONS",
    "PRODUCTION_BASE_URL",
    "SANDBOX_BASE_URL",
    "AuthenticationError",
    "BadRequestError",
    "Client",
    "NotFoundError",
    "OxinsiderApiError",
    "OxinsiderConnectionError",
    "OxinsiderError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "SubscriptionRequiredError",
    "__version__",
]
