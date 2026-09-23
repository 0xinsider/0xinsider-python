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
print(trader["data"].get("grade", "ungraded"))

for trade in client.paginate("list_whale_trades", min_grade="A", limit=100):
    print(trade["size_usd"], trade["market"]["title"])
```

- Every documented operation is a method named after its operationId in snake_case (`listLeaderboard` becomes `list_leaderboard`). Each returns the decoded JSON body; `client.with_response.<method>()` returns the same body with the status and headers beside it.
- `if_none_match="<etag>"` returns `{"object": "not_modified", "data": None, "etag": ...}` when nothing changed.
- `idempotency_key=` is accepted on the webhook mutations that document it.
- The SSE stream is read with `client.request("GET", "/api/v1/stream", stream=True)`, which returns the open `httpx.Response`. `AsyncClient.stream()` (below) reads it resumably instead.
- `oxinsider.AsyncClient` is the same operations, `async`/`await`, on `httpx.AsyncClient`, with bounded concurrency, cooperative cancellation and a resumable stream reader -- see [Async client](#async-client).
- A redirect-only operation returns a streaming `Download` instead of a body: `download_trader_export` (the API answers 302 to a short-lived file location once the job is `ready`) and `redirect_api_openapi_spec` (307 to the web origin). The redirect is followed once, and the credential is never sent to the file host.

### How old is it?

A trader carries `data_quality` inside `data`, and the positions and large-trade pages carry it beside `data`: a `status`, the oldest `as_of` the body rests on, and one entry per field group. `assess_data_quality` turns it into one decision against your own tolerance. It is a pure function and makes no request:

```python
from datetime import timedelta

verdict = oxinsider.assess_data_quality(trader["data"], max_age=timedelta(minutes=15))
if not verdict.ok:
    for failure in verdict.failing:
        print(failure.group, failure.status, failure.reason)
```

A group passes only when its `status` is `fresh`, it carries `as_of`, and that clock is within `max_age`. `fresh` means tracked and clocked, not current enough for you. `unknown` fails: the read cannot date that group, and missing is never recent. `untracked` groups are listed in `verdict.untracked` and left out of the verdict. Pass `groups=["ranking", "volume"]` to judge only the groups you read; a named group the body does not carry fails as `missing`. The TypeScript (`assessDataQuality`) and Go (`AssessDataQuality`) SDKs apply the same rule.

## Types

Every operation is typed from the same OpenAPI document that generates it. The request body, the query values and the response envelope each have a `TypedDict` in `oxinsider.types`, and an editor infers them without an annotation:

```python
trader = client.get_trader("swisstony")        # GetTraderResponse
trader["data"]["pnl"].get("realized")          # float | None
client.list_positions(min_grade="A")           # min_grade is Literal["S", "A", ... "F"]
client.get_trader_context_markdown("swisstony")  # str, not an envelope
```

Nothing is validated, converted or copied: the methods return the decoded JSON exactly as before, so upgrading changes what a type checker sees and nothing that runs.

What the types say, and what they deliberately do not:

- **A key the API omits is an optional key.** `trader["data"]["grade"]` is a type error, because an ungraded wallet has no `grade` and reading it would raise. Use `.get("grade")` and serve the absence: a missing value is not a zero and not an `F`. `pnl.realized` is the same -- it is omitted when no native accounting snapshot matches, and raw total P&L is never a substitute.
- **`| None` is a key that is present and null.** Omitted and null are different facts. Neither is a zero.
- **An enum the API returns is `Literal[...] | str`.** The documented values complete in an editor, and a value the API adds later is not a type error in a client that has not upgraded. An enum you *send* is a strict `Literal`, so a typo fails before it spends a request.
- **A `const` is exact**, which is what lets a union narrow: the Pick of the Day ledger is `PickOfTheDayLedgerSealedEntry | ...OpenedEntry | ...UncommittedEntry`, and `if entry["state"] == "opened":` narrows to the shape that carries the nonce and the payload.
- **Keys added after your release are still in the dictionary** at runtime, as received. A type checker will not know them: read one through `client.request(...)`, which is typed `Any`, or `cast` the value. Regenerating picks them up.
- **A conditional read returns a union.** `client.get_trader(addr, if_none_match=etag)` is `GetTraderResponse | NotModifiedResponse`; without a validator it is just `GetTraderResponse`. `client.with_response.<method>()` returns `ApiResponse[<the same body>]`.

The package ships `py.typed`, so mypy and pyright read these without a stub package.

## Headers, caching and budgets

Every operation method returns the decoded body, and that does not change. When you need the rest of the answer, call the same operation through `with_response` and get an `ApiResponse`: `.data` is the identical body, and `.status` and `.headers` come with it.

```python
r = client.with_response.get_trader("swisstony")
print(r.data["data"].get("grade"), r.status, r.etag, r.request_id)
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

