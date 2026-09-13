"""Read the public discovery document and health from the live API. No key needed."""

import oxinsider

with oxinsider.Client(api_key="") as client:
    discovery = client.get_api_discovery()
    print("api base:", discovery["data"]["api_base_url"])
    health = client.get_health()
    print("health:", health.get("data", {}).get("status", health))
