"""A redirect-only operation's file, streamed from the host the API points at.

``GET /api/v1/trader/{address}/export/download`` answers ``302`` with a
short-lived presigned ``Location`` on the artifact host once the job is
``ready``; ``GET /api/v1/openapi.json`` answers ``307`` to the web origin.
The client follows that one hop itself: the bearer credential is sent to the
API origin only, never to the ``Location`` host, and the bytes are streamed,
so memory stays bounded whatever the file size. No manifest or checksum is
published for an export; ``Download.save`` computes a SHA-256 of what it
wrote, and the artifact's own headers (``content_type``, ``content_encoding``,
``content_length``, ``etag``, ``filename``) are surfaced as received.
"""

from __future__ import annotations

import hashlib
import os
from collections.abc import Iterator
from dataclasses import dataclass
from email.message import Message
from typing import IO

import httpx

from ._errors import OxinsiderError

# ``Download.read`` refuses to buffer more than this unless told otherwise:
# 64 MiB. Use ``save`` or ``iter_bytes`` for anything larger.
DEFAULT_MAX_READ_BYTES = 64 * 1024 * 1024

DEFAULT_CHUNK_SIZE = 64 * 1024


class DownloadError(OxinsiderError):
    """The redirect to the file, or the file transfer itself, failed.

    ``reason`` is one of:

    - ``not_redirected``: the API answered with a success status instead of a
      redirect, so there is no file location to follow.
    - ``missing_location``: the redirect carried no ``Location`` header.
    - ``insecure_location``: the location is plain ``http://`` on a host that is
      not loopback; the transfer is refused before any request is sent.
    - ``unexpected_redirect``: the file host answered with another redirect;
      only the one documented hop is followed.
    - ``unavailable``: the file host answered a non-2xx ``status`` (an expired
      presigned URL answers 403: call the download operation again for a fresh
      location).
    - ``too_large``: ``read`` reached ``max_bytes`` before the end of the file.
    - ``interrupted``: the connection to the file host failed mid-transfer.

    The message never carries the signed location: ``host`` names where the
    file lives and ``status`` the file host's answer when there was one.
    """

    def __init__(
        self,
        message: str,
        *,
        reason: str,
        host: str | None = None,
        status: int | None = None,
    ) -> None:
        super().__init__(message)
        self.reason = reason
        self.host = host
        self.status = status


@dataclass(frozen=True)
class SavedDownload:
    """What ``Download.save`` wrote."""

    path: str
    bytes_written: int
    #: Hex SHA-256 of exactly the bytes written to ``path``.
    sha256: str
    content_type: str | None
    content_encoding: str | None
    filename: str | None
    #: True when the bytes were decoded from ``content_encoding`` (gzip) first.
    decoded: bool


def _filename_from_disposition(value: str | None) -> str | None:
    if not value:
        return None
    message = Message()
    message["Content-Disposition"] = value
    filename = message.get_param("filename", header="Content-Disposition")
    if isinstance(filename, tuple):
        # RFC 2231 encoded: (charset, language, value).
        return filename[2] or None
    return filename or None


