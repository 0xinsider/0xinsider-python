"""Read several traders concurrently, bounded by AsyncClient's max_concurrency.

Measures wall time against the real sandbox for a sequential walk and a
bounded concurrent one over the same addresses, and prints both: the
speedup is whatever the sandbox actually gave this run, not an assumed
multiplier. No key needed; no production data touched.
"""

import asyncio
import time

import oxinsider

ADDRESSES = [f"0x51ab00000000000000000000000000000000ab{i:02d}" for i in range(1, 9)]


async def sequential(client: oxinsider.AsyncClient) -> float:
    start = time.monotonic()
    for address in ADDRESSES:
        await client.get_trader(address)
    return time.monotonic() - start


async def concurrent(client: oxinsider.AsyncClient) -> float:
    start = time.monotonic()
    await asyncio.gather(*(client.get_trader(address) for address in ADDRESSES))
    return time.monotonic() - start


async def main() -> None:
    # max_concurrency bounds how many of the gather's requests are ever in
    # flight at once; raise it for a bigger fan-out, lower it to stay further
    # under the API's per-minute budget. It never rate-limits by itself --
    # pair it with the with_response budgets or a RateLimitedError.retry_after
    # for that.
    async with oxinsider.AsyncClient.sandbox(max_concurrency=8) as client:
        sequential_seconds = await sequential(client)
        concurrent_seconds = await concurrent(client)

    print(f"{len(ADDRESSES)} traders, sequential: {sequential_seconds:.3f}s")
    print(f"{len(ADDRESSES)} traders, concurrent (max_concurrency=8): {concurrent_seconds:.3f}s")
    if concurrent_seconds > 0:
        print(f"measured speedup this run: {sequential_seconds / concurrent_seconds:.2f}x")


if __name__ == "__main__":
    asyncio.run(main())
