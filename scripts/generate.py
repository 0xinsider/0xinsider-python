"""Generate src/oxinsider/_operations.py and _provenance.py from the 0xinsider OpenAPI document.

Usage: python scripts/generate.py [path-or-url] [--app-commit SHA]
Default source: https://0xinsider.com/api/v1/openapi.json

_provenance.py records which document this release was generated from: the
SHA-256 of the document bytes as fetched, its info.version, the operation
count, and the 0xinsider/0xinsider commit that last changed
web/public/api/v1/openapi.json (``--app-commit``, the ``OXINSIDER_APP_COMMIT``
environment variable, or a lookup of the GitHub commits API; ``GH_TOKEN`` is
used when set). An app commit that cannot be resolved is recorded as ``None``
and reported on stderr, never guessed.
"""

from __future__ import annotations

import hashlib
import json
import keyword
import os
import re
import sys
import textwrap
import urllib.request
from pathlib import Path

DEFAULT_SOURCE = "https://0xinsider.com/api/v1/openapi.json"
PACKAGE = Path(__file__).resolve().parent.parent / "src" / "oxinsider"
OUTPUT = PACKAGE / "_operations.py"
PROVENANCE_OUTPUT = PACKAGE / "_provenance.py"
APP_REPOSITORY = "0xinsider/0xinsider"
APP_SPEC_PATH = "web/public/api/v1/openapi.json"
METHODS = ("get", "post", "put", "patch", "delete")
# Operations whose success response is a Server-Sent Events stream. They are
# reachable through Client.request(..., stream=True), not a generated method.
STREAMING_CONTENT = "text/event-stream"
# Operations whose only success response is a redirect (a 3xx and no 2xx): the
# finished export (302 to the artifact host) and the OpenAPI document (307 to
# the web origin). Their method returns Client.download(...), which follows the
# one hop without forwarding the credential and streams the file.
REDIRECT_CODES = ("301", "302", "303", "307", "308")


def load(source: str) -> bytes:
    if source.startswith("http://") or source.startswith("https://"):
        request = urllib.request.Request(source, headers={"User-Agent": "0xinsider-python-generator"})
        with urllib.request.urlopen(request, timeout=60) as response:  # noqa: S310 - fixed https source
            return response.read()
    return Path(source).read_bytes()