## Async client

`oxinsider.AsyncClient` is every operation above as a coroutine, generated from the same operation table as `Client` so the two cannot drift apart. It is built on `httpx.AsyncClient` -- the SDK's one dependency -- rather than a thread-pool wrapper around the sync client, so an `await` never blocks the event loop on the synchronous transport.

```python
import asyncio
import oxinsider

async def main():
    async with oxinsider.AsyncClient() as client:  # reads OXINSIDER_API_KEY
        trader = await client.get_trader("swisstony", expand=["strategy"])
        print(trader["data"].get("grade", "ungraded"))

        async for trade in client.paginate("list_whale_trades", min_grade="A", limit=100):
            print(trade["size_usd"], trade["market"]["title"])

asyncio.run(main())
```

Every operation method, `with_response`, `request`, `download`, `paginate` and `paginate_pages` are the identical contract as `Client`'s, `async`/`await` and `async for` in place of the synchronous calls; `AsyncClient.sandbox()` is the same zero-credential sandbox. `aclose()` closes the underlying `httpx.AsyncClient` when this client built its own (not when you passed `http_client=` yourself, which stays yours to close either way) -- use it as an `async with` block, same as `Client`.

### Bounded concurrency

`max_concurrency` (default `oxinsider.DEFAULT_MAX_CONCURRENCY`, 10) is a constructor argument: an internal `asyncio.Semaphore` bounds how many requests this client holds in flight at once, so an `asyncio.gather` over many independent reads cannot open more connections than you asked for. The semaphore is held only around the send itself -- a `stream()` walk's open connection is released from it as soon as its headers arrive, so one long-lived stream does not starve ordinary calls sharing the client.

```python
async with oxinsider.AsyncClient(max_concurrency=8) as client:
    traders = await asyncio.gather(*(client.get_trader(a) for a in addresses))
```

`examples/async_portfolio.py` measures this against the sandbox rather than assuming a speedup: 8 traders read one at a time took 1.55s in one run; the same 8 with `max_concurrency=8` took 0.16s, a measured 10x for that run -- your own numbers depend on the network and the route. `max_concurrency` bounds concurrency, not your rate: pair it with the `rate_limit` budget on `with_response` or a `RateLimitedError`'s `retry_after` to stay under the API's own per-minute window.

### Cancellation

Cancelling a call -- `asyncio.CancelledError`, an `asyncio.wait_for` timeout, a task group cancelling its members -- is never caught inside `AsyncClient`: it propagates to you, and the in-flight `httpx` request (or an open `stream()` connection) is released as part of that unwind, every request and stream iteration closes its response in a `finally`. Nothing needs an explicit teardown for cleanup; `asyncio.wait_for(client.get_trader("swisstony"), timeout=5)` closes the connection on its own when it fires.

### Resumable streaming

`client.stream()` reads `GET /api/v1/stream` (or another SSE route, by `path=`) and reconnects on its own after a disconnect, instead of the raw `httpx.Response` `Client.request(..., stream=True)` hands back. Every reconnect sends `Last-Event-ID` set to the last frame's `id`, matching the header the stream's own resume contract reads, so a disconnect never skips or repeats a frame already delivered.

```python
async with oxinsider.AsyncClient() as client:
    async for event in client.stream(query={"min_size": "10000"}):
        if event.event == "resync":
            refetch_from_rest()  # a gap or an out-of-window resume point
            continue
        trade = event.json()
        handle(trade)
```