class Download:
    """A file the API redirected to, open and streaming.

    Iterate ``iter_bytes()`` for the decoded file (a gzip-compressed export is
    decompressed to its ``content_type``), ``iter_raw()`` for the bytes exactly
    as the host sent them, ``save(path)`` to write the file and get its SHA-256,
    or ``read()`` for a bounded in-memory copy. Close it, or use it as a context
    manager, so the connection is released; every iterator closes it at the end.
    """

    def __init__(self, response: httpx.Response, *, location: httpx.URL) -> None:
        self._response = response
        self._location = location
        self._closed = False

    @property
    def host(self) -> str:
        """The file host (scheme, host and port), never the signed query."""
        return f"{self._location.scheme}://{self._location.netloc.decode('ascii')}"

    @property
    def status(self) -> int:
        return self._response.status_code

    @property
    def content_type(self) -> str | None:
        """The file's ``Content-Type`` (``application/json``, ``application/x-ndjson``, ``text/csv; charset=utf-8``)."""
        return self._response.headers.get("content-type")

    @property
    def content_encoding(self) -> str | None:
        """``gzip`` for an export: ``iter_bytes`` and ``save`` decode it, ``iter_raw`` does not."""
        return self._response.headers.get("content-encoding")

    @property
    def content_length(self) -> int | None:
        """The size on the wire in bytes (before decoding), when the host says."""
        raw = self._response.headers.get("content-length")
        if raw is None:
            return None
        try:
            return int(raw)
        except ValueError:
            return None

    @property
    def etag(self) -> str | None:
        """The host's ``ETag``: an object identity for conditional requests, not a content hash."""
        return self._response.headers.get("etag")

    @property
    def filename(self) -> str | None:
        """The name the host suggests in ``Content-Disposition`` (``<address>-dataset.json``)."""
        return _filename_from_disposition(self._response.headers.get("content-disposition"))

    @property
    def headers(self) -> httpx.Headers:
        return self._response.headers

    def iter_bytes(self, chunk_size: int = DEFAULT_CHUNK_SIZE) -> Iterator[bytes]:
        """Yield the decoded file in chunks; closes the download at the end."""
        yield from self._iterate(self._response.iter_bytes(chunk_size))

    def iter_raw(self, chunk_size: int = DEFAULT_CHUNK_SIZE) -> Iterator[bytes]:
        """Yield the bytes exactly as sent (gzip-compressed for an export); closes the download at the end."""
        yield from self._iterate(self._response.iter_raw(chunk_size))

    def _iterate(self, chunks: Iterator[bytes]) -> Iterator[bytes]:
        try:
            for chunk in chunks:
                if chunk:
                    yield chunk
        except httpx.HTTPError as error:
            raise DownloadError(
                f"download from {self.host} was interrupted: {error}",
                reason="interrupted",
                host=self.host,
                status=self.status,
            ) from error
        finally:
            self.close()

    def save(
        self,
        path: str | os.PathLike[str] | IO[bytes],
        *,
        decode: bool = True,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
    ) -> SavedDownload:
        """Write the file to ``path`` (a filename or a binary file object).

        With ``decode=True`` (the default) a gzip-compressed export is written
        decompressed, as the file its ``content_type`` names; ``decode=False``
        writes the bytes as sent. Returns the byte count and the SHA-256 of
        exactly what was written. A failure mid-transfer raises
        ``DownloadError`` (``interrupted``); a partial file may be left at
        ``path``.
        """
        chunks = self.iter_bytes(chunk_size) if decode else self.iter_raw(chunk_size)
        digest = hashlib.sha256()
        written = 0
        if hasattr(path, "write"):
            sink: IO[bytes] = path  # type: ignore[assignment]
            for chunk in chunks:
                sink.write(chunk)
                digest.update(chunk)
                written += len(chunk)
            name = getattr(sink, "name", "<stream>")
        else:
            name = os.fspath(path)
            with open(name, "wb") as file:
                for chunk in chunks:
                    file.write(chunk)
                    digest.update(chunk)
                    written += len(chunk)
        return SavedDownload(
            path=str(name),
            bytes_written=written,
            sha256=digest.hexdigest(),
            content_type=self.content_type,
            content_encoding=self.content_encoding,
            filename=self.filename,
            decoded=decode,
        )

    def read(self, *, max_bytes: int = DEFAULT_MAX_READ_BYTES) -> bytes:
        """Return the decoded file, refusing to buffer more than ``max_bytes`` (64 MiB by default)."""
        parts: list[bytes] = []
        total = 0
        for chunk in self.iter_bytes():
            total += len(chunk)
            if total > max_bytes:
                self.close()
                raise DownloadError(
                    f"download from {self.host} exceeds max_bytes={max_bytes}; use save() or iter_bytes()",
                    reason="too_large",
                    host=self.host,
                    status=self.status,
                )
            parts.append(chunk)
        return b"".join(parts)

    def close(self) -> None:
        """Release the connection. Safe to call more than once."""
        if not self._closed:
            self._closed = True
            self._response.close()

    def __enter__(self) -> Download:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def __repr__(self) -> str:
        return (
            f"Download(host={self.host!r}, status={self.status}, content_type={self.content_type!r}, "
            f"content_encoding={self.content_encoding!r}, content_length={self.content_length!r}, "
            f"filename={self.filename!r})"
        )
