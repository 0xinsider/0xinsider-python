"""Where a credential may go.

The API key travels as a bearer header, so the destination decides who
receives it. A credential is sent over ``https://`` anywhere, and over
``http://`` only to a loopback host (a backend on ``localhost``,
``127.0.0.1`` or ``[::1]``). Anything else is refused with
``InsecureTransportError`` before the request exists, so a mistyped base URL
or a plain-http proxy never sees the key. Redirects are never followed
automatically (see ``Client.download``), so an ``https://`` API answer cannot
downgrade a request to ``http://`` behind the client's back.

Owned outside the generated code so regeneration cannot loosen it.
"""

from __future__ import annotations

import ipaddress

import httpx

from ._errors import OxinsiderError


class InsecureTransportError(OxinsiderError):
    """A credential would have been sent over plain HTTP to a host that is not loopback.

    Raised before any request is made. ``origin`` is the refused destination
    (scheme, host and port); the credential is never part of the message.
    """

    def __init__(self, origin: str, *, purpose: str = "the API key") -> None:
        super().__init__(
            f"refusing to send {purpose} to {origin}: use https://, or http:// only on a loopback host "
            "(localhost, 127.0.0.1, [::1])"
        )
        self.origin = origin


def is_loopback_host(host: str) -> bool:
    """``localhost``, any ``127.0.0.0/8`` address, or ``::1`` (bracketed or not)."""
    name = host.strip("[]").lower()
    if name == "localhost":
        return True
    try:
        return ipaddress.ip_address(name).is_loopback
    except ValueError:
        return False


def is_trusted_destination(url: httpx.URL) -> bool:
    """``https:`` anywhere, or ``http:`` to a loopback host only."""
    if url.scheme == "https":
        return True
    return url.scheme == "http" and is_loopback_host(url.host)


def origin_of(url: httpx.URL) -> str:
    return f"{url.scheme}://{url.netloc.decode('ascii')}"


def assert_credential_destination(url: httpx.URL, *, purpose: str = "the API key") -> None:
    """Raise ``InsecureTransportError`` unless ``url`` may receive a credential."""
    if not is_trusted_destination(url):
        raise InsecureTransportError(origin_of(url), purpose=purpose)
