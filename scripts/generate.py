"""Generate src/oxinsider/_operations.py from the published 0xinsider OpenAPI document.

Usage: python scripts/generate.py [path-or-url]
Default source: https://0xinsider.com/api/v1/openapi.json
"""

from __future__ import annotations

import json
import keyword
import re
import sys
import textwrap
import urllib.request
from pathlib import Path

DEFAULT_SOURCE = "https://0xinsider.com/api/v1/openapi.json"
OUTPUT = Path(__file__).resolve().parent.parent / "src" / "oxinsider" / "_operations.py"
METHODS = ("get", "post", "put", "patch", "delete")
# Operations whose success response is a Server-Sent Events stream. They are
# reachable through Client.request(..., stream=True), not a generated method.
STREAMING_CONTENT = "text/event-stream"
# Operations whose only success response is a redirect (a 3xx and no 2xx): the
# finished export (302 to the artifact host) and the OpenAPI document (307 to
# the web origin). Their method returns Client.download(...), which follows the
# one hop without forwarding the credential and streams the file.
REDIRECT_CODES = ("301", "302", "303", "307", "308")


def load(source: str) -> dict:
    if source.startswith("http://") or source.startswith("https://"):
        request = urllib.request.Request(source, headers={"User-Agent": "0xinsider-python-generator"})
        with urllib.request.urlopen(request, timeout=60) as response:  # noqa: S310 - fixed https source
            return json.load(response)
    return json.loads(Path(source).read_text())


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


def generate(doc: dict) -> str:
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
            entries.append(
                {
                    "operation_id": operation_id,
                    "method": method.upper(),
                    "path": path,
                    "streaming": streaming,
                    "redirect": redirect,
                }
            )
            if streaming:
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
        f"streaming={e['streaming']}, redirect={e['redirect']})"
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
        "    redirect: bool = False\n\n\n"
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
    return re.sub(r"[ \t]+\n", "\n", source)


def main() -> None:
    source = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SOURCE
    OUTPUT.write_text(generate(load(source)))
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
