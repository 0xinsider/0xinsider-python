"""Read the live large-trade feed, resuming across a disconnect.

GET /api/v1/stream needs a real credential and an active Pro subscription --
the sandbox does not simulate a Server-Sent Events connection (it answers
GET /api/v1/stream with a 400 explaining exactly that). Set OXINSIDER_API_KEY
and run this against https://api.0xinsider.com.

AsyncClient.stream() reconnects on its own after a disconnect, sending
Last-Event-ID set to the last frame's id so nothing is skipped or repeated,
with exponential backoff between attempts. Interrupt with Ctrl-C to see
cancellation close the connection cleanly.
"""

import asyncio
import os

import oxinsider


async def main() -> None:
    if not os.environ.get(oxinsider.API_KEY_ENV):
        print(f"set {oxinsider.API_KEY_ENV} to a live key with Pro access to run this example")
        return

    delivered = 0
    async with oxinsider.AsyncClient() as client:
        try:
            # min_size narrows the feed to trades at or above this notional,
            # matching the query GET /api/v1/stream documents.
            async for event in client.stream(query={"min_size": "10000"}):
                if event.event == "resync":
                    print("resync:", event.data)
                    continue
                delivered += 1
                trade = event.json()
                print(event.id, trade.get("data", trade).get("size_usd", "?"))
        except oxinsider.StreamClosedError as error:
            print(f"stream closed permanently: {error.code}: {error.message}")
        except KeyboardInterrupt:
            pass

    print(f"delivered {delivered} frames before stopping")


if __name__ == "__main__":
    asyncio.run(main())
