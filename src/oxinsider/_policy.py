"""Where a request may go.

Owned outside the generated code so regeneration cannot loosen it.
"""

from __future__ import annotations

import ipaddress

import httpx


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
