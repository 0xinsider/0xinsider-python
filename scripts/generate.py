"""Generate src/oxinsider/types.py, _operations.py and _provenance.py from the 0xinsider OpenAPI document.

Usage: python scripts/generate.py [path-or-url] [--app-commit SHA]
Default source: https://0xinsider.com/api/v1/openapi.json

types.py carries one TypedDict per documented schema, per request body and per
operation response envelope. _operations.py wires them into the method
signatures: an operation returns its own response type, a Markdown operation
returns ``str``, and a redirect-only operation returns a ``Download``. Nothing
about the requests that go out or the objects that come back changes; the
methods still return the decoded body exactly as the API sent it.

Each operation is emitted twice more, as coroutines: ``AsyncOperationsMixin``
and ``AsyncResponseOperationsMixin`` are the same methods `await`-ing
``self._call``/``self._download`` instead of calling them directly, provided
by ``AsyncClient`` on ``httpx.AsyncClient``. One ``Op.render(asynchronous=...)``
keeps all four mixins (plain and ``with_response``, sync and async) generated
from the same signatures and docstrings, so they cannot drift from each other.

Typing policy, applied here and documented in types.py:

* A key the document lists in ``required`` is a required TypedDict key. A key
  it does not is optional (the class is split into a required base and a
  ``total=False`` body), because the API omits it rather than sending null.
* ``nullable`` adds ``| None``: the key is present and its value is JSON null.
  An omitted key and a null value are different facts and neither is a zero.
* ``const`` becomes an exact ``Literal``: it cannot widen without a new schema,
  which is what makes a discriminated union (``oneOf`` + ``discriminator``)
  narrow on it.
* An ``enum`` a caller SENDS becomes a strict ``Literal``: a typo is caught
  before it spends a request. An ``enum`` the API RETURNS becomes
  ``Literal[...] | str``, so a value added to the API after this release is not
  a type error in a client that has not upgraded yet.

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
from typing import Any

DEFAULT_SOURCE = "https://0xinsider.com/api/v1/openapi.json"
PACKAGE = Path(__file__).resolve().parent.parent / "src" / "oxinsider"
OUTPUT = PACKAGE / "_operations.py"
TYPES_OUTPUT = PACKAGE / "types.py"
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
SCALARS = {"string": "str", "integer": "int", "number": "float", "boolean": "bool", "null": "None"}
REF_PREFIX = "#/components/schemas/"


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


def pascal(name: str) -> str:
    parts = [part for part in re.split(r"[^0-9a-zA-Z]+", name) if part]
    joined = "".join(part[:1].upper() + part[1:] for part in parts)
    return joined if joined and not joined[0].isdigit() else f"X{joined}"


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


def literal(value: Any) -> str:
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, (int, float)):
        return repr(value)
    if value is None:
        return "None"
    return json.dumps(str(value))


def union(parts: list[str], *, pep604: bool) -> str:
    """One type expression for a union.

    ``pep604`` picks the form the position allows: ``A | B`` reads better but is
    only legal in an annotation on Python 3.9 (this package's floor), so a
    module-level alias, which the interpreter evaluates, gets ``Union[A, B]``.
    """
    seen: list[str] = []
    for part in parts:
        if part not in seen:
            seen.append(part)
    if not seen:
        return "Any"
    if len(seen) == 1:
        return seen[0]
    if pep604:
        return " | ".join(seen)
    if len(seen) == 2 and "None" in seen:
        return f"Optional[{[p for p in seen if p != 'None'][0]}]"
    return f"Union[{', '.join(seen)}]"


def optional(expr: str, *, pep604: bool) -> str:
    if expr == "Any" or expr.endswith("| None") or expr.startswith("Optional["):
        return expr
    return f"{expr} | None" if pep604 else f"Optional[{expr}]"


class Types:
    """The TypedDicts and aliases for one document, in the order they are emitted."""

    def __init__(self, doc: dict) -> None:
        self.doc = doc
        self.schemas: dict[str, Any] = (doc.get("components") or {}).get("schemas") or {}
        self.blocks: list[tuple[str, str]] = []  # (name, source), in emission order
        self.names: dict[str, str] = {}  # name -> canonical structure key
        self.by_structure: dict[str, str] = {}  # structure key -> name
        self.component_names: dict[str, str] = {}  # component -> emitted name
        self.in_progress: set[str] = set()
        self.request_only = self._request_only_components()

    # -- component reachability ------------------------------------------------

    def _refs(self, node: Any, out: set[str]) -> None:
        if isinstance(node, dict):
            ref = node.get("$ref")
            if isinstance(ref, str) and ref.startswith(REF_PREFIX):
                name = ref[len(REF_PREFIX) :]
                if name not in out:
                    out.add(name)
                    self._refs(self.schemas.get(name), out)
            for key, value in node.items():
                if key != "$ref":
                    self._refs(value, out)
        elif isinstance(node, list):
            for value in node:
                self._refs(value, out)

    def _request_only_components(self) -> set[str]:
        """Components only a request body reaches.

        Their enums are the caller's to get right, so they are typed strictly.
        A component a response also carries stays permissive.
        """
        requests: set[str] = set()
        responses: set[str] = set()
        for _path, item in (self.doc.get("paths") or {}).items():
            for method in METHODS:
                operation = item.get(method)
                if not isinstance(operation, dict):
                    continue
                self._refs(operation.get("requestBody"), requests)
                self._refs(operation.get("responses"), responses)
        return requests - responses

    # -- naming ----------------------------------------------------------------

    def _unique(self, hint: str) -> str:
        name = pascal(hint)
        if name not in self.names:
            return name
        index = 2
        while f"{name}{index}" in self.names:
            index += 1
        return f"{name}{index}"

    @staticmethod
    def _structure(schema: Any, *, strict: bool, bases: tuple[str, ...]) -> str:
        return json.dumps([schema, strict, list(bases)], sort_keys=True)

    # -- emission --------------------------------------------------------------

    def component(self, name: str, *, strict: bool) -> str:
        """The emitted type for ``#/components/schemas/<name>``."""
        if name in self.component_names:
            return self.component_names[name]
        schema = self.schemas.get(name)
        if schema is None:
            return "Any"
        if name in self.in_progress:
            # A self-referential schema: the class is being emitted, and a
            # deferred annotation resolves to it by name.
            return pascal(name)
        self.in_progress.add(name)
        try:
            emitted = pascal(name)
            expr = self.type_of(schema, hint=emitted, strict=strict, pep604=False, component=emitted)
            if expr != emitted:
                # A scalar, a union or a mapping: an alias carries the name the
                # document gave it, so a signature can still say what it is.
                emitted = self._alias(emitted, expr, schema.get("description"))
        finally:
            self.in_progress.discard(name)
        self.component_names[name] = emitted
        return emitted

    def _alias(self, name: str, expr: str, description: str | None) -> str:
        name = self._unique(name)
        self.names[name] = f"alias:{name}"
        lines = []
        if description:
            for line in textwrap.wrap(first_sentence(description, 300), 112):
                lines.append(f"# {line}")
        lines.append(f"{name} = {expr}")
        self.blocks.append((name, "\n".join(lines)))
        return name

    def type_of(
        self,
        schema: Any,
        *,
        hint: str,
        strict: bool,
        pep604: bool,
        component: str | None = None,
    ) -> str:
        """The Python type for one schema node.

        ``hint`` names an inline object if one has to be emitted, ``strict``
        closes enums (a request the caller builds), and ``pep604`` says whether
        ``A | B`` is legal here or the ``Union[A, B]`` form is needed.
        """
        if not isinstance(schema, dict) or schema == {}:
            return "Any"
        ref = schema.get("$ref")
        if isinstance(ref, str) and ref.startswith(REF_PREFIX):
            return self.component(ref[len(REF_PREFIX) :], strict=strict)
        nullable = bool(schema.get("nullable"))
        types = schema.get("type")
        if isinstance(types, list):
            nullable = nullable or "null" in types
            remaining = [t for t in types if t != "null"]
            types = remaining[0] if len(remaining) == 1 else None
            schema = {**schema, "type": types}
        expr = self._bare_type(schema, hint=hint, strict=strict, pep604=pep604, component=component)
        return optional(expr, pep604=pep604) if nullable else expr

    def _bare_type(
        self,
        schema: dict,
        *,
        hint: str,
        strict: bool,
        pep604: bool,
        component: str | None = None,
    ) -> str:
        for key in ("oneOf", "anyOf"):
            members = schema.get(key)
            if isinstance(members, list) and members:
                parts = [
                    self.type_of(member, hint=f"{hint}{index + 1}", strict=strict, pep604=pep604)
                    for index, member in enumerate(members)
                ]
                return union(parts, pep604=pep604)
        if isinstance(schema.get("allOf"), list) and schema["allOf"]:
            return self._all_of(schema, hint=hint, strict=strict, pep604=pep604, component=component)
        if "const" in schema:
            return f"Literal[{literal(schema['const'])}]"
        enum = schema.get("enum")
        if isinstance(enum, list) and enum:
            values = ", ".join(literal(value) for value in enum)
            closed = f"Literal[{values}]"
            if strict or len(enum) == 1:
                return closed
            widened = SCALARS.get(str(schema.get("type")), "str")
            return union([closed, widened], pep604=pep604)
        kind = schema.get("type")
        if kind == "array":
            items = schema.get("items")
            inner = self.type_of(items, hint=f"{hint}Item", strict=strict, pep604=pep604) if items else "Any"
            return f"list[{inner}]"
        if kind == "object" or "properties" in schema:
            return self._object(schema, hint=hint, strict=strict, pep604=pep604, component=component)
        if isinstance(kind, str) and kind in SCALARS:
            return SCALARS[kind]
        return "Any"

    def _all_of(self, schema: dict, *, hint: str, strict: bool, pep604: bool, component: str | None) -> str:
        members = schema["allOf"]
        refs = [m for m in members if isinstance(m, dict) and "$ref" in m]
        others = [m for m in members if isinstance(m, dict) and "$ref" not in m]
        bases = [self.component(m["$ref"][len(REF_PREFIX) :], strict=strict) for m in refs]
        if not others and len(bases) == 1:
            return bases[0]
        if any(not base.isidentifier() or self.names.get(base, "").startswith("alias:") for base in bases):
            # A base that is not a TypedDict cannot be inherited from.
            return "dict[str, Any]"
        merged: dict[str, Any] = {"type": "object", "properties": {}, "required": []}
        for member in others:
            merged["properties"].update(member.get("properties") or {})
            merged["required"].extend(member.get("required") or [])
            if member.get("description") and not merged.get("description"):
                merged["description"] = member["description"]
        if schema.get("description"):
            merged["description"] = schema["description"]
        if not merged["properties"] and bases:
            return bases[0] if len(bases) == 1 else union(bases, pep604=pep604)
        return self._object(merged, hint=hint, strict=strict, pep604=pep604, bases=tuple(bases), component=component)

    def _object(
        self,
        schema: dict,
        *,
        hint: str,
        strict: bool,
        pep604: bool,
        bases: tuple[str, ...] = (),
        component: str | None = None,
    ) -> str:
        properties: dict[str, Any] = schema.get("properties") or {}
        extra = schema.get("additionalProperties")
        if not properties and not bases:
            if isinstance(extra, dict) and extra:
                value = self.type_of(extra, hint=f"{hint}Value", strict=strict, pep604=pep604)
                return f"dict[str, {value}]"
            return "dict[str, Any]"
        if component is not None and component in self.names:
            return component
        structure = self._structure(schema, strict=strict, bases=bases)
        if component is None and structure in self.by_structure:
            return self.by_structure[structure]
        name = component or self._unique(hint)
        self.names[name] = structure
        self.by_structure.setdefault(structure, name)
        self.blocks.append((name, ""))  # reserve the position; the body follows
        index = len(self.blocks) - 1
        required_names = [key for key in properties if key in (schema.get("required") or [])]
        optional_names = [key for key in properties if key not in (schema.get("required") or [])]
        fields = {
            key: self.type_of(value, hint=f"{name}{pascal(key)}", strict=strict, pep604=True)
            for key, value in properties.items()
        }
        doc = schema.get("description")
        if extra is True or (isinstance(extra, dict) and extra):
            note = (
                "The API sends keys beyond the ones listed here; read them from the "
                "value as a plain mapping (``cast(dict[str, Any], value)``)."
            )
            doc = f"{doc.rstrip()}\n\n{note}" if doc else note
        source = self._class_source(
            name,
            bases=bases,
            required=[(key, fields[key], properties[key]) for key in required_names],
            optional=[(key, fields[key], properties[key]) for key in optional_names],
            doc=doc,
        )
        self.blocks[index] = (name, source)
        return name

    @staticmethod
    def _field_lines(key: str, expr: str, schema: Any) -> list[str]:
        lines = []
        description = schema.get("description") if isinstance(schema, dict) else None
        fmt = schema.get("format") if isinstance(schema, dict) else None
        if fmt and description:
            description = f"{description} Format: {fmt}."
        elif fmt:
            description = f"Format: {fmt}."
        if description:
            for line in textwrap.wrap(first_sentence(description, 220), 108):
                lines.append(f"    # {line}")
        lines.append(f"    {key}: {expr}")
        return lines

    def _class_source(
        self,
        name: str,
        *,
        bases: tuple[str, ...],
        required: list[tuple[str, str, Any]],
        optional: list[tuple[str, str, Any]],
        doc: str | None,
    ) -> str:
        docstring = ""
        if doc:
            paragraphs = [
                textwrap.fill(first_sentence(part, 600), 104, initial_indent="    ", subsequent_indent="    ")
                for part in doc.split("\n\n")
                if part.strip()
            ]
            body = "\n\n".join(paragraphs).lstrip()
            docstring = f'    """{body}"""\n'
        blocks = []
        parent = list(bases)
        if required and optional:
            base_name = f"_{name}Required"
            self.names[base_name] = f"base:{name}"
            header = ", ".join(parent) if parent else "TypedDict"
            lines = [f"class {base_name}({header}):"]
            for key, expr, schema in required:
                lines += self._field_lines(key, expr, schema)
            blocks.append("\n".join(lines))
            parent = [base_name]
        rows = optional if (required and optional) else (required or optional)
        total = "" if (required and not optional) else ", total=False"
        if parent:
            header = ", ".join(parent) + total
        else:
            header = "TypedDict" + total
        lines = [f"class {name}({header}):"]
        if docstring:
            lines.append(docstring.rstrip("\n"))
        for key, expr, schema in rows:
            lines += self._field_lines(key, expr, schema)
        if not rows and not docstring:
            lines.append("    pass")
        blocks.append("\n".join(lines))
        return "\n\n\n".join(blocks)

    def render(self) -> str:
        body = "\n\n\n".join(source for _name, source in self.blocks if source)
        exported = {name for name, source in self.blocks if source and not name.startswith("_")}
        exported.add("NotModifiedResponse")
        imports = ["Any", "Literal", "TypedDict"]
        for candidate in ("Optional", "Union"):
            if re.search(rf"\b{candidate}\[", body):
                imports.append(candidate)
        names = "\n".join(f'    "{name}",' for name in sorted(exported))
        return (
            TYPES_HEADER
            + f"from typing import {', '.join(sorted(imports))}\n\n"
            + f"__all__ = [\n{names}\n]\n\n\n"
            + NOT_MODIFIED_SOURCE
            + "\n\n\n"
            + body
            + "\n"
        )


TYPES_HEADER = '''"""Generated from the 0xinsider OpenAPI document by scripts/generate.py. Do not edit.

Every documented request body, response envelope and schema, as a ``TypedDict``.
They are annotations over the plain decoded JSON: an operation returns the
dictionary the API sent, unchanged, and these say what is in it. Nothing is
validated, converted or copied at runtime, so reading one costs nothing.

What the shapes promise, and what they deliberately do not:

* A key in the document's ``required`` list is a required key here. A key that
  is not is optional: the API omits it rather than sending null, and a missing
  key is not a zero. Read one with ``.get()`` and handle the absence.
* ``| None`` means the key is present and its value can be JSON null. Omitted
  and null are different facts; neither is a zero.
* An ``enum`` the API returns is typed ``Literal[...] | str``: the documented
  values are there for an editor to complete, and a value the API adds after
  this release is not a type error. An ``enum`` you SEND is a strict
  ``Literal``, so a typo fails before it spends a request. A ``const`` is exact,
  which is what lets a union narrow on it (``entry["state"] == "sealed"``).
* Keys the API adds after this release are in the dictionary at runtime, as
  received. A type checker will not know them: read one through
  ``client.request(...)``, which is typed ``Any``, or ``cast`` the value.

These are deferred annotations (PEP 563) written in the ``X | None`` form, so
nothing here is evaluated at import on any supported Python. Resolving them at
runtime with ``typing.get_type_hints`` needs Python 3.10 or newer; reading the
dictionaries does not.

``oxinsider._provenance.OPENAPI_SHA256`` identifies the document these were
generated from.
"""

from __future__ import annotations

'''

NOT_MODIFIED_SOURCE = '''class _NotModifiedResponseRequired(TypedDict):
    object: Literal["not_modified"]
    # Always None: a 304 carries no body, and the cached one you already hold is still current.
    data: None


class NotModifiedResponse(_NotModifiedResponseRequired, total=False):
    """What an operation returns when ``if_none_match`` matched and the API answered 304.

    Keep the body you cached; ``etag`` is the validator to send on the next
    read. ``client.with_response.<method>(...)`` reports the same as
    ``.not_modified``.
    """

    etag: str | None'''


def success_content_types(operation: dict) -> list[str]:
    for code in ("200", "201", "202"):
        response = operation.get("responses", {}).get(code)
        if isinstance(response, dict):
            return list((response.get("content") or {}).keys())
    return []


def success_schema(operation: dict) -> tuple[str | None, Any]:
    for code in ("200", "201", "202"):
        response = operation.get("responses", {}).get(code)
        if isinstance(response, dict):
            content = response.get("content") or {}
            for content_type, media in content.items():
                return content_type, media.get("schema")
            return None, None
    return None, None


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


def generate(doc: dict) -> tuple[str, str, int]:
    types = Types(doc)
    entries = []
    operations = []
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
            operations.append(
                Op(
                    types=types,
                    operation=operation,
                    operation_id=operation_id,
                    method=method.upper(),
                    path=path,
                    params=unique,
                    redirect=redirect,
                )
            )
    table = ",\n".join(
        f'    "{e["operation_id"]}": Operation("{e["method"]}", "{e["path"]}", '
        f"streaming={e['streaming']}, redirect={e['redirect']}"
        + (f', accept="{e["accept"]}"' if e["accept"] != "application/json" else "")
        + ")"
        for e in entries
    )
    version = doc.get("info", {}).get("version", "unknown")
    imported = sorted({name for op in operations for name in op.type_names()})
    type_imports = "from .types import (\n" + "".join(f"    {name},\n" for name in imported) + ")\n" if imported else ""
    body = "".join(op.render(response=False) for op in operations)
    response_body = "".join(op.render(response=True) for op in operations)
    async_body = "".join(op.render(response=False, asynchronous=True) for op in operations)
    async_response_body = "".join(op.render(response=True, asynchronous=True) for op in operations)
    typing_imports = ["Any", "NamedTuple"]
    for candidate in ("Literal", "Optional", "Union"):
        if re.search(rf"\b{candidate}\[", body):
            typing_imports.append(candidate)
    if "@overload" in body:
        typing_imports.append("overload")
    header = (
        '"""Generated from the 0xinsider OpenAPI document by scripts/generate.py. Do not edit.\n\n'
        "One method per documented operation, typed from the document's own schemas.\n"
        "``oxinsider.types`` holds the request and response shapes and the policy they\n"
        'follow; ``Client`` provides ``_call`` and ``_download``."""\n\n'
        "from __future__ import annotations\n\n"
        f"from typing import {', '.join(sorted(typing_imports))}\n\n"
        "from ._download import AsyncDownload, Download\n"
        "from ._response import ApiResponse\n"
        f"{type_imports}\n\n"
        f'OPENAPI_VERSION = "{version}"\n\n\n'
        "class Operation(NamedTuple):\n"
        "    method: str\n"
        "    path: str\n"
        "    streaming: bool = False\n"
        "    redirect: bool = False\n"
        '    accept: str = "application/json"\n\n\n'
        f"OPERATIONS: dict[str, Operation] = {{\n{table},\n}}\n\n\n"
        "class OperationsMixin:\n"
        '    """One method per documented operation, each returning the decoded body.\n\n'
        "    A JSON operation returns its response envelope, a Markdown one the text,\n"
        "    and a redirect-only one a streaming ``Download``. An operation that takes\n"
        "    ``if_none_match`` can also answer ``NotModifiedResponse``: that is the 304,\n"
        '    and it only happens when you send a validator."""\n\n'
        "    def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by Client\n"
        "        raise NotImplementedError\n\n"
        "    def _download(self, operation_id: str, **kwargs: Any) -> Download:  # pragma: no cover - provided by Client\n"
        "        raise NotImplementedError\n\n"
    )
    response_header = (
        "\nclass ResponseOperationsMixin:\n"
        '    """The same operations, each returning an ``ApiResponse`` over the same body.\n\n'
        "    Reached as ``client.with_response``: ``.data`` is exactly what the plain\n"
        "    method returns, beside the status, the headers, the ETag and the budgets.\n"
        '    A redirect-only operation already carries the file\'s own headers."""\n\n'
        "    def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by Client\n"
        "        raise NotImplementedError\n\n"
        "    def _download(self, operation_id: str, **kwargs: Any) -> Download:  # pragma: no cover - provided by Client\n"
        "        raise NotImplementedError\n\n"
    )
    async_header = (
        "\nclass AsyncOperationsMixin:\n"
        '    """The async counterpart of ``OperationsMixin``: the same methods, as coroutines.\n\n'
        "    Provided by ``AsyncClient``, which awaits the request on ``httpx.AsyncClient``\n"
        '    instead of blocking the event loop with the synchronous transport."""\n\n'
        "    async def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by AsyncClient\n"
        "        raise NotImplementedError\n\n"
        "    async def _download(\n"
        "        self, operation_id: str, **kwargs: Any\n"
        "    ) -> AsyncDownload:  # pragma: no cover - provided by AsyncClient\n"
        "        raise NotImplementedError\n\n"
    )
    async_response_header = (
        "\nclass AsyncResponseOperationsMixin:\n"
        '    """The async operations, each returning an ``ApiResponse`` over the same body.\n\n'
        '    Reached as ``async_client.with_response``, mirroring ``ResponseOperationsMixin``."""\n\n'
        "    async def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by AsyncClient\n"
        "        raise NotImplementedError\n\n"
        "    async def _download(\n"
        "        self, operation_id: str, **kwargs: Any\n"
        "    ) -> AsyncDownload:  # pragma: no cover - provided by AsyncClient\n"
        "        raise NotImplementedError\n\n"
    )
    source = (
        header
        + body
        + "\n"
        + response_header
        + response_body
        + "\n"
        + async_header
        + async_body
        + "\n"
        + async_response_header
        + async_response_body
    )
    # Blank docstring lines must not carry the indentation.
    return re.sub(r"[ \t]+\n", "\n", source), types.render(), len(entries)


class Op:
    """One generated operation method, in both its plain and ApiResponse forms."""

    def __init__(
        self,
        *,
        types: Types,
        operation: dict,
        operation_id: str,
        method: str,
        path: str,
        params: list[dict],
        redirect: bool,
    ) -> None:
        self.types = types
        self.operation = operation
        self.operation_id = operation_id
        self.method = method
        self.path = path
        self.name = snake(operation_id)
        self.redirect = redirect
        self.path_params = [p for p in params if p.get("in") == "path"]
        self.query_params = [p for p in params if p.get("in") == "query"]
        header_params = [p for p in params if p.get("in") == "header"]
        self.conditional = any(h["name"].lower() == "if-none-match" for h in header_params)
        self.idempotent = any(h["name"].lower() == "idempotency-key" for h in header_params)
        self.body_type = self._body_type()
        self.body_required = bool((operation.get("requestBody") or {}).get("required", False))
        self.has_body = "requestBody" in operation
        self.return_type = self._return_type()

    def _body_type(self) -> str | None:
        request_body = self.operation.get("requestBody")
        if not request_body:
            return None
        content = request_body.get("content") or {}
        for _content_type, media in content.items():
            schema = media.get("schema")
            if not schema:
                return "Any"
            return self.types.type_of(
                schema,
                hint=f"{pascal(self.operation_id)}Body",
                strict=True,
                pep604=True,
            )
        return "Any"

    def _return_type(self) -> str:
        if self.redirect:
            return "Download"
        _content_type, schema = success_schema(self.operation)
        if schema is None:
            # A documented success with no body of its own: the call still
            # returns whatever Client.request decoded (None for a 204).
            return "Any"
        return self.types.type_of(schema, hint=f"{pascal(self.operation_id)}Response", strict=False, pep604=True)

    def query_type(self, param: dict) -> str:
        schema = param.get("schema") or {}
        expr = self.types.type_of(
            schema,
            hint=f"{pascal(self.operation_id)}{pascal(param['name'])}",
            strict=True,
            pep604=True,
        )
        return optional(expr, pep604=True)

    def type_names(self) -> set[str]:
        """The names this method's signatures import from ``.types``."""
        found: set[str] = set()
        expressions = [self.return_type, self.body_type or ""]
        expressions += [self.query_type(param) for param in self.query_params]
        if self.conditional:
            found.add("NotModifiedResponse")
        for expression in expressions:
            for token in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expression):
                if token in self.types.names and not token.startswith("_"):
                    found.add(token)
        return found

    def _args(self, *, if_none_match: str | None) -> list[str]:
        args = ["self"]
        args += [f"{python_name(p['name'])}: str" for p in self.path_params]
        if self.has_body:
            body_type = self.body_type or "Any"
            args.append(f"body: {body_type}" if self.body_required else f"body: {body_type} | None = None")
        keyword_args = [f"{python_name(p['name'])}: {self.query_type(p)} = None" for p in self.query_params]
        if if_none_match:
            keyword_args.append(if_none_match)
        if self.idempotent:
            keyword_args.append("idempotency_key: str | None = None")
        if keyword_args:
            args.append("*")
            args += keyword_args
        return args

    def _docstring(self, *, asynchronous: bool = False) -> str:
        summary = first_sentence(self.operation.get("summary") or self.operation_id, 200)
        description = first_sentence(self.operation.get("description") or "")
        lines = [f"{summary}.".replace("..", "."), "", f"``{self.method} {self.path}`` (operationId ``{self.operation_id}``)."]
        if description:
            lines += ["", *textwrap.wrap(description, 88)]
        if self.redirect:
            download_type = "AsyncDownload" if asynchronous else "Download"
            article = "an" if asynchronous else "a"
            close_call = "aclose()" if asynchronous else "close()"
            read_call = "aread()" if asynchronous else "read()"
            save_call = "asave(path)" if asynchronous else "save(path)"
            lines += [
                "",
                *textwrap.wrap(
                    f"Returns {article} ``{download_type}``: the redirect is followed once, without the credential, "
                    f"and the file is streamed. Iterate it, ``{save_call}`` it for its SHA-256, or "
                    f"``{read_call}`` it (bounded); ``{close_call}`` it when done. A redirect or transfer fault "
                    "raises ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.",
                    88,
                ),
            ]
        if self.conditional:
            lines += [
                "",
                *textwrap.wrap(
                    "Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: "
                    "a 304 then returns ``NotModifiedResponse`` and your cached body is still current.",
                    88,
                ),
            ]
        if self.query_params:
            lines += ["", "Query parameters:"]
            for param in self.query_params:
                text = first_sentence(param.get("description") or "", 160)
                if param.get("required"):
                    text = f"Required. {text}".strip()
                lines.append(f"    {python_name(param['name'])}: {text}".rstrip())
        return "\n        ".join(line.replace('"""', "'''") for line in lines)

    def _call_args(self) -> str:
        path_map = ", ".join(f'"{p["name"]}": {python_name(p["name"])}' for p in self.path_params)
        query_map = ", ".join(f'"{p["name"]}": {python_name(p["name"])}' for p in self.query_params)
        call = [f'"{self.operation_id}"', f"path_params={{{path_map}}}", f"query={{{query_map}}}"]
        if self.redirect:
            return ", ".join(call)
        if self.has_body:
            call.append("body=body")
        if self.conditional:
            call.append("if_none_match=if_none_match")
        if self.idempotent:
            call.append("idempotency_key=idempotency_key")
        return ", ".join(call)

    def render(self, *, response: bool, asynchronous: bool = False) -> str:
        def wrap(inner: str) -> str:
            return f"ApiResponse[{inner}]" if response and not self.redirect else inner

        keyword = "async def" if asynchronous else "def"
        awaited = "await " if asynchronous else ""
        # A redirect-only operation answers ``Client.download``'s file wrapper,
        # not a decoded body: ``AsyncClient.download`` answers its async
        # counterpart instead, so the annotation must switch with it too.
        return_type = "AsyncDownload" if (asynchronous and self.redirect) else self.return_type
        if self.redirect:
            body_line = f"        return {awaited}self._download({self._call_args()})\n"
        else:
            # Client._call dispatches dynamically and answers ``Any``. Naming the
            # decoded body here is what states its shape, and costs one local.
            body_line = f"        result: RETURN_TYPE = {awaited}self._call({self._call_args()})\n        return result\n"
        if not self.conditional:
            signature = ",\n        ".join(self._args(if_none_match=None))
            plain_only = wrap(return_type)
            return (
                f"    {keyword} {self.name}(\n        {signature},\n    ) -> {plain_only}:\n"
                f'        """{self._docstring(asynchronous=asynchronous)}\n        """\n'
                f"{body_line.replace('RETURN_TYPE', plain_only)}\n"
            )
        plain = wrap(return_type)
        # An ApiResponse is invariant in its body, so the conditional form is a
        # union of the two responses rather than one response over a union.
        conditional = union([plain, wrap("NotModifiedResponse")], pep604=True)
        unmatched = ",\n        ".join(self._args(if_none_match="if_none_match: None = None"))
        matched = ",\n        ".join(self._args(if_none_match="if_none_match: str | None"))
        implementation = ",\n        ".join(self._args(if_none_match="if_none_match: str | None = None"))
        return (
            "    @overload\n"
            f"    {keyword} {self.name}(\n        {unmatched},\n    ) -> {plain}: ...\n\n"
            "    @overload\n"
            f"    {keyword} {self.name}(\n        {matched},\n    ) -> {conditional}: ...\n\n"
            f"    {keyword} {self.name}(\n        {implementation},\n    ) -> {conditional}:\n"
            f'        """{self._docstring(asynchronous=asynchronous)}\n        """\n'
            f"{body_line.replace('RETURN_TYPE', conditional)}\n"
        )


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
    operations, types_source, count = generate(doc)
    TYPES_OUTPUT.write_text(types_source)
    print(f"wrote {TYPES_OUTPUT}")
    OUTPUT.write_text(operations)
    print(f"wrote {OUTPUT} ({count} operations)")
    recorded_source = source if source.startswith(("http://", "https://")) else f"{APP_REPOSITORY}:{APP_SPEC_PATH}"
    PROVENANCE_OUTPUT.write_text(
        provenance(raw, doc, source=recorded_source, app_commit=resolve_app_commit(app_commit), operation_count=count)
    )
    print(f"wrote {PROVENANCE_OUTPUT}")


if __name__ == "__main__":
    main()
