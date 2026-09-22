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

- Every documented operation is a method named after its operationId in snake_case (`listLeaderboard` becomes `list_leaderboard`). Each returns the decoded JSON body; `client.with_response.<method>()` returns the same body with the status and headers beside it.
- `if_none_match="<etag>"` returns `{"object": "not_modified", "data": None, "etag": ...}` when nothing changed.
- `idempotency_key=` is accepted on the webhook mutations that document it.
- The SSE stream is read with `client.request("GET", "/api/v1/stream", stream=True)`, which returns the open `httpx.Response`.
- A redirect-only operation returns a streaming `Download` instead of a body: `download_trader_export` (the API answers 302 to a short-lived file location once the job is `ready`) and `redirect_api_openapi_spec` (307 to the web origin). The redirect is followed once, and the credential is never sent to the file host.

## Headers, caching and budgets

Every operation method returns the decoded body, and that does not change. When you need the rest of the answer, call the same operation through `with_response` and get an `ApiResponse`: `.data` is the identical body, and `.status` and `.headers` come with it.

```python
r = client.with_response.get_trader("swisstony")
print(r.data["data"]["grade"], r.status, r.etag, r.request_id)
```

### Conditional reads

`.etag` on a `200` is what you send back as `if_none_match`. A `304` means your cached copy is still current, and it does not count against your data budget the way a full read does.

```python
cached = client.with_response.get_trader("swisstony")
body, etag = cached.data, cached.etag

fresh = client.with_response.get_trader("swisstony", if_none_match=etag)
if fresh.not_modified:
    pass                      # keep `body`; fresh.etag is the same validator
else:
    body, etag = fresh.data, fresh.etag
```

### Budgets

`.rate_limit`, `.monthly_quota` and `.batch_rate_limit` each return a `Budget` (`limit`, `remaining`, `reset_at`, `reset_after`) or `None` when the response said nothing about that window. `reset_at` is a UNIX epoch second; `reset_after` is seconds from now and only the per-minute window publishes it. `.request_cost` is how many batch items a batch call charged, and `.server_timing_ms` is the API's own processing time.

```python
r = client.with_response.batch_get_traders({"traders": ["swisstony", "0xabc..."]})
print(r.request_cost, r.batch_rate_limit, r.monthly_quota, r.server_timing_ms)

month = r.monthly_quota
if month is not None and month.remaining is not None and month.remaining < 1000:
    slow_down()
```

An absent header is `None`, never `0`. "This response carried no quota information" and "you have no quota left" are different facts, and only the second one should stop your client. A header that is present but not a number reads `None` as well, rather than raising in the middle of your read.

| You want | Read |
| --- | --- |
| The validator for the next conditional read | `.etag` |
| Whether a conditional read matched | `.not_modified` (the `304`) |
| The id to quote in a bug report | `.request_id` (same as `meta.request_id`) |
| How long to wait | `.retry_after` |
| The per-minute window | `.rate_limit` |
| The calendar-month request quota | `.monthly_quota` |
| The batch routes' per-item window | `.batch_rate_limit`, `.request_cost` |
| The API's own processing time | `.server_timing_ms` |
| Whether the sandbox answered | `.sandbox` |
| Anything else | `.header("name")`, `.headers` |

A failure carries the same thing: `OxinsiderApiError.response` is the failed `ApiResponse`, so a `429` can be handled from the window the API described rather than from a guess.

```python
try:
    client.list_whale_trades(limit=100)
except oxinsider.RateLimitedError as error:
    window = error.response.rate_limit if error.response else None
    wait(error.retry_after or (window.reset_after if window else 60))
```

`client.request(method, path, raw=True)` does the same for a hand-built call. `stream=True` already hands back the open `httpx.Response` with its own headers, so the two cannot be combined; a redirect-only operation already returns a `Download` carrying the file's headers.

## Paging

`paginate` walks a cursor-paginated list to the end. The filters go out unchanged on every page; only the cursor moves. `paginate_pages` yields whole envelopes instead of items, when you need `total`, `has_more` or `meta`.

```python
progress = oxinsider.PaginationProgress()
for trade in client.paginate("list_whale_trades", min_grade="A", limit=100, max_pages=20, progress=progress):
    handle(trade)

print(progress.pages_fetched, progress.items_yielded, progress.stopped_by)
if progress.stopped_by == "max_pages":
    print("more to read from", progress.next_cursor)
```

The walk checks each page before handing it to you, so a broken response is visible instead of looking like a finished dataset:

| What came back | What happens |
| --- | --- |
| `has_more: false` | The walk ends. `stopped_by` reads `"exhausted"`. A valid empty page is a normal end. |
| Not a list envelope, or `data` is not a list | `PaginationError` with `reason` `invalid_envelope` or `invalid_data`, before anything is yielded. |
| `has_more: true`, `next_cursor` missing, null or empty | `PaginationError`, `reason` `missing_cursor`. |
| `next_cursor` this walk already requested | `PaginationError`, `reason` `repeated_cursor`, raised before the duplicate request goes out. |
| A 304 from `if_none_match` | The walk ends with `stopped_by` `"not_modified"`. |

`max_pages` and `max_items` are each a positive integer or `None`, checked before the first request; `0`, a negative or a float raises `ValueError` without spending one. Reaching a bound is your choice, not the end of the collection: `stopped_by` says which, and `progress.next_cursor` carries on.

Wherever a walk stops, the checkpoint survives it. `progress.cursor` is the page the walk stopped on -- pass it back as `cursor=` to refetch that page and lose nothing -- and `progress.next_cursor` continues past a page you finished. On a failure (a rate limit, an expired cursor, a dropped connection) the original error is raised unchanged and `oxinsider.pagination_checkpoint(error)` returns the same checkpoint, so recovery never silently restarts at page one:

```python
try:
    for trade in client.paginate("list_whale_trades", min_grade="A"):
        handle(trade)
except oxinsider.OxinsiderError as error:
    resume = oxinsider.pagination_checkpoint(error)
    if resume is not None:
        for trade in client.paginate("list_whale_trades", min_grade="A", cursor=resume.cursor):
            handle(trade)
```

`PaginationError` carries `reason`, `method_name`, `page` (the response as received), `cursor`, `next_cursor`, `pages_fetched`, `items_yielded`, `checkpoint` and the page's `request_id` when it had one. The last `oxinsider.CURSOR_HISTORY_LIMIT` cursors are remembered for the repeat check, which keeps a long walk's memory flat; a cycle longer than that is not detected.

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

Which document a release was generated from is in `src/oxinsider/_provenance.py`, generated alongside: `oxinsider.OPENAPI_SHA256` (the SHA-256 of the document bytes), `oxinsider.OPENAPI_VERSION`, `oxinsider.OPERATION_COUNT`, and `oxinsider.APP_COMMIT`, the `0xinsider/0xinsider` commit that last changed `web/public/api/v1/openapi.json` (or `None` when it could not be resolved). Compare `OPENAPI_SHA256` with `shasum -a 256` of the live document to see whether a release is behind the API.

An operation the document lists only to refuse (`GET /api/v1/mcp` answers `405`: the server offers no server-to-client stream) stays in `oxinsider.OPERATIONS` and gets no method.

## Other official tools

- CLI and MCP server: `npm install --global @0xinsider/mcp` or `brew install 0xinsider/tap/oxinsider`
- Go SDK: `go get github.com/0xinsider/0xinsider-go`
- Remote MCP server: `https://api.0xinsider.com/api/v1/mcp`

## License

MIT