def resolve_app_commit(explicit: str | None) -> str | None:
    """The app commit the document belongs to, or None when it cannot be known."""
    candidate = explicit or os.environ.get("OXINSIDER_APP_COMMIT")
    if candidate:
        return candidate
    url = f"https://api.github.com/repos/{APP_REPOSITORY}/commits?path={APP_SPEC_PATH}&per_page=1"
    headers = {"User-Agent": "0xinsider-python-generator", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310 - fixed https source
            commits = json.load(response)
    except OSError as error:
        print(f"warning: app commit not resolved from the GitHub API ({error}); recording None", file=sys.stderr)
        return None
    if not commits:
        print("warning: the GitHub API listed no commit for the document; recording None", file=sys.stderr)
        return None
    return str(commits[0]["sha"])


def provenance(raw: bytes, doc: dict, *, source: str, app_commit: str | None, operation_count: int) -> str:
    version = doc.get("info", {}).get("version", "unknown")
    commit = "None" if app_commit is None else f'"{app_commit}"'
    return (
        '"""Generated from the 0xinsider OpenAPI document by scripts/generate.py. Do not edit.\n\n'
        "Which document this release was generated from. OPENAPI_SHA256 is the SHA-256 of the\n"
        "document bytes as fetched; APP_COMMIT is the 0xinsider/0xinsider commit that last changed\n"
        "web/public/api/v1/openapi.json when it could be resolved, else None.\n"
        '"""\n\n'
        "from __future__ import annotations\n\n"
        f'OPENAPI_SOURCE = "{source}"\n'
        f'OPENAPI_SHA256 = "{hashlib.sha256(raw).hexdigest()}"\n'
        f'OPENAPI_VERSION = "{version}"\n'
        f"OPERATION_COUNT = {operation_count}\n"
        f'APP_REPOSITORY = "{APP_REPOSITORY}"\n'
        f'APP_SPEC_PATH = "{APP_SPEC_PATH}"\n'
        f"APP_COMMIT: str | None = {commit}\n"
    )


def snake(name: str) -> str:
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return name.lower()


def python_name(name: str) -> str:
    candidate = re.sub(r"[^0-9a-zA-Z_]", "_", name.replace("[]", ""))
    if keyword.iskeyword(candidate) or candidate in {"self", "body", "headers"}:
        candidate += "_"
    return candidate


def first_sentence(text: str, limit: int = 300) -> str:
    text = " ".join((text or "").split())
    if len(text) <= limit:
        return text
    cut = text[:limit]
    return cut[: cut.rfind(" ")] + " ..."


def success_content_types(operation: dict) -> list[str]:
    for code in ("200", "201", "202"):
        response = operation.get("responses", {}).get(code)
        if isinstance(response, dict):
            return list((response.get("content") or {}).keys())
    return []


def is_redirect_only(operation: dict) -> bool:
    responses = operation.get("responses", {})
    has_success = any(code.startswith("2") for code in responses)
    has_redirect = any(code in REDIRECT_CODES for code in responses)
    return has_redirect and not has_success


def has_no_success(operation: dict) -> bool:
    """An operation the server documents only to refuse (GET /api/v1/mcp answers
    405: it offers no server-to-client stream). It stays in OPERATIONS with its
    method and path, and gets no method, because a call could only raise."""
    responses = operation.get("responses", {})
    return not any(code.startswith(("2", "3")) for code in responses)


def generate(doc: dict) -> tuple[str, int]:
    entries = []
    methods = []
    for path, item in doc.get("paths", {}).items():
        shared_params = item.get("parameters", [])
        for method in METHODS:
            operation = item.get(method)
            if not isinstance(operation, dict):
                continue
            operation_id = operation.get("operationId")
            if not operation_id:
                continue
            params = [*shared_params, *operation.get("parameters", [])]
            seen = set()
            unique = []
            for param in params:
                if "$ref" in param or param.get("name", "").endswith("[]"):
                    continue
                key = (param.get("in"), param.get("name"))
                if key in seen:
                    continue
                seen.add(key)
                unique.append(param)
            path_params = [p for p in unique if p.get("in") == "path"]
            query_params = [p for p in unique if p.get("in") == "query"]
            header_params = [p for p in unique if p.get("in") == "header"]
            has_body = "requestBody" in operation
            content_types = success_content_types(operation)
            streaming = content_types == [STREAMING_CONTENT]
            redirect = is_redirect_only(operation)
            # The Accept header a method sends: the operation's success media type
            # (text/markdown for the context.md routes), else application/json.
            accept = content_types[0] if len(content_types) == 1 and not streaming else "application/json"
            entries.append(
                {
                    "operation_id": operation_id,
                    "method": method.upper(),
                    "path": path,
                    "streaming": streaming,
                    "redirect": redirect,
                    "accept": accept,
                }
            )
            if streaming or has_no_success(operation):
                continue
            name = snake(operation_id)
            args = ["self"]
            args += [f"{python_name(p['name'])}: str" for p in path_params]
            if has_body:
                required = operation["requestBody"].get("required", False)
                args.append("body: Any" if required else "body: Any = None")
            kw = [f"{python_name(p['name'])}: Any = None" for p in query_params]
            for header in header_params:
                hname = header["name"].lower()
                if hname == "if-none-match":
                    kw.append("if_none_match: str | None = None")
                elif hname == "idempotency-key":
                    kw.append("idempotency_key: str | None = None")
            if kw:
                args.append("*")
                args += kw
            summary = first_sentence(operation.get("summary") or operation_id, 200)
            description = first_sentence(operation.get("description") or "")
            doc_lines = [f"{summary}.".replace("..", "."), "", f"``{method.upper()} {path}`` (operationId ``{operation_id}``)."]
            if description:
                doc_lines += ["", *textwrap.wrap(description, 88)]
            if redirect:
                doc_lines += [
                    "",
                    *textwrap.wrap(
                        "Returns a ``Download``: the redirect is followed once, without the credential, "
                        "and the file is streamed. Iterate it, ``save(path)`` it for its SHA-256, or "
                        "``read()`` it (bounded); close it when done. A redirect or transfer fault "
                        "raises ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.",
                        88,
                    ),
                ]
            if query_params:
                doc_lines += ["", "Query parameters:"]
                for p in query_params:
                    pdesc = first_sentence(p.get("description") or "", 160)
                    doc_lines.append(f"    {python_name(p['name'])}: {pdesc}".rstrip())
            docstring = "\n        ".join(line.replace('"""', "'''") for line in doc_lines)
            path_map = ", ".join(f'"{p["name"]}": {python_name(p["name"])}' for p in path_params)
            query_map = ", ".join(f'"{p["name"]}": {python_name(p["name"])}' for p in query_params)
            header_args = []
            if any(h["name"].lower() == "if-none-match" for h in header_params):
                header_args.append("if_none_match=if_none_match")
            if any(h["name"].lower() == "idempotency-key" for h in header_params):
                header_args.append("idempotency_key=idempotency_key")
            call = [f'"{operation_id}"', f"path_params={{{path_map}}}", f"query={{{query_map}}}"]
            if has_body:
                call.append("body=body")
            call += header_args
            signature = ",\n        ".join(args)
            if redirect:
                methods.append(
                    f"    def {name}(\n        {signature},\n    ) -> Download:\n"
                    f'        """{docstring}\n        """\n'
                    f"        return self._download({', '.join(call[:3])})\n"
                )
                continue
            methods.append(
                f"    def {name}(\n        {signature},\n    ) -> Any:\n"
                f'        """{docstring}\n        """\n'
                f"        return self._call({', '.join(call)})\n"
            )
    table = ",\n".join(
        f'    "{e["operation_id"]}": Operation("{e["method"]}", "{e["path"]}", '
        f"streaming={e['streaming']}, redirect={e['redirect']}"
        + (f', accept="{e["accept"]}"' if e["accept"] != "application/json" else "")
        + ")"
        for e in entries
    )
    version = doc.get("info", {}).get("version", "unknown")
    header = (
        '"""Generated from the 0xinsider OpenAPI document by scripts/generate.py. Do not edit."""\n\n'
        "from __future__ import annotations\n\n"
        "from typing import Any, NamedTuple\n\n"
        "from ._download import Download\n\n\n"
        f'OPENAPI_VERSION = "{version}"\n\n\n'
        "class Operation(NamedTuple):\n"
        "    method: str\n"
        "    path: str\n"
        "    streaming: bool = False\n"
        "    redirect: bool = False\n"
        '    accept: str = "application/json"\n\n\n'
        f"OPERATIONS: dict[str, Operation] = {{\n{table},\n}}\n\n\n"
        "class OperationsMixin:\n"
        '    """One method per documented operation. Each returns the decoded JSON body,\n'
        '    except a redirect-only operation, which returns a streaming ``Download``."""\n\n'
        "    def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by Client\n"
        "        raise NotImplementedError\n\n"
        "    def _download(self, operation_id: str, **kwargs: Any) -> Download:  # pragma: no cover - provided by Client\n"
        "        raise NotImplementedError\n\n"
    )
    source = header + "\n".join(methods)
    # Blank docstring lines must not carry the indentation.
    return re.sub(r"[ \t]+\n", "\n", source), len(entries)


def main() -> None:
    args = [arg for arg in sys.argv[1:]]
    app_commit: str | None = None
    if "--app-commit" in args:
        index = args.index("--app-commit")
        app_commit = args[index + 1]
        del args[index : index + 2]
    source = args[0] if args else DEFAULT_SOURCE
    raw = load(source)
    doc = json.loads(raw)
    operations, count = generate(doc)
    OUTPUT.write_text(operations)
    print(f"wrote {OUTPUT} ({count} operations)")
    recorded_source = source if source.startswith(("http://", "https://")) else f"{APP_REPOSITORY}:{APP_SPEC_PATH}"
    PROVENANCE_OUTPUT.write_text(
        provenance(raw, doc, source=recorded_source, app_commit=resolve_app_commit(app_commit), operation_count=count)
    )
    print(f"wrote {PROVENANCE_OUTPUT}")


if __name__ == "__main__":
    main()
