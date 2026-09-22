"""Read the public discovery document and health from the live API. No key needed."""

import oxinsider

with oxinsider.Client(api_key="") as client:
    discovery = client.get_api_discovery()
    print("api base:", discovery["data"]["api_base_url"])
    health = client.get_health()
    # `status` is not always sent, so it is an optional key: read it with .get()
    # and say so when it is absent rather than inventing a state.
    print("health:", health["data"].get("status", "unreported"))
