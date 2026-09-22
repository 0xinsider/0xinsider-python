"""Call the 0xinsider sandbox: no key, example data, simulated errors."""

import oxinsider

with oxinsider.Client.sandbox() as client:
    leaderboard = client.list_leaderboard(limit=3)
    print("leaderboard object:", leaderboard["object"], "rows:", len(leaderboard["data"]))

    trader = client.get_trader("0x0000000000000000000000000000000000000001")
    # An ungraded wallet is uncovered, not unskilled: the key is absent, not "F".
    print("trader grade:", trader["data"].get("grade", "ungraded"))

    try:
        client.request("GET", "/api/v1/leaderboard", query={"sandbox_status": 429})
    except oxinsider.RateLimitedError as error:
        print("simulated rate limit:", error.code, "retry after", error.retry_after, "s")
