# 0xinsider Python SDK

Official Python client for the [0xinsider Developer API](https://0xinsider.com/developers): Polymarket sports and esports analytics, wallet grades, large trades, positions, reports and sharp-money flow.

```sh
pip install 0xinsider
```

The distribution is `0xinsider`; the import is `oxinsider`, because a Python module name cannot start with a digit.

## Try it without a key

The [sandbox](https://0xinsider.com/sandbox/api/v1) answers every documented operation with example data. It needs no credential and never touches production data.

```python
import oxinsider

with oxinsider.Client.sandbox() as client:
    page = client.list_leaderboard(limit=5)
    print(page["data"][0]["username"])

    # Any error the operation documents, on demand:
    try:
        client.request("GET", "/api/v1/leaderboard", query={"sandbox_status": 429})
    except oxinsider.RateLimitedError as error:
        print(error.code, error.retry_after)
```

## Live data

Data operations need an API key from [0xinsider.com/developers](https://0xinsider.com/developers) or an OAuth 2.1 access token ([auth.md](https://0xinsider.com/auth.md)), plus an active Pro subscription. Discovery, health and platforms are public.

```python
import oxinsider

client = oxinsider.Client()  # reads OXINSIDER_API_KEY
trader = client.get_trader("swisstony", expand=["strategy", "categories"])
print(trader["data"]["grade"])

for trade in client.paginate("list_whale_trades", min_grade="A", limit=100):
    print(trade["size_usd"], trade["market"]["title"])
```

- Every documented operation is a method named after its operationId in snake_case (`listLeaderboard` becomes `list_leaderboard`). Each returns the decoded JSON body.
- `if_none_match="<etag>"` returns `{"object": "not_modified", "data": None, "etag": ...}` when nothing changed.
- `idempotency_key=` is accepted on the webhook mutations that document it.
- The SSE stream is read with `client.request("GET", "/api/v1/stream", stream=True)`, which returns the open `httpx.Response`.
- A redirect-only operation returns a streaming `Download` instead of a body: `download_trader_export` (the API answers 302 to a short-lived file location once the job is `ready`) and `redirect_api_openapi_spec` (307 to the web origin). The redirect is followed once, and the credential is never sent to the file host.

## Exports

```python
job = client.submit_trader_export("swisstony", format="ndjson")["data"]
# poll client.get_trader_export_status(...) until status == "ready", then:
with client.download_trader_export("swisstony", job_id=job["job_id"]) as download:
    print(download.content_type, download.content_encoding, download.filename)
    saved = download.save("swisstony.ndjson")   # decompressed; decode=False keeps the gzip bytes
print(saved.bytes_written, saved.sha256)
```

`iter_bytes()` streams the decoded file and `iter_raw()` the bytes as sent, so memory stays bounded whatever the size; `read()` returns the file in memory and refuses more than 64 MiB unless `max_bytes` says otherwise. No manifest or checksum is published for an export: `save` returns the SHA-256 of exactly what it wrote, and `etag` is the file host's object identity, not a content hash. A job that is not `ready` raises the API's own `BadRequestError`; an expired location, a refused host, or an interrupted transfer raises `DownloadError` with `reason` (`insecure_location`, `unexpected_redirect`, `unavailable`, `too_large`, `interrupted`, `not_redirected`, `missing_location`) and never the signed URL.

## Where the key goes

The key is sent over `https://` only, or over `http://` to a loopback host (`localhost`, `127.0.0.1`, `[::1]`) for a backend you run yourself. A `base_url` that would send it anywhere else raises `oxinsider.InsecureTransportError` from the constructor, before any request; the same check runs on every request, so a key added later or an `auth=` on your own `httpx.Client` cannot bypass it. A keyless client may still call the public operations on such a base. The SDK never follows a redirect on its own (see `Download`), so an `https://` answer cannot downgrade a request to `http://`.

## Errors

Every non-2xx response from the API raises `oxinsider.OxinsiderApiError` or a subclass: `BadRequestError`, `AuthenticationError`, `SubscriptionRequiredError`, `PermissionDeniedError`, `NotFoundError`, `RateLimitedError` or `ServerError`. Each carries `status`, `code`, `reason`, `param`, `retry_at`, `retry_after` and `request_id`. Branch on `reason` when it is present. For `RateLimitedError`, wait `retry_after` seconds. A request that gets no response raises `OxinsiderConnectionError`.

## How it is built

`src/oxinsider/_operations.py` is generated from the published [OpenAPI document](https://0xinsider.com/api/v1/openapi.json) by `scripts/generate.py`, and a weekly workflow opens a pull request when the contract changes. Releases publish to PyPI from GitHub Actions through trusted publishing.

## Other official tools

- CLI and MCP server: `npm install --global @0xinsider/mcp` or `brew install 0xinsider/tap/oxinsider`
- Go SDK: `go get github.com/0xinsider/0xinsider-go`
- Remote MCP server: `https://api.0xinsider.com/api/v1/mcp`

## License

MIT