Backoff between reconnects is exponential from `backoff_initial` (3s, matching a browser `EventSource`'s own default), capped at `backoff_max` (30s) -- or the server's own `retry:` field for that one attempt, when it sent one -- and resets after a connection opens successfully, so one blip in an otherwise long-lived stream does not creep the delay toward the cap. `max_retries` bounds consecutive failed reconnects (`None`, the default, retries forever, matching a browser `EventSource`); `last_event_id=` resumes a walk started in an earlier process. A terminal `event: error` frame whose payload says the credential was permanently refused (`"retry": false`) raises `oxinsider.StreamClosedError` immediately instead of reconnecting; one that says `"retry": true` (a transient store outage) backs off and reconnects like any other disconnect. `examples/async_stream.py` is a full walkthrough (needs a live key with Pro access; the sandbox does not simulate an SSE connection).

`ServerSentEvent` (`event`, `data`, `id`, and `.json()` to decode `data`) is what each iteration yields.

### Downloads

`AsyncClient.download` and every redirect-only operation (exports, the OpenAPI spec redirect) answer an `AsyncDownload` instead of a `Download`: the same properties, and `aiter_bytes()`, `aiter_raw()`, `aread()`, `asave()`, `aclose()` in place of the synchronous methods. See [Exports](#exports) below for the shape.

```python
async with await client.download_trader_export("swisstony", job_id=job_id) as download:
    saved = await download.asave("swisstony.ndjson")
```

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

Every non-2xx response from the API raises `oxinsider.OxinsiderApiError` or a subclass: `BadRequestError`, `AuthenticationError`, `SubscriptionRequiredError`, `PermissionDeniedError`, `NotFoundError`, `RateLimitedError` or `ServerError`. Each carries `status`, `code`, `reason`, `param`, `retry_at`, `retry_after` and `request_id`. Branch on `reason` when it is present. For `RateLimitedError`, wait `retry_after` seconds. A request that gets no response raises `OxinsiderConnectionError`. `AsyncClient.stream()` raises `oxinsider.StreamClosedError` instead, when a terminal `event: error` frame says the credential backing the stream was permanently refused (see [Resumable streaming](#resumable-streaming)).

## How it is built

`src/oxinsider/_operations.py` and `src/oxinsider/types.py` are generated from the published [OpenAPI document](https://0xinsider.com/api/v1/openapi.json) by `scripts/generate.py`, which also writes the typing policy above into `types.py`. A weekly workflow regenerates them and commits to `main` when the contract changes, so a new field or operation reaches the types without anyone editing a generated file. Releases publish to PyPI from GitHub Actions through trusted publishing.

`_operations.py` generates four mixins from the same operation table: `OperationsMixin` and `ResponseOperationsMixin` (`Client`, sync), and `AsyncOperationsMixin` and `AsyncResponseOperationsMixin` (`AsyncClient`, coroutines that `await` instead of calling directly). One `Op.render(asynchronous=...)` renders all four from the same signatures and docstrings, so the sync and async surfaces cannot drift from each other; `_pagination.py`, `_download.py` and `_stream.py` carry the hand-written async counterparts (`apaginate`/`apaginate_pages`, `AsyncDownload`, the resumable SSE reader) the same way `_policy.py` and `_data_quality.py` stay outside the generated files.

Which document a release was generated from is in `src/oxinsider/_provenance.py`, generated alongside: `oxinsider.OPENAPI_SHA256` (the SHA-256 of the document bytes), `oxinsider.OPENAPI_VERSION`, `oxinsider.OPERATION_COUNT`, and `oxinsider.APP_COMMIT`, the `0xinsider/0xinsider` commit that last changed `web/public/api/v1/openapi.json` (or `None` when it could not be resolved). Compare `OPENAPI_SHA256` with `shasum -a 256` of the live document to see whether a release is behind the API.

An operation the document lists only to refuse (`GET /api/v1/mcp` answers `405`: the server offers no server-to-client stream) stays in `oxinsider.OPERATIONS` and gets no method.

## Other official tools

- CLI and MCP server: `npm install --global @0xinsider/mcp` or `brew install 0xinsider/tap/oxinsider`
- Go SDK: `go get github.com/0xinsider/0xinsider-go`
- Node.js and TypeScript SDK: `@0xinsider/sdk` ([0xinsider/0xinsider-node](https://github.com/0xinsider/0xinsider-node))
- Rust SDK: crate `oxinsider` ([0xinsider/0xinsider-rust](https://github.com/0xinsider/0xinsider-rust))
- Remote MCP server: `https://api.0xinsider.com/api/v1/mcp`

## License

MIT
