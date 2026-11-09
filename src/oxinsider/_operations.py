"""Generated from the 0xinsider OpenAPI document by scripts/generate.py. Do not edit.

One method per documented operation, typed from the document's own schemas.
``oxinsider.types`` holds the request and response shapes and the policy they
follow; ``Client`` provides ``_call`` and ``_download``."""

from __future__ import annotations

from typing import Any, Literal, NamedTuple, overload

from ._download import AsyncDownload, Download
from ._response import ApiResponse
from .types import (
    AccountIdentity,
    BatchGetMarketCloseBody,
    BatchGetMarketCloseResponse,
    BatchGetMarketFlowBody,
    BatchGetMarketFlowResponse,
    BatchGetMarketIntelResponse,
    BatchGetTradersBody,
    BatchGetTradersResponse,
    ComboFillsResponse,
    ComboResponse,
    CombosSummaryResponse,
    CreateMcpJsonRpcResponseBody,
    CreateMcpJsonRpcResponseResponse,
    CreateWebhookRequest,
    CreateWebhookResponse,
    CreateWebhookVerificationAttemptRequest,
    CreateWebhookVerificationAttemptResponse,
    EdgeHunterBoardResponse,
    EdgeHunterObservationsResponse,
    EdgeHunterSignalsResponse,
    ExploreMarketsResponse,
    GetApiDiscoveryResponse,
    GetCategoryLeaderboardResponse,
    GetCoverageResponse,
    GetEventReplaySinceResponse,
    GetGameHoldersResponse,
    GetGameResponse,
    GetGameSharpMoneyResponse,
    GetHealthResponse,
    GetInsiderRadarFlagResponse,
    GetLargeTradeResponse,
    GetMarketCandlesResponse,
    GetMarketCloseResponse,
    GetMarketFlowResponse,
    GetMarketHoldersResponse,
    GetMarketIntelResponse,
    GetMarketSnapshotResponse,
    GetMarketTopHoldersResponse,
    GetMarketWalletsInOutResponse,
    GetPickOfTheDayArchiveResponse,
    GetPickOfTheDayLedgerEntryResponse,
    GetPickOfTheDayLedgerResponse,
    GetPickOfTheDayResponse,
    GetPickOfTheDayStatsResponse,
    GetPositionTimelineResponse,
    GetReportsResponse,
    GetResolutionReportResponse,
    GetSportLeaderboardResponse,
    GetSuspiciousTradeResponse,
    GetTraderCategoryRecordsResponse,
    GetTraderClvResponse,
    GetTraderContextResponse,
    GetTraderExportSnapshotResponse,
    GetTraderGradeAtResponse,
    GetTraderPnlResponse,
    GetTraderResponse,
    GetWhaleTradeResponse,
    ListCategoryLeadersResponse,
    ListGameMarketsResponse,
    ListGameTradesResponse,
    ListGamesResponse,
    ListLargePositionsResponse,
    ListLargeTradeCounterpartyExecutionsResponse,
    ListLargeTradeCounterpartyMakersResponse,
    ListLargeTradeHistoryResponse,
    ListLargeTradesResponse,
    ListLeaderboardLeaguesResponse,
    ListLeaderboardResponse,
    ListMarketTradesResponse,
    ListPositionsResponse,
    ListPropsResponse,
    ListSettledMarketsResponse,
    ListSmartMoneyFlowsResponse,
    ListSuspiciousTradesResponse,
    ListTrendingWalletsResponse,
    ListWebhookDeliveriesResponse,
    ListWebhookEventsResponse,
    ListWebhooksResponse,
    ListWhaleTradeHistoryResponse,
    ListWhaleTradesResponse,
    NotModifiedResponse,
    RedeliverWebhookDeliveryResponse,
    RegisterAgentResponse,
    SearchContentResponse,
    SearchMarketsResponse,
    SubmitWhaleDatasetBody,
    TraderExportJob,
    UpdateWebhookRequest,
    Usage,
    VerifyWebhookRequest,
    WhaleDatasetJob,
)


OPENAPI_VERSION = "1.0.0"


class Operation(NamedTuple):
    method: str
    path: str
    streaming: bool = False
    redirect: bool = False
    accept: str = "application/json"


OPERATIONS: dict[str, Operation] = {
    "getApiDiscovery": Operation("GET", "/api/v1", streaming=False, redirect=False),
    "redirectApiOpenapiSpec": Operation("GET", "/api/v1/openapi.json", streaming=False, redirect=True),
    "registerAgent": Operation("POST", "/api/v1/agents/register", streaming=False, redirect=False),
    "getTrader": Operation("GET", "/api/v1/trader/{address}", streaming=False, redirect=False),
    "getTraderContextMarkdown": Operation("GET", "/api/v1/trader/{address}/context.md", streaming=False, redirect=False, accept="text/markdown"),
    "getTraderGradeAt": Operation("GET", "/api/v1/trader/{address}/grade-at", streaming=False, redirect=False),
    "getTraderClv": Operation("GET", "/api/v1/trader/{address}/clv", streaming=False, redirect=False),
    "getTraderContext": Operation("GET", "/api/v1/trader/{address}/context", streaming=False, redirect=False),
    "batchGetTraders": Operation("POST", "/api/v1/traders/batch", streaming=False, redirect=False),
    "getPositionTimeline": Operation("GET", "/api/v1/trader/{address}/position-timeline", streaming=False, redirect=False),
    "getTraderCategoryRecords": Operation("GET", "/api/v1/trader/{address}/categories", streaming=False, redirect=False),
    "getTraderPnl": Operation("GET", "/api/v1/trader/{address}/pnl", streaming=False, redirect=False),
    "getPositionTimelineById": Operation("GET", "/api/v1/traders/{trader}/position-timeline", streaming=False, redirect=False),
    "listProps": Operation("GET", "/api/v1/props", streaming=False, redirect=False),
    "listPositions": Operation("GET", "/api/v1/positions", streaming=False, redirect=False),
    "listLargePositions": Operation("GET", "/api/v1/large-positions", streaming=False, redirect=False),
    "listLargeTrades": Operation("GET", "/api/v1/large-trades", streaming=False, redirect=False),
    "listWhaleTrades": Operation("GET", "/api/v1/whale-trades", streaming=False, redirect=False),
    "listLargeTradeHistory": Operation("GET", "/api/v1/large-trades/history", streaming=False, redirect=False),
    "listWhaleTradeHistory": Operation("GET", "/api/v1/whale-trades/history", streaming=False, redirect=False),
    "getLargeTrade": Operation("GET", "/api/v1/large-trades/{id}", streaming=False, redirect=False),
    "getWhaleTrade": Operation("GET", "/api/v1/whale-trades/{id}", streaming=False, redirect=False),
    "listLargeTradeCounterpartyExecutions": Operation("GET", "/api/v1/large-trades/{id}/counterparties/executions", streaming=False, redirect=False),
    "listWhaleTradeCounterpartyExecutions": Operation("GET", "/api/v1/whale-trades/{id}/counterparties/executions", streaming=False, redirect=False),
    "listLargeTradeCounterpartyMakers": Operation("GET", "/api/v1/large-trades/{id}/counterparties/executions/{execution_id}/makers", streaming=False, redirect=False),
    "listWhaleTradeCounterpartyMakers": Operation("GET", "/api/v1/whale-trades/{id}/counterparties/executions/{execution_id}/makers", streaming=False, redirect=False),
    "listLeaderboard": Operation("GET", "/api/v1/leaderboard", streaming=False, redirect=False),
    "getPickOfTheDay": Operation("GET", "/api/v1/pick-of-the-day", streaming=False, redirect=False),
    "getPickOfTheDayArchive": Operation("GET", "/api/v1/pick-of-the-day/archive", streaming=False, redirect=False),
    "getPickOfTheDayStats": Operation("GET", "/api/v1/pick-of-the-day/stats", streaming=False, redirect=False),
    "getPickOfTheDayLedger": Operation("GET", "/api/v1/pick-of-the-day/ledger", streaming=False, redirect=False),
    "listTrendingWallets": Operation("GET", "/api/v1/leaderboard/trending", streaming=False, redirect=False),
    "listLeaderboardLeagues": Operation("GET", "/api/v1/leaderboard/leagues", streaming=False, redirect=False),
    "getSportLeaderboard": Operation("GET", "/api/v1/leaderboard/sports/{sport}", streaming=False, redirect=False),
    "listCategoryLeaders": Operation("GET", "/api/v1/leaderboard/categories", streaming=False, redirect=False),
    "getCategoryLeaderboard": Operation("GET", "/api/v1/leaderboard/categories/{slug}", streaming=False, redirect=False),
    "searchMarkets": Operation("GET", "/api/v1/markets/search", streaming=False, redirect=False),
    "searchContent": Operation("GET", "/api/v1/content/search", streaming=False, redirect=False),
    "listSettledMarkets": Operation("GET", "/api/v1/markets/settled", streaming=False, redirect=False),
    "exploreMarkets": Operation("GET", "/api/v1/markets/explore", streaming=False, redirect=False),
    "listSmartMoneyFlows": Operation("GET", "/api/v1/markets/smart-money-flows", streaming=False, redirect=False),
    "listSharpMoneyFlows": Operation("GET", "/api/v1/markets/sharp-money-flows", streaming=False, redirect=False),
    "listPreGameSides": Operation("GET", "/api/v1/sports/pre-game-sides", streaming=False, redirect=False),
    "listPreGameSideObservations": Operation("GET", "/api/v1/sports/pre-game-side-observations", streaming=False, redirect=False),
    "listSportsEdgeSignals": Operation("GET", "/api/v1/sports-edge-signals", streaming=False, redirect=False),
    "listSportsEdgeObservations": Operation("GET", "/api/v1/sports-edge-observations", streaming=False, redirect=False),
    "getCoverage": Operation("GET", "/api/v1/coverage", streaming=False, redirect=False),
    "getPlatforms": Operation("GET", "/api/v1/platforms", streaming=False, redirect=False),
    "getMarketHolders": Operation("GET", "/api/v1/market/{condition_id}/holders", streaming=False, redirect=False),
    "getMarketTopHolders": Operation("GET", "/api/v1/market/{condition_id}/top-holders", streaming=False, redirect=False),
    "getMarketFlow": Operation("GET", "/api/v1/market/{condition_id}/flow", streaming=False, redirect=False),
    "getMarketIntel": Operation("GET", "/api/v1/market/{condition_id}/intel", streaming=False, redirect=False),
    "batchGetMarketFlow": Operation("POST", "/api/v1/markets/flow/batch", streaming=False, redirect=False),
    "batchGetMarketClose": Operation("POST", "/api/v1/markets/close/batch", streaming=False, redirect=False),
    "batchGetMarketIntel": Operation("POST", "/api/v1/markets/intel/batch", streaming=False, redirect=False),
    "getMarketSnapshot": Operation("GET", "/api/v1/market/{condition_id}/snapshot", streaming=False, redirect=False),
    "getMarketCandles": Operation("GET", "/api/v1/market/{condition_id}/candles", streaming=False, redirect=False),
    "getMarketClose": Operation("GET", "/api/v1/market/{condition_id}/close", streaming=False, redirect=False),
    "listMarketTrades": Operation("GET", "/api/v1/market/{condition_id}/trades", streaming=False, redirect=False),
    "getMarketWalletsInOut": Operation("GET", "/api/v1/market/{condition_id}/wallets-in-out", streaming=False, redirect=False),
    "listSuspiciousTrades": Operation("GET", "/api/v1/suspicious-trades", streaming=False, redirect=False),
    "getSuspiciousTrade": Operation("GET", "/api/v1/suspicious-trades/{id}", streaming=False, redirect=False),
    "listGames": Operation("GET", "/api/v1/games", streaming=False, redirect=False),
    "getGame": Operation("GET", "/api/v1/games/{event_slug}", streaming=False, redirect=False),
    "listGameMarkets": Operation("GET", "/api/v1/games/{event_slug}/markets", streaming=False, redirect=False),
    "getGameSharpMoney": Operation("GET", "/api/v1/games/{event_slug}/sharp-money", streaming=False, redirect=False),
    "listGameTrades": Operation("GET", "/api/v1/games/{event_slug}/trades", streaming=False, redirect=False),
    "getGameHolders": Operation("GET", "/api/v1/games/{event_slug}/holders", streaming=False, redirect=False),
    "listInsiderRadar": Operation("GET", "/api/v1/insider-radar", streaming=False, redirect=False),
    "getInsiderRadarFlag": Operation("GET", "/api/v1/insider-radar/{id}", streaming=False, redirect=False),
    "getStream": Operation("GET", "/api/v1/stream", streaming=True, redirect=False),
    "getEventReplaySince": Operation("GET", "/api/v1/events/feed/since", streaming=False, redirect=False),
    "listWebhooks": Operation("GET", "/api/v1/webhooks", streaming=False, redirect=False),
    "createWebhook": Operation("POST", "/api/v1/webhooks", streaming=False, redirect=False),
    "listWebhookEvents": Operation("GET", "/api/v1/webhooks/events", streaming=False, redirect=False),
    "listWebhookDeliveries": Operation("GET", "/api/v1/webhooks/{id}/deliveries", streaming=False, redirect=False),
    "redeliverWebhookDelivery": Operation("POST", "/api/v1/webhooks/{id}/deliveries/{delivery_id}/redeliver", streaming=False, redirect=False),
    "getWebhook": Operation("GET", "/api/v1/webhooks/{id}", streaming=False, redirect=False),
    "updateWebhook": Operation("PATCH", "/api/v1/webhooks/{id}", streaming=False, redirect=False),
    "deleteWebhook": Operation("DELETE", "/api/v1/webhooks/{id}", streaming=False, redirect=False),
    "verifyWebhook": Operation("POST", "/api/v1/webhooks/{id}/verify", streaming=False, redirect=False),
    "prepareWebhookSecret": Operation("POST", "/api/v1/webhooks/{id}/rotate-secret/prepare", streaming=False, redirect=False),
    "activateWebhookSecret": Operation("POST", "/api/v1/webhooks/{id}/rotate-secret/activate", streaming=False, redirect=False),
    "retireWebhookSecret": Operation("POST", "/api/v1/webhooks/{id}/rotate-secret/retire", streaming=False, redirect=False),
    "rotateWebhookSecret": Operation("POST", "/api/v1/webhooks/{id}/rotate-secret", streaming=False, redirect=False),
    "getHealth": Operation("GET", "/api/v1/health", streaming=False, redirect=False),
    "openMcpEventStream": Operation("GET", "/api/v1/mcp", streaming=False, redirect=False),
    "createMcpJsonRpcResponse": Operation("POST", "/api/v1/mcp", streaming=False, redirect=False),
    "getReports": Operation("GET", "/api/v1/reports", streaming=False, redirect=False),
    "getDailyReportSnapshot": Operation("GET", "/api/v1/reports/daily", streaming=False, redirect=False),
    "getWeeklyReportSnapshot": Operation("GET", "/api/v1/reports/weekly", streaming=False, redirect=False),
    "getMonthlyReportSnapshot": Operation("GET", "/api/v1/reports/monthly", streaming=False, redirect=False),
    "getResolutionReport": Operation("GET", "/api/v1/reports/resolutions", streaming=False, redirect=False),
    "getTraderExportSnapshot": Operation("GET", "/api/v1/trader/{address}/export", streaming=False, redirect=False),
    "submitTraderExport": Operation("POST", "/api/v1/trader/{address}/export", streaming=False, redirect=False),
    "getTraderExportStatus": Operation("GET", "/api/v1/trader/{address}/export/status", streaming=False, redirect=False),
    "cancelTraderExport": Operation("POST", "/api/v1/trader/{address}/export/cancel", streaming=False, redirect=False),
    "downloadTraderExport": Operation("GET", "/api/v1/trader/{address}/export/download", streaming=False, redirect=True),
    "getUsage": Operation("GET", "/api/v1/usage", streaming=False, redirect=False),
    "getMarketContextMarkdown": Operation("GET", "/api/v1/market/{condition_id}/context.md", streaming=False, redirect=False, accept="text/markdown"),
    "getAccountIdentity": Operation("GET", "/api/v1/me", streaming=False, redirect=False),
    "submitWhaleDataset": Operation("POST", "/api/v1/datasets/whale-trades", streaming=False, redirect=False),
    "getWhaleDatasetStatus": Operation("GET", "/api/v1/datasets/whale-trades/{job_id}", streaming=False, redirect=False),
    "downloadWhaleDataset": Operation("GET", "/api/v1/datasets/whale-trades/{job_id}/download", streaming=False, redirect=True),
    "cancelWhaleDataset": Operation("POST", "/api/v1/datasets/whale-trades/{job_id}/cancel", streaming=False, redirect=False),
    "getPickOfTheDayLedgerEntry": Operation("GET", "/api/v1/pick-of-the-day/ledger/{pick_id}", streaming=False, redirect=False),
    "createWebhookVerificationAttempt": Operation("POST", "/api/v1/webhooks/{id}/verification-attempts", streaming=False, redirect=False),
    "getWebhookVerificationAttempt": Operation("GET", "/api/v1/webhooks/{id}/verification-attempts/{attempt_id}", streaming=False, redirect=False),
    "listComboFills": Operation("GET", "/api/v1/combos/fills", streaming=False, redirect=False),
    "getCombosSummary": Operation("GET", "/api/v1/combos/summary", streaming=False, redirect=False),
    "getCombo": Operation("GET", "/api/v1/combos/{condition_id}", streaming=False, redirect=False),
    "getEdgeHunter": Operation("GET", "/api/v1/edge-hunter", streaming=False, redirect=False),
}


class OperationsMixin:
    """One method per documented operation, each returning the decoded body.

    A JSON operation returns its response envelope, a Markdown one the text,
    and a redirect-only one a streaming ``Download``. An operation that takes
    ``if_none_match`` can also answer ``NotModifiedResponse``: that is the 304,
    and it only happens when you send a validator."""

    def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by Client
        raise NotImplementedError

    def _download(self, operation_id: str, **kwargs: Any) -> Download:  # pragma: no cover - provided by Client
        raise NotImplementedError

    def get_api_discovery(
        self,
    ) -> GetApiDiscoveryResponse:
        """API discovery.

        ``GET /api/v1`` (operationId ``getApiDiscovery``).

        Unauthenticated API-origin discovery document pointing agents to the canonical API base
        URL, full docs, web-origin OpenAPI spec, health check, and the COMPLETE index of
        authenticated data routes. data.authenticated_routes is the whole authenticated route
        surface, not a sample: it carries every ...
        """
        result: GetApiDiscoveryResponse = self._call("getApiDiscovery", path_params={}, query={})
        return result

    def redirect_api_openapi_spec(
        self,
    ) -> Download:
        """Redirect to the canonical OpenAPI spec.

        ``GET /api/v1/openapi.json`` (operationId ``redirectApiOpenapiSpec``).

        Unauthenticated API-origin compatibility redirect to the canonical web-origin OpenAPI
        JSON document at https://0xinsider.com/api/v1/openapi.json.

        Returns a ``Download``: the redirect is followed once, without the credential, and the
        file is streamed. Iterate it, ``save(path)`` it for its SHA-256, or ``read()`` it
        (bounded); ``close()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.
        """
        return self._download("redirectApiOpenapiSpec", path_params={}, query={})

    def register_agent(
        self,
    ) -> RegisterAgentResponse:
        """Register an agent for a sandbox key.

        ``POST /api/v1/agents/register`` (operationId ``registerAgent``).

        Self-serve agent onboarding: no account, no request body, no human step. Returns a
        sandbox API key (oxi_sk_test_...) and the path to live access. The key works only on the
        sandbox server (https://0xinsider.com/sandbox/api/v1), where it is optional: send it as
        Authorization: Bearer to exercise the ...
        """
        result: RegisterAgentResponse = self._call("registerAgent", path_params={}, query={})
        return result

    @overload
    def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: None = None,
    ) -> GetTraderResponse: ...

    @overload
    def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: str | None,
    ) -> GetTraderResponse | NotModifiedResponse: ...

    def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: str | None = None,
    ) -> GetTraderResponse | NotModifiedResponse:
        """Get trader.

        ``GET /api/v1/trader/{address}`` (operationId ``getTrader``).

        Returns a trader's grade (S through F), P&L, win rate, and optional strategy/category
        data. The path accepts either an Ethereum wallet address, a known trader username, or a
        trd_-prefixed trader ID emitted by this API. A wallet address this API does not track
        yet returns 200 with sync_status ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            expand: Include heavy fields and trust metadata. Repeatable: strategy, categories, trust, breakdowns. breakdowns adds the profile's strategy measures ...
            max_age_s: Opt into a whole-response freshness ceiling in seconds. The server returns 200 only when data_quality.status is fresh or stale and data_quality.as_of is no ...
        """
        result: GetTraderResponse | NotModifiedResponse = self._call("getTrader", path_params={"address": address}, query={"expand": expand, "max_age_s": max_age_s}, if_none_match=if_none_match)
        return result

    def get_trader_context_markdown(
        self,
        address: str,
    ) -> str:
        """Get trader context (Markdown).

        ``GET /api/v1/trader/{address}/context.md`` (operationId ``getTraderContextMarkdown``).

        Returns a single human- and LLM-readable Markdown briefing for one trader: identity,
        grade, P&L, position coverage, and freshness. The path accepts an Ethereum wallet
        address (0x...), a known trader username, or a trd_-prefixed trader ID emitted by this
        API. A wallet address this API does not track ...
        """
        result: str = self._call("getTraderContextMarkdown", path_params={"address": address}, query={})
        return result

    @overload
    def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: None = None,
    ) -> GetTraderGradeAtResponse: ...

    @overload
    def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: str | None,
    ) -> GetTraderGradeAtResponse | NotModifiedResponse: ...

    def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: str | None = None,
    ) -> GetTraderGradeAtResponse | NotModifiedResponse:
        """Get a trader grade proven visible at a past instant.

        ``GET /api/v1/trader/{address}/grade-at`` (operationId ``getTraderGradeAt``).

        Reads one trader's recorded grade at as_of from prospective visibility evidence. Before
        the first recorded observation, after deletion, or during a grade-transition gap, status
        is unknown and grade is null; a recorded ungraded trader instead has status ungraded.
        available_from is the first proven ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            as_of: Required. RFC3339 instant whose historically visible grade is requested. Future instants are refused. Send the trade or decision time, not the ranking date.
        """
        result: GetTraderGradeAtResponse | NotModifiedResponse = self._call("getTraderGradeAt", path_params={"address": address}, query={"as_of": as_of}, if_none_match=if_none_match)
        return result

    @overload
    def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: None = None,
    ) -> GetTraderClvResponse: ...

    @overload
    def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: str | None,
    ) -> GetTraderClvResponse | NotModifiedResponse: ...

    def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: str | None = None,
    ) -> GetTraderClvResponse | NotModifiedResponse:
        """Get a trader's closing line value on large trades.

        ``GET /api/v1/trader/{address}/clv`` (operationId ``getTraderClv``).

        Closing line value (CLV) over one wallet's large trades in a window: the trades GET
        /api/v1/large-trades/history?trader= returns for the same from, to, min_size and
        category, each measured exactly as its clv object is. CLV is in cents per share against
        the market's stored closing line (GET ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            from_: Inclusive RFC3339 lower bound on the trade time. Defaults to 90 days before to.
            to: Exclusive RFC3339 upper bound on the trade time. Defaults to now; must be after from, and at most 366 days after it.
            min_size: Minimum trade size in USD. The capture floor was 3,000 USD before 2026-07-06 and 10,000 USD from then (1,000 USD in earnings markets), so 10000 gives one size ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
        """
        result: GetTraderClvResponse | NotModifiedResponse = self._call("getTraderClv", path_params={"address": address}, query={"from": from_, "to": to, "min_size": min_size, "category": category}, if_none_match=if_none_match)
        return result

    @overload
    def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: None = None,
    ) -> GetTraderContextResponse: ...

    @overload
    def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None,
    ) -> GetTraderContextResponse | NotModifiedResponse: ...

    def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None = None,
    ) -> GetTraderContextResponse | NotModifiedResponse:
        """Get trader context (JSON).

        ``GET /api/v1/trader/{address}/context`` (operationId ``getTraderContext``).

        Returns a single structured context object for one trader: the full trader profile (same
        shape as GET /api/v1/trader/{address}) plus a position_summary (sync coverage and
        realized/unrealized P&L rollups, with an as_of open-position freshness clock), the
        data_as_of freshness timestamp (the ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetTraderContextResponse | NotModifiedResponse = self._call("getTraderContext", path_params={"address": address}, query={}, if_none_match=if_none_match)
        return result

    def batch_get_traders(
        self,
        body: BatchGetTradersBody,
    ) -> BatchGetTradersResponse:
        """Batch traders.

        ``POST /api/v1/traders/batch`` (operationId ``batchGetTraders``).

        Returns traders for 1-25 wallet addresses or known usernames. Results preserve request
        order, duplicate inputs return duplicate rows, and each item is charged one batch item
        unit before execution. A wallet address this API does not track yet returns data with
        sync_status "unknown", matching the ...
        """
        result: BatchGetTradersResponse = self._call("batchGetTraders", path_params={}, query={}, body=body)
        return result

    @overload
    def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetPositionTimelineResponse: ...

    @overload
    def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetPositionTimelineResponse | NotModifiedResponse: ...

    def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetPositionTimelineResponse | NotModifiedResponse:
        """Get a trader's position timeline for one market.

        ``GET /api/v1/trader/{address}/position-timeline`` (operationId ``getPositionTimeline``).

        Returns every stored Polymarket fill for one tracked trader in one market, newest first,
        with outcome-specific running_amount and running_avg_price including all earlier stored
        fills before pagination. Fills come from the full fill ledger, the same rows the trade
        export serves, at any date (#33245; ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            condition_id: Required. Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        result: GetPositionTimelineResponse | NotModifiedResponse = self._call("getPositionTimeline", path_params={"address": address}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: None = None,
    ) -> GetTraderCategoryRecordsResponse: ...

    @overload
    def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: str | None,
    ) -> GetTraderCategoryRecordsResponse | NotModifiedResponse: ...

    def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: str | None = None,
    ) -> GetTraderCategoryRecordsResponse | NotModifiedResponse:
        """Get trader category win records.

        ``GET /api/v1/trader/{address}/categories`` (operationId ``getTraderCategoryRecords``).

        Returns one wallet's win record in every canonical category it has a settled market in:
        wins, decided (wins plus losses) and the rate, per category, busiest category first.
        These are the same counts the Pick of the Day holder chips carry. The Esports record
        also carries games: the wallet's record ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            category: Filter to one canonical category, matched through the same rollup every other category surface uses: soccer, EPL and champions league all reach Soccer, every ...
        """
        result: GetTraderCategoryRecordsResponse | NotModifiedResponse = self._call("getTraderCategoryRecords", path_params={"address": address}, query={"category": category}, if_none_match=if_none_match)
        return result

    def get_trader_pnl(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        sections: list[Literal["entries", "stats", "monthly", "year_totals", "drawdown"]] | None = None,
    ) -> GetTraderPnlResponse:
        """Get trader P&L time series.

        ``GET /api/v1/trader/{address}/pnl`` (operationId ``getTraderPnl``).

        Returns a trader's sports and esports daily P&L time series and pre-derived stats:
        entries (daily realized P&L and its running sum), period stats (all/90d/30d/7d), monthly
        aggregation, per-year totals, the drawdown series, series_status, and realized, which
        reconciles the days with the wallet's ...

        Query parameters:
            from_: Inclusive UTC calendar-date lower bound in YYYY-MM-DD form for the daily series (entries and drawdown). Omit for the whole stored history. A value that is not ...
            to: Inclusive UTC calendar-date upper bound in YYYY-MM-DD form for the daily series (entries and drawdown). Omit for the whole stored history. A value that is not ...
            sections: Which sections of the object to return. Repeatable and comma-separated: entries, stats, monthly, year_totals, drawdown. Omit it, or send it empty, for all ...
        """
        result: GetTraderPnlResponse = self._call("getTraderPnl", path_params={"address": address}, query={"from": from_, "to": to, "sections": sections})
        return result

    @overload
    def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetPositionTimelineResponse: ...

    @overload
    def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetPositionTimelineResponse | NotModifiedResponse: ...

    def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetPositionTimelineResponse | NotModifiedResponse:
        """Get a trader's position timeline (unified identity resolver).

        ``GET /api/v1/traders/{trader}/position-timeline`` (operationId ``getPositionTimelineById``).

        Unified trader-timeline route (#4975). {trader} accepts all five identity shapes - 0x...
        wallet, username, trd_-prefixed trader id, bare integer id, and @username (a username
        lookup only, for all-digit usernames) - resolved by the single shared trader-identity
        resolver. Returns every stored ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            condition_id: Required. Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        result: GetPositionTimelineResponse | NotModifiedResponse = self._call("getPositionTimelineById", path_params={"trader": trader}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: None = None,
    ) -> ListPropsResponse: ...

    @overload
    def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: str | None,
    ) -> ListPropsResponse | NotModifiedResponse: ...

    def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: str | None = None,
    ) -> ListPropsResponse | NotModifiedResponse:
        """List player props across a league.

        ``GET /api/v1/props`` (operationId ``listProps``).

        Player props for the catalog's games of one league, one row per market, ordered by game
        slug, stat, player and line. NFL files props on a game's -player-props and -first-td-
        scorer child events and NBA on the game event; this reads both, so a caller does not
        walk GET /api/v1/games and then each ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            league: Required. League tag as GET /api/v1/games coverage.leagues spells it, for example nfl or nba. Matched case-insensitively.
            starts_after: RFC 3339 kickoff bound. A game with no published kickoff is excluded whenever either bound is set.
            starts_before: RFC 3339 kickoff bound, inclusive.
            player: Part of player.name, ignoring case and accents: jokic matches Nikola Jokić. A row with no player does not match.
            stat: Provider sportsMarketType values to keep, case-insensitive, for example passing_yards or points. Repeat the parameter or send a comma-separated list. An ...
            status: active (default), closed, or all. closed means the provider closed the market or it resolved.
            max_spread_c: Keep only props with an outcome whose cached best ask less best bid is at most this many cents: above 0, at most 100, in steps of 0.01. The books are the ones ...
            min_book_usd_within_2c: Keep only props with an outcome whose cached book holds at least this many USD on each side within 2 cents of its midpoint: bids at or above the midpoint minus ...
            limit: Page size. Out-of-range values are clamped to 1..200.
            cursor: Opaque prp_v1_ cursor from next_cursor, sent with the same filters. A cursor this endpoint did not issue returns 400 with error.param=cursor.
            expand: quotes adds each outcome's cached quote, as on GET /api/v1/games/{event_slug}/markets; it adds 1 to the cost, on every plan. Repeatable: quotes.
        """
        result: ListPropsResponse | NotModifiedResponse = self._call("listProps", path_params={}, query={"league": league, "starts_after": starts_after, "starts_before": starts_before, "player": player, "stat": stat, "status": status, "max_spread_c": max_spread_c, "min_book_usd_within_2c": min_book_usd_within_2c, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: None = None,
    ) -> ListPositionsResponse: ...

    @overload
    def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: str | None,
    ) -> ListPositionsResponse | NotModifiedResponse: ...

    def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: str | None = None,
    ) -> ListPositionsResponse | NotModifiedResponse:
        """List current positions (positions-board feed).

        ``GET /api/v1/positions`` (operationId ``listPositions``).

        Returns the current positions-board feed backed by the wallet_positions mirror. Ordered
        by current_value_usd DESC with deterministic (wallet, condition_id, outcome_index)
        tiebreakers. Pre-reconcile rows (current_value_usd IS NULL) are excluded. Positions on
        resolved markets are excluded: a position ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of current positions to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            consistency: live (default) reads the current value-ordered board. snapshot requires wallet and freezes up to 500 matching rows and 2 MB for up to five minutes. Keep ...
            min_size: Minimum current position value in USD. Defaults to 100 when omitted, or to 0 when wallet is present; send 0 to include every reconciled position.
            category: Exact match against provider-backed market_canonical.category. Sports and esports only (#27311): a category outside them returns 400 bad_request with param ...
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id emitted by V1 responses. Combine with min_size=0 for every reconciled ...
            wallet: Scope to one wallet or a book of wallets (repeatable, up to 25 per request; comma-separated values inside one occurrence also work). Each value is a wallet ...
            min_grade: Minimum trader grade allowlist. `A` matches S and A; `B` matches S, A, B; etc.
            side: Filter by the binary outcome side. `yes` maps to outcome_index=0, `no` to outcome_index=1.
        """
        result: ListPositionsResponse | NotModifiedResponse = self._call("listPositions", path_params={}, query={"limit": limit, "cursor": cursor, "consistency": consistency, "min_size": min_size, "category": category, "condition_id": condition_id, "wallet": wallet, "min_grade": min_grade, "side": side}, if_none_match=if_none_match)
        return result

    def list_large_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        condition_id: str | None = None,
    ) -> ListLargePositionsResponse:
        """List large positions.

        ``GET /api/v1/large-positions`` (operationId ``listLargePositions``).

        Returns the largest current open positions from graded traders, value-descending, with
        opaque cursor pagination. This is a change-detection feed, not a holder list: a row
        needs a current value of at least 50,000 USD and a live detection in the last 24 hours,
        so a wallet that holds a market without ...

        Query parameters:
            limit: Maximum number of large positions to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque pagination cursor from a previous response.
            min_size: Minimum position value in USD. Raises the feed's own floor of 50,000 USD; a smaller value does not lower it.
            category: One RFC 4180 CSV record of exact current provider-backed market_canonical.category values. Legacy unquoted lists such as NBA,WNBA remain valid; values ...
            min_grade: Minimum trader grade. Matched against the trader.grade each row returns, the wallet's current grade, so every row listed shows a grade at or above this floor.
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id (round-trips a value from a list response). Must be 0x followed by 64 ...
        """
        result: ListLargePositionsResponse = self._call("listLargePositions", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "condition_id": condition_id})
        return result

    @overload
    def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListLargeTradesResponse: ...

    @overload
    def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListLargeTradesResponse | NotModifiedResponse: ...

    def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListLargeTradesResponse | NotModifiedResponse:
        """List large trades.

        ``GET /api/v1/large-trades`` (operationId ``listLargeTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of recent large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade now (trader.grade), the wallet's grade when this page is read, not when the trade filled. A wallet re-graded after a trade enters or ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            since: Return only the trades recorded after this one. Pass the id of a large trade this API returned (wt_<n>, or the bare integer). The answer keeps the list shape ...
            condition_id: Only this market's large trades: an exact raw provider condition_id. The page is read from the market's own index, newest first, and pages with cursor; it ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListLargeTradesResponse | NotModifiedResponse = self._call("listLargeTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "min_market_volume_share": min_market_volume_share, "sort": sort, "since": since, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListWhaleTradesResponse: ...

    @overload
    def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListWhaleTradesResponse | NotModifiedResponse: ...

    def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListWhaleTradesResponse | NotModifiedResponse:
        """List whale trades.

        ``GET /api/v1/whale-trades`` (operationId ``listWhaleTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of recent large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade now (trader.grade), the wallet's grade when this page is read, not when the trade filled. A wallet re-graded after a trade enters or ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            since: Return only the trades recorded after this one. Pass the id of a large trade this API returned (wt_<n>, or the bare integer). The answer keeps the list shape ...
            condition_id: Only this market's large trades: an exact raw provider condition_id. The page is read from the market's own index, newest first, and pages with cursor; it ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListWhaleTradesResponse | NotModifiedResponse = self._call("listWhaleTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "min_market_volume_share": min_market_volume_share, "sort": sort, "since": since, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListLargeTradeHistoryResponse: ...

    @overload
    def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListLargeTradeHistoryResponse | NotModifiedResponse: ...

    def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListLargeTradeHistoryResponse | NotModifiedResponse:
        """Replay historical large trades.

        ``GET /api/v1/large-trades/history`` (operationId ``listLargeTradeHistory``).

        Returns historical large trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of historical large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD. The capture floor was 3,000 USD before 2026-07-06 and 10,000 USD from then (1,000 USD in earnings markets), so 10000 gives one size ...
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, username, or trd_-prefixed trader ID, resolved against the traders table. Unknown traders return an ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade as of today (trader.grade), not at trade time. On a historical window it selects wallets by a grade they may have earned after the trade; ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListLargeTradeHistoryResponse | NotModifiedResponse = self._call("listLargeTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to, "min_market_volume_share": min_market_volume_share, "sort": sort, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListWhaleTradeHistoryResponse: ...

    @overload
    def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListWhaleTradeHistoryResponse | NotModifiedResponse: ...

    def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListWhaleTradeHistoryResponse | NotModifiedResponse:
        """Replay historical whale trades.

        ``GET /api/v1/whale-trades/history`` (operationId ``listWhaleTradeHistory``).

        Returns historical whale trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of historical large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD.
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, or username resolved against the traders table. Unknown traders return an empty list.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade.
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListWhaleTradeHistoryResponse | NotModifiedResponse = self._call("listWhaleTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to, "min_market_volume_share": min_market_volume_share, "sort": sort, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> GetLargeTradeResponse: ...

    @overload
    def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> GetLargeTradeResponse | NotModifiedResponse: ...

    def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetLargeTradeResponse | NotModifiedResponse:
        """Get large trade by ID.

        ``GET /api/v1/large-trades/{id}`` (operationId ``getLargeTrade``).

        Returns one large trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetLargeTradeResponse | NotModifiedResponse = self._call("getLargeTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> GetWhaleTradeResponse: ...

    @overload
    def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> GetWhaleTradeResponse | NotModifiedResponse: ...

    def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetWhaleTradeResponse | NotModifiedResponse:
        """Get whale trade by ID.

        ``GET /api/v1/whale-trades/{id}`` (operationId ``getWhaleTrade``).

        Returns one whale trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses. Deprecated alias of GET /api/v1/large-trades/{id}, kept live
        until its sunset on 2027-02-01 (#16304, #29351); every response carries `Deprecation:
        @1790132400` (RFC 9745, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetWhaleTradeResponse | NotModifiedResponse = self._call("getWhaleTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    def list_large_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListLargeTradeCounterpartyExecutionsResponse:
        """Page counterparty executions.

        ``GET /api/v1/large-trades/{id}/counterparties/executions`` (operationId ``listLargeTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by large-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail.

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the large trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ListLargeTradeCounterpartyExecutionsResponse = self._call("listLargeTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    def list_whale_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListLargeTradeCounterpartyExecutionsResponse:
        """Page counterparty executions.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions`` (operationId ``listWhaleTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by whale-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail. Deprecated alias of GET /api/v1/large-
        trades/{id}/counterparties/executions, kept live until its sunset on ...

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ListLargeTradeCounterpartyExecutionsResponse = self._call("listWhaleTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    def list_large_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListLargeTradeCounterpartyMakersResponse:
        """Page maker counterparties.

        ``GET /api/v1/large-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listLargeTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages.

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the large trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ListLargeTradeCounterpartyMakersResponse = self._call("listLargeTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    def list_whale_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListLargeTradeCounterpartyMakersResponse:
        """Page maker counterparties.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listWhaleTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages. Deprecated alias of GET /api/v1/large-
        trades/{id}/counterparties/executions/{execution_id}/makers, kept live until its sunset
        on 2027-02-01 (#16304, #29351); every response ...

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ListLargeTradeCounterpartyMakersResponse = self._call("listWhaleTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    @overload
    def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: None = None,
    ) -> ListLeaderboardResponse: ...

    @overload
    def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: str | None,
    ) -> ListLeaderboardResponse | NotModifiedResponse: ...

    def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: str | None = None,
    ) -> ListLeaderboardResponse | NotModifiedResponse:
        """Get trader leaderboard.

        ``GET /api/v1/leaderboard`` (operationId ``listLeaderboard``).

        Returns ranked traders (grades S/A/B), by default in the board's own order: score
        descending, with a fixed tiebreak so the order never changes between reads of one
        ranking generation. sort, dir and activity reorder and scope the same wallets the way
        the site's leaderboard does (since 2026-11-02, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of ranked traders to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque lbv1_ pagination cursor from a prior response. It binds the finite score/address boundary to the effective category/strategy filters, and on a sorted ...
            category: Filter by category: a sport or esports bucket, matched case-insensitively. League values fold into their sport (NBA and NCAAB into Basketball, NFL into ...
            strategy: Filter by observed trading style. Current styles: two_sided, category_focused, high_activity, diversified, mixed, unclassified. Current styles count the ...
            sort: Order of the list, the sort columns of the site's leaderboard (/skill-leaderboard). rank (default) is the board's own order, the rank the site and the trader ...
            dir: Direction of sort. Omitted, each sort reads in its natural direction: rank 1 first for rank (asc), largest first for every other sort (desc). The opposite ...
            activity: Limit the list to wallets by recent trading, the site leaderboard's split. active: the wallet's last trade, as its current grade recorded it and aged to today, ...
        """
        result: ListLeaderboardResponse | NotModifiedResponse = self._call("listLeaderboard", path_params={}, query={"limit": limit, "cursor": cursor, "category": category, "strategy": strategy, "sort": sort, "dir": dir, "activity": activity}, if_none_match=if_none_match)
        return result

    @overload
    def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: None = None,
    ) -> GetPickOfTheDayResponse: ...

    @overload
    def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: str | None,
    ) -> GetPickOfTheDayResponse | NotModifiedResponse: ...

    def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayResponse | NotModifiedResponse:
        """Get today's or a past day's Pick of the Day.

        ``GET /api/v1/pick-of-the-day`` (operationId ``getPickOfTheDay``).

        Returns entitled published picks for the current product day, or for the past product
        day named by `date`. Pro includes five selections in total: the designated free
        selection and the first four non-free selections in publication order. Max opens every
        available selection, up to twenty-five. A day ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            date: A product day (America/New_York) in YYYY-MM-DD format, on or before today. Omit it, or send today, for the current read. A past day with no published pick ...
            view: full (default) is the whole recorded set: every pick with its holders, lead backer, sports context, thesis and entry_authorization, and the top-level copy of ...
            pick_id: One entitled published pick of the day, by its stable decimal-string pick_id. The body carries that pick once, as picks[0], beside state, pick_date and ...
        """
        result: GetPickOfTheDayResponse | NotModifiedResponse = self._call("getPickOfTheDay", path_params={}, query={"date": date, "view": view, "pick_id": pick_id}, if_none_match=if_none_match)
        return result

    @overload
    def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetPickOfTheDayArchiveResponse: ...

    @overload
    def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetPickOfTheDayArchiveResponse | NotModifiedResponse: ...

    def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayArchiveResponse | NotModifiedResponse:
        """Get the Pick of the Day track record.

        ``GET /api/v1/pick-of-the-day/archive`` (operationId ``getPickOfTheDayArchive``).

        Returns published picks that have not been withdrawn, with their outcome, modeled
        return, unit score, closing-line value, and cumulative record. Resolved game details and
        results are public. For unauthorized unresolved selections, game identity, category,
        image, publication time, and backed facts ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: full (default) is every row with every field, plus days and hit_rate with its per-pick series. summary returns view, hit_rate without series, one page of short ...
            limit: Rows per page of picks, 1 to 200, default 50. An integer outside that range is clamped into it, like every list limit, and X-Effective-Query reports the limit ...
            cursor: The page.next_cursor of the previous page: the rows after it, newest first. A cursor is a position in the record, so a pick published while you page does not ...
        """
        result: GetPickOfTheDayArchiveResponse | NotModifiedResponse = self._call("getPickOfTheDayArchive", path_params={}, query={"view": view, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: None = None,
    ) -> GetPickOfTheDayStatsResponse: ...

    @overload
    def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: str | None,
    ) -> GetPickOfTheDayStatsResponse | NotModifiedResponse: ...

    def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayStatsResponse | NotModifiedResponse:
        """Get the Pick of the Day track-record breakdown.

        ``GET /api/v1/pick-of-the-day/stats`` (operationId ``getPickOfTheDayStats``).

        The figures behind the stats page, computed from the same rows the archive publishes:
        the hit rate, the win rate the market expected at publication, flat-stake outcome stats
        (drawdown, rolling form, profit factor, concentration), and buckets by day, sport,
        category, access group, month, entry-price ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: full (default) is every section. summary returns view, sections and every section except the five that grow with the record: series, days, categories, months ...
            sections: Exactly the sections to return, in the body's order whatever the request order. Repeatable and comma-separated: hit_rate, series, market_expectations, ...
        """
        result: GetPickOfTheDayStatsResponse | NotModifiedResponse = self._call("getPickOfTheDayStats", path_params={}, query={"view": view, "sections": sections}, if_none_match=if_none_match)
        return result

    @overload
    def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: None = None,
    ) -> GetPickOfTheDayLedgerResponse: ...

    @overload
    def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: str | None,
    ) -> GetPickOfTheDayLedgerResponse | NotModifiedResponse: ...

    def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayLedgerResponse | NotModifiedResponse:
        """Get the Pick of the Day commitment ledger.

        ``GET /api/v1/pick-of-the-day/ledger`` (operationId ``getPickOfTheDayLedger``).

        Returns the pre-game commitment for every published pick, so the public track record can
        be checked by someone who was not watching when the pick dropped. One entry per
        (pick_date, pick_rank), ascending by pick_date then pick_rank, in one of three states.
        `sealed` is an unresolved pick: the hash, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetPickOfTheDayLedgerResponse | NotModifiedResponse = self._call("getPickOfTheDayLedger", path_params={}, query={}, if_none_match=if_none_match)
        return result

    def list_trending_wallets(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        window: Literal["7d", "30d"] | None = None,
    ) -> ListTrendingWalletsResponse:
        """List trending wallets.

        ``GET /api/v1/leaderboard/trending`` (operationId ``listTrendingWallets``).

        Returns wallets ranked by Polymarket weekly/monthly P&L (Polymarket-only discovery),
        with opaque page-cursor pagination. trending_pnl_usd and the by-PNL row order come from
        Polymarket's canonical leaderboard (data-
        api.polymarket.com/v2/leaderboard?time_period=week|month&sort_by=PNL), not a locally ...

        Query parameters:
            limit: Polymarket's weekly leaderboard caps the ranked set at 50 wallets; requests above 50 still return at most 50. Out-of-range values are clamped to 1..50.
            cursor: Opaque pagination cursor from a previous response, bound to its effective limit, window and ranked-board generation. A changed board or request scope returns ...
            window: Trailing window.
        """
        result: ListTrendingWalletsResponse = self._call("listTrendingWallets", path_params={}, query={"limit": limit, "cursor": cursor, "window": window})
        return result

    @overload
    def list_leaderboard_leagues(
        self,
        *,
        if_none_match: None = None,
    ) -> ListLeaderboardLeaguesResponse: ...

    @overload
    def list_leaderboard_leagues(
        self,
        *,
        if_none_match: str | None,
    ) -> ListLeaderboardLeaguesResponse | NotModifiedResponse: ...

    def list_leaderboard_leagues(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ListLeaderboardLeaguesResponse | NotModifiedResponse:
        """List the leagues that have a leaderboard.

        ``GET /api/v1/leaderboard/leagues`` (operationId ``listLeaderboardLeagues``).

        Every league with its own skill leaderboard, grouped by sport, most ranked wallets
        first. Each row's `sport` and `slug` are the `{sport}` path segment and `league` value
        of GET /api/v1/leaderboard/sports/{sport}. A league is listed once its edge sort ranks
        at least `min_ranked` wallets. 503 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ListLeaderboardLeaguesResponse | NotModifiedResponse = self._call("listLeaderboardLeagues", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> GetSportLeaderboardResponse: ...

    @overload
    def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> GetSportLeaderboardResponse | NotModifiedResponse: ...

    def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> GetSportLeaderboardResponse | NotModifiedResponse:
        """Get a sport or league leaderboard.

        ``GET /api/v1/leaderboard/sports/{sport}`` (operationId ``getSportLeaderboard``).

        One sport's skill leaderboard, or with `league` one league's, the board the site's sport
        pages show. Wallets need `min_resolved` resolved markets in the sport or league.
        `sort=edge` (the default) ranks `edge_skill`, the edge over the price paid pulled toward
        the board's `edge_average` by how much ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            league: A league slug of the sport, for example premier-league or cs2, from GET /api/v1/leaderboard/leagues. Omit it for the sport board.
            sort: Ranking axis. Any other value returns 400 bad_request with error.param=sort.
            limit: Rows to return from the top of the board. Out-of-range values are clamped to 1..100.
        """
        result: GetSportLeaderboardResponse | NotModifiedResponse = self._call("getSportLeaderboard", path_params={"sport": sport}, query={"league": league, "sort": sort, "limit": limit}, if_none_match=if_none_match)
        return result

    @overload
    def list_category_leaders(
        self,
        *,
        if_none_match: None = None,
    ) -> ListCategoryLeadersResponse: ...

    @overload
    def list_category_leaders(
        self,
        *,
        if_none_match: str | None,
    ) -> ListCategoryLeadersResponse | NotModifiedResponse: ...

    def list_category_leaders(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ListCategoryLeadersResponse | NotModifiedResponse:
        """List every category's top edge leaders.

        ``GET /api/v1/leaderboard/categories`` (operationId ``listCategoryLeaders``).

        Every sports and esports category's top three edge leaders in one read, the board the
        site's categories index shows. In each category, wallets are ranked as GET
        /api/v1/leaderboard/categories/{slug} ranks them, by the 95% lower bound of their edge
        over the price they paid; only wallets whose lower ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ListCategoryLeadersResponse | NotModifiedResponse = self._call("listCategoryLeaders", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetCategoryLeaderboardResponse: ...

    @overload
    def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetCategoryLeaderboardResponse | NotModifiedResponse: ...

    def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetCategoryLeaderboardResponse | NotModifiedResponse:
        """Get a category's edge leaderboard.

        ``GET /api/v1/leaderboard/categories/{slug}`` (operationId ``getCategoryLeaderboard``).

        One sports or esports category's edge leaderboard, the board the site's category pages
        show. Wallets are ranked by edge_lower_bound, the 95% lower bound of their edge over the
        price they paid in the category, counted over independent events (independent_events
        breaks ties, then the wallet). Only ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            active_within: Keep wallets that traded in the category within this window. all (the default) keeps every ranked wallet.
            min_events: Independent events a wallet needs in the category to be listed. The site offers 0, 50, 100 and 250. Clamped to 0..1000000.
            limit: Maximum number of leaders to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque cel_ pagination cursor from a prior response. It binds the lower-bound/independent-event/wallet boundary to the committed category-skill ranking and to ...
        """
        result: GetCategoryLeaderboardResponse | NotModifiedResponse = self._call("getCategoryLeaderboard", path_params={"slug": slug}, query={"active_within": active_within, "min_events": min_events, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    def search_markets(
        self,
        *,
        q: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        category: str | None = None,
    ) -> SearchMarketsResponse:
        """Search markets.

        ``GET /api/v1/markets/search`` (operationId ``searchMarkets``).

        Search prediction markets by keyword. Returns one representative market per matching
        event, preferring the market whose title is q, then a winner market over a spread, total
        or prop, with status, category, platform metadata and the event_slug. Cursor pagination
        advances over grouped market results ...

        Query parameters:
            q: Required. Search query. Must be 2-512 characters before whitespace trimming and hold at least 2 letters or digits after trimming; a query with fewer letters or digits ...
            limit: Maximum number of matching markets to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            status: Filter by market status. A market is closed once Polymarket has closed trading or it has resolved, and active otherwise; all returns both.
            category: Filter by category. Sports and esports only (#27411): a category outside them returns 400 bad_request with param category and names the accepted buckets. The ...
        """
        result: SearchMarketsResponse = self._call("searchMarkets", path_params={}, query={"q": q, "limit": limit, "cursor": cursor, "status": status, "category": category})
        return result

    def search_content(
        self,
        *,
        q: str | None = None,
        limit: int | None = None,
    ) -> SearchContentResponse:
        """Search editorial content.

        ``GET /api/v1/content/search`` (operationId ``searchContent``).

        Search 0xinsider editorial content by keyword. Returns backend-owned learn, glossary,
        comparison, research, and trading-strategy items with canonical URLs. Opaque ranking
        scores are not exposed.

        Query parameters:
            q: Required. Search query. Must be 1-256 characters before whitespace trimming and non-empty after trimming.
            limit: Maximum content items to return. Out-of-range values are clamped to 1..50.
        """
        result: SearchContentResponse = self._call("searchContent", path_params={}, query={"q": q, "limit": limit})
        return result

    @overload
    def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ListSettledMarketsResponse: ...

    @overload
    def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ListSettledMarketsResponse | NotModifiedResponse: ...

    def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ListSettledMarketsResponse | NotModifiedResponse:
        """List settled game markets since a time.

        ``GET /api/v1/markets/settled`` (operationId ``listSettledMarkets``).

        Game markets Polymarket settled, as 0xinsider recorded them, oldest first by
        (settlement.observed_at, settlement_id): one row per market per settled state, the
        object the market_settled webhook delivers as data. It is the webhook's pull side: catch
        up after downtime from since, or poll with ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            since: RFC 3339 time, required without cursor. Rows whose settlement.observed_at is at or after it. With cursor, the cursor's position replaces it.
            sports_market_type: Comma-separated provider market types to keep, case-insensitive: moneyline, spreads, totals, a prop type; at most 64. Omitted: moneyline, or with cursor the ...
            league: Comma-separated leagues to keep, as the rows' league reports them (nba, epl, or pga for PGA Tour golf); at most 32, each starting with a letter and holding no ...
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque stl_v1_ cursor from next_cursor. It replaces since and keeps the filters it was issued for: a sports_market_type or league sent with it must match them, ...
        """
        result: ListSettledMarketsResponse | NotModifiedResponse = self._call("listSettledMarkets", path_params={}, query={"since": since, "sports_market_type": sports_market_type, "league": league, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: None = None,
    ) -> ExploreMarketsResponse: ...

    @overload
    def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: str | None,
    ) -> ExploreMarketsResponse | NotModifiedResponse: ...

    def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: str | None = None,
    ) -> ExploreMarketsResponse | NotModifiedResponse:
        """Explore markets.

        ``GET /api/v1/markets/explore`` (operationId ``exploreMarkets``).

        Browse whale-active titled markets with category, platform, status, and keyword filters.
        Explore is Polymarket-only: the platform parameter is accepted for backward-
        compatibility but every request returns Polymarket markets. Paginates visible discovery
        entries rather than raw market rows, returns ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            status: Filter by market status. A market is closed once Polymarket has closed trading or it has resolved, and active otherwise; all returns both.
            platform: Filter by source platform. Explore is Polymarket-only; polymarket is the only supported value and the parameter is accepted for backward-compatibility but does ...
            sort: Sort order for the discovery feed. `large_trades` ranks by large-trade activity; `whales` is its deprecated spelling and selects the same order until its ...
            cursor: Opaque pagination cursor from the previous response.
            limit: Page size. Out-of-range values are clamped to 1..48.
            q: Keyword search against market titles. At most 64 characters before whitespace trimming.
        """
        result: ExploreMarketsResponse | NotModifiedResponse = self._call("exploreMarkets", path_params={}, query={"category": category, "status": status, "platform": platform, "sort": sort, "cursor": cursor, "limit": limit, "q": q}, if_none_match=if_none_match)
        return result

    @overload
    def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListSmartMoneyFlowsResponse: ...

    @overload
    def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListSmartMoneyFlowsResponse | NotModifiedResponse: ...

    def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListSmartMoneyFlowsResponse | NotModifiedResponse:
        """List ranked sharp-money flows (deprecated alias).

        ``GET /api/v1/markets/smart-money-flows`` (operationId ``listSmartMoneyFlows``).

        Ranks sports and esports markets (#27306) by absolute net S/A/B-grade whale flow over a
        requested timeframe. Use this discovery endpoint to answer where sharp money is flowing
        before drilling into a specific market with /api/v1/market/{condition_id}/flow.
        Pagination is anchored by an opaque cursor ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp, normalized effective filters, ranking and aggregate collection ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
            condition_id: Only this market's flow: an exact raw provider condition_id. Cannot be combined with event_slug (400). An unknown market returns an empty list.
            event_slug: Only the markets of one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListSmartMoneyFlowsResponse | NotModifiedResponse = self._call("listSmartMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListSmartMoneyFlowsResponse: ...

    @overload
    def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListSmartMoneyFlowsResponse | NotModifiedResponse: ...

    def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListSmartMoneyFlowsResponse | NotModifiedResponse:
        """List ranked sharp-money flows.

        ``GET /api/v1/markets/sharp-money-flows`` (operationId ``listSharpMoneyFlows``).

        Canonical path for ranked sharp-money flows; /api/v1/markets/smart-money-flows remains
        live as a deprecated byte-identical alias of it. Ranks sports and esports markets
        (#27306) by absolute net S/A/B-grade whale flow over a requested timeframe. Use this
        discovery endpoint to answer where sharp ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp, normalized effective filters, ranking and aggregate collection ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
            condition_id: Only this market's flow: an exact raw provider condition_id. Cannot be combined with event_slug (400). An unknown market returns an empty list.
            event_slug: Only the markets of one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListSmartMoneyFlowsResponse | NotModifiedResponse = self._call("listSharpMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    def get_coverage(
        self,
    ) -> GetCoverageResponse:
        """Which reads the API serves for Polymarket.

        ``GET /api/v1/coverage`` (operationId ``getCoverage``).

        Unauthenticated discovery endpoint that declares which V1 data surfaces the API serves
        for Polymarket, the one venue it covers. Every capability reports supported. Coverage is
        sports and esports markets only (#27299): a market outside them answers 404 not_found
        with error.reason ...
        """
        result: GetCoverageResponse = self._call("getCoverage", path_params={}, query={})
        return result

    def get_platforms(
        self,
    ) -> GetCoverageResponse:
        """Get platform capability matrix.

        ``GET /api/v1/platforms`` (operationId ``getPlatforms``).

        Deprecated since #16315: use GET /api/v1/coverage, which serves the same body. This path
        stays live until its sunset on 2027-02-01 (#29351) and answers with Deprecation, Sunset
        and successor Link headers; from that date it answers 410 Gone with error.code
        endpoint_retired. Unauthenticated discovery ...
        """
        result: GetCoverageResponse = self._call("getPlatforms", path_params={}, query={})
        return result

    @overload
    def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetMarketHoldersResponse: ...

    @overload
    def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetMarketHoldersResponse | NotModifiedResponse: ...

    def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketHoldersResponse | NotModifiedResponse:
        """List a market's graded holders.

        ``GET /api/v1/market/{condition_id}/holders`` (operationId ``getMarketHolders``).

        The graded holder roster of one market, the list a Pick of the Day shows for its market,
        for any Polymarket market: every S/A/B wallet with open shares on either outcome, from a
        complete provider holder scan, each with its shares, Polymarket's own currentValue for
        the leg, its grade, its win record ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            outcome: Keep holders netting one side. `all` (default) lists both.
            min_grade: Narrow within the graded cohort: `S` keeps S, `A` keeps S and A, `B` (default) keeps S, A and B. `C`, `D` and `F` are rejected with 400: the route lists the ...
            limit: Maximum holders per page. Out-of-range values are clamped to 1..100.
            cursor: Opaque pagination cursor from the previous response's next_cursor. New cursors carry an absolute next offset bound to normalized condition_id, outcome and ...
        """
        result: GetMarketHoldersResponse | NotModifiedResponse = self._call("getMarketHolders", path_params={"condition_id": condition_id}, query={"outcome": outcome, "min_grade": min_grade, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> GetMarketTopHoldersResponse: ...

    @overload
    def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> GetMarketTopHoldersResponse | NotModifiedResponse: ...

    def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketTopHoldersResponse | NotModifiedResponse:
        """List a market's top holders, every grade.

        ``GET /api/v1/market/{condition_id}/top-holders`` (operationId ``getMarketTopHolders``).

        The largest holders of one market on each outcome, every grade from S to F and ungraded
        wallets included: the table the market's event page shows under Top holders. Each
        outcome lists up to 100 wallets, largest `shares` first, from Polymarket's holder board,
        with the provider's current value, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum holders per outcome. Out-of-range values are clamped to 1..100. `totals` covers the whole sample whatever the limit.
        """
        result: GetMarketTopHoldersResponse | NotModifiedResponse = self._call("getMarketTopHolders", path_params={"condition_id": condition_id}, query={"limit": limit}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> GetMarketFlowResponse: ...

    @overload
    def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> GetMarketFlowResponse | NotModifiedResponse: ...

    def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketFlowResponse | NotModifiedResponse:
        """Get a market's flow and top positions.

        ``GET /api/v1/market/{condition_id}/flow`` (operationId ``getMarketFlow``).

        Canonical since #16312; GET /api/v1/market/{condition_id}/intel is its deprecated alias
        and serves the same body under object market_intel. One market's flow and top positions:
        the signed flow of every tracked large trade in the window (net_flow_usd and its YES or
        NO direction), the large-trade ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        result: GetMarketFlowResponse | NotModifiedResponse = self._call("getMarketFlow", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> GetMarketIntelResponse: ...

    @overload
    def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> GetMarketIntelResponse | NotModifiedResponse: ...

    def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketIntelResponse | NotModifiedResponse:
        """Get market intelligence.

        ``GET /api/v1/market/{condition_id}/intel`` (operationId ``getMarketIntel``).

        Deprecated since #16312: use GET /api/v1/market/{condition_id}/flow, which serves the
        same body under object market_flow. This path stays live until its sunset on 2027-02-01
        (#29351), keeps object market_intel, and answers with Deprecation, Sunset and successor
        Link headers; from that date it ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        result: GetMarketIntelResponse | NotModifiedResponse = self._call("getMarketIntel", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)
        return result

    def batch_get_market_flow(
        self,
        body: BatchGetMarketFlowBody,
    ) -> BatchGetMarketFlowResponse:
        """Batch market flow.

        ``POST /api/v1/markets/flow/batch`` (operationId ``batchGetMarketFlow``).

        Returns each market's flow and top positions for 1-25 raw provider condition_id values.
        Results preserve request order, duplicate inputs return duplicate rows, and each item is
        charged one batch item unit before execution. Do not pass prefixed mkt_ IDs; use
        market.condition_id from search or ...
        """
        result: BatchGetMarketFlowResponse = self._call("batchGetMarketFlow", path_params={}, query={}, body=body)
        return result

    def batch_get_market_close(
        self,
        body: BatchGetMarketCloseBody,
    ) -> BatchGetMarketCloseResponse:
        """Batch market closing lines.

        ``POST /api/v1/markets/close/batch`` (operationId ``batchGetMarketClose``).

        Returns the closing line of 1-25 sports or esports markets in one request. Each ok
        item's data is the body GET /api/v1/market/{condition_id}/close returns for that market:
        status measured with both outcome legs, pending, or unavailable with unavailable_reason,
        judged at one clock for the whole ...
        """
        result: BatchGetMarketCloseResponse = self._call("batchGetMarketClose", path_params={}, query={}, body=body)
        return result

    def batch_get_market_intel(
        self,
        body: BatchGetMarketFlowBody,
    ) -> BatchGetMarketIntelResponse:
        """Batch market intelligence.

        ``POST /api/v1/markets/intel/batch`` (operationId ``batchGetMarketIntel``).

        Deprecated since #16312: use POST /api/v1/markets/flow/batch, which returns the same
        items under object market_flow_batch. This path stays live until its sunset on
        2027-02-01 (#29351), keeps object market_intel_batch, and answers with Deprecation,
        Sunset and successor Link headers; from that date ...
        """
        result: BatchGetMarketIntelResponse = self._call("batchGetMarketIntel", path_params={}, query={}, body=body)
        return result

    @overload
    def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: None = None,
    ) -> GetMarketSnapshotResponse: ...

    @overload
    def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: str | None,
    ) -> GetMarketSnapshotResponse | NotModifiedResponse: ...

    def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketSnapshotResponse | NotModifiedResponse:
        """Get market live snapshot.

        ``GET /api/v1/market/{condition_id}/snapshot`` (operationId ``getMarketSnapshot``).

        Provider-first market card snapshot with canonical identity, outcome labels, cached top-
        of-book when available, liquidity, live sports context, and explicit
        freshness/unavailable states.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            expand: Include trust metadata for current_price and spread_bps. Repeatable: trust.
        """
        result: GetMarketSnapshotResponse | NotModifiedResponse = self._call("getMarketSnapshot", path_params={"condition_id": condition_id}, query={"expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: None = None,
    ) -> GetMarketCandlesResponse: ...

    @overload
    def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: str | None,
    ) -> GetMarketCandlesResponse | NotModifiedResponse: ...

    def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketCandlesResponse | NotModifiedResponse:
        """Get market OHLC price candles.

        ``GET /api/v1/market/{condition_id}/candles`` (operationId ``getMarketCandles``).

        Provider-first bucketed OHLC price candles for a market's outcome tokens, derived from
        our stored copy of the Polymarket CLOB prices-history series (the same series the
        market-detail chart renders; covers open and resolved markets). Because the stored data
        is daily, a 1d bucket typically carries ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            resolution: Bucketing granularity. 1d aggregates by UTC calendar day, 1w by ISO week (Monday 00:00 UTC start). Defaults to 1d.
            from_: Exclusive lower bound as a URL-decoded unix timestamp in seconds; points at or before this timestamp are omitted (the underlying daily snapshot read filters ...
            to: Inclusive upper bound as a URL-decoded unix timestamp in seconds; points after this timestamp are omitted. If from is also present, from must be less than or ...
        """
        result: GetMarketCandlesResponse | NotModifiedResponse = self._call("getMarketCandles", path_params={"condition_id": condition_id}, query={"resolution": resolution, "from": from_, "to": to}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: None = None,
    ) -> GetMarketCloseResponse: ...

    @overload
    def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: str | None,
    ) -> GetMarketCloseResponse | NotModifiedResponse: ...

    def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetMarketCloseResponse | NotModifiedResponse:
        """Get a market's closing line.

        ``GET /api/v1/market/{condition_id}/close`` (operationId ``getMarketClose``).

        The closing line of one sports or esports market: the price Polymarket's own price-
        history series recorded for each outcome in the last minute bucket that ended at or
        before kickoff (the market's game start time), read once after the market settles and
        stored unchanged. outcomes[0] is the YES leg ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetMarketCloseResponse | NotModifiedResponse = self._call("getMarketClose", path_params={"condition_id": condition_id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ListMarketTradesResponse: ...

    @overload
    def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ListMarketTradesResponse | NotModifiedResponse: ...

    def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ListMarketTradesResponse | NotModifiedResponse:
        """List a market's taker fills in a time window.

        ``GET /api/v1/market/{condition_id}/trades`` (operationId ``listMarketTrades``).

        One market's taker fills of 100 USD or more, newest first by (traded_at,
        transaction_hash, log_index), from 0xinsider's own record of the exchange's on-chain
        fills. Each fill appears once: its id is the transaction hash and the log index of its
        fill event, so a walk can be deduplicated and joined ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            from_: Inclusive RFC 3339 lower bound on traded_at. Omitted or earlier than coverage.recorded_from: the walk runs to the start of the record (coverage.recorded_from). ...
            to: Exclusive RFC 3339 upper bound on traded_at. A first page ends at the earlier of to and coverage.complete_through. With cursor, it must match the cursor's.
            limit: Page size. Out-of-range values are clamped to 1..500.
            cursor: Opaque mtr_v1_ cursor from next_cursor. It continues the walk before the last fill of the previous page and keeps the market, from and to it was issued for: ...
        """
        result: ListMarketTradesResponse | NotModifiedResponse = self._call("listMarketTrades", path_params={"condition_id": condition_id}, query={"from": from_, "to": to, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> GetMarketWalletsInOutResponse: ...

    @overload
    def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> GetMarketWalletsInOutResponse | NotModifiedResponse: ...

    def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketWalletsInOutResponse | NotModifiedResponse:
        """Get a market's net buyers and sellers.

        ``GET /api/v1/market/{condition_id}/wallets-in-out`` (operationId ``getMarketWalletsInOut``).

        One market's net buyers and net sellers over the last 24 hours or 7 days, live: the body
        the 0xinsider market page's wallets in/out panel reads for a Pro viewer, from the same
        aggregate and cache (reads are cached for up to 60 seconds). A wallet's net is its buys
        minus its sells in the window ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            window: The window the nets are summed over, ending at the read's clock: 24h (the default) or 7d.
        """
        result: GetMarketWalletsInOutResponse | NotModifiedResponse = self._call("getMarketWalletsInOut", path_params={"condition_id": condition_id}, query={"window": window}, if_none_match=if_none_match)
        return result

    @overload
    def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: None = None,
    ) -> ListSuspiciousTradesResponse: ...

    @overload
    def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None,
    ) -> ListSuspiciousTradesResponse | NotModifiedResponse: ...

    def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None = None,
    ) -> ListSuspiciousTradesResponse | NotModifiedResponse:
        """Get suspicious trades.

        ``GET /api/v1/suspicious-trades`` (operationId ``listSuspiciousTrades``).

        Stored trades whose recorded suspicion score meets the live flag threshold. Evidence
        contains the scorer's stored signals. Cursor-paginated by suspicion score. mode=live
        (default) uses fresh cached pages; mode=stable pins pagination to one published scoring
        generation and returns cursor_expired ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of suspicious trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
            mode: Pagination mode. live (default) keeps the 120-second response cache; stable pins the walk to one published scoring generation and binds the cursor to the limit ...
        """
        result: ListSuspiciousTradesResponse | NotModifiedResponse = self._call("listSuspiciousTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity, "mode": mode}, if_none_match=if_none_match)
        return result

    @overload
    def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> GetSuspiciousTradeResponse: ...

    @overload
    def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> GetSuspiciousTradeResponse | NotModifiedResponse: ...

    def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetSuspiciousTradeResponse | NotModifiedResponse:
        """Get suspicious trade by ID.

        ``GET /api/v1/suspicious-trades/{id}`` (operationId ``getSuspiciousTrade``).

        Returns one suspicious trade by raw whale_alerts.id or the rf_-prefixed id emitted by
        list responses. A flag on a market outside sports and esports returns 404 not_found with
        error.reason=market_out_of_scope (#27305); stop requesting it. Canonical since
        2026-09-23; GET /api/v1/insider-radar/{id} is ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetSuspiciousTradeResponse | NotModifiedResponse = self._call("getSuspiciousTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: None = None,
    ) -> ListGamesResponse: ...

    @overload
    def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: str | None,
    ) -> ListGamesResponse | NotModifiedResponse: ...

    def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: str | None = None,
    ) -> ListGamesResponse | NotModifiedResponse:
        """List covered games.

        ``GET /api/v1/games`` (operationId ``listGames``).

        One coherent game view per row: both sides with their provider ids and live scores, the
        UTC kickoff, the provider's own status, the esports series format, and the game's winner
        markets (the moneyline, or a soccer game's three 1X2 legs) with their condition ids and
        outcome token ids. Spreads, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            sport: Canonical sport bucket, case-insensitive, with - and _ read as a space: table-tennis and Table Tennis are the same bucket. Omit for every covered sport. A ...
            league: League tag, case-insensitive, as this list's coverage.leagues spells it (GET /api/v1/coverage lists no leagues): nfl, epl, cs2, euroleague, cbb, cwbb. ...
            status: Keep only games in this state. ended, cancelled and postponed also list finished games that have left the live board, read from their stored records, for ...
            starts_after: RFC 3339 instant. Keep only games whose kickoff is at or after it. Games with no published kickoff are excluded whenever either bound is set. With a finished ...
            starts_before: RFC 3339 instant. Keep only games whose kickoff is at or before it. Must be at or after starts_after.
            window: Which games to read. all, the default, lists the whole covered catalog, which can start with games the provider still holds open weeks after kickoff. now lists ...
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque gms_v1_ cursor from next_cursor. It pins the page position (kickoff and event_slug), not a snapshot: the catalog is live, so a game added or removed ...
            expand: sharp_money adds each game's sharp_money, the GameSharpMoney object GET /api/v1/games/{event_slug}/sharp-money returns, read from the sport board's cached ...
        """
        result: ListGamesResponse | NotModifiedResponse = self._call("listGames", path_params={}, query={"sport": sport, "league": league, "status": status, "starts_after": starts_after, "starts_before": starts_before, "window": window, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: None = None,
    ) -> GetGameResponse: ...

    @overload
    def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: str | None,
    ) -> GetGameResponse | NotModifiedResponse: ...

    def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: str | None = None,
    ) -> GetGameResponse | NotModifiedResponse:
        """Get one game.

        ``GET /api/v1/games/{event_slug}`` (operationId ``getGame``).

        The same game object GET /api/v1/games returns, for one event_slug, including soccer 1X2
        home, draw and away market sides and draw_offered. The slug is the identity the
        live_sports_updated webhook pulse carries, so a receiver can read the full game straight
        from a pulse. A slug outside the ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetGameResponse | NotModifiedResponse = self._call("getGame", path_params={"event_slug": event_slug}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: None = None,
    ) -> ListGameMarketsResponse: ...

    @overload
    def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: str | None,
    ) -> ListGameMarketsResponse | NotModifiedResponse: ...

    def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: str | None = None,
    ) -> ListGameMarketsResponse | NotModifiedResponse:
        """List a game's markets.

        ``GET /api/v1/games/{event_slug}/markets`` (operationId ``listGameMarkets``).

        Every stored Polymarket market of one event_slug: the moneyline, spreads, totals, team
        totals, half and quarter lines, player props and the rest, plus the markets of the
        event's child events (a soccer game's exact score, halftime result and more-markets
        events), each with its own event_slug. The ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            sports_market_type: Comma-separated provider market types to keep, case-insensitive: spreads, totals, points, first_half_totals. Omitted keeps every type. An unknown type returns ...
            status: active, closed or all. closed means the provider closed the market or it resolved.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque gmk_v1_ cursor from next_cursor, sent with the same filters. It pins the page position (sports_market_type, line, condition_id), not a snapshot. A ...
            expand: sharp_money adds each row's sharp_money: the game page's per-line split, side USD and S, A and B wallet counts per outcome. One read for the event whatever the ...
        """
        result: ListGameMarketsResponse | NotModifiedResponse = self._call("listGameMarkets", path_params={"event_slug": event_slug}, query={"sports_market_type": sports_market_type, "status": status, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: None = None,
    ) -> GetGameSharpMoneyResponse: ...

    @overload
    def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: str | None,
    ) -> GetGameSharpMoneyResponse | NotModifiedResponse: ...

    def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: str | None = None,
    ) -> GetGameSharpMoneyResponse | NotModifiedResponse:
        """Get one game's sharp money.

        ``GET /api/v1/games/{event_slug}/sharp-money`` (operationId ``getGameSharpMoney``).

        Where the graded money sits on a whole game, in one read: the S, A and B grade wallets'
        USD on each outcome (home, away and, for a 1X2 game, draw) summed across the game's
        markets, each outcome's integer share, the leader and wallet counts by grade, with the
        backend's verdict on the split. It is ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetGameSharpMoneyResponse | NotModifiedResponse = self._call("getGameSharpMoney", path_params={"event_slug": event_slug}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> ListGameTradesResponse: ...

    @overload
    def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> ListGameTradesResponse | NotModifiedResponse: ...

    def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> ListGameTradesResponse | NotModifiedResponse:
        """List a game's trades.

        ``GET /api/v1/games/{event_slug}/trades`` (operationId ``listGameTrades``).

        A game's newest fills across every market in it, newest first and live: the moneyline,
        spreads, totals and every prop, player props included. The same rows the 0xinsider game
        page's activity list shows a Pro viewer, read from the same live stream. Every fill, not
        only large ones: GET ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Newest fills to return. Out-of-range values are clamped to 1..200.
        """
        result: ListGameTradesResponse | NotModifiedResponse = self._call("listGameTrades", path_params={"event_slug": event_slug}, query={"limit": limit}, if_none_match=if_none_match)
        return result

    def get_game_holders(
        self,
        event_slug: str,
        *,
        condition_ids: list[str] | None = None,
        limit: int | None = None,
    ) -> GetGameHoldersResponse:
        """Get a game's holders.

        ``GET /api/v1/games/{event_slug}/holders`` (operationId ``getGameHolders``).

        The S, A and B graded holders of up to 25 markets of one game in one call. Each item is
        GET /api/v1/market/{condition_id}/holders for one market, unfiltered and cut to limit,
        with the same market, scan and totals beside it. Pass condition_ids from GET
        /api/v1/games/{event_slug}/markets; a market ...

        Query parameters:
            condition_ids: Required. 1 to 25 condition_id values of this game's markets, comma-separated. The key may also repeat (condition_ids=a&condition_ids=b). A raw provider condition_id or ...
            limit: Holders per market. Out-of-range values are clamped to 1..100.
        """
        result: GetGameHoldersResponse = self._call("getGameHolders", path_params={"event_slug": event_slug}, query={"condition_ids": condition_ids, "limit": limit})
        return result

    @overload
    def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: None = None,
    ) -> ListSuspiciousTradesResponse: ...

    @overload
    def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None,
    ) -> ListSuspiciousTradesResponse | NotModifiedResponse: ...

    def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None = None,
    ) -> ListSuspiciousTradesResponse | NotModifiedResponse:
        """Get insider radar flags.

        ``GET /api/v1/insider-radar`` (operationId ``listInsiderRadar``).

        Deprecated alias of GET /api/v1/suspicious-trades (2026-09-23), kept live until its
        sunset on 2027-02-01 (#29351); responses carry Deprecation, Sunset and a Link
        rel="successor-version" to it, and from that date the path answers 410 Gone with
        error.code endpoint_retired. Stored trades whose ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of radar flags to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
            mode: Pagination mode. live (default) keeps the 120-second response cache; stable pins the walk to one published scoring generation and binds the cursor to the limit ...
        """
        result: ListSuspiciousTradesResponse | NotModifiedResponse = self._call("listInsiderRadar", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity, "mode": mode}, if_none_match=if_none_match)
        return result

    @overload
    def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> GetInsiderRadarFlagResponse: ...

    @overload
    def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> GetInsiderRadarFlagResponse | NotModifiedResponse: ...

    def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetInsiderRadarFlagResponse | NotModifiedResponse:
        """Get insider radar flag by ID.

        ``GET /api/v1/insider-radar/{id}`` (operationId ``getInsiderRadarFlag``).

        Deprecated alias of GET /api/v1/suspicious-trades/{id} (2026-09-23), kept live until its
        sunset on 2027-02-01 (#29351); responses carry Deprecation, Sunset and a Link
        rel="successor-version" to it, and from that date the path answers 410 Gone with
        error.code endpoint_retired. The envelope keeps ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetInsiderRadarFlagResponse | NotModifiedResponse = self._call("getInsiderRadarFlag", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    def get_event_replay_since(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        trader: str | None = None,
        condition_id: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_size: float | str | None = None,
        expand: list[Literal["trade"]] | None = None,
    ) -> GetEventReplaySinceResponse:
        """Replay public large-trade events.

        ``GET /api/v1/events/feed/since`` (operationId ``getEventReplaySince``).

        Returns durable public large-trade events strictly after an opaque cursor, in commit
        order: events are ordered by the position at which their write became visible to every
        reader (whale_alerts.inserted_xid), then by whale_alerts.id, and a page never reaches
        past the oldest write transaction still ...

        Query parameters:
            cursor: Opaque event replay cursor returned as next_cursor by a prior response. The cursor maps to the global (whale_alerts.inserted_xid, whale_alerts.id) commit-order ...
            limit: Maximum durable public whale-trade events to return. Out-of-range values are clamped to 1..100.
            trader: Only this wallet's trades: a wallet address, trd_-prefixed trader id or username resolved against the traders table. Bound to the cursor: a cursor issued under ...
            condition_id: Only trades on this market: the raw provider condition_id or its mkt_-prefixed id. Bound to the cursor.
            min_grade: Only trades by wallets at this grade or better (S best), read from the wallet's newest ranking at request time; a wallet with no grade never passes. For the ...
            min_grade_at_trade: Only trades whose grade_at_trade, the grade the wallet held when the trade filled, is at this grade or better (S best). Only a trade whose grade at the fill is ...
            min_size: Only trades of at least this USD amount. Decimal and scientific query spellings normalize exactly to cents, rounding half away from zero; maximum 1e15 USD. ...
            expand: Repeatable. trade adds the public trade read to every event (the object GET /api/v1/whale-trades/{id} returns for it), from one query per page, so a page of ...
        """
        result: GetEventReplaySinceResponse = self._call("getEventReplaySince", path_params={}, query={"cursor": cursor, "limit": limit, "trader": trader, "condition_id": condition_id, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "min_size": min_size, "expand": expand})
        return result

    def list_webhooks(
        self,
    ) -> ListWebhooksResponse:
        """List builder webhook destinations.

        ``GET /api/v1/webhooks`` (operationId ``listWebhooks``).

        Returns webhook destinations owned by the authenticated API key user. Deleted endpoints
        are omitted; an endpoint paused with PATCH or disabled after consecutive failures is
        listed with status disabled. Subscribable event_types and their payload shapes are
        described by GET /api/v1/webhooks/events. ...
        """
        result: ListWebhooksResponse = self._call("listWebhooks", path_params={}, query={})
        return result

    def create_webhook(
        self,
        body: CreateWebhookRequest,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Create a builder webhook destination.

        ``POST /api/v1/webhooks`` (operationId ``createWebhook``).

        Creates a pending HTTPS webhook destination. The response includes one-time
        signing_secret and verification.token values. Deliveries are not sent until the endpoint
        is verified, and verification requires the destination to answer 2xx to a signed
        webhook.verification challenge (see POST ...
        """
        result: CreateWebhookResponse = self._call("createWebhook", path_params={}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    def list_webhook_events(
        self,
    ) -> ListWebhookEventsResponse:
        """List webhook event catalog.

        ``GET /api/v1/webhooks/events`` (operationId ``listWebhookEvents``).

        Self-describing catalog of every webhook event type: its description, data payload
        shape, and whether it is active (has a firing producer) or dormant (subscribable but not
        yet delivered; no event type is dormant today). The catalog is identical for every
        authenticated key and exposes no ...
        """
        result: ListWebhookEventsResponse = self._call("listWebhookEvents", path_params={}, query={})
        return result

    def list_webhook_deliveries(
        self,
        id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListWebhookDeliveriesResponse:
        """List webhook delivery log.

        ``GET /api/v1/webhooks/{id}/deliveries`` (operationId ``listWebhookDeliveries``).

        Recent delivery attempts for one webhook destination owned by the authenticated API key
        user, newest first, with opaque cursor pagination. Returns 404 (identical to an unknown
        id) when the endpoint is not owned by the caller, so a non-owner cannot tell an owned-
        but-empty log apart from someone ...

        Query parameters:
            cursor: Opaque pagination cursor returned as next_cursor by a prior response. Omit to fetch the newest page.
            limit: Maximum delivery rows to return per page. Out-of-range values are clamped to 1..100.
        """
        result: ListWebhookDeliveriesResponse = self._call("listWebhookDeliveries", path_params={"id": id}, query={"cursor": cursor, "limit": limit})
        return result

    def redeliver_webhook_delivery(
        self,
        id: str,
        delivery_id: str,
        *,
        idempotency_key: str | None = None,
    ) -> RedeliverWebhookDeliveryResponse:
        """Redeliver a dead-lettered webhook delivery.

        ``POST /api/v1/webhooks/{id}/deliveries/{delivery_id}/redeliver`` (operationId ``redeliverWebhookDelivery``).

        Returns one dead_letter delivery to the delivery queue with a fresh attempt budget:
        status becomes pending, attempt_count resets to 0, and next_attempt_at is now, so the
        delivery worker claims it like any queued delivery, under the same per-owner and per-
        origin concurrency limits. Use it after a ...
        """
        result: RedeliverWebhookDeliveryResponse = self._call("redeliverWebhookDelivery", path_params={"id": id, "delivery_id": delivery_id}, query={}, idempotency_key=idempotency_key)
        return result

    def get_webhook(
        self,
        id: str,
    ) -> CreateWebhookResponse:
        """Get one builder webhook destination.

        ``GET /api/v1/webhooks/{id}`` (operationId ``getWebhook``).

        Returns one webhook destination owned by the authenticated API key user.
        """
        result: CreateWebhookResponse = self._call("getWebhook", path_params={"id": id}, query={})
        return result

    def update_webhook(
        self,
        id: str,
        body: UpdateWebhookRequest,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Update a builder webhook destination.

        ``PATCH /api/v1/webhooks/{id}`` (operationId ``updateWebhook``).

        Updates name, HTTPS URL, event types, or enabled state. URL changes force
        pending_verification and return a new verification token; the new destination must
        answer 2xx to the signed webhook.verification challenge before deliveries resume. A URL
        change returns 409 with ...
        """
        result: CreateWebhookResponse = self._call("updateWebhook", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    def delete_webhook(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Disable a builder webhook destination.

        ``DELETE /api/v1/webhooks/{id}`` (operationId ``deleteWebhook``).

        Soft-deletes a webhook destination owned by the authenticated API key user. Existing
        delivery audit rows remain retained.
        """
        result: CreateWebhookResponse = self._call("deleteWebhook", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    def verify_webhook(
        self,
        id: str,
        body: VerifyWebhookRequest,
    ) -> CreateWebhookResponse:
        """Verify a builder webhook destination.

        ``POST /api/v1/webhooks/{id}/verify`` (operationId ``verifyWebhook``).

        Activates a pending webhook destination. Two conditions must both hold: the one-time
        verification token matches and has not expired, AND the destination answers 2xx to a
        signed challenge this operation POSTs to the endpoint's stored url. The challenge body
        is ...
        """
        result: CreateWebhookResponse = self._call("verifyWebhook", path_params={"id": id}, query={}, body=body)
        return result

    def prepare_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Prepare a staged builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/prepare`` (operationId ``prepareWebhookSecret``).

        Creates a pending signing secret while the current secret remains active. Deploy the
        returned one-time signing_secret to the receiver before calling activate. The response
        exposes secret_rotation.status=pending; an existing pending secret is returned again so
        a lost response can be recovered safely.
        """
        result: CreateWebhookResponse = self._call("prepareWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    def activate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Activate a staged builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/activate`` (operationId ``activateWebhookSecret``).

        Promotes the prepared signing secret to current, returns it once, and signs every
        delivery with both the new and previous secrets for one hour. Call retire after the
        receiver has completed its rollout. The current secret remains available through the
        existing immediate rotate-secret route for ...
        """
        result: CreateWebhookResponse = self._call("activateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    def retire_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Retire the previous builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/retire`` (operationId ``retireWebhookSecret``).

        Ends the one-hour dual-signature overlap and removes the previous signing secret from
        future delivery authorization. Call this after the receiver accepts the activated
        secret. The operation is idempotent and does not return signing_secret.
        """
        result: CreateWebhookResponse = self._call("retireWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    def rotate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Rotate a builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret`` (operationId ``rotateWebhookSecret``).

        Rotates the endpoint signing secret and returns the new signing_secret once in the
        response. Returns 409 with error.reason=webhook_delivery_in_progress while a live
        delivery freezes the current signing nonce; retry after it completes.
        """
        result: CreateWebhookResponse = self._call("rotateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    @overload
    def get_health(
        self,
        *,
        if_none_match: None = None,
    ) -> GetHealthResponse: ...

    @overload
    def get_health(
        self,
        *,
        if_none_match: str | None,
    ) -> GetHealthResponse | NotModifiedResponse: ...

    def get_health(
        self,
        *,
        if_none_match: str | None = None,
    ) -> GetHealthResponse | NotModifiedResponse:
        """Health check.

        ``GET /api/v1/health`` (operationId ``getHealth``).

        Returns API health status. No authentication required. Limited to 120 requests per
        minute per IP.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetHealthResponse | NotModifiedResponse = self._call("getHealth", path_params={}, query={}, if_none_match=if_none_match)
        return result

    def create_mcp_json_rpc_response(
        self,
        body: CreateMcpJsonRpcResponseBody,
    ) -> CreateMcpJsonRpcResponseResponse:
        """Remote MCP endpoint (JSON-RPC).

        ``POST /api/v1/mcp`` (operationId ``createMcpJsonRpcResponse``).

        Model Context Protocol (MCP) Streamable HTTP transport. Accepts one JSON-RPC 2.0 request
        or notification. ID-bearing initialize, ping, tools/list, and tools/call requests (and
        server/discover on revision 2026-07-28) receive one same-ID JSON-RPC response; an
        unknown method, or a notification method ...
        """
        result: CreateMcpJsonRpcResponseResponse = self._call("createMcpJsonRpcResponse", path_params={}, query={}, body=body)
        return result

    def get_reports(
        self,
        *,
        granularity: Literal["daily", "weekly", "monthly"] | None = None,
        period: str | None = None,
    ) -> GetReportsResponse:
        """Unified report snapshot (granularity selector).

        ``GET /api/v1/reports`` (operationId ``getReports``).

        Unified convenience route (#4975) that consolidates the three singular report routes.
        Dispatches to the exact per-granularity cap (daily 50, weekly 100, monthly 200) and date
        window the legacy /api/v1/reports/{daily,weekly,monthly} routes use, so the response
        body is byte-identical to the matching ...

        Query parameters:
            granularity: Required. Report granularity selector.
            period: Required. Period token for the granularity. daily: UTC date YYYY-MM-DD. weekly: ISO week YYYY-WW for a durable canonical snapshot, or a from,to YYYY-MM-DD pair for an ...
        """
        result: GetReportsResponse = self._call("getReports", path_params={}, query={"granularity": granularity, "period": period})
        return result

    def get_daily_report_snapshot(
        self,
        *,
        date: str | None = None,
    ) -> GetReportsResponse:
        """Daily report snapshot.

        ``GET /api/v1/reports/daily`` (operationId ``getDailyReportSnapshot``).

        Returns a dated daily whale-activity report snapshot with source_range, snapshot.status,
        completeness, and reconciliation metadata. Report whale volume is local whale-alert
        activity volume, not provider lifetime trader volume.

        Query parameters:
            date: Required. UTC report date in YYYY-MM-DD format, from 2024-03-01 (the first day report data covers) through tomorrow UTC. Any other date returns 400 bad_request with ...
        """
        result: GetReportsResponse = self._call("getDailyReportSnapshot", path_params={}, query={"date": date})
        return result

    def get_weekly_report_snapshot(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        week: str | None = None,
    ) -> GetReportsResponse:
        """Weekly report snapshot.

        ``GET /api/v1/reports/weekly`` (operationId ``getWeeklyReportSnapshot``).

        Returns a weekly whale-activity report snapshot. Pass an ISO YYYY-WW token for a durable
        canonical snapshot, or an exact from/to UTC range of at most 31 inclusive days for an
        ephemeral response. The response identifies closed ranges as final and current ranges as
        rolling.

        Query parameters:
            from_: UTC source-range start in YYYY-MM-DD format; required with to. Together with to, selects an exact ephemeral range of at most 31 inclusive UTC days. A start ...
            to: UTC source-range end in YYYY-MM-DD format; required with from. Together with from, selects an exact ephemeral range of at most 31 inclusive UTC days. An end ...
            week: ISO week selector in YYYY-WW format; alternative to from/to. Selects a durable canonical snapshot. A week that ends before 2024-03-01, the first day report ...
        """
        result: GetReportsResponse = self._call("getWeeklyReportSnapshot", path_params={}, query={"from": from_, "to": to, "week": week})
        return result

    def get_monthly_report_snapshot(
        self,
        *,
        month: str | None = None,
    ) -> GetReportsResponse:
        """Monthly report snapshot.

        ``GET /api/v1/reports/monthly`` (operationId ``getMonthlyReportSnapshot``).

        Returns a UTC monthly whale-activity report snapshot with source_range, completeness,
        and reconciliation metadata.

        Query parameters:
            month: Required. UTC report month in YYYY-MM format. A month that ends before 2024-03-01, the first day report data covers, or starts after tomorrow UTC returns 400 bad_request ...
        """
        result: GetReportsResponse = self._call("getMonthlyReportSnapshot", path_params={}, query={"month": month})
        return result

    @overload
    def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: None = None,
    ) -> GetResolutionReportResponse: ...

    @overload
    def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: str | None,
    ) -> GetResolutionReportResponse | NotModifiedResponse: ...

    def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: str | None = None,
    ) -> GetResolutionReportResponse | NotModifiedResponse:
        """Get the daily resolution report.

        ``GET /api/v1/reports/resolutions`` (operationId ``getResolutionReport``).

        One UTC day's resolved markets: how often the side the profitable (S, A and B grade)
        wallets held won, beside how often every qualifying wallet's side won, one vote each.
        `markets` lists each market they held a position in, with the consensus side, its
        confidence, and the full roster of wallets, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            date: Required. UTC report date in YYYY-MM-DD format, no later than today UTC. Any other value returns 400 bad_request with error.param=date.
            view: `totals` returns the counts without `markets`. Any other value than full or totals returns 400 bad_request with error.param=view.
        """
        result: GetResolutionReportResponse | NotModifiedResponse = self._call("getResolutionReport", path_params={}, query={"date": date, "view": view}, if_none_match=if_none_match)
        return result

    def get_trader_export_snapshot(
        self,
        address: str,
    ) -> GetTraderExportSnapshotResponse:
        """Trader export snapshot metadata.

        ``GET /api/v1/trader/{address}/export`` (operationId ``getTraderExportSnapshot``).

        Returns export source-range, completeness, volume reconciliation, row-count estimate,
        and large-export policy for one trader. To download the full dataset programmatically,
        POST to this same path to submit an async export job (json | ndjson | csv), then poll
        the status route and follow the download ...
        """
        result: GetTraderExportSnapshotResponse = self._call("getTraderExportSnapshot", path_params={"address": address}, query={})
        return result

    def submit_trader_export(
        self,
        address: str,
        *,
        format: Literal["json", "ndjson", "csv"] | None = None,
        fresh: bool | None = None,
    ) -> TraderExportJob:
        """Submit a trader dataset export job.

        ``POST /api/v1/trader/{address}/export`` (operationId ``submitTraderExport``).

        Queues an async export of the trader's full dataset in the requested format (json
        default, ndjson, or csv) and returns the job resource. Poll the status route at
        poll_after_s until terminal is true, then follow the download route while status is
        'ready' (until expires_at, 24 hours from submit). ...

        Query parameters:
            format: Output serialization. json = full envelope document (default); ndjson = full envelope as line 1 then one trade object per line; csv = flat trades rows only.
            fresh: true: do not reuse a finished, running or reconciling job; only a queued job is reused, so the file is a snapshot read after this submit. Consumes quota when ...
        """
        result: TraderExportJob = self._call("submitTraderExport", path_params={"address": address}, query={"format": format, "fresh": fresh})
        return result

    def get_trader_export_status(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> TraderExportJob:
        """Poll a trader export job.

        ``GET /api/v1/trader/{address}/export/status`` (operationId ``getTraderExportStatus``).

        Returns the job resource for a submitted export: status (queued | running |
        cancel_requested | reconcile_required | ready | failed | expired | cancelled), terminal,
        next_action and poll_after_s, the lifecycle timestamps, the retention window
        (expires_at) and, once the file is written, data_as_of ...

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        result: TraderExportJob = self._call("getTraderExportStatus", path_params={"address": address}, query={"job_id": job_id})
        return result

    def cancel_trader_export(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> TraderExportJob:
        """Cancel a trader export job.

        ``POST /api/v1/trader/{address}/export/cancel`` (operationId ``cancelTraderExport``).

        Cancels a submitted export and returns the job resource, the same shape the status route
        returns. A queued job reads cancelled at once and no worker will start it. A running job
        reads cancel_requested until the worker reaches its next safe point, then cancelled: the
        worker checks every 5 seconds ...

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        result: TraderExportJob = self._call("cancelTraderExport", path_params={"address": address}, query={"job_id": job_id})
        return result

    def download_trader_export(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> Download:
        """Download a finished trader export.

        ``GET /api/v1/trader/{address}/export/download`` (operationId ``downloadTraderExport``).

        Redirects (302) to a presigned URL lasting at most one hour and no later than the job's
        expires_at for the finished export file while the job status is 'ready' and expires_at
        has not passed. The file is gzip-compressed and served with the format's Content-Type
        (application/json, ...

        Returns a ``Download``: the redirect is followed once, without the credential, and the
        file is streamed. Iterate it, ``save(path)`` it for its SHA-256, or ``read()`` it
        (bounded); ``close()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        return self._download("downloadTraderExport", path_params={"address": address}, query={"job_id": job_id})

    def get_usage(
        self,
    ) -> Usage:
        """Inspect current API usage without spending primary request quota.

        ``GET /api/v1/usage`` (operationId ``getUsage``).

        Returns the authenticated caller sliding-window request budget, UTC-day usage and
        monthly quota. This control-plane endpoint remains available for a valid credential
        after paid data access lapses and does not increment the primary Redis rate-limit
        counter, monthly quota or API usage table; it ...
        """
        result: Usage = self._call("getUsage", path_params={}, query={})
        return result

    def get_market_context_markdown(
        self,
        condition_id: str,
    ) -> str:
        """Get market context (Markdown).

        ``GET /api/v1/market/{condition_id}/context.md`` (operationId ``getMarketContextMarkdown``).

        Authenticated, self-contained Polymarket market evidence document. Renders the same
        typed data as the market snapshot with trust included: identity, outcome labels and
        tokens, cached quotes, liquidity, live sports, and per-source freshness or unavailable
        reasons. Provider text is encoded as ...
        """
        result: str = self._call("getMarketContextMarkdown", path_params={"condition_id": condition_id}, query={})
        return result

    def get_account_identity(
        self,
    ) -> AccountIdentity:
        """Identify the authenticated account and credential.

        ``GET /api/v1/me`` (operationId ``getAccountIdentity``).

        Returns caller-owned account and credential IDs, credential validity, paid-data
        entitlement and approved scopes. Null scopes mean full legacy developer-key access.
        Valid credentials can use this control-plane diagnostic path after paid access lapses;
        data routes still require active paid access. ...
        """
        result: AccountIdentity = self._call("getAccountIdentity", path_params={}, query={})
        return result

    def submit_whale_dataset(
        self,
        body: SubmitWhaleDatasetBody,
    ) -> WhaleDatasetJob:
        """Create an immutable whale dataset.

        ``POST /api/v1/datasets/whale-trades`` (operationId ``submitWhaleDataset``).

        Extract at most 1,000,000 rows and 256 MiB uncompressed; exceeding either bound fails
        the job and publishes no partial file. Window and filters freeze on admission; rows and
        source facts freeze on one worker database snapshot. NDJSON uses exact decimal strings,
        with no current grade or market ...
        """
        result: WhaleDatasetJob = self._call("submitWhaleDataset", path_params={}, query={}, body=body)
        return result

    def get_whale_dataset_status(
        self,
        job_id: str,
    ) -> WhaleDatasetJob:
        """Read a whale dataset job.

        ``GET /api/v1/datasets/whale-trades/{job_id}`` (operationId ``getWhaleDatasetStatus``).

        Read queued, running, cancel_requested, ready, failed, reconcile_required, expired or
        cancelled. Poll only while next_action is poll, after poll_after_s. Ready manifests
        contain count, content and compressed SHA-256, schema, filters, source, horizon, expiry
        and replay continuation. Deltas do not ...
        """
        result: WhaleDatasetJob = self._call("getWhaleDatasetStatus", path_params={"job_id": job_id}, query={})
        return result

    def download_whale_dataset(
        self,
        job_id: str,
    ) -> Download:
        """Download an immutable whale dataset.

        ``GET /api/v1/datasets/whale-trades/{job_id}/download`` (operationId ``downloadWhaleDataset``).

        Download only a ready artifact; status handles failure and cancellation. Retired
        artifacts return 410 at serving time. Paid export scope; jobs are private to the
        credential owner. Shares the 20/day owner export quota and fair worker admission with
        trader exports; datasets also have a combined ...

        Returns a ``Download``: the redirect is followed once, without the credential, and the
        file is streamed. Iterate it, ``save(path)`` it for its SHA-256, or ``read()`` it
        (bounded); ``close()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.
        """
        return self._download("downloadWhaleDataset", path_params={"job_id": job_id}, query={})

    def cancel_whale_dataset(
        self,
        job_id: str,
    ) -> WhaleDatasetJob:
        """Cancel a whale dataset job.

        ``POST /api/v1/datasets/whale-trades/{job_id}/cancel`` (operationId ``cancelWhaleDataset``).

        Cancel queued jobs immediately and request running jobs stop at their next safe point.
        Repeating cancel converges on the current state; cancellation after the completion fence
        leaves the artifact ready. Paid export scope; jobs are private to the credential owner.
        Shares the 20/day owner export ...
        """
        result: WhaleDatasetJob = self._call("cancelWhaleDataset", path_params={"job_id": job_id}, query={})
        return result

    @overload
    def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: None = None,
    ) -> GetPickOfTheDayLedgerEntryResponse: ...

    @overload
    def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: str | None,
    ) -> GetPickOfTheDayLedgerEntryResponse | NotModifiedResponse: ...

    def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayLedgerEntryResponse | NotModifiedResponse:
        """Read a pick proof by stable id.

        ``GET /api/v1/pick-of-the-day/ledger/{pick_id}`` (operationId ``getPickOfTheDayLedgerEntry``).

        Public read of one published pick by its stable decimal-string pick_id. Same proof
        gating, canonical bytes, ETag and integrity failures as the ledger. Invalid ids return
        400; absent or unpublished picks return 404. Withdrawal from recommendations or the
        archive does not remove a published ledger ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetPickOfTheDayLedgerEntryResponse | NotModifiedResponse = self._call("getPickOfTheDayLedgerEntry", path_params={"pick_id": pick_id}, query={}, if_none_match=if_none_match)
        return result

    def create_webhook_verification_attempt(
        self,
        id: str,
        body: CreateWebhookVerificationAttemptRequest,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookVerificationAttemptResponse:
        """Admit asynchronous webhook verification.

        ``POST /api/v1/webhooks/{id}/verification-attempts`` (operationId ``createWebhookVerificationAttempt``).

        Additive asynchronous consent flow; the legacy POST /verify keeps its synchronous
        200/422 behavior and retry policy. Commits one durable attempt and returns 202 without
        awaiting DNS or the receiver. Send the original verification_token. Optional
        Idempotency-Key replays the original admission ...
        """
        result: CreateWebhookVerificationAttemptResponse = self._call("createWebhookVerificationAttempt", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    def get_webhook_verification_attempt(
        self,
        id: str,
        attempt_id: str,
    ) -> CreateWebhookVerificationAttemptResponse:
        """Read webhook verification attempt status.

        ``GET /api/v1/webhooks/{id}/verification-attempts/{attempt_id}`` (operationId ``getWebhookVerificationAttempt``).

        Fresh primary-database status for one attempt owned by the authenticated account and
        webhook. queued/running means consent is pending; only verified activates the unchanged
        endpoint after receiver 2xx. failed/cancelled/expired are terminal. Polling never issues
        a challenge or restarts work. At ...
        """
        result: CreateWebhookVerificationAttemptResponse = self._call("getWebhookVerificationAttempt", path_params={"id": id, "attempt_id": attempt_id}, query={})
        return result

    @overload
    def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: None = None,
    ) -> ComboFillsResponse: ...

    @overload
    def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: str | None,
    ) -> ComboFillsResponse | NotModifiedResponse: ...

    def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: str | None = None,
    ) -> ComboFillsResponse | NotModifiedResponse:
        """List combo fills.

        ``GET /api/v1/combos/fills`` (operationId ``listComboFills``).

        Returns live Polymarket combo taker fills with exact decimal-string economics, wallet
        identities, grades, legs, conjunction results, and ingest coverage. Requires an active
        Pro or Max API key. Listing includes executions with price at most 0.95; use combo
        detail for complete history. Sports and ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            result: CSV of pending, won, or lost; all clears the filter. Unknown results appear only in unfiltered lists.
            legs: CSV of 2, 3, 4, or 5+; all clears the filter. A combo matches any named pick count.
            min_stake: Minimum collateral in whole USDC.
            min_multiplier: 0 disables the filter; otherwise use 2..1000000. Minimum shares per dollar at execution.
            grades: CSV of S, A, B, C, D, F; all clears the filter. Ungraded wallets do not match.
            sports: CSV of nfl, ncaaf, nba, wnba, baseball, hockey, soccer, tennis, table-tennis, esports, mma, boxing, golf, cricket, f1, pickleball; all clears the filter. ...
            sort: Recent is newest first; largest ranks collateral; payout ranks buy-fill shares and excludes sells.
            window: Defaults to all for recent and 24h for largest or payout.
            limit: Page size. Integer values outside the range are clamped to 1..200.
            cursor: Exclusive block_number:log_index cursor for recent only; send the returned next_cursor unchanged.
            offset: Offset for ranked largest or payout ordering; use returned next_offset.
        """
        result: ComboFillsResponse | NotModifiedResponse = self._call("listComboFills", path_params={}, query={"result": result, "legs": legs, "min_stake": min_stake, "min_multiplier": min_multiplier, "grades": grades, "sports": sports, "sort": sort, "window": window, "limit": limit, "cursor": cursor, "offset": offset}, if_none_match=if_none_match)
        return result

    @overload
    def get_combos_summary(
        self,
        *,
        if_none_match: None = None,
    ) -> CombosSummaryResponse: ...

    @overload
    def get_combos_summary(
        self,
        *,
        if_none_match: str | None,
    ) -> CombosSummaryResponse | NotModifiedResponse: ...

    def get_combos_summary(
        self,
        *,
        if_none_match: str | None = None,
    ) -> CombosSummaryResponse | NotModifiedResponse:
        """Get live combo count.

        ``GET /api/v1/combos/summary`` (operationId ``getCombosSummary``).

        Returns the stored count of traded combos whose YES conjunction remains pending, with
        its computation timestamp. Sports and esports only (#27449): a combo with a leg outside
        them is not counted. Requires an active Pro or Max API key. The count is refreshed by
        the ingest owner at most every five ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: CombosSummaryResponse | NotModifiedResponse = self._call("getCombosSummary", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: None = None,
    ) -> ComboResponse: ...

    @overload
    def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: str | None,
    ) -> ComboResponse | NotModifiedResponse: ...

    def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: str | None = None,
    ) -> ComboResponse | NotModifiedResponse:
        """Get combo detail.

        ``GET /api/v1/combos/{condition_id}`` (operationId ``getCombo``).

        Returns one Polymarket combo with its legs, conjunction result, all-time trade totals,
        newest 100 taker fills, lifecycle totals, and ingest coverage. Requires an active Pro or
        Max API key. Detail retains execution history above the listing price cap. A malformed
        combo ID returns 400; an unknown ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ComboResponse | NotModifiedResponse = self._call("getCombo", path_params={"condition_id": condition_id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: None = None,
    ) -> EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse: ...

    @overload
    def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: str | None,
    ) -> EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse | NotModifiedResponse: ...

    def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: str | None = None,
    ) -> EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse | NotModifiedResponse:
        """Get Edge Hunter.

        ``GET /api/v1/edge-hunter`` (operationId ``getEdgeHunter``).

        Max-only canonical Edge Hunter API with board, signals and observations views. An active
        Pro credential receives 403 forbidden with reason max_plan_required. Default board
        admission and ordering remain compatible: B grade floor, 30-row cap, 48-hour kickoff
        horizon, full Max projection and both ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: Response mode. board preserves the full quoted board; signals exposes ranked records and category evidence; observations exposes cohort measurements and ...
            category: Legacy canonical bucket alias, now accepted in every view. Provider aliases canonicalize: NFL reaches Football and EPL reaches Soccer. Use leagues for a ...
            cohort: Required for view=observations; wider_holder, in_play or emerging_pile. Rejected for board and signals. wider_holder covers pregame markets that view=signals ...
            admission: Opt-in admission rule for view=observations with cohort=wider_holder; rejected for every other view and cohort. most_held_48h returns the most-held selection ...
            min_grade: Board and signals: S, A or B, default B. Requires a piled-side holder at the selected grade floor or better, without removing other holders. Rejected for ...
            limit: Board row cap defaults to 30 and clamps integer values to 1..30; total counts selected admitted rows before the cap. Signals and observations page size ...
            cursor: Opaque canonical Edge Hunter cursor from next_cursor. Bound to view, every normalized selection axis, grade/horizon where applicable, source snapshot and ...
            horizon_hours: Kickoff window for board (default 48) or signals (default 12). Integer values clamp to 1..48. Rejected for observations, whose pre-game universe is fixed at 48 ...
            kind: All views: sports excludes the Esports bucket; esports selects only Esports. Omit for both. Combines with other selections using AND. Selected reads echo ...
            sports: Canonical sport buckets, including Esports and Table Tennis, matched case-insensitively. Unknown names and league aliases such as NFL are rejected in sports; ...
            leagues: Normalized machine/provider league identities, such as nfl, cfb, nba, epl, cs2, lol, dota2 or valorant. Known wire/tag aliases normalize; other provider keys ...
            market_types: Exact provider sports_market_type values. This is an open provider taxonomy, distinct from exact market IDs. Read market_context.market_type; missing selected ...
            condition_ids: Exact market selections. Raw provider condition IDs and the existing mkt_-prefixed aliases normalize to raw IDs. Unknown well-formed IDs return an empty ...
            event_slugs: Exact provider event slugs. Use event_slug returned on the row; no title or slug-prefix guessing. All views. Repeat this query key or put comma-separated ...
            series_slugs: Exact provider series slugs. Read market_context.series_slug; a missing selected series excludes the row. All views. Repeat this query key or put ...
        """
        result: EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse | NotModifiedResponse = self._call("getEdgeHunter", path_params={}, query={"view": view, "category": category, "cohort": cohort, "admission": admission, "min_grade": min_grade, "limit": limit, "cursor": cursor, "horizon_hours": horizon_hours, "kind": kind, "sports": sports, "leagues": leagues, "market_types": market_types, "condition_ids": condition_ids, "event_slugs": event_slugs, "series_slugs": series_slugs}, if_none_match=if_none_match)
        return result



class ResponseOperationsMixin:
    """The same operations, each returning an ``ApiResponse`` over the same body.

    Reached as ``client.with_response``: ``.data`` is exactly what the plain
    method returns, beside the status, the headers, the ETag and the budgets.
    A redirect-only operation already carries the file's own headers."""

    def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by Client
        raise NotImplementedError

    def _download(self, operation_id: str, **kwargs: Any) -> Download:  # pragma: no cover - provided by Client
        raise NotImplementedError

    def get_api_discovery(
        self,
    ) -> ApiResponse[GetApiDiscoveryResponse]:
        """API discovery.

        ``GET /api/v1`` (operationId ``getApiDiscovery``).

        Unauthenticated API-origin discovery document pointing agents to the canonical API base
        URL, full docs, web-origin OpenAPI spec, health check, and the COMPLETE index of
        authenticated data routes. data.authenticated_routes is the whole authenticated route
        surface, not a sample: it carries every ...
        """
        result: ApiResponse[GetApiDiscoveryResponse] = self._call("getApiDiscovery", path_params={}, query={})
        return result

    def redirect_api_openapi_spec(
        self,
    ) -> Download:
        """Redirect to the canonical OpenAPI spec.

        ``GET /api/v1/openapi.json`` (operationId ``redirectApiOpenapiSpec``).

        Unauthenticated API-origin compatibility redirect to the canonical web-origin OpenAPI
        JSON document at https://0xinsider.com/api/v1/openapi.json.

        Returns a ``Download``: the redirect is followed once, without the credential, and the
        file is streamed. Iterate it, ``save(path)`` it for its SHA-256, or ``read()`` it
        (bounded); ``close()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.
        """
        return self._download("redirectApiOpenapiSpec", path_params={}, query={})

    def register_agent(
        self,
    ) -> ApiResponse[RegisterAgentResponse]:
        """Register an agent for a sandbox key.

        ``POST /api/v1/agents/register`` (operationId ``registerAgent``).

        Self-serve agent onboarding: no account, no request body, no human step. Returns a
        sandbox API key (oxi_sk_test_...) and the path to live access. The key works only on the
        sandbox server (https://0xinsider.com/sandbox/api/v1), where it is optional: send it as
        Authorization: Bearer to exercise the ...
        """
        result: ApiResponse[RegisterAgentResponse] = self._call("registerAgent", path_params={}, query={})
        return result

    @overload
    def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderResponse]: ...

    @overload
    def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderResponse] | ApiResponse[NotModifiedResponse]:
        """Get trader.

        ``GET /api/v1/trader/{address}`` (operationId ``getTrader``).

        Returns a trader's grade (S through F), P&L, win rate, and optional strategy/category
        data. The path accepts either an Ethereum wallet address, a known trader username, or a
        trd_-prefixed trader ID emitted by this API. A wallet address this API does not track
        yet returns 200 with sync_status ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            expand: Include heavy fields and trust metadata. Repeatable: strategy, categories, trust, breakdowns. breakdowns adds the profile's strategy measures ...
            max_age_s: Opt into a whole-response freshness ceiling in seconds. The server returns 200 only when data_quality.status is fresh or stale and data_quality.as_of is no ...
        """
        result: ApiResponse[GetTraderResponse] | ApiResponse[NotModifiedResponse] = self._call("getTrader", path_params={"address": address}, query={"expand": expand, "max_age_s": max_age_s}, if_none_match=if_none_match)
        return result

    def get_trader_context_markdown(
        self,
        address: str,
    ) -> ApiResponse[str]:
        """Get trader context (Markdown).

        ``GET /api/v1/trader/{address}/context.md`` (operationId ``getTraderContextMarkdown``).

        Returns a single human- and LLM-readable Markdown briefing for one trader: identity,
        grade, P&L, position coverage, and freshness. The path accepts an Ethereum wallet
        address (0x...), a known trader username, or a trd_-prefixed trader ID emitted by this
        API. A wallet address this API does not track ...
        """
        result: ApiResponse[str] = self._call("getTraderContextMarkdown", path_params={"address": address}, query={})
        return result

    @overload
    def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderGradeAtResponse]: ...

    @overload
    def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderGradeAtResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderGradeAtResponse] | ApiResponse[NotModifiedResponse]:
        """Get a trader grade proven visible at a past instant.

        ``GET /api/v1/trader/{address}/grade-at`` (operationId ``getTraderGradeAt``).

        Reads one trader's recorded grade at as_of from prospective visibility evidence. Before
        the first recorded observation, after deletion, or during a grade-transition gap, status
        is unknown and grade is null; a recorded ungraded trader instead has status ungraded.
        available_from is the first proven ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            as_of: Required. RFC3339 instant whose historically visible grade is requested. Future instants are refused. Send the trade or decision time, not the ranking date.
        """
        result: ApiResponse[GetTraderGradeAtResponse] | ApiResponse[NotModifiedResponse] = self._call("getTraderGradeAt", path_params={"address": address}, query={"as_of": as_of}, if_none_match=if_none_match)
        return result

    @overload
    def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderClvResponse]: ...

    @overload
    def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderClvResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderClvResponse] | ApiResponse[NotModifiedResponse]:
        """Get a trader's closing line value on large trades.

        ``GET /api/v1/trader/{address}/clv`` (operationId ``getTraderClv``).

        Closing line value (CLV) over one wallet's large trades in a window: the trades GET
        /api/v1/large-trades/history?trader= returns for the same from, to, min_size and
        category, each measured exactly as its clv object is. CLV is in cents per share against
        the market's stored closing line (GET ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            from_: Inclusive RFC3339 lower bound on the trade time. Defaults to 90 days before to.
            to: Exclusive RFC3339 upper bound on the trade time. Defaults to now; must be after from, and at most 366 days after it.
            min_size: Minimum trade size in USD. The capture floor was 3,000 USD before 2026-07-06 and 10,000 USD from then (1,000 USD in earnings markets), so 10000 gives one size ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
        """
        result: ApiResponse[GetTraderClvResponse] | ApiResponse[NotModifiedResponse] = self._call("getTraderClv", path_params={"address": address}, query={"from": from_, "to": to, "min_size": min_size, "category": category}, if_none_match=if_none_match)
        return result

    @overload
    def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderContextResponse]: ...

    @overload
    def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderContextResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderContextResponse] | ApiResponse[NotModifiedResponse]:
        """Get trader context (JSON).

        ``GET /api/v1/trader/{address}/context`` (operationId ``getTraderContext``).

        Returns a single structured context object for one trader: the full trader profile (same
        shape as GET /api/v1/trader/{address}) plus a position_summary (sync coverage and
        realized/unrealized P&L rollups, with an as_of open-position freshness clock), the
        data_as_of freshness timestamp (the ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetTraderContextResponse] | ApiResponse[NotModifiedResponse] = self._call("getTraderContext", path_params={"address": address}, query={}, if_none_match=if_none_match)
        return result

    def batch_get_traders(
        self,
        body: BatchGetTradersBody,
    ) -> ApiResponse[BatchGetTradersResponse]:
        """Batch traders.

        ``POST /api/v1/traders/batch`` (operationId ``batchGetTraders``).

        Returns traders for 1-25 wallet addresses or known usernames. Results preserve request
        order, duplicate inputs return duplicate rows, and each item is charged one batch item
        unit before execution. A wallet address this API does not track yet returns data with
        sync_status "unknown", matching the ...
        """
        result: ApiResponse[BatchGetTradersResponse] = self._call("batchGetTraders", path_params={}, query={}, body=body)
        return result

    @overload
    def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPositionTimelineResponse]: ...

    @overload
    def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse]:
        """Get a trader's position timeline for one market.

        ``GET /api/v1/trader/{address}/position-timeline`` (operationId ``getPositionTimeline``).

        Returns every stored Polymarket fill for one tracked trader in one market, newest first,
        with outcome-specific running_amount and running_avg_price including all earlier stored
        fills before pagination. Fills come from the full fill ledger, the same rows the trade
        export serves, at any date (#33245; ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            condition_id: Required. Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        result: ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse] = self._call("getPositionTimeline", path_params={"address": address}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderCategoryRecordsResponse]: ...

    @overload
    def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderCategoryRecordsResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderCategoryRecordsResponse] | ApiResponse[NotModifiedResponse]:
        """Get trader category win records.

        ``GET /api/v1/trader/{address}/categories`` (operationId ``getTraderCategoryRecords``).

        Returns one wallet's win record in every canonical category it has a settled market in:
        wins, decided (wins plus losses) and the rate, per category, busiest category first.
        These are the same counts the Pick of the Day holder chips carry. The Esports record
        also carries games: the wallet's record ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            category: Filter to one canonical category, matched through the same rollup every other category surface uses: soccer, EPL and champions league all reach Soccer, every ...
        """
        result: ApiResponse[GetTraderCategoryRecordsResponse] | ApiResponse[NotModifiedResponse] = self._call("getTraderCategoryRecords", path_params={"address": address}, query={"category": category}, if_none_match=if_none_match)
        return result

    def get_trader_pnl(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        sections: list[Literal["entries", "stats", "monthly", "year_totals", "drawdown"]] | None = None,
    ) -> ApiResponse[GetTraderPnlResponse]:
        """Get trader P&L time series.

        ``GET /api/v1/trader/{address}/pnl`` (operationId ``getTraderPnl``).

        Returns a trader's sports and esports daily P&L time series and pre-derived stats:
        entries (daily realized P&L and its running sum), period stats (all/90d/30d/7d), monthly
        aggregation, per-year totals, the drawdown series, series_status, and realized, which
        reconciles the days with the wallet's ...

        Query parameters:
            from_: Inclusive UTC calendar-date lower bound in YYYY-MM-DD form for the daily series (entries and drawdown). Omit for the whole stored history. A value that is not ...
            to: Inclusive UTC calendar-date upper bound in YYYY-MM-DD form for the daily series (entries and drawdown). Omit for the whole stored history. A value that is not ...
            sections: Which sections of the object to return. Repeatable and comma-separated: entries, stats, monthly, year_totals, drawdown. Omit it, or send it empty, for all ...
        """
        result: ApiResponse[GetTraderPnlResponse] = self._call("getTraderPnl", path_params={"address": address}, query={"from": from_, "to": to, "sections": sections})
        return result

    @overload
    def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPositionTimelineResponse]: ...

    @overload
    def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse]:
        """Get a trader's position timeline (unified identity resolver).

        ``GET /api/v1/traders/{trader}/position-timeline`` (operationId ``getPositionTimelineById``).

        Unified trader-timeline route (#4975). {trader} accepts all five identity shapes - 0x...
        wallet, username, trd_-prefixed trader id, bare integer id, and @username (a username
        lookup only, for all-digit usernames) - resolved by the single shared trader-identity
        resolver. Returns every stored ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            condition_id: Required. Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        result: ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse] = self._call("getPositionTimelineById", path_params={"trader": trader}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListPropsResponse]: ...

    @overload
    def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListPropsResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListPropsResponse] | ApiResponse[NotModifiedResponse]:
        """List player props across a league.

        ``GET /api/v1/props`` (operationId ``listProps``).

        Player props for the catalog's games of one league, one row per market, ordered by game
        slug, stat, player and line. NFL files props on a game's -player-props and -first-td-
        scorer child events and NBA on the game event; this reads both, so a caller does not
        walk GET /api/v1/games and then each ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            league: Required. League tag as GET /api/v1/games coverage.leagues spells it, for example nfl or nba. Matched case-insensitively.
            starts_after: RFC 3339 kickoff bound. A game with no published kickoff is excluded whenever either bound is set.
            starts_before: RFC 3339 kickoff bound, inclusive.
            player: Part of player.name, ignoring case and accents: jokic matches Nikola Jokić. A row with no player does not match.
            stat: Provider sportsMarketType values to keep, case-insensitive, for example passing_yards or points. Repeat the parameter or send a comma-separated list. An ...
            status: active (default), closed, or all. closed means the provider closed the market or it resolved.
            max_spread_c: Keep only props with an outcome whose cached best ask less best bid is at most this many cents: above 0, at most 100, in steps of 0.01. The books are the ones ...
            min_book_usd_within_2c: Keep only props with an outcome whose cached book holds at least this many USD on each side within 2 cents of its midpoint: bids at or above the midpoint minus ...
            limit: Page size. Out-of-range values are clamped to 1..200.
            cursor: Opaque prp_v1_ cursor from next_cursor, sent with the same filters. A cursor this endpoint did not issue returns 400 with error.param=cursor.
            expand: quotes adds each outcome's cached quote, as on GET /api/v1/games/{event_slug}/markets; it adds 1 to the cost, on every plan. Repeatable: quotes.
        """
        result: ApiResponse[ListPropsResponse] | ApiResponse[NotModifiedResponse] = self._call("listProps", path_params={}, query={"league": league, "starts_after": starts_after, "starts_before": starts_before, "player": player, "stat": stat, "status": status, "max_spread_c": max_spread_c, "min_book_usd_within_2c": min_book_usd_within_2c, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListPositionsResponse]: ...

    @overload
    def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListPositionsResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListPositionsResponse] | ApiResponse[NotModifiedResponse]:
        """List current positions (positions-board feed).

        ``GET /api/v1/positions`` (operationId ``listPositions``).

        Returns the current positions-board feed backed by the wallet_positions mirror. Ordered
        by current_value_usd DESC with deterministic (wallet, condition_id, outcome_index)
        tiebreakers. Pre-reconcile rows (current_value_usd IS NULL) are excluded. Positions on
        resolved markets are excluded: a position ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of current positions to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            consistency: live (default) reads the current value-ordered board. snapshot requires wallet and freezes up to 500 matching rows and 2 MB for up to five minutes. Keep ...
            min_size: Minimum current position value in USD. Defaults to 100 when omitted, or to 0 when wallet is present; send 0 to include every reconciled position.
            category: Exact match against provider-backed market_canonical.category. Sports and esports only (#27311): a category outside them returns 400 bad_request with param ...
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id emitted by V1 responses. Combine with min_size=0 for every reconciled ...
            wallet: Scope to one wallet or a book of wallets (repeatable, up to 25 per request; comma-separated values inside one occurrence also work). Each value is a wallet ...
            min_grade: Minimum trader grade allowlist. `A` matches S and A; `B` matches S, A, B; etc.
            side: Filter by the binary outcome side. `yes` maps to outcome_index=0, `no` to outcome_index=1.
        """
        result: ApiResponse[ListPositionsResponse] | ApiResponse[NotModifiedResponse] = self._call("listPositions", path_params={}, query={"limit": limit, "cursor": cursor, "consistency": consistency, "min_size": min_size, "category": category, "condition_id": condition_id, "wallet": wallet, "min_grade": min_grade, "side": side}, if_none_match=if_none_match)
        return result

    def list_large_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        condition_id: str | None = None,
    ) -> ApiResponse[ListLargePositionsResponse]:
        """List large positions.

        ``GET /api/v1/large-positions`` (operationId ``listLargePositions``).

        Returns the largest current open positions from graded traders, value-descending, with
        opaque cursor pagination. This is a change-detection feed, not a holder list: a row
        needs a current value of at least 50,000 USD and a live detection in the last 24 hours,
        so a wallet that holds a market without ...

        Query parameters:
            limit: Maximum number of large positions to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque pagination cursor from a previous response.
            min_size: Minimum position value in USD. Raises the feed's own floor of 50,000 USD; a smaller value does not lower it.
            category: One RFC 4180 CSV record of exact current provider-backed market_canonical.category values. Legacy unquoted lists such as NBA,WNBA remain valid; values ...
            min_grade: Minimum trader grade. Matched against the trader.grade each row returns, the wallet's current grade, so every row listed shows a grade at or above this floor.
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id (round-trips a value from a list response). Must be 0x followed by 64 ...
        """
        result: ApiResponse[ListLargePositionsResponse] = self._call("listLargePositions", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "condition_id": condition_id})
        return result

    @overload
    def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListLargeTradesResponse]: ...

    @overload
    def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListLargeTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListLargeTradesResponse] | ApiResponse[NotModifiedResponse]:
        """List large trades.

        ``GET /api/v1/large-trades`` (operationId ``listLargeTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of recent large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade now (trader.grade), the wallet's grade when this page is read, not when the trade filled. A wallet re-graded after a trade enters or ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            since: Return only the trades recorded after this one. Pass the id of a large trade this API returned (wt_<n>, or the bare integer). The answer keeps the list shape ...
            condition_id: Only this market's large trades: an exact raw provider condition_id. The page is read from the market's own index, newest first, and pages with cursor; it ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListLargeTradesResponse] | ApiResponse[NotModifiedResponse] = self._call("listLargeTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "min_market_volume_share": min_market_volume_share, "sort": sort, "since": since, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListWhaleTradesResponse]: ...

    @overload
    def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListWhaleTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListWhaleTradesResponse] | ApiResponse[NotModifiedResponse]:
        """List whale trades.

        ``GET /api/v1/whale-trades`` (operationId ``listWhaleTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of recent large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade now (trader.grade), the wallet's grade when this page is read, not when the trade filled. A wallet re-graded after a trade enters or ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            since: Return only the trades recorded after this one. Pass the id of a large trade this API returned (wt_<n>, or the bare integer). The answer keeps the list shape ...
            condition_id: Only this market's large trades: an exact raw provider condition_id. The page is read from the market's own index, newest first, and pages with cursor; it ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListWhaleTradesResponse] | ApiResponse[NotModifiedResponse] = self._call("listWhaleTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "min_market_volume_share": min_market_volume_share, "sort": sort, "since": since, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListLargeTradeHistoryResponse]: ...

    @overload
    def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListLargeTradeHistoryResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListLargeTradeHistoryResponse] | ApiResponse[NotModifiedResponse]:
        """Replay historical large trades.

        ``GET /api/v1/large-trades/history`` (operationId ``listLargeTradeHistory``).

        Returns historical large trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of historical large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD. The capture floor was 3,000 USD before 2026-07-06 and 10,000 USD from then (1,000 USD in earnings markets), so 10000 gives one size ...
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, username, or trd_-prefixed trader ID, resolved against the traders table. Unknown traders return an ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade as of today (trader.grade), not at trade time. On a historical window it selects wallets by a grade they may have earned after the trade; ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListLargeTradeHistoryResponse] | ApiResponse[NotModifiedResponse] = self._call("listLargeTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to, "min_market_volume_share": min_market_volume_share, "sort": sort, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListWhaleTradeHistoryResponse]: ...

    @overload
    def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListWhaleTradeHistoryResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListWhaleTradeHistoryResponse] | ApiResponse[NotModifiedResponse]:
        """Replay historical whale trades.

        ``GET /api/v1/whale-trades/history`` (operationId ``listWhaleTradeHistory``).

        Returns historical whale trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of historical large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD.
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, or username resolved against the traders table. Unknown traders return an empty list.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade.
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListWhaleTradeHistoryResponse] | ApiResponse[NotModifiedResponse] = self._call("listWhaleTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to, "min_market_volume_share": min_market_volume_share, "sort": sort, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetLargeTradeResponse]: ...

    @overload
    def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetLargeTradeResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetLargeTradeResponse] | ApiResponse[NotModifiedResponse]:
        """Get large trade by ID.

        ``GET /api/v1/large-trades/{id}`` (operationId ``getLargeTrade``).

        Returns one large trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetLargeTradeResponse] | ApiResponse[NotModifiedResponse] = self._call("getLargeTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetWhaleTradeResponse]: ...

    @overload
    def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetWhaleTradeResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetWhaleTradeResponse] | ApiResponse[NotModifiedResponse]:
        """Get whale trade by ID.

        ``GET /api/v1/whale-trades/{id}`` (operationId ``getWhaleTrade``).

        Returns one whale trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses. Deprecated alias of GET /api/v1/large-trades/{id}, kept live
        until its sunset on 2027-02-01 (#16304, #29351); every response carries `Deprecation:
        @1790132400` (RFC 9745, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetWhaleTradeResponse] | ApiResponse[NotModifiedResponse] = self._call("getWhaleTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    def list_large_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListLargeTradeCounterpartyExecutionsResponse]:
        """Page counterparty executions.

        ``GET /api/v1/large-trades/{id}/counterparties/executions`` (operationId ``listLargeTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by large-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail.

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the large trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListLargeTradeCounterpartyExecutionsResponse] = self._call("listLargeTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    def list_whale_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListLargeTradeCounterpartyExecutionsResponse]:
        """Page counterparty executions.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions`` (operationId ``listWhaleTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by whale-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail. Deprecated alias of GET /api/v1/large-
        trades/{id}/counterparties/executions, kept live until its sunset on ...

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListLargeTradeCounterpartyExecutionsResponse] = self._call("listWhaleTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    def list_large_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListLargeTradeCounterpartyMakersResponse]:
        """Page maker counterparties.

        ``GET /api/v1/large-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listLargeTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages.

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the large trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListLargeTradeCounterpartyMakersResponse] = self._call("listLargeTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    def list_whale_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListLargeTradeCounterpartyMakersResponse]:
        """Page maker counterparties.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listWhaleTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages. Deprecated alias of GET /api/v1/large-
        trades/{id}/counterparties/executions/{execution_id}/makers, kept live until its sunset
        on 2027-02-01 (#16304, #29351); every response ...

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListLargeTradeCounterpartyMakersResponse] = self._call("listWhaleTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    @overload
    def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListLeaderboardResponse]: ...

    @overload
    def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListLeaderboardResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListLeaderboardResponse] | ApiResponse[NotModifiedResponse]:
        """Get trader leaderboard.

        ``GET /api/v1/leaderboard`` (operationId ``listLeaderboard``).

        Returns ranked traders (grades S/A/B), by default in the board's own order: score
        descending, with a fixed tiebreak so the order never changes between reads of one
        ranking generation. sort, dir and activity reorder and scope the same wallets the way
        the site's leaderboard does (since 2026-11-02, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of ranked traders to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque lbv1_ pagination cursor from a prior response. It binds the finite score/address boundary to the effective category/strategy filters, and on a sorted ...
            category: Filter by category: a sport or esports bucket, matched case-insensitively. League values fold into their sport (NBA and NCAAB into Basketball, NFL into ...
            strategy: Filter by observed trading style. Current styles: two_sided, category_focused, high_activity, diversified, mixed, unclassified. Current styles count the ...
            sort: Order of the list, the sort columns of the site's leaderboard (/skill-leaderboard). rank (default) is the board's own order, the rank the site and the trader ...
            dir: Direction of sort. Omitted, each sort reads in its natural direction: rank 1 first for rank (asc), largest first for every other sort (desc). The opposite ...
            activity: Limit the list to wallets by recent trading, the site leaderboard's split. active: the wallet's last trade, as its current grade recorded it and aged to today, ...
        """
        result: ApiResponse[ListLeaderboardResponse] | ApiResponse[NotModifiedResponse] = self._call("listLeaderboard", path_params={}, query={"limit": limit, "cursor": cursor, "category": category, "strategy": strategy, "sort": sort, "dir": dir, "activity": activity}, if_none_match=if_none_match)
        return result

    @overload
    def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayResponse]: ...

    @overload
    def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayResponse] | ApiResponse[NotModifiedResponse]:
        """Get today's or a past day's Pick of the Day.

        ``GET /api/v1/pick-of-the-day`` (operationId ``getPickOfTheDay``).

        Returns entitled published picks for the current product day, or for the past product
        day named by `date`. Pro includes five selections in total: the designated free
        selection and the first four non-free selections in publication order. Max opens every
        available selection, up to twenty-five. A day ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            date: A product day (America/New_York) in YYYY-MM-DD format, on or before today. Omit it, or send today, for the current read. A past day with no published pick ...
            view: full (default) is the whole recorded set: every pick with its holders, lead backer, sports context, thesis and entry_authorization, and the top-level copy of ...
            pick_id: One entitled published pick of the day, by its stable decimal-string pick_id. The body carries that pick once, as picks[0], beside state, pick_date and ...
        """
        result: ApiResponse[GetPickOfTheDayResponse] | ApiResponse[NotModifiedResponse] = self._call("getPickOfTheDay", path_params={}, query={"date": date, "view": view, "pick_id": pick_id}, if_none_match=if_none_match)
        return result

    @overload
    def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayArchiveResponse]: ...

    @overload
    def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayArchiveResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayArchiveResponse] | ApiResponse[NotModifiedResponse]:
        """Get the Pick of the Day track record.

        ``GET /api/v1/pick-of-the-day/archive`` (operationId ``getPickOfTheDayArchive``).

        Returns published picks that have not been withdrawn, with their outcome, modeled
        return, unit score, closing-line value, and cumulative record. Resolved game details and
        results are public. For unauthorized unresolved selections, game identity, category,
        image, publication time, and backed facts ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: full (default) is every row with every field, plus days and hit_rate with its per-pick series. summary returns view, hit_rate without series, one page of short ...
            limit: Rows per page of picks, 1 to 200, default 50. An integer outside that range is clamped into it, like every list limit, and X-Effective-Query reports the limit ...
            cursor: The page.next_cursor of the previous page: the rows after it, newest first. A cursor is a position in the record, so a pick published while you page does not ...
        """
        result: ApiResponse[GetPickOfTheDayArchiveResponse] | ApiResponse[NotModifiedResponse] = self._call("getPickOfTheDayArchive", path_params={}, query={"view": view, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayStatsResponse]: ...

    @overload
    def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayStatsResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayStatsResponse] | ApiResponse[NotModifiedResponse]:
        """Get the Pick of the Day track-record breakdown.

        ``GET /api/v1/pick-of-the-day/stats`` (operationId ``getPickOfTheDayStats``).

        The figures behind the stats page, computed from the same rows the archive publishes:
        the hit rate, the win rate the market expected at publication, flat-stake outcome stats
        (drawdown, rolling form, profit factor, concentration), and buckets by day, sport,
        category, access group, month, entry-price ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: full (default) is every section. summary returns view, sections and every section except the five that grow with the record: series, days, categories, months ...
            sections: Exactly the sections to return, in the body's order whatever the request order. Repeatable and comma-separated: hit_rate, series, market_expectations, ...
        """
        result: ApiResponse[GetPickOfTheDayStatsResponse] | ApiResponse[NotModifiedResponse] = self._call("getPickOfTheDayStats", path_params={}, query={"view": view, "sections": sections}, if_none_match=if_none_match)
        return result

    @overload
    def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayLedgerResponse]: ...

    @overload
    def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayLedgerResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayLedgerResponse] | ApiResponse[NotModifiedResponse]:
        """Get the Pick of the Day commitment ledger.

        ``GET /api/v1/pick-of-the-day/ledger`` (operationId ``getPickOfTheDayLedger``).

        Returns the pre-game commitment for every published pick, so the public track record can
        be checked by someone who was not watching when the pick dropped. One entry per
        (pick_date, pick_rank), ascending by pick_date then pick_rank, in one of three states.
        `sealed` is an unresolved pick: the hash, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetPickOfTheDayLedgerResponse] | ApiResponse[NotModifiedResponse] = self._call("getPickOfTheDayLedger", path_params={}, query={}, if_none_match=if_none_match)
        return result

    def list_trending_wallets(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        window: Literal["7d", "30d"] | None = None,
    ) -> ApiResponse[ListTrendingWalletsResponse]:
        """List trending wallets.

        ``GET /api/v1/leaderboard/trending`` (operationId ``listTrendingWallets``).

        Returns wallets ranked by Polymarket weekly/monthly P&L (Polymarket-only discovery),
        with opaque page-cursor pagination. trending_pnl_usd and the by-PNL row order come from
        Polymarket's canonical leaderboard (data-
        api.polymarket.com/v2/leaderboard?time_period=week|month&sort_by=PNL), not a locally ...

        Query parameters:
            limit: Polymarket's weekly leaderboard caps the ranked set at 50 wallets; requests above 50 still return at most 50. Out-of-range values are clamped to 1..50.
            cursor: Opaque pagination cursor from a previous response, bound to its effective limit, window and ranked-board generation. A changed board or request scope returns ...
            window: Trailing window.
        """
        result: ApiResponse[ListTrendingWalletsResponse] = self._call("listTrendingWallets", path_params={}, query={"limit": limit, "cursor": cursor, "window": window})
        return result

    @overload
    def list_leaderboard_leagues(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[ListLeaderboardLeaguesResponse]: ...

    @overload
    def list_leaderboard_leagues(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[ListLeaderboardLeaguesResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_leaderboard_leagues(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListLeaderboardLeaguesResponse] | ApiResponse[NotModifiedResponse]:
        """List the leagues that have a leaderboard.

        ``GET /api/v1/leaderboard/leagues`` (operationId ``listLeaderboardLeagues``).

        Every league with its own skill leaderboard, grouped by sport, most ranked wallets
        first. Each row's `sport` and `slug` are the `{sport}` path segment and `league` value
        of GET /api/v1/leaderboard/sports/{sport}. A league is listed once its edge sort ranks
        at least `min_ranked` wallets. 503 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[ListLeaderboardLeaguesResponse] | ApiResponse[NotModifiedResponse] = self._call("listLeaderboardLeagues", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetSportLeaderboardResponse]: ...

    @overload
    def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetSportLeaderboardResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetSportLeaderboardResponse] | ApiResponse[NotModifiedResponse]:
        """Get a sport or league leaderboard.

        ``GET /api/v1/leaderboard/sports/{sport}`` (operationId ``getSportLeaderboard``).

        One sport's skill leaderboard, or with `league` one league's, the board the site's sport
        pages show. Wallets need `min_resolved` resolved markets in the sport or league.
        `sort=edge` (the default) ranks `edge_skill`, the edge over the price paid pulled toward
        the board's `edge_average` by how much ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            league: A league slug of the sport, for example premier-league or cs2, from GET /api/v1/leaderboard/leagues. Omit it for the sport board.
            sort: Ranking axis. Any other value returns 400 bad_request with error.param=sort.
            limit: Rows to return from the top of the board. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[GetSportLeaderboardResponse] | ApiResponse[NotModifiedResponse] = self._call("getSportLeaderboard", path_params={"sport": sport}, query={"league": league, "sort": sort, "limit": limit}, if_none_match=if_none_match)
        return result

    @overload
    def list_category_leaders(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[ListCategoryLeadersResponse]: ...

    @overload
    def list_category_leaders(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[ListCategoryLeadersResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_category_leaders(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListCategoryLeadersResponse] | ApiResponse[NotModifiedResponse]:
        """List every category's top edge leaders.

        ``GET /api/v1/leaderboard/categories`` (operationId ``listCategoryLeaders``).

        Every sports and esports category's top three edge leaders in one read, the board the
        site's categories index shows. In each category, wallets are ranked as GET
        /api/v1/leaderboard/categories/{slug} ranks them, by the 95% lower bound of their edge
        over the price they paid; only wallets whose lower ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[ListCategoryLeadersResponse] | ApiResponse[NotModifiedResponse] = self._call("listCategoryLeaders", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetCategoryLeaderboardResponse]: ...

    @overload
    def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetCategoryLeaderboardResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetCategoryLeaderboardResponse] | ApiResponse[NotModifiedResponse]:
        """Get a category's edge leaderboard.

        ``GET /api/v1/leaderboard/categories/{slug}`` (operationId ``getCategoryLeaderboard``).

        One sports or esports category's edge leaderboard, the board the site's category pages
        show. Wallets are ranked by edge_lower_bound, the 95% lower bound of their edge over the
        price they paid in the category, counted over independent events (independent_events
        breaks ties, then the wallet). Only ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            active_within: Keep wallets that traded in the category within this window. all (the default) keeps every ranked wallet.
            min_events: Independent events a wallet needs in the category to be listed. The site offers 0, 50, 100 and 250. Clamped to 0..1000000.
            limit: Maximum number of leaders to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque cel_ pagination cursor from a prior response. It binds the lower-bound/independent-event/wallet boundary to the committed category-skill ranking and to ...
        """
        result: ApiResponse[GetCategoryLeaderboardResponse] | ApiResponse[NotModifiedResponse] = self._call("getCategoryLeaderboard", path_params={"slug": slug}, query={"active_within": active_within, "min_events": min_events, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    def search_markets(
        self,
        *,
        q: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        category: str | None = None,
    ) -> ApiResponse[SearchMarketsResponse]:
        """Search markets.

        ``GET /api/v1/markets/search`` (operationId ``searchMarkets``).

        Search prediction markets by keyword. Returns one representative market per matching
        event, preferring the market whose title is q, then a winner market over a spread, total
        or prop, with status, category, platform metadata and the event_slug. Cursor pagination
        advances over grouped market results ...

        Query parameters:
            q: Required. Search query. Must be 2-512 characters before whitespace trimming and hold at least 2 letters or digits after trimming; a query with fewer letters or digits ...
            limit: Maximum number of matching markets to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            status: Filter by market status. A market is closed once Polymarket has closed trading or it has resolved, and active otherwise; all returns both.
            category: Filter by category. Sports and esports only (#27411): a category outside them returns 400 bad_request with param category and names the accepted buckets. The ...
        """
        result: ApiResponse[SearchMarketsResponse] = self._call("searchMarkets", path_params={}, query={"q": q, "limit": limit, "cursor": cursor, "status": status, "category": category})
        return result

    def search_content(
        self,
        *,
        q: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[SearchContentResponse]:
        """Search editorial content.

        ``GET /api/v1/content/search`` (operationId ``searchContent``).

        Search 0xinsider editorial content by keyword. Returns backend-owned learn, glossary,
        comparison, research, and trading-strategy items with canonical URLs. Opaque ranking
        scores are not exposed.

        Query parameters:
            q: Required. Search query. Must be 1-256 characters before whitespace trimming and non-empty after trimming.
            limit: Maximum content items to return. Out-of-range values are clamped to 1..50.
        """
        result: ApiResponse[SearchContentResponse] = self._call("searchContent", path_params={}, query={"q": q, "limit": limit})
        return result

    @overload
    def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSettledMarketsResponse]: ...

    @overload
    def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSettledMarketsResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSettledMarketsResponse] | ApiResponse[NotModifiedResponse]:
        """List settled game markets since a time.

        ``GET /api/v1/markets/settled`` (operationId ``listSettledMarkets``).

        Game markets Polymarket settled, as 0xinsider recorded them, oldest first by
        (settlement.observed_at, settlement_id): one row per market per settled state, the
        object the market_settled webhook delivers as data. It is the webhook's pull side: catch
        up after downtime from since, or poll with ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            since: RFC 3339 time, required without cursor. Rows whose settlement.observed_at is at or after it. With cursor, the cursor's position replaces it.
            sports_market_type: Comma-separated provider market types to keep, case-insensitive: moneyline, spreads, totals, a prop type; at most 64. Omitted: moneyline, or with cursor the ...
            league: Comma-separated leagues to keep, as the rows' league reports them (nba, epl, or pga for PGA Tour golf); at most 32, each starting with a letter and holding no ...
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque stl_v1_ cursor from next_cursor. It replaces since and keeps the filters it was issued for: a sports_market_type or league sent with it must match them, ...
        """
        result: ApiResponse[ListSettledMarketsResponse] | ApiResponse[NotModifiedResponse] = self._call("listSettledMarkets", path_params={}, query={"since": since, "sports_market_type": sports_market_type, "league": league, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ExploreMarketsResponse]: ...

    @overload
    def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ExploreMarketsResponse] | ApiResponse[NotModifiedResponse]: ...

    def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ExploreMarketsResponse] | ApiResponse[NotModifiedResponse]:
        """Explore markets.

        ``GET /api/v1/markets/explore`` (operationId ``exploreMarkets``).

        Browse whale-active titled markets with category, platform, status, and keyword filters.
        Explore is Polymarket-only: the platform parameter is accepted for backward-
        compatibility but every request returns Polymarket markets. Paginates visible discovery
        entries rather than raw market rows, returns ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            status: Filter by market status. A market is closed once Polymarket has closed trading or it has resolved, and active otherwise; all returns both.
            platform: Filter by source platform. Explore is Polymarket-only; polymarket is the only supported value and the parameter is accepted for backward-compatibility but does ...
            sort: Sort order for the discovery feed. `large_trades` ranks by large-trade activity; `whales` is its deprecated spelling and selects the same order until its ...
            cursor: Opaque pagination cursor from the previous response.
            limit: Page size. Out-of-range values are clamped to 1..48.
            q: Keyword search against market titles. At most 64 characters before whitespace trimming.
        """
        result: ApiResponse[ExploreMarketsResponse] | ApiResponse[NotModifiedResponse] = self._call("exploreMarkets", path_params={}, query={"category": category, "status": status, "platform": platform, "sort": sort, "cursor": cursor, "limit": limit, "q": q}, if_none_match=if_none_match)
        return result

    @overload
    def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse]: ...

    @overload
    def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse]:
        """List ranked sharp-money flows (deprecated alias).

        ``GET /api/v1/markets/smart-money-flows`` (operationId ``listSmartMoneyFlows``).

        Ranks sports and esports markets (#27306) by absolute net S/A/B-grade whale flow over a
        requested timeframe. Use this discovery endpoint to answer where sharp money is flowing
        before drilling into a specific market with /api/v1/market/{condition_id}/flow.
        Pagination is anchored by an opaque cursor ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp, normalized effective filters, ranking and aggregate collection ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
            condition_id: Only this market's flow: an exact raw provider condition_id. Cannot be combined with event_slug (400). An unknown market returns an empty list.
            event_slug: Only the markets of one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse] = self._call("listSmartMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse]: ...

    @overload
    def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse]:
        """List ranked sharp-money flows.

        ``GET /api/v1/markets/sharp-money-flows`` (operationId ``listSharpMoneyFlows``).

        Canonical path for ranked sharp-money flows; /api/v1/markets/smart-money-flows remains
        live as a deprecated byte-identical alias of it. Ranks sports and esports markets
        (#27306) by absolute net S/A/B-grade whale flow over a requested timeframe. Use this
        discovery endpoint to answer where sharp ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp, normalized effective filters, ranking and aggregate collection ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
            condition_id: Only this market's flow: an exact raw provider condition_id. Cannot be combined with event_slug (400). An unknown market returns an empty list.
            event_slug: Only the markets of one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse] = self._call("listSharpMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    def get_coverage(
        self,
    ) -> ApiResponse[GetCoverageResponse]:
        """Which reads the API serves for Polymarket.

        ``GET /api/v1/coverage`` (operationId ``getCoverage``).

        Unauthenticated discovery endpoint that declares which V1 data surfaces the API serves
        for Polymarket, the one venue it covers. Every capability reports supported. Coverage is
        sports and esports markets only (#27299): a market outside them answers 404 not_found
        with error.reason ...
        """
        result: ApiResponse[GetCoverageResponse] = self._call("getCoverage", path_params={}, query={})
        return result

    def get_platforms(
        self,
    ) -> ApiResponse[GetCoverageResponse]:
        """Get platform capability matrix.

        ``GET /api/v1/platforms`` (operationId ``getPlatforms``).

        Deprecated since #16315: use GET /api/v1/coverage, which serves the same body. This path
        stays live until its sunset on 2027-02-01 (#29351) and answers with Deprecation, Sunset
        and successor Link headers; from that date it answers 410 Gone with error.code
        endpoint_retired. Unauthenticated discovery ...
        """
        result: ApiResponse[GetCoverageResponse] = self._call("getPlatforms", path_params={}, query={})
        return result

    @overload
    def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketHoldersResponse]: ...

    @overload
    def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketHoldersResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketHoldersResponse] | ApiResponse[NotModifiedResponse]:
        """List a market's graded holders.

        ``GET /api/v1/market/{condition_id}/holders`` (operationId ``getMarketHolders``).

        The graded holder roster of one market, the list a Pick of the Day shows for its market,
        for any Polymarket market: every S/A/B wallet with open shares on either outcome, from a
        complete provider holder scan, each with its shares, Polymarket's own currentValue for
        the leg, its grade, its win record ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            outcome: Keep holders netting one side. `all` (default) lists both.
            min_grade: Narrow within the graded cohort: `S` keeps S, `A` keeps S and A, `B` (default) keeps S, A and B. `C`, `D` and `F` are rejected with 400: the route lists the ...
            limit: Maximum holders per page. Out-of-range values are clamped to 1..100.
            cursor: Opaque pagination cursor from the previous response's next_cursor. New cursors carry an absolute next offset bound to normalized condition_id, outcome and ...
        """
        result: ApiResponse[GetMarketHoldersResponse] | ApiResponse[NotModifiedResponse] = self._call("getMarketHolders", path_params={"condition_id": condition_id}, query={"outcome": outcome, "min_grade": min_grade, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketTopHoldersResponse]: ...

    @overload
    def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketTopHoldersResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketTopHoldersResponse] | ApiResponse[NotModifiedResponse]:
        """List a market's top holders, every grade.

        ``GET /api/v1/market/{condition_id}/top-holders`` (operationId ``getMarketTopHolders``).

        The largest holders of one market on each outcome, every grade from S to F and ungraded
        wallets included: the table the market's event page shows under Top holders. Each
        outcome lists up to 100 wallets, largest `shares` first, from Polymarket's holder board,
        with the provider's current value, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum holders per outcome. Out-of-range values are clamped to 1..100. `totals` covers the whole sample whatever the limit.
        """
        result: ApiResponse[GetMarketTopHoldersResponse] | ApiResponse[NotModifiedResponse] = self._call("getMarketTopHolders", path_params={"condition_id": condition_id}, query={"limit": limit}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketFlowResponse]: ...

    @overload
    def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketFlowResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketFlowResponse] | ApiResponse[NotModifiedResponse]:
        """Get a market's flow and top positions.

        ``GET /api/v1/market/{condition_id}/flow`` (operationId ``getMarketFlow``).

        Canonical since #16312; GET /api/v1/market/{condition_id}/intel is its deprecated alias
        and serves the same body under object market_intel. One market's flow and top positions:
        the signed flow of every tracked large trade in the window (net_flow_usd and its YES or
        NO direction), the large-trade ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        result: ApiResponse[GetMarketFlowResponse] | ApiResponse[NotModifiedResponse] = self._call("getMarketFlow", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketIntelResponse]: ...

    @overload
    def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketIntelResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketIntelResponse] | ApiResponse[NotModifiedResponse]:
        """Get market intelligence.

        ``GET /api/v1/market/{condition_id}/intel`` (operationId ``getMarketIntel``).

        Deprecated since #16312: use GET /api/v1/market/{condition_id}/flow, which serves the
        same body under object market_flow. This path stays live until its sunset on 2027-02-01
        (#29351), keeps object market_intel, and answers with Deprecation, Sunset and successor
        Link headers; from that date it ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        result: ApiResponse[GetMarketIntelResponse] | ApiResponse[NotModifiedResponse] = self._call("getMarketIntel", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)
        return result

    def batch_get_market_flow(
        self,
        body: BatchGetMarketFlowBody,
    ) -> ApiResponse[BatchGetMarketFlowResponse]:
        """Batch market flow.

        ``POST /api/v1/markets/flow/batch`` (operationId ``batchGetMarketFlow``).

        Returns each market's flow and top positions for 1-25 raw provider condition_id values.
        Results preserve request order, duplicate inputs return duplicate rows, and each item is
        charged one batch item unit before execution. Do not pass prefixed mkt_ IDs; use
        market.condition_id from search or ...
        """
        result: ApiResponse[BatchGetMarketFlowResponse] = self._call("batchGetMarketFlow", path_params={}, query={}, body=body)
        return result

    def batch_get_market_close(
        self,
        body: BatchGetMarketCloseBody,
    ) -> ApiResponse[BatchGetMarketCloseResponse]:
        """Batch market closing lines.

        ``POST /api/v1/markets/close/batch`` (operationId ``batchGetMarketClose``).

        Returns the closing line of 1-25 sports or esports markets in one request. Each ok
        item's data is the body GET /api/v1/market/{condition_id}/close returns for that market:
        status measured with both outcome legs, pending, or unavailable with unavailable_reason,
        judged at one clock for the whole ...
        """
        result: ApiResponse[BatchGetMarketCloseResponse] = self._call("batchGetMarketClose", path_params={}, query={}, body=body)
        return result

    def batch_get_market_intel(
        self,
        body: BatchGetMarketFlowBody,
    ) -> ApiResponse[BatchGetMarketIntelResponse]:
        """Batch market intelligence.

        ``POST /api/v1/markets/intel/batch`` (operationId ``batchGetMarketIntel``).

        Deprecated since #16312: use POST /api/v1/markets/flow/batch, which returns the same
        items under object market_flow_batch. This path stays live until its sunset on
        2027-02-01 (#29351), keeps object market_intel_batch, and answers with Deprecation,
        Sunset and successor Link headers; from that date ...
        """
        result: ApiResponse[BatchGetMarketIntelResponse] = self._call("batchGetMarketIntel", path_params={}, query={}, body=body)
        return result

    @overload
    def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketSnapshotResponse]: ...

    @overload
    def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketSnapshotResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketSnapshotResponse] | ApiResponse[NotModifiedResponse]:
        """Get market live snapshot.

        ``GET /api/v1/market/{condition_id}/snapshot`` (operationId ``getMarketSnapshot``).

        Provider-first market card snapshot with canonical identity, outcome labels, cached top-
        of-book when available, liquidity, live sports context, and explicit
        freshness/unavailable states.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            expand: Include trust metadata for current_price and spread_bps. Repeatable: trust.
        """
        result: ApiResponse[GetMarketSnapshotResponse] | ApiResponse[NotModifiedResponse] = self._call("getMarketSnapshot", path_params={"condition_id": condition_id}, query={"expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketCandlesResponse]: ...

    @overload
    def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketCandlesResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketCandlesResponse] | ApiResponse[NotModifiedResponse]:
        """Get market OHLC price candles.

        ``GET /api/v1/market/{condition_id}/candles`` (operationId ``getMarketCandles``).

        Provider-first bucketed OHLC price candles for a market's outcome tokens, derived from
        our stored copy of the Polymarket CLOB prices-history series (the same series the
        market-detail chart renders; covers open and resolved markets). Because the stored data
        is daily, a 1d bucket typically carries ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            resolution: Bucketing granularity. 1d aggregates by UTC calendar day, 1w by ISO week (Monday 00:00 UTC start). Defaults to 1d.
            from_: Exclusive lower bound as a URL-decoded unix timestamp in seconds; points at or before this timestamp are omitted (the underlying daily snapshot read filters ...
            to: Inclusive upper bound as a URL-decoded unix timestamp in seconds; points after this timestamp are omitted. If from is also present, from must be less than or ...
        """
        result: ApiResponse[GetMarketCandlesResponse] | ApiResponse[NotModifiedResponse] = self._call("getMarketCandles", path_params={"condition_id": condition_id}, query={"resolution": resolution, "from": from_, "to": to}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketCloseResponse]: ...

    @overload
    def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketCloseResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketCloseResponse] | ApiResponse[NotModifiedResponse]:
        """Get a market's closing line.

        ``GET /api/v1/market/{condition_id}/close`` (operationId ``getMarketClose``).

        The closing line of one sports or esports market: the price Polymarket's own price-
        history series recorded for each outcome in the last minute bucket that ended at or
        before kickoff (the market's game start time), read once after the market settles and
        stored unchanged. outcomes[0] is the YES leg ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetMarketCloseResponse] | ApiResponse[NotModifiedResponse] = self._call("getMarketClose", path_params={"condition_id": condition_id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListMarketTradesResponse]: ...

    @overload
    def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListMarketTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListMarketTradesResponse] | ApiResponse[NotModifiedResponse]:
        """List a market's taker fills in a time window.

        ``GET /api/v1/market/{condition_id}/trades`` (operationId ``listMarketTrades``).

        One market's taker fills of 100 USD or more, newest first by (traded_at,
        transaction_hash, log_index), from 0xinsider's own record of the exchange's on-chain
        fills. Each fill appears once: its id is the transaction hash and the log index of its
        fill event, so a walk can be deduplicated and joined ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            from_: Inclusive RFC 3339 lower bound on traded_at. Omitted or earlier than coverage.recorded_from: the walk runs to the start of the record (coverage.recorded_from). ...
            to: Exclusive RFC 3339 upper bound on traded_at. A first page ends at the earlier of to and coverage.complete_through. With cursor, it must match the cursor's.
            limit: Page size. Out-of-range values are clamped to 1..500.
            cursor: Opaque mtr_v1_ cursor from next_cursor. It continues the walk before the last fill of the previous page and keeps the market, from and to it was issued for: ...
        """
        result: ApiResponse[ListMarketTradesResponse] | ApiResponse[NotModifiedResponse] = self._call("listMarketTrades", path_params={"condition_id": condition_id}, query={"from": from_, "to": to, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketWalletsInOutResponse]: ...

    @overload
    def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketWalletsInOutResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketWalletsInOutResponse] | ApiResponse[NotModifiedResponse]:
        """Get a market's net buyers and sellers.

        ``GET /api/v1/market/{condition_id}/wallets-in-out`` (operationId ``getMarketWalletsInOut``).

        One market's net buyers and net sellers over the last 24 hours or 7 days, live: the body
        the 0xinsider market page's wallets in/out panel reads for a Pro viewer, from the same
        aggregate and cache (reads are cached for up to 60 seconds). A wallet's net is its buys
        minus its sells in the window ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            window: The window the nets are summed over, ending at the read's clock: 24h (the default) or 7d.
        """
        result: ApiResponse[GetMarketWalletsInOutResponse] | ApiResponse[NotModifiedResponse] = self._call("getMarketWalletsInOut", path_params={"condition_id": condition_id}, query={"window": window}, if_none_match=if_none_match)
        return result

    @overload
    def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSuspiciousTradesResponse]: ...

    @overload
    def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse]:
        """Get suspicious trades.

        ``GET /api/v1/suspicious-trades`` (operationId ``listSuspiciousTrades``).

        Stored trades whose recorded suspicion score meets the live flag threshold. Evidence
        contains the scorer's stored signals. Cursor-paginated by suspicion score. mode=live
        (default) uses fresh cached pages; mode=stable pins pagination to one published scoring
        generation and returns cursor_expired ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of suspicious trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
            mode: Pagination mode. live (default) keeps the 120-second response cache; stable pins the walk to one published scoring generation and binds the cursor to the limit ...
        """
        result: ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse] = self._call("listSuspiciousTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity, "mode": mode}, if_none_match=if_none_match)
        return result

    @overload
    def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetSuspiciousTradeResponse]: ...

    @overload
    def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetSuspiciousTradeResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetSuspiciousTradeResponse] | ApiResponse[NotModifiedResponse]:
        """Get suspicious trade by ID.

        ``GET /api/v1/suspicious-trades/{id}`` (operationId ``getSuspiciousTrade``).

        Returns one suspicious trade by raw whale_alerts.id or the rf_-prefixed id emitted by
        list responses. A flag on a market outside sports and esports returns 404 not_found with
        error.reason=market_out_of_scope (#27305); stop requesting it. Canonical since
        2026-09-23; GET /api/v1/insider-radar/{id} is ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetSuspiciousTradeResponse] | ApiResponse[NotModifiedResponse] = self._call("getSuspiciousTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListGamesResponse]: ...

    @overload
    def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListGamesResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListGamesResponse] | ApiResponse[NotModifiedResponse]:
        """List covered games.

        ``GET /api/v1/games`` (operationId ``listGames``).

        One coherent game view per row: both sides with their provider ids and live scores, the
        UTC kickoff, the provider's own status, the esports series format, and the game's winner
        markets (the moneyline, or a soccer game's three 1X2 legs) with their condition ids and
        outcome token ids. Spreads, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            sport: Canonical sport bucket, case-insensitive, with - and _ read as a space: table-tennis and Table Tennis are the same bucket. Omit for every covered sport. A ...
            league: League tag, case-insensitive, as this list's coverage.leagues spells it (GET /api/v1/coverage lists no leagues): nfl, epl, cs2, euroleague, cbb, cwbb. ...
            status: Keep only games in this state. ended, cancelled and postponed also list finished games that have left the live board, read from their stored records, for ...
            starts_after: RFC 3339 instant. Keep only games whose kickoff is at or after it. Games with no published kickoff are excluded whenever either bound is set. With a finished ...
            starts_before: RFC 3339 instant. Keep only games whose kickoff is at or before it. Must be at or after starts_after.
            window: Which games to read. all, the default, lists the whole covered catalog, which can start with games the provider still holds open weeks after kickoff. now lists ...
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque gms_v1_ cursor from next_cursor. It pins the page position (kickoff and event_slug), not a snapshot: the catalog is live, so a game added or removed ...
            expand: sharp_money adds each game's sharp_money, the GameSharpMoney object GET /api/v1/games/{event_slug}/sharp-money returns, read from the sport board's cached ...
        """
        result: ApiResponse[ListGamesResponse] | ApiResponse[NotModifiedResponse] = self._call("listGames", path_params={}, query={"sport": sport, "league": league, "status": status, "starts_after": starts_after, "starts_before": starts_before, "window": window, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetGameResponse]: ...

    @overload
    def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetGameResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetGameResponse] | ApiResponse[NotModifiedResponse]:
        """Get one game.

        ``GET /api/v1/games/{event_slug}`` (operationId ``getGame``).

        The same game object GET /api/v1/games returns, for one event_slug, including soccer 1X2
        home, draw and away market sides and draw_offered. The slug is the identity the
        live_sports_updated webhook pulse carries, so a receiver can read the full game straight
        from a pulse. A slug outside the ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetGameResponse] | ApiResponse[NotModifiedResponse] = self._call("getGame", path_params={"event_slug": event_slug}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListGameMarketsResponse]: ...

    @overload
    def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListGameMarketsResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListGameMarketsResponse] | ApiResponse[NotModifiedResponse]:
        """List a game's markets.

        ``GET /api/v1/games/{event_slug}/markets`` (operationId ``listGameMarkets``).

        Every stored Polymarket market of one event_slug: the moneyline, spreads, totals, team
        totals, half and quarter lines, player props and the rest, plus the markets of the
        event's child events (a soccer game's exact score, halftime result and more-markets
        events), each with its own event_slug. The ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            sports_market_type: Comma-separated provider market types to keep, case-insensitive: spreads, totals, points, first_half_totals. Omitted keeps every type. An unknown type returns ...
            status: active, closed or all. closed means the provider closed the market or it resolved.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque gmk_v1_ cursor from next_cursor, sent with the same filters. It pins the page position (sports_market_type, line, condition_id), not a snapshot. A ...
            expand: sharp_money adds each row's sharp_money: the game page's per-line split, side USD and S, A and B wallet counts per outcome. One read for the event whatever the ...
        """
        result: ApiResponse[ListGameMarketsResponse] | ApiResponse[NotModifiedResponse] = self._call("listGameMarkets", path_params={"event_slug": event_slug}, query={"sports_market_type": sports_market_type, "status": status, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetGameSharpMoneyResponse]: ...

    @overload
    def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetGameSharpMoneyResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetGameSharpMoneyResponse] | ApiResponse[NotModifiedResponse]:
        """Get one game's sharp money.

        ``GET /api/v1/games/{event_slug}/sharp-money`` (operationId ``getGameSharpMoney``).

        Where the graded money sits on a whole game, in one read: the S, A and B grade wallets'
        USD on each outcome (home, away and, for a 1X2 game, draw) summed across the game's
        markets, each outcome's integer share, the leader and wallet counts by grade, with the
        backend's verdict on the split. It is ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetGameSharpMoneyResponse] | ApiResponse[NotModifiedResponse] = self._call("getGameSharpMoney", path_params={"event_slug": event_slug}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListGameTradesResponse]: ...

    @overload
    def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListGameTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListGameTradesResponse] | ApiResponse[NotModifiedResponse]:
        """List a game's trades.

        ``GET /api/v1/games/{event_slug}/trades`` (operationId ``listGameTrades``).

        A game's newest fills across every market in it, newest first and live: the moneyline,
        spreads, totals and every prop, player props included. The same rows the 0xinsider game
        page's activity list shows a Pro viewer, read from the same live stream. Every fill, not
        only large ones: GET ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Newest fills to return. Out-of-range values are clamped to 1..200.
        """
        result: ApiResponse[ListGameTradesResponse] | ApiResponse[NotModifiedResponse] = self._call("listGameTrades", path_params={"event_slug": event_slug}, query={"limit": limit}, if_none_match=if_none_match)
        return result

    def get_game_holders(
        self,
        event_slug: str,
        *,
        condition_ids: list[str] | None = None,
        limit: int | None = None,
    ) -> ApiResponse[GetGameHoldersResponse]:
        """Get a game's holders.

        ``GET /api/v1/games/{event_slug}/holders`` (operationId ``getGameHolders``).

        The S, A and B graded holders of up to 25 markets of one game in one call. Each item is
        GET /api/v1/market/{condition_id}/holders for one market, unfiltered and cut to limit,
        with the same market, scan and totals beside it. Pass condition_ids from GET
        /api/v1/games/{event_slug}/markets; a market ...

        Query parameters:
            condition_ids: Required. 1 to 25 condition_id values of this game's markets, comma-separated. The key may also repeat (condition_ids=a&condition_ids=b). A raw provider condition_id or ...
            limit: Holders per market. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[GetGameHoldersResponse] = self._call("getGameHolders", path_params={"event_slug": event_slug}, query={"condition_ids": condition_ids, "limit": limit})
        return result

    @overload
    def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSuspiciousTradesResponse]: ...

    @overload
    def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse]:
        """Get insider radar flags.

        ``GET /api/v1/insider-radar`` (operationId ``listInsiderRadar``).

        Deprecated alias of GET /api/v1/suspicious-trades (2026-09-23), kept live until its
        sunset on 2027-02-01 (#29351); responses carry Deprecation, Sunset and a Link
        rel="successor-version" to it, and from that date the path answers 410 Gone with
        error.code endpoint_retired. Stored trades whose ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of radar flags to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
            mode: Pagination mode. live (default) keeps the 120-second response cache; stable pins the walk to one published scoring generation and binds the cursor to the limit ...
        """
        result: ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse] = self._call("listInsiderRadar", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity, "mode": mode}, if_none_match=if_none_match)
        return result

    @overload
    def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetInsiderRadarFlagResponse]: ...

    @overload
    def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetInsiderRadarFlagResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetInsiderRadarFlagResponse] | ApiResponse[NotModifiedResponse]:
        """Get insider radar flag by ID.

        ``GET /api/v1/insider-radar/{id}`` (operationId ``getInsiderRadarFlag``).

        Deprecated alias of GET /api/v1/suspicious-trades/{id} (2026-09-23), kept live until its
        sunset on 2027-02-01 (#29351); responses carry Deprecation, Sunset and a Link
        rel="successor-version" to it, and from that date the path answers 410 Gone with
        error.code endpoint_retired. The envelope keeps ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetInsiderRadarFlagResponse] | ApiResponse[NotModifiedResponse] = self._call("getInsiderRadarFlag", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    def get_event_replay_since(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        trader: str | None = None,
        condition_id: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_size: float | str | None = None,
        expand: list[Literal["trade"]] | None = None,
    ) -> ApiResponse[GetEventReplaySinceResponse]:
        """Replay public large-trade events.

        ``GET /api/v1/events/feed/since`` (operationId ``getEventReplaySince``).

        Returns durable public large-trade events strictly after an opaque cursor, in commit
        order: events are ordered by the position at which their write became visible to every
        reader (whale_alerts.inserted_xid), then by whale_alerts.id, and a page never reaches
        past the oldest write transaction still ...

        Query parameters:
            cursor: Opaque event replay cursor returned as next_cursor by a prior response. The cursor maps to the global (whale_alerts.inserted_xid, whale_alerts.id) commit-order ...
            limit: Maximum durable public whale-trade events to return. Out-of-range values are clamped to 1..100.
            trader: Only this wallet's trades: a wallet address, trd_-prefixed trader id or username resolved against the traders table. Bound to the cursor: a cursor issued under ...
            condition_id: Only trades on this market: the raw provider condition_id or its mkt_-prefixed id. Bound to the cursor.
            min_grade: Only trades by wallets at this grade or better (S best), read from the wallet's newest ranking at request time; a wallet with no grade never passes. For the ...
            min_grade_at_trade: Only trades whose grade_at_trade, the grade the wallet held when the trade filled, is at this grade or better (S best). Only a trade whose grade at the fill is ...
            min_size: Only trades of at least this USD amount. Decimal and scientific query spellings normalize exactly to cents, rounding half away from zero; maximum 1e15 USD. ...
            expand: Repeatable. trade adds the public trade read to every event (the object GET /api/v1/whale-trades/{id} returns for it), from one query per page, so a page of ...
        """
        result: ApiResponse[GetEventReplaySinceResponse] = self._call("getEventReplaySince", path_params={}, query={"cursor": cursor, "limit": limit, "trader": trader, "condition_id": condition_id, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "min_size": min_size, "expand": expand})
        return result

    def list_webhooks(
        self,
    ) -> ApiResponse[ListWebhooksResponse]:
        """List builder webhook destinations.

        ``GET /api/v1/webhooks`` (operationId ``listWebhooks``).

        Returns webhook destinations owned by the authenticated API key user. Deleted endpoints
        are omitted; an endpoint paused with PATCH or disabled after consecutive failures is
        listed with status disabled. Subscribable event_types and their payload shapes are
        described by GET /api/v1/webhooks/events. ...
        """
        result: ApiResponse[ListWebhooksResponse] = self._call("listWebhooks", path_params={}, query={})
        return result

    def create_webhook(
        self,
        body: CreateWebhookRequest,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Create a builder webhook destination.

        ``POST /api/v1/webhooks`` (operationId ``createWebhook``).

        Creates a pending HTTPS webhook destination. The response includes one-time
        signing_secret and verification.token values. Deliveries are not sent until the endpoint
        is verified, and verification requires the destination to answer 2xx to a signed
        webhook.verification challenge (see POST ...
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("createWebhook", path_params={}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    def list_webhook_events(
        self,
    ) -> ApiResponse[ListWebhookEventsResponse]:
        """List webhook event catalog.

        ``GET /api/v1/webhooks/events`` (operationId ``listWebhookEvents``).

        Self-describing catalog of every webhook event type: its description, data payload
        shape, and whether it is active (has a firing producer) or dormant (subscribable but not
        yet delivered; no event type is dormant today). The catalog is identical for every
        authenticated key and exposes no ...
        """
        result: ApiResponse[ListWebhookEventsResponse] = self._call("listWebhookEvents", path_params={}, query={})
        return result

    def list_webhook_deliveries(
        self,
        id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListWebhookDeliveriesResponse]:
        """List webhook delivery log.

        ``GET /api/v1/webhooks/{id}/deliveries`` (operationId ``listWebhookDeliveries``).

        Recent delivery attempts for one webhook destination owned by the authenticated API key
        user, newest first, with opaque cursor pagination. Returns 404 (identical to an unknown
        id) when the endpoint is not owned by the caller, so a non-owner cannot tell an owned-
        but-empty log apart from someone ...

        Query parameters:
            cursor: Opaque pagination cursor returned as next_cursor by a prior response. Omit to fetch the newest page.
            limit: Maximum delivery rows to return per page. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListWebhookDeliveriesResponse] = self._call("listWebhookDeliveries", path_params={"id": id}, query={"cursor": cursor, "limit": limit})
        return result

    def redeliver_webhook_delivery(
        self,
        id: str,
        delivery_id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[RedeliverWebhookDeliveryResponse]:
        """Redeliver a dead-lettered webhook delivery.

        ``POST /api/v1/webhooks/{id}/deliveries/{delivery_id}/redeliver`` (operationId ``redeliverWebhookDelivery``).

        Returns one dead_letter delivery to the delivery queue with a fresh attempt budget:
        status becomes pending, attempt_count resets to 0, and next_attempt_at is now, so the
        delivery worker claims it like any queued delivery, under the same per-owner and per-
        origin concurrency limits. Use it after a ...
        """
        result: ApiResponse[RedeliverWebhookDeliveryResponse] = self._call("redeliverWebhookDelivery", path_params={"id": id, "delivery_id": delivery_id}, query={}, idempotency_key=idempotency_key)
        return result

    def get_webhook(
        self,
        id: str,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Get one builder webhook destination.

        ``GET /api/v1/webhooks/{id}`` (operationId ``getWebhook``).

        Returns one webhook destination owned by the authenticated API key user.
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("getWebhook", path_params={"id": id}, query={})
        return result

    def update_webhook(
        self,
        id: str,
        body: UpdateWebhookRequest,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Update a builder webhook destination.

        ``PATCH /api/v1/webhooks/{id}`` (operationId ``updateWebhook``).

        Updates name, HTTPS URL, event types, or enabled state. URL changes force
        pending_verification and return a new verification token; the new destination must
        answer 2xx to the signed webhook.verification challenge before deliveries resume. A URL
        change returns 409 with ...
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("updateWebhook", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    def delete_webhook(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Disable a builder webhook destination.

        ``DELETE /api/v1/webhooks/{id}`` (operationId ``deleteWebhook``).

        Soft-deletes a webhook destination owned by the authenticated API key user. Existing
        delivery audit rows remain retained.
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("deleteWebhook", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    def verify_webhook(
        self,
        id: str,
        body: VerifyWebhookRequest,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Verify a builder webhook destination.

        ``POST /api/v1/webhooks/{id}/verify`` (operationId ``verifyWebhook``).

        Activates a pending webhook destination. Two conditions must both hold: the one-time
        verification token matches and has not expired, AND the destination answers 2xx to a
        signed challenge this operation POSTs to the endpoint's stored url. The challenge body
        is ...
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("verifyWebhook", path_params={"id": id}, query={}, body=body)
        return result

    def prepare_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Prepare a staged builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/prepare`` (operationId ``prepareWebhookSecret``).

        Creates a pending signing secret while the current secret remains active. Deploy the
        returned one-time signing_secret to the receiver before calling activate. The response
        exposes secret_rotation.status=pending; an existing pending secret is returned again so
        a lost response can be recovered safely.
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("prepareWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    def activate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Activate a staged builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/activate`` (operationId ``activateWebhookSecret``).

        Promotes the prepared signing secret to current, returns it once, and signs every
        delivery with both the new and previous secrets for one hour. Call retire after the
        receiver has completed its rollout. The current secret remains available through the
        existing immediate rotate-secret route for ...
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("activateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    def retire_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Retire the previous builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/retire`` (operationId ``retireWebhookSecret``).

        Ends the one-hour dual-signature overlap and removes the previous signing secret from
        future delivery authorization. Call this after the receiver accepts the activated
        secret. The operation is idempotent and does not return signing_secret.
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("retireWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    def rotate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Rotate a builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret`` (operationId ``rotateWebhookSecret``).

        Rotates the endpoint signing secret and returns the new signing_secret once in the
        response. Returns 409 with error.reason=webhook_delivery_in_progress while a live
        delivery freezes the current signing nonce; retry after it completes.
        """
        result: ApiResponse[CreateWebhookResponse] = self._call("rotateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    @overload
    def get_health(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetHealthResponse]: ...

    @overload
    def get_health(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetHealthResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_health(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetHealthResponse] | ApiResponse[NotModifiedResponse]:
        """Health check.

        ``GET /api/v1/health`` (operationId ``getHealth``).

        Returns API health status. No authentication required. Limited to 120 requests per
        minute per IP.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetHealthResponse] | ApiResponse[NotModifiedResponse] = self._call("getHealth", path_params={}, query={}, if_none_match=if_none_match)
        return result

    def create_mcp_json_rpc_response(
        self,
        body: CreateMcpJsonRpcResponseBody,
    ) -> ApiResponse[CreateMcpJsonRpcResponseResponse]:
        """Remote MCP endpoint (JSON-RPC).

        ``POST /api/v1/mcp`` (operationId ``createMcpJsonRpcResponse``).

        Model Context Protocol (MCP) Streamable HTTP transport. Accepts one JSON-RPC 2.0 request
        or notification. ID-bearing initialize, ping, tools/list, and tools/call requests (and
        server/discover on revision 2026-07-28) receive one same-ID JSON-RPC response; an
        unknown method, or a notification method ...
        """
        result: ApiResponse[CreateMcpJsonRpcResponseResponse] = self._call("createMcpJsonRpcResponse", path_params={}, query={}, body=body)
        return result

    def get_reports(
        self,
        *,
        granularity: Literal["daily", "weekly", "monthly"] | None = None,
        period: str | None = None,
    ) -> ApiResponse[GetReportsResponse]:
        """Unified report snapshot (granularity selector).

        ``GET /api/v1/reports`` (operationId ``getReports``).

        Unified convenience route (#4975) that consolidates the three singular report routes.
        Dispatches to the exact per-granularity cap (daily 50, weekly 100, monthly 200) and date
        window the legacy /api/v1/reports/{daily,weekly,monthly} routes use, so the response
        body is byte-identical to the matching ...

        Query parameters:
            granularity: Required. Report granularity selector.
            period: Required. Period token for the granularity. daily: UTC date YYYY-MM-DD. weekly: ISO week YYYY-WW for a durable canonical snapshot, or a from,to YYYY-MM-DD pair for an ...
        """
        result: ApiResponse[GetReportsResponse] = self._call("getReports", path_params={}, query={"granularity": granularity, "period": period})
        return result

    def get_daily_report_snapshot(
        self,
        *,
        date: str | None = None,
    ) -> ApiResponse[GetReportsResponse]:
        """Daily report snapshot.

        ``GET /api/v1/reports/daily`` (operationId ``getDailyReportSnapshot``).

        Returns a dated daily whale-activity report snapshot with source_range, snapshot.status,
        completeness, and reconciliation metadata. Report whale volume is local whale-alert
        activity volume, not provider lifetime trader volume.

        Query parameters:
            date: Required. UTC report date in YYYY-MM-DD format, from 2024-03-01 (the first day report data covers) through tomorrow UTC. Any other date returns 400 bad_request with ...
        """
        result: ApiResponse[GetReportsResponse] = self._call("getDailyReportSnapshot", path_params={}, query={"date": date})
        return result

    def get_weekly_report_snapshot(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        week: str | None = None,
    ) -> ApiResponse[GetReportsResponse]:
        """Weekly report snapshot.

        ``GET /api/v1/reports/weekly`` (operationId ``getWeeklyReportSnapshot``).

        Returns a weekly whale-activity report snapshot. Pass an ISO YYYY-WW token for a durable
        canonical snapshot, or an exact from/to UTC range of at most 31 inclusive days for an
        ephemeral response. The response identifies closed ranges as final and current ranges as
        rolling.

        Query parameters:
            from_: UTC source-range start in YYYY-MM-DD format; required with to. Together with to, selects an exact ephemeral range of at most 31 inclusive UTC days. A start ...
            to: UTC source-range end in YYYY-MM-DD format; required with from. Together with from, selects an exact ephemeral range of at most 31 inclusive UTC days. An end ...
            week: ISO week selector in YYYY-WW format; alternative to from/to. Selects a durable canonical snapshot. A week that ends before 2024-03-01, the first day report ...
        """
        result: ApiResponse[GetReportsResponse] = self._call("getWeeklyReportSnapshot", path_params={}, query={"from": from_, "to": to, "week": week})
        return result

    def get_monthly_report_snapshot(
        self,
        *,
        month: str | None = None,
    ) -> ApiResponse[GetReportsResponse]:
        """Monthly report snapshot.

        ``GET /api/v1/reports/monthly`` (operationId ``getMonthlyReportSnapshot``).

        Returns a UTC monthly whale-activity report snapshot with source_range, completeness,
        and reconciliation metadata.

        Query parameters:
            month: Required. UTC report month in YYYY-MM format. A month that ends before 2024-03-01, the first day report data covers, or starts after tomorrow UTC returns 400 bad_request ...
        """
        result: ApiResponse[GetReportsResponse] = self._call("getMonthlyReportSnapshot", path_params={}, query={"month": month})
        return result

    @overload
    def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetResolutionReportResponse]: ...

    @overload
    def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetResolutionReportResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetResolutionReportResponse] | ApiResponse[NotModifiedResponse]:
        """Get the daily resolution report.

        ``GET /api/v1/reports/resolutions`` (operationId ``getResolutionReport``).

        One UTC day's resolved markets: how often the side the profitable (S, A and B grade)
        wallets held won, beside how often every qualifying wallet's side won, one vote each.
        `markets` lists each market they held a position in, with the consensus side, its
        confidence, and the full roster of wallets, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            date: Required. UTC report date in YYYY-MM-DD format, no later than today UTC. Any other value returns 400 bad_request with error.param=date.
            view: `totals` returns the counts without `markets`. Any other value than full or totals returns 400 bad_request with error.param=view.
        """
        result: ApiResponse[GetResolutionReportResponse] | ApiResponse[NotModifiedResponse] = self._call("getResolutionReport", path_params={}, query={"date": date, "view": view}, if_none_match=if_none_match)
        return result

    def get_trader_export_snapshot(
        self,
        address: str,
    ) -> ApiResponse[GetTraderExportSnapshotResponse]:
        """Trader export snapshot metadata.

        ``GET /api/v1/trader/{address}/export`` (operationId ``getTraderExportSnapshot``).

        Returns export source-range, completeness, volume reconciliation, row-count estimate,
        and large-export policy for one trader. To download the full dataset programmatically,
        POST to this same path to submit an async export job (json | ndjson | csv), then poll
        the status route and follow the download ...
        """
        result: ApiResponse[GetTraderExportSnapshotResponse] = self._call("getTraderExportSnapshot", path_params={"address": address}, query={})
        return result

    def submit_trader_export(
        self,
        address: str,
        *,
        format: Literal["json", "ndjson", "csv"] | None = None,
        fresh: bool | None = None,
    ) -> ApiResponse[TraderExportJob]:
        """Submit a trader dataset export job.

        ``POST /api/v1/trader/{address}/export`` (operationId ``submitTraderExport``).

        Queues an async export of the trader's full dataset in the requested format (json
        default, ndjson, or csv) and returns the job resource. Poll the status route at
        poll_after_s until terminal is true, then follow the download route while status is
        'ready' (until expires_at, 24 hours from submit). ...

        Query parameters:
            format: Output serialization. json = full envelope document (default); ndjson = full envelope as line 1 then one trade object per line; csv = flat trades rows only.
            fresh: true: do not reuse a finished, running or reconciling job; only a queued job is reused, so the file is a snapshot read after this submit. Consumes quota when ...
        """
        result: ApiResponse[TraderExportJob] = self._call("submitTraderExport", path_params={"address": address}, query={"format": format, "fresh": fresh})
        return result

    def get_trader_export_status(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> ApiResponse[TraderExportJob]:
        """Poll a trader export job.

        ``GET /api/v1/trader/{address}/export/status`` (operationId ``getTraderExportStatus``).

        Returns the job resource for a submitted export: status (queued | running |
        cancel_requested | reconcile_required | ready | failed | expired | cancelled), terminal,
        next_action and poll_after_s, the lifecycle timestamps, the retention window
        (expires_at) and, once the file is written, data_as_of ...

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        result: ApiResponse[TraderExportJob] = self._call("getTraderExportStatus", path_params={"address": address}, query={"job_id": job_id})
        return result

    def cancel_trader_export(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> ApiResponse[TraderExportJob]:
        """Cancel a trader export job.

        ``POST /api/v1/trader/{address}/export/cancel`` (operationId ``cancelTraderExport``).

        Cancels a submitted export and returns the job resource, the same shape the status route
        returns. A queued job reads cancelled at once and no worker will start it. A running job
        reads cancel_requested until the worker reaches its next safe point, then cancelled: the
        worker checks every 5 seconds ...

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        result: ApiResponse[TraderExportJob] = self._call("cancelTraderExport", path_params={"address": address}, query={"job_id": job_id})
        return result

    def download_trader_export(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> Download:
        """Download a finished trader export.

        ``GET /api/v1/trader/{address}/export/download`` (operationId ``downloadTraderExport``).

        Redirects (302) to a presigned URL lasting at most one hour and no later than the job's
        expires_at for the finished export file while the job status is 'ready' and expires_at
        has not passed. The file is gzip-compressed and served with the format's Content-Type
        (application/json, ...

        Returns a ``Download``: the redirect is followed once, without the credential, and the
        file is streamed. Iterate it, ``save(path)`` it for its SHA-256, or ``read()`` it
        (bounded); ``close()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        return self._download("downloadTraderExport", path_params={"address": address}, query={"job_id": job_id})

    def get_usage(
        self,
    ) -> ApiResponse[Usage]:
        """Inspect current API usage without spending primary request quota.

        ``GET /api/v1/usage`` (operationId ``getUsage``).

        Returns the authenticated caller sliding-window request budget, UTC-day usage and
        monthly quota. This control-plane endpoint remains available for a valid credential
        after paid data access lapses and does not increment the primary Redis rate-limit
        counter, monthly quota or API usage table; it ...
        """
        result: ApiResponse[Usage] = self._call("getUsage", path_params={}, query={})
        return result

    def get_market_context_markdown(
        self,
        condition_id: str,
    ) -> ApiResponse[str]:
        """Get market context (Markdown).

        ``GET /api/v1/market/{condition_id}/context.md`` (operationId ``getMarketContextMarkdown``).

        Authenticated, self-contained Polymarket market evidence document. Renders the same
        typed data as the market snapshot with trust included: identity, outcome labels and
        tokens, cached quotes, liquidity, live sports, and per-source freshness or unavailable
        reasons. Provider text is encoded as ...
        """
        result: ApiResponse[str] = self._call("getMarketContextMarkdown", path_params={"condition_id": condition_id}, query={})
        return result

    def get_account_identity(
        self,
    ) -> ApiResponse[AccountIdentity]:
        """Identify the authenticated account and credential.

        ``GET /api/v1/me`` (operationId ``getAccountIdentity``).

        Returns caller-owned account and credential IDs, credential validity, paid-data
        entitlement and approved scopes. Null scopes mean full legacy developer-key access.
        Valid credentials can use this control-plane diagnostic path after paid access lapses;
        data routes still require active paid access. ...
        """
        result: ApiResponse[AccountIdentity] = self._call("getAccountIdentity", path_params={}, query={})
        return result

    def submit_whale_dataset(
        self,
        body: SubmitWhaleDatasetBody,
    ) -> ApiResponse[WhaleDatasetJob]:
        """Create an immutable whale dataset.

        ``POST /api/v1/datasets/whale-trades`` (operationId ``submitWhaleDataset``).

        Extract at most 1,000,000 rows and 256 MiB uncompressed; exceeding either bound fails
        the job and publishes no partial file. Window and filters freeze on admission; rows and
        source facts freeze on one worker database snapshot. NDJSON uses exact decimal strings,
        with no current grade or market ...
        """
        result: ApiResponse[WhaleDatasetJob] = self._call("submitWhaleDataset", path_params={}, query={}, body=body)
        return result

    def get_whale_dataset_status(
        self,
        job_id: str,
    ) -> ApiResponse[WhaleDatasetJob]:
        """Read a whale dataset job.

        ``GET /api/v1/datasets/whale-trades/{job_id}`` (operationId ``getWhaleDatasetStatus``).

        Read queued, running, cancel_requested, ready, failed, reconcile_required, expired or
        cancelled. Poll only while next_action is poll, after poll_after_s. Ready manifests
        contain count, content and compressed SHA-256, schema, filters, source, horizon, expiry
        and replay continuation. Deltas do not ...
        """
        result: ApiResponse[WhaleDatasetJob] = self._call("getWhaleDatasetStatus", path_params={"job_id": job_id}, query={})
        return result

    def download_whale_dataset(
        self,
        job_id: str,
    ) -> Download:
        """Download an immutable whale dataset.

        ``GET /api/v1/datasets/whale-trades/{job_id}/download`` (operationId ``downloadWhaleDataset``).

        Download only a ready artifact; status handles failure and cancellation. Retired
        artifacts return 410 at serving time. Paid export scope; jobs are private to the
        credential owner. Shares the 20/day owner export quota and fair worker admission with
        trader exports; datasets also have a combined ...

        Returns a ``Download``: the redirect is followed once, without the credential, and the
        file is streamed. Iterate it, ``save(path)`` it for its SHA-256, or ``read()`` it
        (bounded); ``close()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.
        """
        return self._download("downloadWhaleDataset", path_params={"job_id": job_id}, query={})

    def cancel_whale_dataset(
        self,
        job_id: str,
    ) -> ApiResponse[WhaleDatasetJob]:
        """Cancel a whale dataset job.

        ``POST /api/v1/datasets/whale-trades/{job_id}/cancel`` (operationId ``cancelWhaleDataset``).

        Cancel queued jobs immediately and request running jobs stop at their next safe point.
        Repeating cancel converges on the current state; cancellation after the completion fence
        leaves the artifact ready. Paid export scope; jobs are private to the credential owner.
        Shares the 20/day owner export ...
        """
        result: ApiResponse[WhaleDatasetJob] = self._call("cancelWhaleDataset", path_params={"job_id": job_id}, query={})
        return result

    @overload
    def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayLedgerEntryResponse]: ...

    @overload
    def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayLedgerEntryResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayLedgerEntryResponse] | ApiResponse[NotModifiedResponse]:
        """Read a pick proof by stable id.

        ``GET /api/v1/pick-of-the-day/ledger/{pick_id}`` (operationId ``getPickOfTheDayLedgerEntry``).

        Public read of one published pick by its stable decimal-string pick_id. Same proof
        gating, canonical bytes, ETag and integrity failures as the ledger. Invalid ids return
        400; absent or unpublished picks return 404. Withdrawal from recommendations or the
        archive does not remove a published ledger ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetPickOfTheDayLedgerEntryResponse] | ApiResponse[NotModifiedResponse] = self._call("getPickOfTheDayLedgerEntry", path_params={"pick_id": pick_id}, query={}, if_none_match=if_none_match)
        return result

    def create_webhook_verification_attempt(
        self,
        id: str,
        body: CreateWebhookVerificationAttemptRequest,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookVerificationAttemptResponse]:
        """Admit asynchronous webhook verification.

        ``POST /api/v1/webhooks/{id}/verification-attempts`` (operationId ``createWebhookVerificationAttempt``).

        Additive asynchronous consent flow; the legacy POST /verify keeps its synchronous
        200/422 behavior and retry policy. Commits one durable attempt and returns 202 without
        awaiting DNS or the receiver. Send the original verification_token. Optional
        Idempotency-Key replays the original admission ...
        """
        result: ApiResponse[CreateWebhookVerificationAttemptResponse] = self._call("createWebhookVerificationAttempt", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    def get_webhook_verification_attempt(
        self,
        id: str,
        attempt_id: str,
    ) -> ApiResponse[CreateWebhookVerificationAttemptResponse]:
        """Read webhook verification attempt status.

        ``GET /api/v1/webhooks/{id}/verification-attempts/{attempt_id}`` (operationId ``getWebhookVerificationAttempt``).

        Fresh primary-database status for one attempt owned by the authenticated account and
        webhook. queued/running means consent is pending; only verified activates the unchanged
        endpoint after receiver 2xx. failed/cancelled/expired are terminal. Polling never issues
        a challenge or restarts work. At ...
        """
        result: ApiResponse[CreateWebhookVerificationAttemptResponse] = self._call("getWebhookVerificationAttempt", path_params={"id": id, "attempt_id": attempt_id}, query={})
        return result

    @overload
    def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ComboFillsResponse]: ...

    @overload
    def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ComboFillsResponse] | ApiResponse[NotModifiedResponse]: ...

    def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ComboFillsResponse] | ApiResponse[NotModifiedResponse]:
        """List combo fills.

        ``GET /api/v1/combos/fills`` (operationId ``listComboFills``).

        Returns live Polymarket combo taker fills with exact decimal-string economics, wallet
        identities, grades, legs, conjunction results, and ingest coverage. Requires an active
        Pro or Max API key. Listing includes executions with price at most 0.95; use combo
        detail for complete history. Sports and ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            result: CSV of pending, won, or lost; all clears the filter. Unknown results appear only in unfiltered lists.
            legs: CSV of 2, 3, 4, or 5+; all clears the filter. A combo matches any named pick count.
            min_stake: Minimum collateral in whole USDC.
            min_multiplier: 0 disables the filter; otherwise use 2..1000000. Minimum shares per dollar at execution.
            grades: CSV of S, A, B, C, D, F; all clears the filter. Ungraded wallets do not match.
            sports: CSV of nfl, ncaaf, nba, wnba, baseball, hockey, soccer, tennis, table-tennis, esports, mma, boxing, golf, cricket, f1, pickleball; all clears the filter. ...
            sort: Recent is newest first; largest ranks collateral; payout ranks buy-fill shares and excludes sells.
            window: Defaults to all for recent and 24h for largest or payout.
            limit: Page size. Integer values outside the range are clamped to 1..200.
            cursor: Exclusive block_number:log_index cursor for recent only; send the returned next_cursor unchanged.
            offset: Offset for ranked largest or payout ordering; use returned next_offset.
        """
        result: ApiResponse[ComboFillsResponse] | ApiResponse[NotModifiedResponse] = self._call("listComboFills", path_params={}, query={"result": result, "legs": legs, "min_stake": min_stake, "min_multiplier": min_multiplier, "grades": grades, "sports": sports, "sort": sort, "window": window, "limit": limit, "cursor": cursor, "offset": offset}, if_none_match=if_none_match)
        return result

    @overload
    def get_combos_summary(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[CombosSummaryResponse]: ...

    @overload
    def get_combos_summary(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[CombosSummaryResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_combos_summary(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[CombosSummaryResponse] | ApiResponse[NotModifiedResponse]:
        """Get live combo count.

        ``GET /api/v1/combos/summary`` (operationId ``getCombosSummary``).

        Returns the stored count of traded combos whose YES conjunction remains pending, with
        its computation timestamp. Sports and esports only (#27449): a combo with a leg outside
        them is not counted. Requires an active Pro or Max API key. The count is refreshed by
        the ingest owner at most every five ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[CombosSummaryResponse] | ApiResponse[NotModifiedResponse] = self._call("getCombosSummary", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[ComboResponse]: ...

    @overload
    def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[ComboResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[ComboResponse] | ApiResponse[NotModifiedResponse]:
        """Get combo detail.

        ``GET /api/v1/combos/{condition_id}`` (operationId ``getCombo``).

        Returns one Polymarket combo with its legs, conjunction result, all-time trade totals,
        newest 100 taker fills, lifecycle totals, and ingest coverage. Requires an active Pro or
        Max API key. Detail retains execution history above the listing price cap. A malformed
        combo ID returns 400; an unknown ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[ComboResponse] | ApiResponse[NotModifiedResponse] = self._call("getCombo", path_params={"condition_id": condition_id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse]: ...

    @overload
    def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse] | ApiResponse[NotModifiedResponse]: ...

    def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse] | ApiResponse[NotModifiedResponse]:
        """Get Edge Hunter.

        ``GET /api/v1/edge-hunter`` (operationId ``getEdgeHunter``).

        Max-only canonical Edge Hunter API with board, signals and observations views. An active
        Pro credential receives 403 forbidden with reason max_plan_required. Default board
        admission and ordering remain compatible: B grade floor, 30-row cap, 48-hour kickoff
        horizon, full Max projection and both ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: Response mode. board preserves the full quoted board; signals exposes ranked records and category evidence; observations exposes cohort measurements and ...
            category: Legacy canonical bucket alias, now accepted in every view. Provider aliases canonicalize: NFL reaches Football and EPL reaches Soccer. Use leagues for a ...
            cohort: Required for view=observations; wider_holder, in_play or emerging_pile. Rejected for board and signals. wider_holder covers pregame markets that view=signals ...
            admission: Opt-in admission rule for view=observations with cohort=wider_holder; rejected for every other view and cohort. most_held_48h returns the most-held selection ...
            min_grade: Board and signals: S, A or B, default B. Requires a piled-side holder at the selected grade floor or better, without removing other holders. Rejected for ...
            limit: Board row cap defaults to 30 and clamps integer values to 1..30; total counts selected admitted rows before the cap. Signals and observations page size ...
            cursor: Opaque canonical Edge Hunter cursor from next_cursor. Bound to view, every normalized selection axis, grade/horizon where applicable, source snapshot and ...
            horizon_hours: Kickoff window for board (default 48) or signals (default 12). Integer values clamp to 1..48. Rejected for observations, whose pre-game universe is fixed at 48 ...
            kind: All views: sports excludes the Esports bucket; esports selects only Esports. Omit for both. Combines with other selections using AND. Selected reads echo ...
            sports: Canonical sport buckets, including Esports and Table Tennis, matched case-insensitively. Unknown names and league aliases such as NFL are rejected in sports; ...
            leagues: Normalized machine/provider league identities, such as nfl, cfb, nba, epl, cs2, lol, dota2 or valorant. Known wire/tag aliases normalize; other provider keys ...
            market_types: Exact provider sports_market_type values. This is an open provider taxonomy, distinct from exact market IDs. Read market_context.market_type; missing selected ...
            condition_ids: Exact market selections. Raw provider condition IDs and the existing mkt_-prefixed aliases normalize to raw IDs. Unknown well-formed IDs return an empty ...
            event_slugs: Exact provider event slugs. Use event_slug returned on the row; no title or slug-prefix guessing. All views. Repeat this query key or put comma-separated ...
            series_slugs: Exact provider series slugs. Read market_context.series_slug; a missing selected series excludes the row. All views. Repeat this query key or put ...
        """
        result: ApiResponse[EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse] | ApiResponse[NotModifiedResponse] = self._call("getEdgeHunter", path_params={}, query={"view": view, "category": category, "cohort": cohort, "admission": admission, "min_grade": min_grade, "limit": limit, "cursor": cursor, "horizon_hours": horizon_hours, "kind": kind, "sports": sports, "leagues": leagues, "market_types": market_types, "condition_ids": condition_ids, "event_slugs": event_slugs, "series_slugs": series_slugs}, if_none_match=if_none_match)
        return result



class AsyncOperationsMixin:
    """The async counterpart of ``OperationsMixin``: the same methods, as coroutines.

    Provided by ``AsyncClient``, which awaits the request on ``httpx.AsyncClient``
    instead of blocking the event loop with the synchronous transport."""

    async def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by AsyncClient
        raise NotImplementedError

    async def _download(
        self, operation_id: str, **kwargs: Any
    ) -> AsyncDownload:  # pragma: no cover - provided by AsyncClient
        raise NotImplementedError

    async def get_api_discovery(
        self,
    ) -> GetApiDiscoveryResponse:
        """API discovery.

        ``GET /api/v1`` (operationId ``getApiDiscovery``).

        Unauthenticated API-origin discovery document pointing agents to the canonical API base
        URL, full docs, web-origin OpenAPI spec, health check, and the COMPLETE index of
        authenticated data routes. data.authenticated_routes is the whole authenticated route
        surface, not a sample: it carries every ...
        """
        result: GetApiDiscoveryResponse = await self._call("getApiDiscovery", path_params={}, query={})
        return result

    async def redirect_api_openapi_spec(
        self,
    ) -> AsyncDownload:
        """Redirect to the canonical OpenAPI spec.

        ``GET /api/v1/openapi.json`` (operationId ``redirectApiOpenapiSpec``).

        Unauthenticated API-origin compatibility redirect to the canonical web-origin OpenAPI
        JSON document at https://0xinsider.com/api/v1/openapi.json.

        Returns an ``AsyncDownload``: the redirect is followed once, without the credential, and
        the file is streamed. Iterate it, ``asave(path)`` it for its SHA-256, or ``aread()`` it
        (bounded); ``aclose()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.
        """
        return await self._download("redirectApiOpenapiSpec", path_params={}, query={})

    async def register_agent(
        self,
    ) -> RegisterAgentResponse:
        """Register an agent for a sandbox key.

        ``POST /api/v1/agents/register`` (operationId ``registerAgent``).

        Self-serve agent onboarding: no account, no request body, no human step. Returns a
        sandbox API key (oxi_sk_test_...) and the path to live access. The key works only on the
        sandbox server (https://0xinsider.com/sandbox/api/v1), where it is optional: send it as
        Authorization: Bearer to exercise the ...
        """
        result: RegisterAgentResponse = await self._call("registerAgent", path_params={}, query={})
        return result

    @overload
    async def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: None = None,
    ) -> GetTraderResponse: ...

    @overload
    async def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: str | None,
    ) -> GetTraderResponse | NotModifiedResponse: ...

    async def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: str | None = None,
    ) -> GetTraderResponse | NotModifiedResponse:
        """Get trader.

        ``GET /api/v1/trader/{address}`` (operationId ``getTrader``).

        Returns a trader's grade (S through F), P&L, win rate, and optional strategy/category
        data. The path accepts either an Ethereum wallet address, a known trader username, or a
        trd_-prefixed trader ID emitted by this API. A wallet address this API does not track
        yet returns 200 with sync_status ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            expand: Include heavy fields and trust metadata. Repeatable: strategy, categories, trust, breakdowns. breakdowns adds the profile's strategy measures ...
            max_age_s: Opt into a whole-response freshness ceiling in seconds. The server returns 200 only when data_quality.status is fresh or stale and data_quality.as_of is no ...
        """
        result: GetTraderResponse | NotModifiedResponse = await self._call("getTrader", path_params={"address": address}, query={"expand": expand, "max_age_s": max_age_s}, if_none_match=if_none_match)
        return result

    async def get_trader_context_markdown(
        self,
        address: str,
    ) -> str:
        """Get trader context (Markdown).

        ``GET /api/v1/trader/{address}/context.md`` (operationId ``getTraderContextMarkdown``).

        Returns a single human- and LLM-readable Markdown briefing for one trader: identity,
        grade, P&L, position coverage, and freshness. The path accepts an Ethereum wallet
        address (0x...), a known trader username, or a trd_-prefixed trader ID emitted by this
        API. A wallet address this API does not track ...
        """
        result: str = await self._call("getTraderContextMarkdown", path_params={"address": address}, query={})
        return result

    @overload
    async def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: None = None,
    ) -> GetTraderGradeAtResponse: ...

    @overload
    async def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: str | None,
    ) -> GetTraderGradeAtResponse | NotModifiedResponse: ...

    async def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: str | None = None,
    ) -> GetTraderGradeAtResponse | NotModifiedResponse:
        """Get a trader grade proven visible at a past instant.

        ``GET /api/v1/trader/{address}/grade-at`` (operationId ``getTraderGradeAt``).

        Reads one trader's recorded grade at as_of from prospective visibility evidence. Before
        the first recorded observation, after deletion, or during a grade-transition gap, status
        is unknown and grade is null; a recorded ungraded trader instead has status ungraded.
        available_from is the first proven ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            as_of: Required. RFC3339 instant whose historically visible grade is requested. Future instants are refused. Send the trade or decision time, not the ranking date.
        """
        result: GetTraderGradeAtResponse | NotModifiedResponse = await self._call("getTraderGradeAt", path_params={"address": address}, query={"as_of": as_of}, if_none_match=if_none_match)
        return result

    @overload
    async def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: None = None,
    ) -> GetTraderClvResponse: ...

    @overload
    async def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: str | None,
    ) -> GetTraderClvResponse | NotModifiedResponse: ...

    async def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: str | None = None,
    ) -> GetTraderClvResponse | NotModifiedResponse:
        """Get a trader's closing line value on large trades.

        ``GET /api/v1/trader/{address}/clv`` (operationId ``getTraderClv``).

        Closing line value (CLV) over one wallet's large trades in a window: the trades GET
        /api/v1/large-trades/history?trader= returns for the same from, to, min_size and
        category, each measured exactly as its clv object is. CLV is in cents per share against
        the market's stored closing line (GET ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            from_: Inclusive RFC3339 lower bound on the trade time. Defaults to 90 days before to.
            to: Exclusive RFC3339 upper bound on the trade time. Defaults to now; must be after from, and at most 366 days after it.
            min_size: Minimum trade size in USD. The capture floor was 3,000 USD before 2026-07-06 and 10,000 USD from then (1,000 USD in earnings markets), so 10000 gives one size ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
        """
        result: GetTraderClvResponse | NotModifiedResponse = await self._call("getTraderClv", path_params={"address": address}, query={"from": from_, "to": to, "min_size": min_size, "category": category}, if_none_match=if_none_match)
        return result

    @overload
    async def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: None = None,
    ) -> GetTraderContextResponse: ...

    @overload
    async def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None,
    ) -> GetTraderContextResponse | NotModifiedResponse: ...

    async def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None = None,
    ) -> GetTraderContextResponse | NotModifiedResponse:
        """Get trader context (JSON).

        ``GET /api/v1/trader/{address}/context`` (operationId ``getTraderContext``).

        Returns a single structured context object for one trader: the full trader profile (same
        shape as GET /api/v1/trader/{address}) plus a position_summary (sync coverage and
        realized/unrealized P&L rollups, with an as_of open-position freshness clock), the
        data_as_of freshness timestamp (the ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetTraderContextResponse | NotModifiedResponse = await self._call("getTraderContext", path_params={"address": address}, query={}, if_none_match=if_none_match)
        return result

    async def batch_get_traders(
        self,
        body: BatchGetTradersBody,
    ) -> BatchGetTradersResponse:
        """Batch traders.

        ``POST /api/v1/traders/batch`` (operationId ``batchGetTraders``).

        Returns traders for 1-25 wallet addresses or known usernames. Results preserve request
        order, duplicate inputs return duplicate rows, and each item is charged one batch item
        unit before execution. A wallet address this API does not track yet returns data with
        sync_status "unknown", matching the ...
        """
        result: BatchGetTradersResponse = await self._call("batchGetTraders", path_params={}, query={}, body=body)
        return result

    @overload
    async def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetPositionTimelineResponse: ...

    @overload
    async def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetPositionTimelineResponse | NotModifiedResponse: ...

    async def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetPositionTimelineResponse | NotModifiedResponse:
        """Get a trader's position timeline for one market.

        ``GET /api/v1/trader/{address}/position-timeline`` (operationId ``getPositionTimeline``).

        Returns every stored Polymarket fill for one tracked trader in one market, newest first,
        with outcome-specific running_amount and running_avg_price including all earlier stored
        fills before pagination. Fills come from the full fill ledger, the same rows the trade
        export serves, at any date (#33245; ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            condition_id: Required. Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        result: GetPositionTimelineResponse | NotModifiedResponse = await self._call("getPositionTimeline", path_params={"address": address}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: None = None,
    ) -> GetTraderCategoryRecordsResponse: ...

    @overload
    async def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: str | None,
    ) -> GetTraderCategoryRecordsResponse | NotModifiedResponse: ...

    async def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: str | None = None,
    ) -> GetTraderCategoryRecordsResponse | NotModifiedResponse:
        """Get trader category win records.

        ``GET /api/v1/trader/{address}/categories`` (operationId ``getTraderCategoryRecords``).

        Returns one wallet's win record in every canonical category it has a settled market in:
        wins, decided (wins plus losses) and the rate, per category, busiest category first.
        These are the same counts the Pick of the Day holder chips carry. The Esports record
        also carries games: the wallet's record ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            category: Filter to one canonical category, matched through the same rollup every other category surface uses: soccer, EPL and champions league all reach Soccer, every ...
        """
        result: GetTraderCategoryRecordsResponse | NotModifiedResponse = await self._call("getTraderCategoryRecords", path_params={"address": address}, query={"category": category}, if_none_match=if_none_match)
        return result

    async def get_trader_pnl(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        sections: list[Literal["entries", "stats", "monthly", "year_totals", "drawdown"]] | None = None,
    ) -> GetTraderPnlResponse:
        """Get trader P&L time series.

        ``GET /api/v1/trader/{address}/pnl`` (operationId ``getTraderPnl``).

        Returns a trader's sports and esports daily P&L time series and pre-derived stats:
        entries (daily realized P&L and its running sum), period stats (all/90d/30d/7d), monthly
        aggregation, per-year totals, the drawdown series, series_status, and realized, which
        reconciles the days with the wallet's ...

        Query parameters:
            from_: Inclusive UTC calendar-date lower bound in YYYY-MM-DD form for the daily series (entries and drawdown). Omit for the whole stored history. A value that is not ...
            to: Inclusive UTC calendar-date upper bound in YYYY-MM-DD form for the daily series (entries and drawdown). Omit for the whole stored history. A value that is not ...
            sections: Which sections of the object to return. Repeatable and comma-separated: entries, stats, monthly, year_totals, drawdown. Omit it, or send it empty, for all ...
        """
        result: GetTraderPnlResponse = await self._call("getTraderPnl", path_params={"address": address}, query={"from": from_, "to": to, "sections": sections})
        return result

    @overload
    async def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetPositionTimelineResponse: ...

    @overload
    async def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetPositionTimelineResponse | NotModifiedResponse: ...

    async def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetPositionTimelineResponse | NotModifiedResponse:
        """Get a trader's position timeline (unified identity resolver).

        ``GET /api/v1/traders/{trader}/position-timeline`` (operationId ``getPositionTimelineById``).

        Unified trader-timeline route (#4975). {trader} accepts all five identity shapes - 0x...
        wallet, username, trd_-prefixed trader id, bare integer id, and @username (a username
        lookup only, for all-digit usernames) - resolved by the single shared trader-identity
        resolver. Returns every stored ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            condition_id: Required. Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        result: GetPositionTimelineResponse | NotModifiedResponse = await self._call("getPositionTimelineById", path_params={"trader": trader}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: None = None,
    ) -> ListPropsResponse: ...

    @overload
    async def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: str | None,
    ) -> ListPropsResponse | NotModifiedResponse: ...

    async def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: str | None = None,
    ) -> ListPropsResponse | NotModifiedResponse:
        """List player props across a league.

        ``GET /api/v1/props`` (operationId ``listProps``).

        Player props for the catalog's games of one league, one row per market, ordered by game
        slug, stat, player and line. NFL files props on a game's -player-props and -first-td-
        scorer child events and NBA on the game event; this reads both, so a caller does not
        walk GET /api/v1/games and then each ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            league: Required. League tag as GET /api/v1/games coverage.leagues spells it, for example nfl or nba. Matched case-insensitively.
            starts_after: RFC 3339 kickoff bound. A game with no published kickoff is excluded whenever either bound is set.
            starts_before: RFC 3339 kickoff bound, inclusive.
            player: Part of player.name, ignoring case and accents: jokic matches Nikola Jokić. A row with no player does not match.
            stat: Provider sportsMarketType values to keep, case-insensitive, for example passing_yards or points. Repeat the parameter or send a comma-separated list. An ...
            status: active (default), closed, or all. closed means the provider closed the market or it resolved.
            max_spread_c: Keep only props with an outcome whose cached best ask less best bid is at most this many cents: above 0, at most 100, in steps of 0.01. The books are the ones ...
            min_book_usd_within_2c: Keep only props with an outcome whose cached book holds at least this many USD on each side within 2 cents of its midpoint: bids at or above the midpoint minus ...
            limit: Page size. Out-of-range values are clamped to 1..200.
            cursor: Opaque prp_v1_ cursor from next_cursor, sent with the same filters. A cursor this endpoint did not issue returns 400 with error.param=cursor.
            expand: quotes adds each outcome's cached quote, as on GET /api/v1/games/{event_slug}/markets; it adds 1 to the cost, on every plan. Repeatable: quotes.
        """
        result: ListPropsResponse | NotModifiedResponse = await self._call("listProps", path_params={}, query={"league": league, "starts_after": starts_after, "starts_before": starts_before, "player": player, "stat": stat, "status": status, "max_spread_c": max_spread_c, "min_book_usd_within_2c": min_book_usd_within_2c, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    async def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: None = None,
    ) -> ListPositionsResponse: ...

    @overload
    async def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: str | None,
    ) -> ListPositionsResponse | NotModifiedResponse: ...

    async def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: str | None = None,
    ) -> ListPositionsResponse | NotModifiedResponse:
        """List current positions (positions-board feed).

        ``GET /api/v1/positions`` (operationId ``listPositions``).

        Returns the current positions-board feed backed by the wallet_positions mirror. Ordered
        by current_value_usd DESC with deterministic (wallet, condition_id, outcome_index)
        tiebreakers. Pre-reconcile rows (current_value_usd IS NULL) are excluded. Positions on
        resolved markets are excluded: a position ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of current positions to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            consistency: live (default) reads the current value-ordered board. snapshot requires wallet and freezes up to 500 matching rows and 2 MB for up to five minutes. Keep ...
            min_size: Minimum current position value in USD. Defaults to 100 when omitted, or to 0 when wallet is present; send 0 to include every reconciled position.
            category: Exact match against provider-backed market_canonical.category. Sports and esports only (#27311): a category outside them returns 400 bad_request with param ...
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id emitted by V1 responses. Combine with min_size=0 for every reconciled ...
            wallet: Scope to one wallet or a book of wallets (repeatable, up to 25 per request; comma-separated values inside one occurrence also work). Each value is a wallet ...
            min_grade: Minimum trader grade allowlist. `A` matches S and A; `B` matches S, A, B; etc.
            side: Filter by the binary outcome side. `yes` maps to outcome_index=0, `no` to outcome_index=1.
        """
        result: ListPositionsResponse | NotModifiedResponse = await self._call("listPositions", path_params={}, query={"limit": limit, "cursor": cursor, "consistency": consistency, "min_size": min_size, "category": category, "condition_id": condition_id, "wallet": wallet, "min_grade": min_grade, "side": side}, if_none_match=if_none_match)
        return result

    async def list_large_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        condition_id: str | None = None,
    ) -> ListLargePositionsResponse:
        """List large positions.

        ``GET /api/v1/large-positions`` (operationId ``listLargePositions``).

        Returns the largest current open positions from graded traders, value-descending, with
        opaque cursor pagination. This is a change-detection feed, not a holder list: a row
        needs a current value of at least 50,000 USD and a live detection in the last 24 hours,
        so a wallet that holds a market without ...

        Query parameters:
            limit: Maximum number of large positions to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque pagination cursor from a previous response.
            min_size: Minimum position value in USD. Raises the feed's own floor of 50,000 USD; a smaller value does not lower it.
            category: One RFC 4180 CSV record of exact current provider-backed market_canonical.category values. Legacy unquoted lists such as NBA,WNBA remain valid; values ...
            min_grade: Minimum trader grade. Matched against the trader.grade each row returns, the wallet's current grade, so every row listed shows a grade at or above this floor.
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id (round-trips a value from a list response). Must be 0x followed by 64 ...
        """
        result: ListLargePositionsResponse = await self._call("listLargePositions", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "condition_id": condition_id})
        return result

    @overload
    async def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListLargeTradesResponse: ...

    @overload
    async def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListLargeTradesResponse | NotModifiedResponse: ...

    async def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListLargeTradesResponse | NotModifiedResponse:
        """List large trades.

        ``GET /api/v1/large-trades`` (operationId ``listLargeTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of recent large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade now (trader.grade), the wallet's grade when this page is read, not when the trade filled. A wallet re-graded after a trade enters or ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            since: Return only the trades recorded after this one. Pass the id of a large trade this API returned (wt_<n>, or the bare integer). The answer keeps the list shape ...
            condition_id: Only this market's large trades: an exact raw provider condition_id. The page is read from the market's own index, newest first, and pages with cursor; it ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListLargeTradesResponse | NotModifiedResponse = await self._call("listLargeTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "min_market_volume_share": min_market_volume_share, "sort": sort, "since": since, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListWhaleTradesResponse: ...

    @overload
    async def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListWhaleTradesResponse | NotModifiedResponse: ...

    async def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListWhaleTradesResponse | NotModifiedResponse:
        """List whale trades.

        ``GET /api/v1/whale-trades`` (operationId ``listWhaleTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of recent large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade now (trader.grade), the wallet's grade when this page is read, not when the trade filled. A wallet re-graded after a trade enters or ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            since: Return only the trades recorded after this one. Pass the id of a large trade this API returned (wt_<n>, or the bare integer). The answer keeps the list shape ...
            condition_id: Only this market's large trades: an exact raw provider condition_id. The page is read from the market's own index, newest first, and pages with cursor; it ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListWhaleTradesResponse | NotModifiedResponse = await self._call("listWhaleTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "min_market_volume_share": min_market_volume_share, "sort": sort, "since": since, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListLargeTradeHistoryResponse: ...

    @overload
    async def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListLargeTradeHistoryResponse | NotModifiedResponse: ...

    async def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListLargeTradeHistoryResponse | NotModifiedResponse:
        """Replay historical large trades.

        ``GET /api/v1/large-trades/history`` (operationId ``listLargeTradeHistory``).

        Returns historical large trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of historical large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD. The capture floor was 3,000 USD before 2026-07-06 and 10,000 USD from then (1,000 USD in earnings markets), so 10000 gives one size ...
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, username, or trd_-prefixed trader ID, resolved against the traders table. Unknown traders return an ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade as of today (trader.grade), not at trade time. On a historical window it selects wallets by a grade they may have earned after the trade; ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListLargeTradeHistoryResponse | NotModifiedResponse = await self._call("listLargeTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to, "min_market_volume_share": min_market_volume_share, "sort": sort, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListWhaleTradeHistoryResponse: ...

    @overload
    async def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListWhaleTradeHistoryResponse | NotModifiedResponse: ...

    async def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListWhaleTradeHistoryResponse | NotModifiedResponse:
        """Replay historical whale trades.

        ``GET /api/v1/whale-trades/history`` (operationId ``listWhaleTradeHistory``).

        Returns historical whale trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of historical large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD.
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, or username resolved against the traders table. Unknown traders return an empty list.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade.
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListWhaleTradeHistoryResponse | NotModifiedResponse = await self._call("listWhaleTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to, "min_market_volume_share": min_market_volume_share, "sort": sort, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> GetLargeTradeResponse: ...

    @overload
    async def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> GetLargeTradeResponse | NotModifiedResponse: ...

    async def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetLargeTradeResponse | NotModifiedResponse:
        """Get large trade by ID.

        ``GET /api/v1/large-trades/{id}`` (operationId ``getLargeTrade``).

        Returns one large trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetLargeTradeResponse | NotModifiedResponse = await self._call("getLargeTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> GetWhaleTradeResponse: ...

    @overload
    async def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> GetWhaleTradeResponse | NotModifiedResponse: ...

    async def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetWhaleTradeResponse | NotModifiedResponse:
        """Get whale trade by ID.

        ``GET /api/v1/whale-trades/{id}`` (operationId ``getWhaleTrade``).

        Returns one whale trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses. Deprecated alias of GET /api/v1/large-trades/{id}, kept live
        until its sunset on 2027-02-01 (#16304, #29351); every response carries `Deprecation:
        @1790132400` (RFC 9745, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetWhaleTradeResponse | NotModifiedResponse = await self._call("getWhaleTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    async def list_large_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListLargeTradeCounterpartyExecutionsResponse:
        """Page counterparty executions.

        ``GET /api/v1/large-trades/{id}/counterparties/executions`` (operationId ``listLargeTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by large-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail.

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the large trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ListLargeTradeCounterpartyExecutionsResponse = await self._call("listLargeTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    async def list_whale_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListLargeTradeCounterpartyExecutionsResponse:
        """Page counterparty executions.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions`` (operationId ``listWhaleTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by whale-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail. Deprecated alias of GET /api/v1/large-
        trades/{id}/counterparties/executions, kept live until its sunset on ...

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ListLargeTradeCounterpartyExecutionsResponse = await self._call("listWhaleTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    async def list_large_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListLargeTradeCounterpartyMakersResponse:
        """Page maker counterparties.

        ``GET /api/v1/large-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listLargeTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages.

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the large trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ListLargeTradeCounterpartyMakersResponse = await self._call("listLargeTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    async def list_whale_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListLargeTradeCounterpartyMakersResponse:
        """Page maker counterparties.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listWhaleTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages. Deprecated alias of GET /api/v1/large-
        trades/{id}/counterparties/executions/{execution_id}/makers, kept live until its sunset
        on 2027-02-01 (#16304, #29351); every response ...

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ListLargeTradeCounterpartyMakersResponse = await self._call("listWhaleTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    @overload
    async def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: None = None,
    ) -> ListLeaderboardResponse: ...

    @overload
    async def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: str | None,
    ) -> ListLeaderboardResponse | NotModifiedResponse: ...

    async def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: str | None = None,
    ) -> ListLeaderboardResponse | NotModifiedResponse:
        """Get trader leaderboard.

        ``GET /api/v1/leaderboard`` (operationId ``listLeaderboard``).

        Returns ranked traders (grades S/A/B), by default in the board's own order: score
        descending, with a fixed tiebreak so the order never changes between reads of one
        ranking generation. sort, dir and activity reorder and scope the same wallets the way
        the site's leaderboard does (since 2026-11-02, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of ranked traders to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque lbv1_ pagination cursor from a prior response. It binds the finite score/address boundary to the effective category/strategy filters, and on a sorted ...
            category: Filter by category: a sport or esports bucket, matched case-insensitively. League values fold into their sport (NBA and NCAAB into Basketball, NFL into ...
            strategy: Filter by observed trading style. Current styles: two_sided, category_focused, high_activity, diversified, mixed, unclassified. Current styles count the ...
            sort: Order of the list, the sort columns of the site's leaderboard (/skill-leaderboard). rank (default) is the board's own order, the rank the site and the trader ...
            dir: Direction of sort. Omitted, each sort reads in its natural direction: rank 1 first for rank (asc), largest first for every other sort (desc). The opposite ...
            activity: Limit the list to wallets by recent trading, the site leaderboard's split. active: the wallet's last trade, as its current grade recorded it and aged to today, ...
        """
        result: ListLeaderboardResponse | NotModifiedResponse = await self._call("listLeaderboard", path_params={}, query={"limit": limit, "cursor": cursor, "category": category, "strategy": strategy, "sort": sort, "dir": dir, "activity": activity}, if_none_match=if_none_match)
        return result

    @overload
    async def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: None = None,
    ) -> GetPickOfTheDayResponse: ...

    @overload
    async def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: str | None,
    ) -> GetPickOfTheDayResponse | NotModifiedResponse: ...

    async def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayResponse | NotModifiedResponse:
        """Get today's or a past day's Pick of the Day.

        ``GET /api/v1/pick-of-the-day`` (operationId ``getPickOfTheDay``).

        Returns entitled published picks for the current product day, or for the past product
        day named by `date`. Pro includes five selections in total: the designated free
        selection and the first four non-free selections in publication order. Max opens every
        available selection, up to twenty-five. A day ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            date: A product day (America/New_York) in YYYY-MM-DD format, on or before today. Omit it, or send today, for the current read. A past day with no published pick ...
            view: full (default) is the whole recorded set: every pick with its holders, lead backer, sports context, thesis and entry_authorization, and the top-level copy of ...
            pick_id: One entitled published pick of the day, by its stable decimal-string pick_id. The body carries that pick once, as picks[0], beside state, pick_date and ...
        """
        result: GetPickOfTheDayResponse | NotModifiedResponse = await self._call("getPickOfTheDay", path_params={}, query={"date": date, "view": view, "pick_id": pick_id}, if_none_match=if_none_match)
        return result

    @overload
    async def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetPickOfTheDayArchiveResponse: ...

    @overload
    async def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetPickOfTheDayArchiveResponse | NotModifiedResponse: ...

    async def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayArchiveResponse | NotModifiedResponse:
        """Get the Pick of the Day track record.

        ``GET /api/v1/pick-of-the-day/archive`` (operationId ``getPickOfTheDayArchive``).

        Returns published picks that have not been withdrawn, with their outcome, modeled
        return, unit score, closing-line value, and cumulative record. Resolved game details and
        results are public. For unauthorized unresolved selections, game identity, category,
        image, publication time, and backed facts ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: full (default) is every row with every field, plus days and hit_rate with its per-pick series. summary returns view, hit_rate without series, one page of short ...
            limit: Rows per page of picks, 1 to 200, default 50. An integer outside that range is clamped into it, like every list limit, and X-Effective-Query reports the limit ...
            cursor: The page.next_cursor of the previous page: the rows after it, newest first. A cursor is a position in the record, so a pick published while you page does not ...
        """
        result: GetPickOfTheDayArchiveResponse | NotModifiedResponse = await self._call("getPickOfTheDayArchive", path_params={}, query={"view": view, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: None = None,
    ) -> GetPickOfTheDayStatsResponse: ...

    @overload
    async def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: str | None,
    ) -> GetPickOfTheDayStatsResponse | NotModifiedResponse: ...

    async def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayStatsResponse | NotModifiedResponse:
        """Get the Pick of the Day track-record breakdown.

        ``GET /api/v1/pick-of-the-day/stats`` (operationId ``getPickOfTheDayStats``).

        The figures behind the stats page, computed from the same rows the archive publishes:
        the hit rate, the win rate the market expected at publication, flat-stake outcome stats
        (drawdown, rolling form, profit factor, concentration), and buckets by day, sport,
        category, access group, month, entry-price ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: full (default) is every section. summary returns view, sections and every section except the five that grow with the record: series, days, categories, months ...
            sections: Exactly the sections to return, in the body's order whatever the request order. Repeatable and comma-separated: hit_rate, series, market_expectations, ...
        """
        result: GetPickOfTheDayStatsResponse | NotModifiedResponse = await self._call("getPickOfTheDayStats", path_params={}, query={"view": view, "sections": sections}, if_none_match=if_none_match)
        return result

    @overload
    async def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: None = None,
    ) -> GetPickOfTheDayLedgerResponse: ...

    @overload
    async def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: str | None,
    ) -> GetPickOfTheDayLedgerResponse | NotModifiedResponse: ...

    async def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayLedgerResponse | NotModifiedResponse:
        """Get the Pick of the Day commitment ledger.

        ``GET /api/v1/pick-of-the-day/ledger`` (operationId ``getPickOfTheDayLedger``).

        Returns the pre-game commitment for every published pick, so the public track record can
        be checked by someone who was not watching when the pick dropped. One entry per
        (pick_date, pick_rank), ascending by pick_date then pick_rank, in one of three states.
        `sealed` is an unresolved pick: the hash, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetPickOfTheDayLedgerResponse | NotModifiedResponse = await self._call("getPickOfTheDayLedger", path_params={}, query={}, if_none_match=if_none_match)
        return result

    async def list_trending_wallets(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        window: Literal["7d", "30d"] | None = None,
    ) -> ListTrendingWalletsResponse:
        """List trending wallets.

        ``GET /api/v1/leaderboard/trending`` (operationId ``listTrendingWallets``).

        Returns wallets ranked by Polymarket weekly/monthly P&L (Polymarket-only discovery),
        with opaque page-cursor pagination. trending_pnl_usd and the by-PNL row order come from
        Polymarket's canonical leaderboard (data-
        api.polymarket.com/v2/leaderboard?time_period=week|month&sort_by=PNL), not a locally ...

        Query parameters:
            limit: Polymarket's weekly leaderboard caps the ranked set at 50 wallets; requests above 50 still return at most 50. Out-of-range values are clamped to 1..50.
            cursor: Opaque pagination cursor from a previous response, bound to its effective limit, window and ranked-board generation. A changed board or request scope returns ...
            window: Trailing window.
        """
        result: ListTrendingWalletsResponse = await self._call("listTrendingWallets", path_params={}, query={"limit": limit, "cursor": cursor, "window": window})
        return result

    @overload
    async def list_leaderboard_leagues(
        self,
        *,
        if_none_match: None = None,
    ) -> ListLeaderboardLeaguesResponse: ...

    @overload
    async def list_leaderboard_leagues(
        self,
        *,
        if_none_match: str | None,
    ) -> ListLeaderboardLeaguesResponse | NotModifiedResponse: ...

    async def list_leaderboard_leagues(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ListLeaderboardLeaguesResponse | NotModifiedResponse:
        """List the leagues that have a leaderboard.

        ``GET /api/v1/leaderboard/leagues`` (operationId ``listLeaderboardLeagues``).

        Every league with its own skill leaderboard, grouped by sport, most ranked wallets
        first. Each row's `sport` and `slug` are the `{sport}` path segment and `league` value
        of GET /api/v1/leaderboard/sports/{sport}. A league is listed once its edge sort ranks
        at least `min_ranked` wallets. 503 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ListLeaderboardLeaguesResponse | NotModifiedResponse = await self._call("listLeaderboardLeagues", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> GetSportLeaderboardResponse: ...

    @overload
    async def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> GetSportLeaderboardResponse | NotModifiedResponse: ...

    async def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> GetSportLeaderboardResponse | NotModifiedResponse:
        """Get a sport or league leaderboard.

        ``GET /api/v1/leaderboard/sports/{sport}`` (operationId ``getSportLeaderboard``).

        One sport's skill leaderboard, or with `league` one league's, the board the site's sport
        pages show. Wallets need `min_resolved` resolved markets in the sport or league.
        `sort=edge` (the default) ranks `edge_skill`, the edge over the price paid pulled toward
        the board's `edge_average` by how much ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            league: A league slug of the sport, for example premier-league or cs2, from GET /api/v1/leaderboard/leagues. Omit it for the sport board.
            sort: Ranking axis. Any other value returns 400 bad_request with error.param=sort.
            limit: Rows to return from the top of the board. Out-of-range values are clamped to 1..100.
        """
        result: GetSportLeaderboardResponse | NotModifiedResponse = await self._call("getSportLeaderboard", path_params={"sport": sport}, query={"league": league, "sort": sort, "limit": limit}, if_none_match=if_none_match)
        return result

    @overload
    async def list_category_leaders(
        self,
        *,
        if_none_match: None = None,
    ) -> ListCategoryLeadersResponse: ...

    @overload
    async def list_category_leaders(
        self,
        *,
        if_none_match: str | None,
    ) -> ListCategoryLeadersResponse | NotModifiedResponse: ...

    async def list_category_leaders(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ListCategoryLeadersResponse | NotModifiedResponse:
        """List every category's top edge leaders.

        ``GET /api/v1/leaderboard/categories`` (operationId ``listCategoryLeaders``).

        Every sports and esports category's top three edge leaders in one read, the board the
        site's categories index shows. In each category, wallets are ranked as GET
        /api/v1/leaderboard/categories/{slug} ranks them, by the 95% lower bound of their edge
        over the price they paid; only wallets whose lower ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ListCategoryLeadersResponse | NotModifiedResponse = await self._call("listCategoryLeaders", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetCategoryLeaderboardResponse: ...

    @overload
    async def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetCategoryLeaderboardResponse | NotModifiedResponse: ...

    async def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetCategoryLeaderboardResponse | NotModifiedResponse:
        """Get a category's edge leaderboard.

        ``GET /api/v1/leaderboard/categories/{slug}`` (operationId ``getCategoryLeaderboard``).

        One sports or esports category's edge leaderboard, the board the site's category pages
        show. Wallets are ranked by edge_lower_bound, the 95% lower bound of their edge over the
        price they paid in the category, counted over independent events (independent_events
        breaks ties, then the wallet). Only ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            active_within: Keep wallets that traded in the category within this window. all (the default) keeps every ranked wallet.
            min_events: Independent events a wallet needs in the category to be listed. The site offers 0, 50, 100 and 250. Clamped to 0..1000000.
            limit: Maximum number of leaders to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque cel_ pagination cursor from a prior response. It binds the lower-bound/independent-event/wallet boundary to the committed category-skill ranking and to ...
        """
        result: GetCategoryLeaderboardResponse | NotModifiedResponse = await self._call("getCategoryLeaderboard", path_params={"slug": slug}, query={"active_within": active_within, "min_events": min_events, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    async def search_markets(
        self,
        *,
        q: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        category: str | None = None,
    ) -> SearchMarketsResponse:
        """Search markets.

        ``GET /api/v1/markets/search`` (operationId ``searchMarkets``).

        Search prediction markets by keyword. Returns one representative market per matching
        event, preferring the market whose title is q, then a winner market over a spread, total
        or prop, with status, category, platform metadata and the event_slug. Cursor pagination
        advances over grouped market results ...

        Query parameters:
            q: Required. Search query. Must be 2-512 characters before whitespace trimming and hold at least 2 letters or digits after trimming; a query with fewer letters or digits ...
            limit: Maximum number of matching markets to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            status: Filter by market status. A market is closed once Polymarket has closed trading or it has resolved, and active otherwise; all returns both.
            category: Filter by category. Sports and esports only (#27411): a category outside them returns 400 bad_request with param category and names the accepted buckets. The ...
        """
        result: SearchMarketsResponse = await self._call("searchMarkets", path_params={}, query={"q": q, "limit": limit, "cursor": cursor, "status": status, "category": category})
        return result

    async def search_content(
        self,
        *,
        q: str | None = None,
        limit: int | None = None,
    ) -> SearchContentResponse:
        """Search editorial content.

        ``GET /api/v1/content/search`` (operationId ``searchContent``).

        Search 0xinsider editorial content by keyword. Returns backend-owned learn, glossary,
        comparison, research, and trading-strategy items with canonical URLs. Opaque ranking
        scores are not exposed.

        Query parameters:
            q: Required. Search query. Must be 1-256 characters before whitespace trimming and non-empty after trimming.
            limit: Maximum content items to return. Out-of-range values are clamped to 1..50.
        """
        result: SearchContentResponse = await self._call("searchContent", path_params={}, query={"q": q, "limit": limit})
        return result

    @overload
    async def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ListSettledMarketsResponse: ...

    @overload
    async def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ListSettledMarketsResponse | NotModifiedResponse: ...

    async def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ListSettledMarketsResponse | NotModifiedResponse:
        """List settled game markets since a time.

        ``GET /api/v1/markets/settled`` (operationId ``listSettledMarkets``).

        Game markets Polymarket settled, as 0xinsider recorded them, oldest first by
        (settlement.observed_at, settlement_id): one row per market per settled state, the
        object the market_settled webhook delivers as data. It is the webhook's pull side: catch
        up after downtime from since, or poll with ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            since: RFC 3339 time, required without cursor. Rows whose settlement.observed_at is at or after it. With cursor, the cursor's position replaces it.
            sports_market_type: Comma-separated provider market types to keep, case-insensitive: moneyline, spreads, totals, a prop type; at most 64. Omitted: moneyline, or with cursor the ...
            league: Comma-separated leagues to keep, as the rows' league reports them (nba, epl, or pga for PGA Tour golf); at most 32, each starting with a letter and holding no ...
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque stl_v1_ cursor from next_cursor. It replaces since and keeps the filters it was issued for: a sports_market_type or league sent with it must match them, ...
        """
        result: ListSettledMarketsResponse | NotModifiedResponse = await self._call("listSettledMarkets", path_params={}, query={"since": since, "sports_market_type": sports_market_type, "league": league, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: None = None,
    ) -> ExploreMarketsResponse: ...

    @overload
    async def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: str | None,
    ) -> ExploreMarketsResponse | NotModifiedResponse: ...

    async def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: str | None = None,
    ) -> ExploreMarketsResponse | NotModifiedResponse:
        """Explore markets.

        ``GET /api/v1/markets/explore`` (operationId ``exploreMarkets``).

        Browse whale-active titled markets with category, platform, status, and keyword filters.
        Explore is Polymarket-only: the platform parameter is accepted for backward-
        compatibility but every request returns Polymarket markets. Paginates visible discovery
        entries rather than raw market rows, returns ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            status: Filter by market status. A market is closed once Polymarket has closed trading or it has resolved, and active otherwise; all returns both.
            platform: Filter by source platform. Explore is Polymarket-only; polymarket is the only supported value and the parameter is accepted for backward-compatibility but does ...
            sort: Sort order for the discovery feed. `large_trades` ranks by large-trade activity; `whales` is its deprecated spelling and selects the same order until its ...
            cursor: Opaque pagination cursor from the previous response.
            limit: Page size. Out-of-range values are clamped to 1..48.
            q: Keyword search against market titles. At most 64 characters before whitespace trimming.
        """
        result: ExploreMarketsResponse | NotModifiedResponse = await self._call("exploreMarkets", path_params={}, query={"category": category, "status": status, "platform": platform, "sort": sort, "cursor": cursor, "limit": limit, "q": q}, if_none_match=if_none_match)
        return result

    @overload
    async def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListSmartMoneyFlowsResponse: ...

    @overload
    async def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListSmartMoneyFlowsResponse | NotModifiedResponse: ...

    async def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListSmartMoneyFlowsResponse | NotModifiedResponse:
        """List ranked sharp-money flows (deprecated alias).

        ``GET /api/v1/markets/smart-money-flows`` (operationId ``listSmartMoneyFlows``).

        Ranks sports and esports markets (#27306) by absolute net S/A/B-grade whale flow over a
        requested timeframe. Use this discovery endpoint to answer where sharp money is flowing
        before drilling into a specific market with /api/v1/market/{condition_id}/flow.
        Pagination is anchored by an opaque cursor ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp, normalized effective filters, ranking and aggregate collection ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
            condition_id: Only this market's flow: an exact raw provider condition_id. Cannot be combined with event_slug (400). An unknown market returns an empty list.
            event_slug: Only the markets of one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListSmartMoneyFlowsResponse | NotModifiedResponse = await self._call("listSmartMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ListSmartMoneyFlowsResponse: ...

    @overload
    async def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ListSmartMoneyFlowsResponse | NotModifiedResponse: ...

    async def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ListSmartMoneyFlowsResponse | NotModifiedResponse:
        """List ranked sharp-money flows.

        ``GET /api/v1/markets/sharp-money-flows`` (operationId ``listSharpMoneyFlows``).

        Canonical path for ranked sharp-money flows; /api/v1/markets/smart-money-flows remains
        live as a deprecated byte-identical alias of it. Ranks sports and esports markets
        (#27306) by absolute net S/A/B-grade whale flow over a requested timeframe. Use this
        discovery endpoint to answer where sharp ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp, normalized effective filters, ranking and aggregate collection ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
            condition_id: Only this market's flow: an exact raw provider condition_id. Cannot be combined with event_slug (400). An unknown market returns an empty list.
            event_slug: Only the markets of one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ListSmartMoneyFlowsResponse | NotModifiedResponse = await self._call("listSharpMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    async def get_coverage(
        self,
    ) -> GetCoverageResponse:
        """Which reads the API serves for Polymarket.

        ``GET /api/v1/coverage`` (operationId ``getCoverage``).

        Unauthenticated discovery endpoint that declares which V1 data surfaces the API serves
        for Polymarket, the one venue it covers. Every capability reports supported. Coverage is
        sports and esports markets only (#27299): a market outside them answers 404 not_found
        with error.reason ...
        """
        result: GetCoverageResponse = await self._call("getCoverage", path_params={}, query={})
        return result

    async def get_platforms(
        self,
    ) -> GetCoverageResponse:
        """Get platform capability matrix.

        ``GET /api/v1/platforms`` (operationId ``getPlatforms``).

        Deprecated since #16315: use GET /api/v1/coverage, which serves the same body. This path
        stays live until its sunset on 2027-02-01 (#29351) and answers with Deprecation, Sunset
        and successor Link headers; from that date it answers 410 Gone with error.code
        endpoint_retired. Unauthenticated discovery ...
        """
        result: GetCoverageResponse = await self._call("getPlatforms", path_params={}, query={})
        return result

    @overload
    async def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> GetMarketHoldersResponse: ...

    @overload
    async def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> GetMarketHoldersResponse | NotModifiedResponse: ...

    async def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketHoldersResponse | NotModifiedResponse:
        """List a market's graded holders.

        ``GET /api/v1/market/{condition_id}/holders`` (operationId ``getMarketHolders``).

        The graded holder roster of one market, the list a Pick of the Day shows for its market,
        for any Polymarket market: every S/A/B wallet with open shares on either outcome, from a
        complete provider holder scan, each with its shares, Polymarket's own currentValue for
        the leg, its grade, its win record ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            outcome: Keep holders netting one side. `all` (default) lists both.
            min_grade: Narrow within the graded cohort: `S` keeps S, `A` keeps S and A, `B` (default) keeps S, A and B. `C`, `D` and `F` are rejected with 400: the route lists the ...
            limit: Maximum holders per page. Out-of-range values are clamped to 1..100.
            cursor: Opaque pagination cursor from the previous response's next_cursor. New cursors carry an absolute next offset bound to normalized condition_id, outcome and ...
        """
        result: GetMarketHoldersResponse | NotModifiedResponse = await self._call("getMarketHolders", path_params={"condition_id": condition_id}, query={"outcome": outcome, "min_grade": min_grade, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> GetMarketTopHoldersResponse: ...

    @overload
    async def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> GetMarketTopHoldersResponse | NotModifiedResponse: ...

    async def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketTopHoldersResponse | NotModifiedResponse:
        """List a market's top holders, every grade.

        ``GET /api/v1/market/{condition_id}/top-holders`` (operationId ``getMarketTopHolders``).

        The largest holders of one market on each outcome, every grade from S to F and ungraded
        wallets included: the table the market's event page shows under Top holders. Each
        outcome lists up to 100 wallets, largest `shares` first, from Polymarket's holder board,
        with the provider's current value, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum holders per outcome. Out-of-range values are clamped to 1..100. `totals` covers the whole sample whatever the limit.
        """
        result: GetMarketTopHoldersResponse | NotModifiedResponse = await self._call("getMarketTopHolders", path_params={"condition_id": condition_id}, query={"limit": limit}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> GetMarketFlowResponse: ...

    @overload
    async def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> GetMarketFlowResponse | NotModifiedResponse: ...

    async def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketFlowResponse | NotModifiedResponse:
        """Get a market's flow and top positions.

        ``GET /api/v1/market/{condition_id}/flow`` (operationId ``getMarketFlow``).

        Canonical since #16312; GET /api/v1/market/{condition_id}/intel is its deprecated alias
        and serves the same body under object market_intel. One market's flow and top positions:
        the signed flow of every tracked large trade in the window (net_flow_usd and its YES or
        NO direction), the large-trade ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        result: GetMarketFlowResponse | NotModifiedResponse = await self._call("getMarketFlow", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> GetMarketIntelResponse: ...

    @overload
    async def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> GetMarketIntelResponse | NotModifiedResponse: ...

    async def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketIntelResponse | NotModifiedResponse:
        """Get market intelligence.

        ``GET /api/v1/market/{condition_id}/intel`` (operationId ``getMarketIntel``).

        Deprecated since #16312: use GET /api/v1/market/{condition_id}/flow, which serves the
        same body under object market_flow. This path stays live until its sunset on 2027-02-01
        (#29351), keeps object market_intel, and answers with Deprecation, Sunset and successor
        Link headers; from that date it ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        result: GetMarketIntelResponse | NotModifiedResponse = await self._call("getMarketIntel", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)
        return result

    async def batch_get_market_flow(
        self,
        body: BatchGetMarketFlowBody,
    ) -> BatchGetMarketFlowResponse:
        """Batch market flow.

        ``POST /api/v1/markets/flow/batch`` (operationId ``batchGetMarketFlow``).

        Returns each market's flow and top positions for 1-25 raw provider condition_id values.
        Results preserve request order, duplicate inputs return duplicate rows, and each item is
        charged one batch item unit before execution. Do not pass prefixed mkt_ IDs; use
        market.condition_id from search or ...
        """
        result: BatchGetMarketFlowResponse = await self._call("batchGetMarketFlow", path_params={}, query={}, body=body)
        return result

    async def batch_get_market_close(
        self,
        body: BatchGetMarketCloseBody,
    ) -> BatchGetMarketCloseResponse:
        """Batch market closing lines.

        ``POST /api/v1/markets/close/batch`` (operationId ``batchGetMarketClose``).

        Returns the closing line of 1-25 sports or esports markets in one request. Each ok
        item's data is the body GET /api/v1/market/{condition_id}/close returns for that market:
        status measured with both outcome legs, pending, or unavailable with unavailable_reason,
        judged at one clock for the whole ...
        """
        result: BatchGetMarketCloseResponse = await self._call("batchGetMarketClose", path_params={}, query={}, body=body)
        return result

    async def batch_get_market_intel(
        self,
        body: BatchGetMarketFlowBody,
    ) -> BatchGetMarketIntelResponse:
        """Batch market intelligence.

        ``POST /api/v1/markets/intel/batch`` (operationId ``batchGetMarketIntel``).

        Deprecated since #16312: use POST /api/v1/markets/flow/batch, which returns the same
        items under object market_flow_batch. This path stays live until its sunset on
        2027-02-01 (#29351), keeps object market_intel_batch, and answers with Deprecation,
        Sunset and successor Link headers; from that date ...
        """
        result: BatchGetMarketIntelResponse = await self._call("batchGetMarketIntel", path_params={}, query={}, body=body)
        return result

    @overload
    async def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: None = None,
    ) -> GetMarketSnapshotResponse: ...

    @overload
    async def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: str | None,
    ) -> GetMarketSnapshotResponse | NotModifiedResponse: ...

    async def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketSnapshotResponse | NotModifiedResponse:
        """Get market live snapshot.

        ``GET /api/v1/market/{condition_id}/snapshot`` (operationId ``getMarketSnapshot``).

        Provider-first market card snapshot with canonical identity, outcome labels, cached top-
        of-book when available, liquidity, live sports context, and explicit
        freshness/unavailable states.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            expand: Include trust metadata for current_price and spread_bps. Repeatable: trust.
        """
        result: GetMarketSnapshotResponse | NotModifiedResponse = await self._call("getMarketSnapshot", path_params={"condition_id": condition_id}, query={"expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: None = None,
    ) -> GetMarketCandlesResponse: ...

    @overload
    async def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: str | None,
    ) -> GetMarketCandlesResponse | NotModifiedResponse: ...

    async def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketCandlesResponse | NotModifiedResponse:
        """Get market OHLC price candles.

        ``GET /api/v1/market/{condition_id}/candles`` (operationId ``getMarketCandles``).

        Provider-first bucketed OHLC price candles for a market's outcome tokens, derived from
        our stored copy of the Polymarket CLOB prices-history series (the same series the
        market-detail chart renders; covers open and resolved markets). Because the stored data
        is daily, a 1d bucket typically carries ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            resolution: Bucketing granularity. 1d aggregates by UTC calendar day, 1w by ISO week (Monday 00:00 UTC start). Defaults to 1d.
            from_: Exclusive lower bound as a URL-decoded unix timestamp in seconds; points at or before this timestamp are omitted (the underlying daily snapshot read filters ...
            to: Inclusive upper bound as a URL-decoded unix timestamp in seconds; points after this timestamp are omitted. If from is also present, from must be less than or ...
        """
        result: GetMarketCandlesResponse | NotModifiedResponse = await self._call("getMarketCandles", path_params={"condition_id": condition_id}, query={"resolution": resolution, "from": from_, "to": to}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: None = None,
    ) -> GetMarketCloseResponse: ...

    @overload
    async def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: str | None,
    ) -> GetMarketCloseResponse | NotModifiedResponse: ...

    async def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetMarketCloseResponse | NotModifiedResponse:
        """Get a market's closing line.

        ``GET /api/v1/market/{condition_id}/close`` (operationId ``getMarketClose``).

        The closing line of one sports or esports market: the price Polymarket's own price-
        history series recorded for each outcome in the last minute bucket that ended at or
        before kickoff (the market's game start time), read once after the market settles and
        stored unchanged. outcomes[0] is the YES leg ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetMarketCloseResponse | NotModifiedResponse = await self._call("getMarketClose", path_params={"condition_id": condition_id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ListMarketTradesResponse: ...

    @overload
    async def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ListMarketTradesResponse | NotModifiedResponse: ...

    async def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ListMarketTradesResponse | NotModifiedResponse:
        """List a market's taker fills in a time window.

        ``GET /api/v1/market/{condition_id}/trades`` (operationId ``listMarketTrades``).

        One market's taker fills of 100 USD or more, newest first by (traded_at,
        transaction_hash, log_index), from 0xinsider's own record of the exchange's on-chain
        fills. Each fill appears once: its id is the transaction hash and the log index of its
        fill event, so a walk can be deduplicated and joined ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            from_: Inclusive RFC 3339 lower bound on traded_at. Omitted or earlier than coverage.recorded_from: the walk runs to the start of the record (coverage.recorded_from). ...
            to: Exclusive RFC 3339 upper bound on traded_at. A first page ends at the earlier of to and coverage.complete_through. With cursor, it must match the cursor's.
            limit: Page size. Out-of-range values are clamped to 1..500.
            cursor: Opaque mtr_v1_ cursor from next_cursor. It continues the walk before the last fill of the previous page and keeps the market, from and to it was issued for: ...
        """
        result: ListMarketTradesResponse | NotModifiedResponse = await self._call("listMarketTrades", path_params={"condition_id": condition_id}, query={"from": from_, "to": to, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> GetMarketWalletsInOutResponse: ...

    @overload
    async def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> GetMarketWalletsInOutResponse | NotModifiedResponse: ...

    async def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> GetMarketWalletsInOutResponse | NotModifiedResponse:
        """Get a market's net buyers and sellers.

        ``GET /api/v1/market/{condition_id}/wallets-in-out`` (operationId ``getMarketWalletsInOut``).

        One market's net buyers and net sellers over the last 24 hours or 7 days, live: the body
        the 0xinsider market page's wallets in/out panel reads for a Pro viewer, from the same
        aggregate and cache (reads are cached for up to 60 seconds). A wallet's net is its buys
        minus its sells in the window ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            window: The window the nets are summed over, ending at the read's clock: 24h (the default) or 7d.
        """
        result: GetMarketWalletsInOutResponse | NotModifiedResponse = await self._call("getMarketWalletsInOut", path_params={"condition_id": condition_id}, query={"window": window}, if_none_match=if_none_match)
        return result

    @overload
    async def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: None = None,
    ) -> ListSuspiciousTradesResponse: ...

    @overload
    async def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None,
    ) -> ListSuspiciousTradesResponse | NotModifiedResponse: ...

    async def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None = None,
    ) -> ListSuspiciousTradesResponse | NotModifiedResponse:
        """Get suspicious trades.

        ``GET /api/v1/suspicious-trades`` (operationId ``listSuspiciousTrades``).

        Stored trades whose recorded suspicion score meets the live flag threshold. Evidence
        contains the scorer's stored signals. Cursor-paginated by suspicion score. mode=live
        (default) uses fresh cached pages; mode=stable pins pagination to one published scoring
        generation and returns cursor_expired ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of suspicious trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
            mode: Pagination mode. live (default) keeps the 120-second response cache; stable pins the walk to one published scoring generation and binds the cursor to the limit ...
        """
        result: ListSuspiciousTradesResponse | NotModifiedResponse = await self._call("listSuspiciousTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity, "mode": mode}, if_none_match=if_none_match)
        return result

    @overload
    async def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> GetSuspiciousTradeResponse: ...

    @overload
    async def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> GetSuspiciousTradeResponse | NotModifiedResponse: ...

    async def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetSuspiciousTradeResponse | NotModifiedResponse:
        """Get suspicious trade by ID.

        ``GET /api/v1/suspicious-trades/{id}`` (operationId ``getSuspiciousTrade``).

        Returns one suspicious trade by raw whale_alerts.id or the rf_-prefixed id emitted by
        list responses. A flag on a market outside sports and esports returns 404 not_found with
        error.reason=market_out_of_scope (#27305); stop requesting it. Canonical since
        2026-09-23; GET /api/v1/insider-radar/{id} is ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetSuspiciousTradeResponse | NotModifiedResponse = await self._call("getSuspiciousTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: None = None,
    ) -> ListGamesResponse: ...

    @overload
    async def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: str | None,
    ) -> ListGamesResponse | NotModifiedResponse: ...

    async def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: str | None = None,
    ) -> ListGamesResponse | NotModifiedResponse:
        """List covered games.

        ``GET /api/v1/games`` (operationId ``listGames``).

        One coherent game view per row: both sides with their provider ids and live scores, the
        UTC kickoff, the provider's own status, the esports series format, and the game's winner
        markets (the moneyline, or a soccer game's three 1X2 legs) with their condition ids and
        outcome token ids. Spreads, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            sport: Canonical sport bucket, case-insensitive, with - and _ read as a space: table-tennis and Table Tennis are the same bucket. Omit for every covered sport. A ...
            league: League tag, case-insensitive, as this list's coverage.leagues spells it (GET /api/v1/coverage lists no leagues): nfl, epl, cs2, euroleague, cbb, cwbb. ...
            status: Keep only games in this state. ended, cancelled and postponed also list finished games that have left the live board, read from their stored records, for ...
            starts_after: RFC 3339 instant. Keep only games whose kickoff is at or after it. Games with no published kickoff are excluded whenever either bound is set. With a finished ...
            starts_before: RFC 3339 instant. Keep only games whose kickoff is at or before it. Must be at or after starts_after.
            window: Which games to read. all, the default, lists the whole covered catalog, which can start with games the provider still holds open weeks after kickoff. now lists ...
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque gms_v1_ cursor from next_cursor. It pins the page position (kickoff and event_slug), not a snapshot: the catalog is live, so a game added or removed ...
            expand: sharp_money adds each game's sharp_money, the GameSharpMoney object GET /api/v1/games/{event_slug}/sharp-money returns, read from the sport board's cached ...
        """
        result: ListGamesResponse | NotModifiedResponse = await self._call("listGames", path_params={}, query={"sport": sport, "league": league, "status": status, "starts_after": starts_after, "starts_before": starts_before, "window": window, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    async def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: None = None,
    ) -> GetGameResponse: ...

    @overload
    async def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: str | None,
    ) -> GetGameResponse | NotModifiedResponse: ...

    async def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: str | None = None,
    ) -> GetGameResponse | NotModifiedResponse:
        """Get one game.

        ``GET /api/v1/games/{event_slug}`` (operationId ``getGame``).

        The same game object GET /api/v1/games returns, for one event_slug, including soccer 1X2
        home, draw and away market sides and draw_offered. The slug is the identity the
        live_sports_updated webhook pulse carries, so a receiver can read the full game straight
        from a pulse. A slug outside the ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetGameResponse | NotModifiedResponse = await self._call("getGame", path_params={"event_slug": event_slug}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: None = None,
    ) -> ListGameMarketsResponse: ...

    @overload
    async def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: str | None,
    ) -> ListGameMarketsResponse | NotModifiedResponse: ...

    async def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: str | None = None,
    ) -> ListGameMarketsResponse | NotModifiedResponse:
        """List a game's markets.

        ``GET /api/v1/games/{event_slug}/markets`` (operationId ``listGameMarkets``).

        Every stored Polymarket market of one event_slug: the moneyline, spreads, totals, team
        totals, half and quarter lines, player props and the rest, plus the markets of the
        event's child events (a soccer game's exact score, halftime result and more-markets
        events), each with its own event_slug. The ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            sports_market_type: Comma-separated provider market types to keep, case-insensitive: spreads, totals, points, first_half_totals. Omitted keeps every type. An unknown type returns ...
            status: active, closed or all. closed means the provider closed the market or it resolved.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque gmk_v1_ cursor from next_cursor, sent with the same filters. It pins the page position (sports_market_type, line, condition_id), not a snapshot. A ...
            expand: sharp_money adds each row's sharp_money: the game page's per-line split, side USD and S, A and B wallet counts per outcome. One read for the event whatever the ...
        """
        result: ListGameMarketsResponse | NotModifiedResponse = await self._call("listGameMarkets", path_params={"event_slug": event_slug}, query={"sports_market_type": sports_market_type, "status": status, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    async def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: None = None,
    ) -> GetGameSharpMoneyResponse: ...

    @overload
    async def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: str | None,
    ) -> GetGameSharpMoneyResponse | NotModifiedResponse: ...

    async def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: str | None = None,
    ) -> GetGameSharpMoneyResponse | NotModifiedResponse:
        """Get one game's sharp money.

        ``GET /api/v1/games/{event_slug}/sharp-money`` (operationId ``getGameSharpMoney``).

        Where the graded money sits on a whole game, in one read: the S, A and B grade wallets'
        USD on each outcome (home, away and, for a 1X2 game, draw) summed across the game's
        markets, each outcome's integer share, the leader and wallet counts by grade, with the
        backend's verdict on the split. It is ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetGameSharpMoneyResponse | NotModifiedResponse = await self._call("getGameSharpMoney", path_params={"event_slug": event_slug}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> ListGameTradesResponse: ...

    @overload
    async def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> ListGameTradesResponse | NotModifiedResponse: ...

    async def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> ListGameTradesResponse | NotModifiedResponse:
        """List a game's trades.

        ``GET /api/v1/games/{event_slug}/trades`` (operationId ``listGameTrades``).

        A game's newest fills across every market in it, newest first and live: the moneyline,
        spreads, totals and every prop, player props included. The same rows the 0xinsider game
        page's activity list shows a Pro viewer, read from the same live stream. Every fill, not
        only large ones: GET ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Newest fills to return. Out-of-range values are clamped to 1..200.
        """
        result: ListGameTradesResponse | NotModifiedResponse = await self._call("listGameTrades", path_params={"event_slug": event_slug}, query={"limit": limit}, if_none_match=if_none_match)
        return result

    async def get_game_holders(
        self,
        event_slug: str,
        *,
        condition_ids: list[str] | None = None,
        limit: int | None = None,
    ) -> GetGameHoldersResponse:
        """Get a game's holders.

        ``GET /api/v1/games/{event_slug}/holders`` (operationId ``getGameHolders``).

        The S, A and B graded holders of up to 25 markets of one game in one call. Each item is
        GET /api/v1/market/{condition_id}/holders for one market, unfiltered and cut to limit,
        with the same market, scan and totals beside it. Pass condition_ids from GET
        /api/v1/games/{event_slug}/markets; a market ...

        Query parameters:
            condition_ids: Required. 1 to 25 condition_id values of this game's markets, comma-separated. The key may also repeat (condition_ids=a&condition_ids=b). A raw provider condition_id or ...
            limit: Holders per market. Out-of-range values are clamped to 1..100.
        """
        result: GetGameHoldersResponse = await self._call("getGameHolders", path_params={"event_slug": event_slug}, query={"condition_ids": condition_ids, "limit": limit})
        return result

    @overload
    async def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: None = None,
    ) -> ListSuspiciousTradesResponse: ...

    @overload
    async def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None,
    ) -> ListSuspiciousTradesResponse | NotModifiedResponse: ...

    async def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None = None,
    ) -> ListSuspiciousTradesResponse | NotModifiedResponse:
        """Get insider radar flags.

        ``GET /api/v1/insider-radar`` (operationId ``listInsiderRadar``).

        Deprecated alias of GET /api/v1/suspicious-trades (2026-09-23), kept live until its
        sunset on 2027-02-01 (#29351); responses carry Deprecation, Sunset and a Link
        rel="successor-version" to it, and from that date the path answers 410 Gone with
        error.code endpoint_retired. Stored trades whose ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of radar flags to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
            mode: Pagination mode. live (default) keeps the 120-second response cache; stable pins the walk to one published scoring generation and binds the cursor to the limit ...
        """
        result: ListSuspiciousTradesResponse | NotModifiedResponse = await self._call("listInsiderRadar", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity, "mode": mode}, if_none_match=if_none_match)
        return result

    @overload
    async def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> GetInsiderRadarFlagResponse: ...

    @overload
    async def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> GetInsiderRadarFlagResponse | NotModifiedResponse: ...

    async def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetInsiderRadarFlagResponse | NotModifiedResponse:
        """Get insider radar flag by ID.

        ``GET /api/v1/insider-radar/{id}`` (operationId ``getInsiderRadarFlag``).

        Deprecated alias of GET /api/v1/suspicious-trades/{id} (2026-09-23), kept live until its
        sunset on 2027-02-01 (#29351); responses carry Deprecation, Sunset and a Link
        rel="successor-version" to it, and from that date the path answers 410 Gone with
        error.code endpoint_retired. The envelope keeps ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetInsiderRadarFlagResponse | NotModifiedResponse = await self._call("getInsiderRadarFlag", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    async def get_event_replay_since(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        trader: str | None = None,
        condition_id: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_size: float | str | None = None,
        expand: list[Literal["trade"]] | None = None,
    ) -> GetEventReplaySinceResponse:
        """Replay public large-trade events.

        ``GET /api/v1/events/feed/since`` (operationId ``getEventReplaySince``).

        Returns durable public large-trade events strictly after an opaque cursor, in commit
        order: events are ordered by the position at which their write became visible to every
        reader (whale_alerts.inserted_xid), then by whale_alerts.id, and a page never reaches
        past the oldest write transaction still ...

        Query parameters:
            cursor: Opaque event replay cursor returned as next_cursor by a prior response. The cursor maps to the global (whale_alerts.inserted_xid, whale_alerts.id) commit-order ...
            limit: Maximum durable public whale-trade events to return. Out-of-range values are clamped to 1..100.
            trader: Only this wallet's trades: a wallet address, trd_-prefixed trader id or username resolved against the traders table. Bound to the cursor: a cursor issued under ...
            condition_id: Only trades on this market: the raw provider condition_id or its mkt_-prefixed id. Bound to the cursor.
            min_grade: Only trades by wallets at this grade or better (S best), read from the wallet's newest ranking at request time; a wallet with no grade never passes. For the ...
            min_grade_at_trade: Only trades whose grade_at_trade, the grade the wallet held when the trade filled, is at this grade or better (S best). Only a trade whose grade at the fill is ...
            min_size: Only trades of at least this USD amount. Decimal and scientific query spellings normalize exactly to cents, rounding half away from zero; maximum 1e15 USD. ...
            expand: Repeatable. trade adds the public trade read to every event (the object GET /api/v1/whale-trades/{id} returns for it), from one query per page, so a page of ...
        """
        result: GetEventReplaySinceResponse = await self._call("getEventReplaySince", path_params={}, query={"cursor": cursor, "limit": limit, "trader": trader, "condition_id": condition_id, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "min_size": min_size, "expand": expand})
        return result

    async def list_webhooks(
        self,
    ) -> ListWebhooksResponse:
        """List builder webhook destinations.

        ``GET /api/v1/webhooks`` (operationId ``listWebhooks``).

        Returns webhook destinations owned by the authenticated API key user. Deleted endpoints
        are omitted; an endpoint paused with PATCH or disabled after consecutive failures is
        listed with status disabled. Subscribable event_types and their payload shapes are
        described by GET /api/v1/webhooks/events. ...
        """
        result: ListWebhooksResponse = await self._call("listWebhooks", path_params={}, query={})
        return result

    async def create_webhook(
        self,
        body: CreateWebhookRequest,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Create a builder webhook destination.

        ``POST /api/v1/webhooks`` (operationId ``createWebhook``).

        Creates a pending HTTPS webhook destination. The response includes one-time
        signing_secret and verification.token values. Deliveries are not sent until the endpoint
        is verified, and verification requires the destination to answer 2xx to a signed
        webhook.verification challenge (see POST ...
        """
        result: CreateWebhookResponse = await self._call("createWebhook", path_params={}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    async def list_webhook_events(
        self,
    ) -> ListWebhookEventsResponse:
        """List webhook event catalog.

        ``GET /api/v1/webhooks/events`` (operationId ``listWebhookEvents``).

        Self-describing catalog of every webhook event type: its description, data payload
        shape, and whether it is active (has a firing producer) or dormant (subscribable but not
        yet delivered; no event type is dormant today). The catalog is identical for every
        authenticated key and exposes no ...
        """
        result: ListWebhookEventsResponse = await self._call("listWebhookEvents", path_params={}, query={})
        return result

    async def list_webhook_deliveries(
        self,
        id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ListWebhookDeliveriesResponse:
        """List webhook delivery log.

        ``GET /api/v1/webhooks/{id}/deliveries`` (operationId ``listWebhookDeliveries``).

        Recent delivery attempts for one webhook destination owned by the authenticated API key
        user, newest first, with opaque cursor pagination. Returns 404 (identical to an unknown
        id) when the endpoint is not owned by the caller, so a non-owner cannot tell an owned-
        but-empty log apart from someone ...

        Query parameters:
            cursor: Opaque pagination cursor returned as next_cursor by a prior response. Omit to fetch the newest page.
            limit: Maximum delivery rows to return per page. Out-of-range values are clamped to 1..100.
        """
        result: ListWebhookDeliveriesResponse = await self._call("listWebhookDeliveries", path_params={"id": id}, query={"cursor": cursor, "limit": limit})
        return result

    async def redeliver_webhook_delivery(
        self,
        id: str,
        delivery_id: str,
        *,
        idempotency_key: str | None = None,
    ) -> RedeliverWebhookDeliveryResponse:
        """Redeliver a dead-lettered webhook delivery.

        ``POST /api/v1/webhooks/{id}/deliveries/{delivery_id}/redeliver`` (operationId ``redeliverWebhookDelivery``).

        Returns one dead_letter delivery to the delivery queue with a fresh attempt budget:
        status becomes pending, attempt_count resets to 0, and next_attempt_at is now, so the
        delivery worker claims it like any queued delivery, under the same per-owner and per-
        origin concurrency limits. Use it after a ...
        """
        result: RedeliverWebhookDeliveryResponse = await self._call("redeliverWebhookDelivery", path_params={"id": id, "delivery_id": delivery_id}, query={}, idempotency_key=idempotency_key)
        return result

    async def get_webhook(
        self,
        id: str,
    ) -> CreateWebhookResponse:
        """Get one builder webhook destination.

        ``GET /api/v1/webhooks/{id}`` (operationId ``getWebhook``).

        Returns one webhook destination owned by the authenticated API key user.
        """
        result: CreateWebhookResponse = await self._call("getWebhook", path_params={"id": id}, query={})
        return result

    async def update_webhook(
        self,
        id: str,
        body: UpdateWebhookRequest,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Update a builder webhook destination.

        ``PATCH /api/v1/webhooks/{id}`` (operationId ``updateWebhook``).

        Updates name, HTTPS URL, event types, or enabled state. URL changes force
        pending_verification and return a new verification token; the new destination must
        answer 2xx to the signed webhook.verification challenge before deliveries resume. A URL
        change returns 409 with ...
        """
        result: CreateWebhookResponse = await self._call("updateWebhook", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    async def delete_webhook(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Disable a builder webhook destination.

        ``DELETE /api/v1/webhooks/{id}`` (operationId ``deleteWebhook``).

        Soft-deletes a webhook destination owned by the authenticated API key user. Existing
        delivery audit rows remain retained.
        """
        result: CreateWebhookResponse = await self._call("deleteWebhook", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    async def verify_webhook(
        self,
        id: str,
        body: VerifyWebhookRequest,
    ) -> CreateWebhookResponse:
        """Verify a builder webhook destination.

        ``POST /api/v1/webhooks/{id}/verify`` (operationId ``verifyWebhook``).

        Activates a pending webhook destination. Two conditions must both hold: the one-time
        verification token matches and has not expired, AND the destination answers 2xx to a
        signed challenge this operation POSTs to the endpoint's stored url. The challenge body
        is ...
        """
        result: CreateWebhookResponse = await self._call("verifyWebhook", path_params={"id": id}, query={}, body=body)
        return result

    async def prepare_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Prepare a staged builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/prepare`` (operationId ``prepareWebhookSecret``).

        Creates a pending signing secret while the current secret remains active. Deploy the
        returned one-time signing_secret to the receiver before calling activate. The response
        exposes secret_rotation.status=pending; an existing pending secret is returned again so
        a lost response can be recovered safely.
        """
        result: CreateWebhookResponse = await self._call("prepareWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    async def activate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Activate a staged builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/activate`` (operationId ``activateWebhookSecret``).

        Promotes the prepared signing secret to current, returns it once, and signs every
        delivery with both the new and previous secrets for one hour. Call retire after the
        receiver has completed its rollout. The current secret remains available through the
        existing immediate rotate-secret route for ...
        """
        result: CreateWebhookResponse = await self._call("activateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    async def retire_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Retire the previous builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/retire`` (operationId ``retireWebhookSecret``).

        Ends the one-hour dual-signature overlap and removes the previous signing secret from
        future delivery authorization. Call this after the receiver accepts the activated
        secret. The operation is idempotent and does not return signing_secret.
        """
        result: CreateWebhookResponse = await self._call("retireWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    async def rotate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookResponse:
        """Rotate a builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret`` (operationId ``rotateWebhookSecret``).

        Rotates the endpoint signing secret and returns the new signing_secret once in the
        response. Returns 409 with error.reason=webhook_delivery_in_progress while a live
        delivery freezes the current signing nonce; retry after it completes.
        """
        result: CreateWebhookResponse = await self._call("rotateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    @overload
    async def get_health(
        self,
        *,
        if_none_match: None = None,
    ) -> GetHealthResponse: ...

    @overload
    async def get_health(
        self,
        *,
        if_none_match: str | None,
    ) -> GetHealthResponse | NotModifiedResponse: ...

    async def get_health(
        self,
        *,
        if_none_match: str | None = None,
    ) -> GetHealthResponse | NotModifiedResponse:
        """Health check.

        ``GET /api/v1/health`` (operationId ``getHealth``).

        Returns API health status. No authentication required. Limited to 120 requests per
        minute per IP.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetHealthResponse | NotModifiedResponse = await self._call("getHealth", path_params={}, query={}, if_none_match=if_none_match)
        return result

    async def create_mcp_json_rpc_response(
        self,
        body: CreateMcpJsonRpcResponseBody,
    ) -> CreateMcpJsonRpcResponseResponse:
        """Remote MCP endpoint (JSON-RPC).

        ``POST /api/v1/mcp`` (operationId ``createMcpJsonRpcResponse``).

        Model Context Protocol (MCP) Streamable HTTP transport. Accepts one JSON-RPC 2.0 request
        or notification. ID-bearing initialize, ping, tools/list, and tools/call requests (and
        server/discover on revision 2026-07-28) receive one same-ID JSON-RPC response; an
        unknown method, or a notification method ...
        """
        result: CreateMcpJsonRpcResponseResponse = await self._call("createMcpJsonRpcResponse", path_params={}, query={}, body=body)
        return result

    async def get_reports(
        self,
        *,
        granularity: Literal["daily", "weekly", "monthly"] | None = None,
        period: str | None = None,
    ) -> GetReportsResponse:
        """Unified report snapshot (granularity selector).

        ``GET /api/v1/reports`` (operationId ``getReports``).

        Unified convenience route (#4975) that consolidates the three singular report routes.
        Dispatches to the exact per-granularity cap (daily 50, weekly 100, monthly 200) and date
        window the legacy /api/v1/reports/{daily,weekly,monthly} routes use, so the response
        body is byte-identical to the matching ...

        Query parameters:
            granularity: Required. Report granularity selector.
            period: Required. Period token for the granularity. daily: UTC date YYYY-MM-DD. weekly: ISO week YYYY-WW for a durable canonical snapshot, or a from,to YYYY-MM-DD pair for an ...
        """
        result: GetReportsResponse = await self._call("getReports", path_params={}, query={"granularity": granularity, "period": period})
        return result

    async def get_daily_report_snapshot(
        self,
        *,
        date: str | None = None,
    ) -> GetReportsResponse:
        """Daily report snapshot.

        ``GET /api/v1/reports/daily`` (operationId ``getDailyReportSnapshot``).

        Returns a dated daily whale-activity report snapshot with source_range, snapshot.status,
        completeness, and reconciliation metadata. Report whale volume is local whale-alert
        activity volume, not provider lifetime trader volume.

        Query parameters:
            date: Required. UTC report date in YYYY-MM-DD format, from 2024-03-01 (the first day report data covers) through tomorrow UTC. Any other date returns 400 bad_request with ...
        """
        result: GetReportsResponse = await self._call("getDailyReportSnapshot", path_params={}, query={"date": date})
        return result

    async def get_weekly_report_snapshot(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        week: str | None = None,
    ) -> GetReportsResponse:
        """Weekly report snapshot.

        ``GET /api/v1/reports/weekly`` (operationId ``getWeeklyReportSnapshot``).

        Returns a weekly whale-activity report snapshot. Pass an ISO YYYY-WW token for a durable
        canonical snapshot, or an exact from/to UTC range of at most 31 inclusive days for an
        ephemeral response. The response identifies closed ranges as final and current ranges as
        rolling.

        Query parameters:
            from_: UTC source-range start in YYYY-MM-DD format; required with to. Together with to, selects an exact ephemeral range of at most 31 inclusive UTC days. A start ...
            to: UTC source-range end in YYYY-MM-DD format; required with from. Together with from, selects an exact ephemeral range of at most 31 inclusive UTC days. An end ...
            week: ISO week selector in YYYY-WW format; alternative to from/to. Selects a durable canonical snapshot. A week that ends before 2024-03-01, the first day report ...
        """
        result: GetReportsResponse = await self._call("getWeeklyReportSnapshot", path_params={}, query={"from": from_, "to": to, "week": week})
        return result

    async def get_monthly_report_snapshot(
        self,
        *,
        month: str | None = None,
    ) -> GetReportsResponse:
        """Monthly report snapshot.

        ``GET /api/v1/reports/monthly`` (operationId ``getMonthlyReportSnapshot``).

        Returns a UTC monthly whale-activity report snapshot with source_range, completeness,
        and reconciliation metadata.

        Query parameters:
            month: Required. UTC report month in YYYY-MM format. A month that ends before 2024-03-01, the first day report data covers, or starts after tomorrow UTC returns 400 bad_request ...
        """
        result: GetReportsResponse = await self._call("getMonthlyReportSnapshot", path_params={}, query={"month": month})
        return result

    @overload
    async def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: None = None,
    ) -> GetResolutionReportResponse: ...

    @overload
    async def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: str | None,
    ) -> GetResolutionReportResponse | NotModifiedResponse: ...

    async def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: str | None = None,
    ) -> GetResolutionReportResponse | NotModifiedResponse:
        """Get the daily resolution report.

        ``GET /api/v1/reports/resolutions`` (operationId ``getResolutionReport``).

        One UTC day's resolved markets: how often the side the profitable (S, A and B grade)
        wallets held won, beside how often every qualifying wallet's side won, one vote each.
        `markets` lists each market they held a position in, with the consensus side, its
        confidence, and the full roster of wallets, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            date: Required. UTC report date in YYYY-MM-DD format, no later than today UTC. Any other value returns 400 bad_request with error.param=date.
            view: `totals` returns the counts without `markets`. Any other value than full or totals returns 400 bad_request with error.param=view.
        """
        result: GetResolutionReportResponse | NotModifiedResponse = await self._call("getResolutionReport", path_params={}, query={"date": date, "view": view}, if_none_match=if_none_match)
        return result

    async def get_trader_export_snapshot(
        self,
        address: str,
    ) -> GetTraderExportSnapshotResponse:
        """Trader export snapshot metadata.

        ``GET /api/v1/trader/{address}/export`` (operationId ``getTraderExportSnapshot``).

        Returns export source-range, completeness, volume reconciliation, row-count estimate,
        and large-export policy for one trader. To download the full dataset programmatically,
        POST to this same path to submit an async export job (json | ndjson | csv), then poll
        the status route and follow the download ...
        """
        result: GetTraderExportSnapshotResponse = await self._call("getTraderExportSnapshot", path_params={"address": address}, query={})
        return result

    async def submit_trader_export(
        self,
        address: str,
        *,
        format: Literal["json", "ndjson", "csv"] | None = None,
        fresh: bool | None = None,
    ) -> TraderExportJob:
        """Submit a trader dataset export job.

        ``POST /api/v1/trader/{address}/export`` (operationId ``submitTraderExport``).

        Queues an async export of the trader's full dataset in the requested format (json
        default, ndjson, or csv) and returns the job resource. Poll the status route at
        poll_after_s until terminal is true, then follow the download route while status is
        'ready' (until expires_at, 24 hours from submit). ...

        Query parameters:
            format: Output serialization. json = full envelope document (default); ndjson = full envelope as line 1 then one trade object per line; csv = flat trades rows only.
            fresh: true: do not reuse a finished, running or reconciling job; only a queued job is reused, so the file is a snapshot read after this submit. Consumes quota when ...
        """
        result: TraderExportJob = await self._call("submitTraderExport", path_params={"address": address}, query={"format": format, "fresh": fresh})
        return result

    async def get_trader_export_status(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> TraderExportJob:
        """Poll a trader export job.

        ``GET /api/v1/trader/{address}/export/status`` (operationId ``getTraderExportStatus``).

        Returns the job resource for a submitted export: status (queued | running |
        cancel_requested | reconcile_required | ready | failed | expired | cancelled), terminal,
        next_action and poll_after_s, the lifecycle timestamps, the retention window
        (expires_at) and, once the file is written, data_as_of ...

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        result: TraderExportJob = await self._call("getTraderExportStatus", path_params={"address": address}, query={"job_id": job_id})
        return result

    async def cancel_trader_export(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> TraderExportJob:
        """Cancel a trader export job.

        ``POST /api/v1/trader/{address}/export/cancel`` (operationId ``cancelTraderExport``).

        Cancels a submitted export and returns the job resource, the same shape the status route
        returns. A queued job reads cancelled at once and no worker will start it. A running job
        reads cancel_requested until the worker reaches its next safe point, then cancelled: the
        worker checks every 5 seconds ...

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        result: TraderExportJob = await self._call("cancelTraderExport", path_params={"address": address}, query={"job_id": job_id})
        return result

    async def download_trader_export(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> AsyncDownload:
        """Download a finished trader export.

        ``GET /api/v1/trader/{address}/export/download`` (operationId ``downloadTraderExport``).

        Redirects (302) to a presigned URL lasting at most one hour and no later than the job's
        expires_at for the finished export file while the job status is 'ready' and expires_at
        has not passed. The file is gzip-compressed and served with the format's Content-Type
        (application/json, ...

        Returns an ``AsyncDownload``: the redirect is followed once, without the credential, and
        the file is streamed. Iterate it, ``asave(path)`` it for its SHA-256, or ``aread()`` it
        (bounded); ``aclose()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        return await self._download("downloadTraderExport", path_params={"address": address}, query={"job_id": job_id})

    async def get_usage(
        self,
    ) -> Usage:
        """Inspect current API usage without spending primary request quota.

        ``GET /api/v1/usage`` (operationId ``getUsage``).

        Returns the authenticated caller sliding-window request budget, UTC-day usage and
        monthly quota. This control-plane endpoint remains available for a valid credential
        after paid data access lapses and does not increment the primary Redis rate-limit
        counter, monthly quota or API usage table; it ...
        """
        result: Usage = await self._call("getUsage", path_params={}, query={})
        return result

    async def get_market_context_markdown(
        self,
        condition_id: str,
    ) -> str:
        """Get market context (Markdown).

        ``GET /api/v1/market/{condition_id}/context.md`` (operationId ``getMarketContextMarkdown``).

        Authenticated, self-contained Polymarket market evidence document. Renders the same
        typed data as the market snapshot with trust included: identity, outcome labels and
        tokens, cached quotes, liquidity, live sports, and per-source freshness or unavailable
        reasons. Provider text is encoded as ...
        """
        result: str = await self._call("getMarketContextMarkdown", path_params={"condition_id": condition_id}, query={})
        return result

    async def get_account_identity(
        self,
    ) -> AccountIdentity:
        """Identify the authenticated account and credential.

        ``GET /api/v1/me`` (operationId ``getAccountIdentity``).

        Returns caller-owned account and credential IDs, credential validity, paid-data
        entitlement and approved scopes. Null scopes mean full legacy developer-key access.
        Valid credentials can use this control-plane diagnostic path after paid access lapses;
        data routes still require active paid access. ...
        """
        result: AccountIdentity = await self._call("getAccountIdentity", path_params={}, query={})
        return result

    async def submit_whale_dataset(
        self,
        body: SubmitWhaleDatasetBody,
    ) -> WhaleDatasetJob:
        """Create an immutable whale dataset.

        ``POST /api/v1/datasets/whale-trades`` (operationId ``submitWhaleDataset``).

        Extract at most 1,000,000 rows and 256 MiB uncompressed; exceeding either bound fails
        the job and publishes no partial file. Window and filters freeze on admission; rows and
        source facts freeze on one worker database snapshot. NDJSON uses exact decimal strings,
        with no current grade or market ...
        """
        result: WhaleDatasetJob = await self._call("submitWhaleDataset", path_params={}, query={}, body=body)
        return result

    async def get_whale_dataset_status(
        self,
        job_id: str,
    ) -> WhaleDatasetJob:
        """Read a whale dataset job.

        ``GET /api/v1/datasets/whale-trades/{job_id}`` (operationId ``getWhaleDatasetStatus``).

        Read queued, running, cancel_requested, ready, failed, reconcile_required, expired or
        cancelled. Poll only while next_action is poll, after poll_after_s. Ready manifests
        contain count, content and compressed SHA-256, schema, filters, source, horizon, expiry
        and replay continuation. Deltas do not ...
        """
        result: WhaleDatasetJob = await self._call("getWhaleDatasetStatus", path_params={"job_id": job_id}, query={})
        return result

    async def download_whale_dataset(
        self,
        job_id: str,
    ) -> AsyncDownload:
        """Download an immutable whale dataset.

        ``GET /api/v1/datasets/whale-trades/{job_id}/download`` (operationId ``downloadWhaleDataset``).

        Download only a ready artifact; status handles failure and cancellation. Retired
        artifacts return 410 at serving time. Paid export scope; jobs are private to the
        credential owner. Shares the 20/day owner export quota and fair worker admission with
        trader exports; datasets also have a combined ...

        Returns an ``AsyncDownload``: the redirect is followed once, without the credential, and
        the file is streamed. Iterate it, ``asave(path)`` it for its SHA-256, or ``aread()`` it
        (bounded); ``aclose()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.
        """
        return await self._download("downloadWhaleDataset", path_params={"job_id": job_id}, query={})

    async def cancel_whale_dataset(
        self,
        job_id: str,
    ) -> WhaleDatasetJob:
        """Cancel a whale dataset job.

        ``POST /api/v1/datasets/whale-trades/{job_id}/cancel`` (operationId ``cancelWhaleDataset``).

        Cancel queued jobs immediately and request running jobs stop at their next safe point.
        Repeating cancel converges on the current state; cancellation after the completion fence
        leaves the artifact ready. Paid export scope; jobs are private to the credential owner.
        Shares the 20/day owner export ...
        """
        result: WhaleDatasetJob = await self._call("cancelWhaleDataset", path_params={"job_id": job_id}, query={})
        return result

    @overload
    async def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: None = None,
    ) -> GetPickOfTheDayLedgerEntryResponse: ...

    @overload
    async def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: str | None,
    ) -> GetPickOfTheDayLedgerEntryResponse | NotModifiedResponse: ...

    async def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: str | None = None,
    ) -> GetPickOfTheDayLedgerEntryResponse | NotModifiedResponse:
        """Read a pick proof by stable id.

        ``GET /api/v1/pick-of-the-day/ledger/{pick_id}`` (operationId ``getPickOfTheDayLedgerEntry``).

        Public read of one published pick by its stable decimal-string pick_id. Same proof
        gating, canonical bytes, ETag and integrity failures as the ledger. Invalid ids return
        400; absent or unpublished picks return 404. Withdrawal from recommendations or the
        archive does not remove a published ledger ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: GetPickOfTheDayLedgerEntryResponse | NotModifiedResponse = await self._call("getPickOfTheDayLedgerEntry", path_params={"pick_id": pick_id}, query={}, if_none_match=if_none_match)
        return result

    async def create_webhook_verification_attempt(
        self,
        id: str,
        body: CreateWebhookVerificationAttemptRequest,
        *,
        idempotency_key: str | None = None,
    ) -> CreateWebhookVerificationAttemptResponse:
        """Admit asynchronous webhook verification.

        ``POST /api/v1/webhooks/{id}/verification-attempts`` (operationId ``createWebhookVerificationAttempt``).

        Additive asynchronous consent flow; the legacy POST /verify keeps its synchronous
        200/422 behavior and retry policy. Commits one durable attempt and returns 202 without
        awaiting DNS or the receiver. Send the original verification_token. Optional
        Idempotency-Key replays the original admission ...
        """
        result: CreateWebhookVerificationAttemptResponse = await self._call("createWebhookVerificationAttempt", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    async def get_webhook_verification_attempt(
        self,
        id: str,
        attempt_id: str,
    ) -> CreateWebhookVerificationAttemptResponse:
        """Read webhook verification attempt status.

        ``GET /api/v1/webhooks/{id}/verification-attempts/{attempt_id}`` (operationId ``getWebhookVerificationAttempt``).

        Fresh primary-database status for one attempt owned by the authenticated account and
        webhook. queued/running means consent is pending; only verified activates the unchanged
        endpoint after receiver 2xx. failed/cancelled/expired are terminal. Polling never issues
        a challenge or restarts work. At ...
        """
        result: CreateWebhookVerificationAttemptResponse = await self._call("getWebhookVerificationAttempt", path_params={"id": id, "attempt_id": attempt_id}, query={})
        return result

    @overload
    async def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: None = None,
    ) -> ComboFillsResponse: ...

    @overload
    async def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: str | None,
    ) -> ComboFillsResponse | NotModifiedResponse: ...

    async def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: str | None = None,
    ) -> ComboFillsResponse | NotModifiedResponse:
        """List combo fills.

        ``GET /api/v1/combos/fills`` (operationId ``listComboFills``).

        Returns live Polymarket combo taker fills with exact decimal-string economics, wallet
        identities, grades, legs, conjunction results, and ingest coverage. Requires an active
        Pro or Max API key. Listing includes executions with price at most 0.95; use combo
        detail for complete history. Sports and ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            result: CSV of pending, won, or lost; all clears the filter. Unknown results appear only in unfiltered lists.
            legs: CSV of 2, 3, 4, or 5+; all clears the filter. A combo matches any named pick count.
            min_stake: Minimum collateral in whole USDC.
            min_multiplier: 0 disables the filter; otherwise use 2..1000000. Minimum shares per dollar at execution.
            grades: CSV of S, A, B, C, D, F; all clears the filter. Ungraded wallets do not match.
            sports: CSV of nfl, ncaaf, nba, wnba, baseball, hockey, soccer, tennis, table-tennis, esports, mma, boxing, golf, cricket, f1, pickleball; all clears the filter. ...
            sort: Recent is newest first; largest ranks collateral; payout ranks buy-fill shares and excludes sells.
            window: Defaults to all for recent and 24h for largest or payout.
            limit: Page size. Integer values outside the range are clamped to 1..200.
            cursor: Exclusive block_number:log_index cursor for recent only; send the returned next_cursor unchanged.
            offset: Offset for ranked largest or payout ordering; use returned next_offset.
        """
        result: ComboFillsResponse | NotModifiedResponse = await self._call("listComboFills", path_params={}, query={"result": result, "legs": legs, "min_stake": min_stake, "min_multiplier": min_multiplier, "grades": grades, "sports": sports, "sort": sort, "window": window, "limit": limit, "cursor": cursor, "offset": offset}, if_none_match=if_none_match)
        return result

    @overload
    async def get_combos_summary(
        self,
        *,
        if_none_match: None = None,
    ) -> CombosSummaryResponse: ...

    @overload
    async def get_combos_summary(
        self,
        *,
        if_none_match: str | None,
    ) -> CombosSummaryResponse | NotModifiedResponse: ...

    async def get_combos_summary(
        self,
        *,
        if_none_match: str | None = None,
    ) -> CombosSummaryResponse | NotModifiedResponse:
        """Get live combo count.

        ``GET /api/v1/combos/summary`` (operationId ``getCombosSummary``).

        Returns the stored count of traded combos whose YES conjunction remains pending, with
        its computation timestamp. Sports and esports only (#27449): a combo with a leg outside
        them is not counted. Requires an active Pro or Max API key. The count is refreshed by
        the ingest owner at most every five ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: CombosSummaryResponse | NotModifiedResponse = await self._call("getCombosSummary", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: None = None,
    ) -> ComboResponse: ...

    @overload
    async def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: str | None,
    ) -> ComboResponse | NotModifiedResponse: ...

    async def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: str | None = None,
    ) -> ComboResponse | NotModifiedResponse:
        """Get combo detail.

        ``GET /api/v1/combos/{condition_id}`` (operationId ``getCombo``).

        Returns one Polymarket combo with its legs, conjunction result, all-time trade totals,
        newest 100 taker fills, lifecycle totals, and ingest coverage. Requires an active Pro or
        Max API key. Detail retains execution history above the listing price cap. A malformed
        combo ID returns 400; an unknown ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ComboResponse | NotModifiedResponse = await self._call("getCombo", path_params={"condition_id": condition_id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: None = None,
    ) -> EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse: ...

    @overload
    async def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: str | None,
    ) -> EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse | NotModifiedResponse: ...

    async def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: str | None = None,
    ) -> EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse | NotModifiedResponse:
        """Get Edge Hunter.

        ``GET /api/v1/edge-hunter`` (operationId ``getEdgeHunter``).

        Max-only canonical Edge Hunter API with board, signals and observations views. An active
        Pro credential receives 403 forbidden with reason max_plan_required. Default board
        admission and ordering remain compatible: B grade floor, 30-row cap, 48-hour kickoff
        horizon, full Max projection and both ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: Response mode. board preserves the full quoted board; signals exposes ranked records and category evidence; observations exposes cohort measurements and ...
            category: Legacy canonical bucket alias, now accepted in every view. Provider aliases canonicalize: NFL reaches Football and EPL reaches Soccer. Use leagues for a ...
            cohort: Required for view=observations; wider_holder, in_play or emerging_pile. Rejected for board and signals. wider_holder covers pregame markets that view=signals ...
            admission: Opt-in admission rule for view=observations with cohort=wider_holder; rejected for every other view and cohort. most_held_48h returns the most-held selection ...
            min_grade: Board and signals: S, A or B, default B. Requires a piled-side holder at the selected grade floor or better, without removing other holders. Rejected for ...
            limit: Board row cap defaults to 30 and clamps integer values to 1..30; total counts selected admitted rows before the cap. Signals and observations page size ...
            cursor: Opaque canonical Edge Hunter cursor from next_cursor. Bound to view, every normalized selection axis, grade/horizon where applicable, source snapshot and ...
            horizon_hours: Kickoff window for board (default 48) or signals (default 12). Integer values clamp to 1..48. Rejected for observations, whose pre-game universe is fixed at 48 ...
            kind: All views: sports excludes the Esports bucket; esports selects only Esports. Omit for both. Combines with other selections using AND. Selected reads echo ...
            sports: Canonical sport buckets, including Esports and Table Tennis, matched case-insensitively. Unknown names and league aliases such as NFL are rejected in sports; ...
            leagues: Normalized machine/provider league identities, such as nfl, cfb, nba, epl, cs2, lol, dota2 or valorant. Known wire/tag aliases normalize; other provider keys ...
            market_types: Exact provider sports_market_type values. This is an open provider taxonomy, distinct from exact market IDs. Read market_context.market_type; missing selected ...
            condition_ids: Exact market selections. Raw provider condition IDs and the existing mkt_-prefixed aliases normalize to raw IDs. Unknown well-formed IDs return an empty ...
            event_slugs: Exact provider event slugs. Use event_slug returned on the row; no title or slug-prefix guessing. All views. Repeat this query key or put comma-separated ...
            series_slugs: Exact provider series slugs. Read market_context.series_slug; a missing selected series excludes the row. All views. Repeat this query key or put ...
        """
        result: EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse | NotModifiedResponse = await self._call("getEdgeHunter", path_params={}, query={"view": view, "category": category, "cohort": cohort, "admission": admission, "min_grade": min_grade, "limit": limit, "cursor": cursor, "horizon_hours": horizon_hours, "kind": kind, "sports": sports, "leagues": leagues, "market_types": market_types, "condition_ids": condition_ids, "event_slugs": event_slugs, "series_slugs": series_slugs}, if_none_match=if_none_match)
        return result



class AsyncResponseOperationsMixin:
    """The async operations, each returning an ``ApiResponse`` over the same body.

    Reached as ``async_client.with_response``, mirroring ``ResponseOperationsMixin``."""

    async def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by AsyncClient
        raise NotImplementedError

    async def _download(
        self, operation_id: str, **kwargs: Any
    ) -> AsyncDownload:  # pragma: no cover - provided by AsyncClient
        raise NotImplementedError

    async def get_api_discovery(
        self,
    ) -> ApiResponse[GetApiDiscoveryResponse]:
        """API discovery.

        ``GET /api/v1`` (operationId ``getApiDiscovery``).

        Unauthenticated API-origin discovery document pointing agents to the canonical API base
        URL, full docs, web-origin OpenAPI spec, health check, and the COMPLETE index of
        authenticated data routes. data.authenticated_routes is the whole authenticated route
        surface, not a sample: it carries every ...
        """
        result: ApiResponse[GetApiDiscoveryResponse] = await self._call("getApiDiscovery", path_params={}, query={})
        return result

    async def redirect_api_openapi_spec(
        self,
    ) -> AsyncDownload:
        """Redirect to the canonical OpenAPI spec.

        ``GET /api/v1/openapi.json`` (operationId ``redirectApiOpenapiSpec``).

        Unauthenticated API-origin compatibility redirect to the canonical web-origin OpenAPI
        JSON document at https://0xinsider.com/api/v1/openapi.json.

        Returns an ``AsyncDownload``: the redirect is followed once, without the credential, and
        the file is streamed. Iterate it, ``asave(path)`` it for its SHA-256, or ``aread()`` it
        (bounded); ``aclose()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.
        """
        return await self._download("redirectApiOpenapiSpec", path_params={}, query={})

    async def register_agent(
        self,
    ) -> ApiResponse[RegisterAgentResponse]:
        """Register an agent for a sandbox key.

        ``POST /api/v1/agents/register`` (operationId ``registerAgent``).

        Self-serve agent onboarding: no account, no request body, no human step. Returns a
        sandbox API key (oxi_sk_test_...) and the path to live access. The key works only on the
        sandbox server (https://0xinsider.com/sandbox/api/v1), where it is optional: send it as
        Authorization: Bearer to exercise the ...
        """
        result: ApiResponse[RegisterAgentResponse] = await self._call("registerAgent", path_params={}, query={})
        return result

    @overload
    async def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderResponse]: ...

    @overload
    async def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_trader(
        self,
        address: str,
        *,
        expand: list[Literal["strategy", "categories", "quant_metrics", "trust", "breakdowns"]] | None = None,
        max_age_s: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderResponse] | ApiResponse[NotModifiedResponse]:
        """Get trader.

        ``GET /api/v1/trader/{address}`` (operationId ``getTrader``).

        Returns a trader's grade (S through F), P&L, win rate, and optional strategy/category
        data. The path accepts either an Ethereum wallet address, a known trader username, or a
        trd_-prefixed trader ID emitted by this API. A wallet address this API does not track
        yet returns 200 with sync_status ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            expand: Include heavy fields and trust metadata. Repeatable: strategy, categories, trust, breakdowns. breakdowns adds the profile's strategy measures ...
            max_age_s: Opt into a whole-response freshness ceiling in seconds. The server returns 200 only when data_quality.status is fresh or stale and data_quality.as_of is no ...
        """
        result: ApiResponse[GetTraderResponse] | ApiResponse[NotModifiedResponse] = await self._call("getTrader", path_params={"address": address}, query={"expand": expand, "max_age_s": max_age_s}, if_none_match=if_none_match)
        return result

    async def get_trader_context_markdown(
        self,
        address: str,
    ) -> ApiResponse[str]:
        """Get trader context (Markdown).

        ``GET /api/v1/trader/{address}/context.md`` (operationId ``getTraderContextMarkdown``).

        Returns a single human- and LLM-readable Markdown briefing for one trader: identity,
        grade, P&L, position coverage, and freshness. The path accepts an Ethereum wallet
        address (0x...), a known trader username, or a trd_-prefixed trader ID emitted by this
        API. A wallet address this API does not track ...
        """
        result: ApiResponse[str] = await self._call("getTraderContextMarkdown", path_params={"address": address}, query={})
        return result

    @overload
    async def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderGradeAtResponse]: ...

    @overload
    async def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderGradeAtResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_trader_grade_at(
        self,
        address: str,
        *,
        as_of: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderGradeAtResponse] | ApiResponse[NotModifiedResponse]:
        """Get a trader grade proven visible at a past instant.

        ``GET /api/v1/trader/{address}/grade-at`` (operationId ``getTraderGradeAt``).

        Reads one trader's recorded grade at as_of from prospective visibility evidence. Before
        the first recorded observation, after deletion, or during a grade-transition gap, status
        is unknown and grade is null; a recorded ungraded trader instead has status ungraded.
        available_from is the first proven ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            as_of: Required. RFC3339 instant whose historically visible grade is requested. Future instants are refused. Send the trade or decision time, not the ranking date.
        """
        result: ApiResponse[GetTraderGradeAtResponse] | ApiResponse[NotModifiedResponse] = await self._call("getTraderGradeAt", path_params={"address": address}, query={"as_of": as_of}, if_none_match=if_none_match)
        return result

    @overload
    async def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderClvResponse]: ...

    @overload
    async def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderClvResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_trader_clv(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderClvResponse] | ApiResponse[NotModifiedResponse]:
        """Get a trader's closing line value on large trades.

        ``GET /api/v1/trader/{address}/clv`` (operationId ``getTraderClv``).

        Closing line value (CLV) over one wallet's large trades in a window: the trades GET
        /api/v1/large-trades/history?trader= returns for the same from, to, min_size and
        category, each measured exactly as its clv object is. CLV is in cents per share against
        the market's stored closing line (GET ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            from_: Inclusive RFC3339 lower bound on the trade time. Defaults to 90 days before to.
            to: Exclusive RFC3339 upper bound on the trade time. Defaults to now; must be after from, and at most 366 days after it.
            min_size: Minimum trade size in USD. The capture floor was 3,000 USD before 2026-07-06 and 10,000 USD from then (1,000 USD in earnings markets), so 10000 gives one size ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
        """
        result: ApiResponse[GetTraderClvResponse] | ApiResponse[NotModifiedResponse] = await self._call("getTraderClv", path_params={"address": address}, query={"from": from_, "to": to, "min_size": min_size, "category": category}, if_none_match=if_none_match)
        return result

    @overload
    async def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderContextResponse]: ...

    @overload
    async def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderContextResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderContextResponse] | ApiResponse[NotModifiedResponse]:
        """Get trader context (JSON).

        ``GET /api/v1/trader/{address}/context`` (operationId ``getTraderContext``).

        Returns a single structured context object for one trader: the full trader profile (same
        shape as GET /api/v1/trader/{address}) plus a position_summary (sync coverage and
        realized/unrealized P&L rollups, with an as_of open-position freshness clock), the
        data_as_of freshness timestamp (the ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetTraderContextResponse] | ApiResponse[NotModifiedResponse] = await self._call("getTraderContext", path_params={"address": address}, query={}, if_none_match=if_none_match)
        return result

    async def batch_get_traders(
        self,
        body: BatchGetTradersBody,
    ) -> ApiResponse[BatchGetTradersResponse]:
        """Batch traders.

        ``POST /api/v1/traders/batch`` (operationId ``batchGetTraders``).

        Returns traders for 1-25 wallet addresses or known usernames. Results preserve request
        order, duplicate inputs return duplicate rows, and each item is charged one batch item
        unit before execution. A wallet address this API does not track yet returns data with
        sync_status "unknown", matching the ...
        """
        result: ApiResponse[BatchGetTradersResponse] = await self._call("batchGetTraders", path_params={}, query={}, body=body)
        return result

    @overload
    async def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPositionTimelineResponse]: ...

    @overload
    async def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse]:
        """Get a trader's position timeline for one market.

        ``GET /api/v1/trader/{address}/position-timeline`` (operationId ``getPositionTimeline``).

        Returns every stored Polymarket fill for one tracked trader in one market, newest first,
        with outcome-specific running_amount and running_avg_price including all earlier stored
        fills before pagination. Fills come from the full fill ledger, the same rows the trade
        export serves, at any date (#33245; ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            condition_id: Required. Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        result: ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse] = await self._call("getPositionTimeline", path_params={"address": address}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetTraderCategoryRecordsResponse]: ...

    @overload
    async def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetTraderCategoryRecordsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_trader_category_records(
        self,
        address: str,
        *,
        category: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetTraderCategoryRecordsResponse] | ApiResponse[NotModifiedResponse]:
        """Get trader category win records.

        ``GET /api/v1/trader/{address}/categories`` (operationId ``getTraderCategoryRecords``).

        Returns one wallet's win record in every canonical category it has a settled market in:
        wins, decided (wins plus losses) and the rate, per category, busiest category first.
        These are the same counts the Pick of the Day holder chips carry. The Esports record
        also carries games: the wallet's record ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            category: Filter to one canonical category, matched through the same rollup every other category surface uses: soccer, EPL and champions league all reach Soccer, every ...
        """
        result: ApiResponse[GetTraderCategoryRecordsResponse] | ApiResponse[NotModifiedResponse] = await self._call("getTraderCategoryRecords", path_params={"address": address}, query={"category": category}, if_none_match=if_none_match)
        return result

    async def get_trader_pnl(
        self,
        address: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        sections: list[Literal["entries", "stats", "monthly", "year_totals", "drawdown"]] | None = None,
    ) -> ApiResponse[GetTraderPnlResponse]:
        """Get trader P&L time series.

        ``GET /api/v1/trader/{address}/pnl`` (operationId ``getTraderPnl``).

        Returns a trader's sports and esports daily P&L time series and pre-derived stats:
        entries (daily realized P&L and its running sum), period stats (all/90d/30d/7d), monthly
        aggregation, per-year totals, the drawdown series, series_status, and realized, which
        reconciles the days with the wallet's ...

        Query parameters:
            from_: Inclusive UTC calendar-date lower bound in YYYY-MM-DD form for the daily series (entries and drawdown). Omit for the whole stored history. A value that is not ...
            to: Inclusive UTC calendar-date upper bound in YYYY-MM-DD form for the daily series (entries and drawdown). Omit for the whole stored history. A value that is not ...
            sections: Which sections of the object to return. Repeatable and comma-separated: entries, stats, monthly, year_totals, drawdown. Omit it, or send it empty, for all ...
        """
        result: ApiResponse[GetTraderPnlResponse] = await self._call("getTraderPnl", path_params={"address": address}, query={"from": from_, "to": to, "sections": sections})
        return result

    @overload
    async def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPositionTimelineResponse]: ...

    @overload
    async def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse]:
        """Get a trader's position timeline (unified identity resolver).

        ``GET /api/v1/traders/{trader}/position-timeline`` (operationId ``getPositionTimelineById``).

        Unified trader-timeline route (#4975). {trader} accepts all five identity shapes - 0x...
        wallet, username, trd_-prefixed trader id, bare integer id, and @username (a username
        lookup only, for all-digit usernames) - resolved by the single shared trader-identity
        resolver. Returns every stored ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            condition_id: Required. Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        result: ApiResponse[GetPositionTimelineResponse] | ApiResponse[NotModifiedResponse] = await self._call("getPositionTimelineById", path_params={"trader": trader}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListPropsResponse]: ...

    @overload
    async def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListPropsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_props(
        self,
        *,
        league: str | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        player: str | None = None,
        stat: list[str] | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        max_spread_c: float | None = None,
        min_book_usd_within_2c: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["quotes"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListPropsResponse] | ApiResponse[NotModifiedResponse]:
        """List player props across a league.

        ``GET /api/v1/props`` (operationId ``listProps``).

        Player props for the catalog's games of one league, one row per market, ordered by game
        slug, stat, player and line. NFL files props on a game's -player-props and -first-td-
        scorer child events and NBA on the game event; this reads both, so a caller does not
        walk GET /api/v1/games and then each ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            league: Required. League tag as GET /api/v1/games coverage.leagues spells it, for example nfl or nba. Matched case-insensitively.
            starts_after: RFC 3339 kickoff bound. A game with no published kickoff is excluded whenever either bound is set.
            starts_before: RFC 3339 kickoff bound, inclusive.
            player: Part of player.name, ignoring case and accents: jokic matches Nikola Jokić. A row with no player does not match.
            stat: Provider sportsMarketType values to keep, case-insensitive, for example passing_yards or points. Repeat the parameter or send a comma-separated list. An ...
            status: active (default), closed, or all. closed means the provider closed the market or it resolved.
            max_spread_c: Keep only props with an outcome whose cached best ask less best bid is at most this many cents: above 0, at most 100, in steps of 0.01. The books are the ones ...
            min_book_usd_within_2c: Keep only props with an outcome whose cached book holds at least this many USD on each side within 2 cents of its midpoint: bids at or above the midpoint minus ...
            limit: Page size. Out-of-range values are clamped to 1..200.
            cursor: Opaque prp_v1_ cursor from next_cursor, sent with the same filters. A cursor this endpoint did not issue returns 400 with error.param=cursor.
            expand: quotes adds each outcome's cached quote, as on GET /api/v1/games/{event_slug}/markets; it adds 1 to the cost, on every plan. Repeatable: quotes.
        """
        result: ApiResponse[ListPropsResponse] | ApiResponse[NotModifiedResponse] = await self._call("listProps", path_params={}, query={"league": league, "starts_after": starts_after, "starts_before": starts_before, "player": player, "stat": stat, "status": status, "max_spread_c": max_spread_c, "min_book_usd_within_2c": min_book_usd_within_2c, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    async def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListPositionsResponse]: ...

    @overload
    async def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListPositionsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        consistency: Literal["live", "snapshot"] | None = None,
        min_size: float | None = None,
        category: str | None = None,
        condition_id: str | None = None,
        wallet: list[str] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        side: Literal["yes", "no"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListPositionsResponse] | ApiResponse[NotModifiedResponse]:
        """List current positions (positions-board feed).

        ``GET /api/v1/positions`` (operationId ``listPositions``).

        Returns the current positions-board feed backed by the wallet_positions mirror. Ordered
        by current_value_usd DESC with deterministic (wallet, condition_id, outcome_index)
        tiebreakers. Pre-reconcile rows (current_value_usd IS NULL) are excluded. Positions on
        resolved markets are excluded: a position ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of current positions to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            consistency: live (default) reads the current value-ordered board. snapshot requires wallet and freezes up to 500 matching rows and 2 MB for up to five minutes. Keep ...
            min_size: Minimum current position value in USD. Defaults to 100 when omitted, or to 0 when wallet is present; send 0 to include every reconciled position.
            category: Exact match against provider-backed market_canonical.category. Sports and esports only (#27311): a category outside them returns 400 bad_request with param ...
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id emitted by V1 responses. Combine with min_size=0 for every reconciled ...
            wallet: Scope to one wallet or a book of wallets (repeatable, up to 25 per request; comma-separated values inside one occurrence also work). Each value is a wallet ...
            min_grade: Minimum trader grade allowlist. `A` matches S and A; `B` matches S, A, B; etc.
            side: Filter by the binary outcome side. `yes` maps to outcome_index=0, `no` to outcome_index=1.
        """
        result: ApiResponse[ListPositionsResponse] | ApiResponse[NotModifiedResponse] = await self._call("listPositions", path_params={}, query={"limit": limit, "cursor": cursor, "consistency": consistency, "min_size": min_size, "category": category, "condition_id": condition_id, "wallet": wallet, "min_grade": min_grade, "side": side}, if_none_match=if_none_match)
        return result

    async def list_large_positions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        condition_id: str | None = None,
    ) -> ApiResponse[ListLargePositionsResponse]:
        """List large positions.

        ``GET /api/v1/large-positions`` (operationId ``listLargePositions``).

        Returns the largest current open positions from graded traders, value-descending, with
        opaque cursor pagination. This is a change-detection feed, not a holder list: a row
        needs a current value of at least 50,000 USD and a live detection in the last 24 hours,
        so a wallet that holds a market without ...

        Query parameters:
            limit: Maximum number of large positions to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque pagination cursor from a previous response.
            min_size: Minimum position value in USD. Raises the feed's own floor of 50,000 USD; a smaller value does not lower it.
            category: One RFC 4180 CSV record of exact current provider-backed market_canonical.category values. Legacy unquoted lists such as NBA,WNBA remain valid; values ...
            min_grade: Minimum trader grade. Matched against the trader.grade each row returns, the wallet's current grade, so every row listed shows a grade at or above this floor.
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id (round-trips a value from a list response). Must be 0x followed by 64 ...
        """
        result: ApiResponse[ListLargePositionsResponse] = await self._call("listLargePositions", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "condition_id": condition_id})
        return result

    @overload
    async def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListLargeTradesResponse]: ...

    @overload
    async def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListLargeTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_large_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListLargeTradesResponse] | ApiResponse[NotModifiedResponse]:
        """List large trades.

        ``GET /api/v1/large-trades`` (operationId ``listLargeTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of recent large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade now (trader.grade), the wallet's grade when this page is read, not when the trade filled. A wallet re-graded after a trade enters or ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            since: Return only the trades recorded after this one. Pass the id of a large trade this API returned (wt_<n>, or the bare integer). The answer keeps the list shape ...
            condition_id: Only this market's large trades: an exact raw provider condition_id. The page is read from the market's own index, newest first, and pages with cursor; it ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListLargeTradesResponse] | ApiResponse[NotModifiedResponse] = await self._call("listLargeTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "min_market_volume_share": min_market_volume_share, "sort": sort, "since": since, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListWhaleTradesResponse]: ...

    @overload
    async def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListWhaleTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_whale_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        since: str | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListWhaleTradesResponse] | ApiResponse[NotModifiedResponse]:
        """List whale trades.

        ``GET /api/v1/whale-trades`` (operationId ``listWhaleTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of recent large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade now (trader.grade), the wallet's grade when this page is read, not when the trade filled. A wallet re-graded after a trade enters or ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            since: Return only the trades recorded after this one. Pass the id of a large trade this API returned (wt_<n>, or the bare integer). The answer keeps the list shape ...
            condition_id: Only this market's large trades: an exact raw provider condition_id. The page is read from the market's own index, newest first, and pages with cursor; it ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListWhaleTradesResponse] | ApiResponse[NotModifiedResponse] = await self._call("listWhaleTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "min_market_volume_share": min_market_volume_share, "sort": sort, "since": since, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListLargeTradeHistoryResponse]: ...

    @overload
    async def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListLargeTradeHistoryResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_large_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListLargeTradeHistoryResponse] | ApiResponse[NotModifiedResponse]:
        """Replay historical large trades.

        ``GET /api/v1/large-trades/history`` (operationId ``listLargeTradeHistory``).

        Returns historical large trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of historical large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD. The capture floor was 3,000 USD before 2026-07-06 and 10,000 USD from then (1,000 USD in earnings markets), so 10000 gives one size ...
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, username, or trd_-prefixed trader ID, resolved against the traders table. Unknown traders return an ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade as of today (trader.grade), not at trade time. On a historical window it selects wallets by a grade they may have earned after the trade; ...
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListLargeTradeHistoryResponse] | ApiResponse[NotModifiedResponse] = await self._call("listLargeTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to, "min_market_volume_share": min_market_volume_share, "sort": sort, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListWhaleTradeHistoryResponse]: ...

    @overload
    async def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListWhaleTradeHistoryResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_whale_trade_history(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_size: float | None = None,
        condition_id: str | None = None,
        trader: str | None = None,
        category: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        suspicious_only: bool | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        from_: str | None = None,
        to: str | None = None,
        min_market_volume_share: float | None = None,
        sort: Literal["recent", "market_volume_share"] | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListWhaleTradeHistoryResponse] | ApiResponse[NotModifiedResponse]:
        """Replay historical whale trades.

        ``GET /api/v1/whale-trades/history`` (operationId ``listWhaleTradeHistory``).

        Returns historical whale trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of historical large trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD.
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, or username resolved against the traders table. Unknown traders return an empty list.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade.
            min_grade_at_trade: Minimum grade the trader held when the trade filled (trader.grade_at_trade). Only rows whose trader.grade_at_trade_status is graded can match, so a trade ...
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
            min_market_volume_share: Keep only trades whose market_volume_share is known and at least this. A fraction, not a percent: 0.01 is one percent of the market's traded volume. A trade ...
            sort: Order of the returned page. recent is newest first and is the default. market_volume_share ranks by each trade's share of its market's traded volume, biggest ...
            event_slug: Only the large trades in one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListWhaleTradeHistoryResponse] | ApiResponse[NotModifiedResponse] = await self._call("listWhaleTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to, "min_market_volume_share": min_market_volume_share, "sort": sort, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetLargeTradeResponse]: ...

    @overload
    async def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetLargeTradeResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_large_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetLargeTradeResponse] | ApiResponse[NotModifiedResponse]:
        """Get large trade by ID.

        ``GET /api/v1/large-trades/{id}`` (operationId ``getLargeTrade``).

        Returns one large trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetLargeTradeResponse] | ApiResponse[NotModifiedResponse] = await self._call("getLargeTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetWhaleTradeResponse]: ...

    @overload
    async def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetWhaleTradeResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetWhaleTradeResponse] | ApiResponse[NotModifiedResponse]:
        """Get whale trade by ID.

        ``GET /api/v1/whale-trades/{id}`` (operationId ``getWhaleTrade``).

        Returns one whale trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses. Deprecated alias of GET /api/v1/large-trades/{id}, kept live
        until its sunset on 2027-02-01 (#16304, #29351); every response carries `Deprecation:
        @1790132400` (RFC 9745, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetWhaleTradeResponse] | ApiResponse[NotModifiedResponse] = await self._call("getWhaleTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    async def list_large_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListLargeTradeCounterpartyExecutionsResponse]:
        """Page counterparty executions.

        ``GET /api/v1/large-trades/{id}/counterparties/executions`` (operationId ``listLargeTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by large-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail.

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the large trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListLargeTradeCounterpartyExecutionsResponse] = await self._call("listLargeTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    async def list_whale_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListLargeTradeCounterpartyExecutionsResponse]:
        """Page counterparty executions.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions`` (operationId ``listWhaleTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by whale-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail. Deprecated alias of GET /api/v1/large-
        trades/{id}/counterparties/executions, kept live until its sunset on ...

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListLargeTradeCounterpartyExecutionsResponse] = await self._call("listWhaleTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    async def list_large_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListLargeTradeCounterpartyMakersResponse]:
        """Page maker counterparties.

        ``GET /api/v1/large-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listLargeTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages.

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the large trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListLargeTradeCounterpartyMakersResponse] = await self._call("listLargeTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    async def list_whale_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: str | None = None,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListLargeTradeCounterpartyMakersResponse]:
        """Page maker counterparties.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listWhaleTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages. Deprecated alias of GET /api/v1/large-
        trades/{id}/counterparties/executions/{execution_id}/makers, kept live until its sunset
        on 2027-02-01 (#16304, #29351); every response ...

        Query parameters:
            snapshot_id: Required. Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListLargeTradeCounterpartyMakersResponse] = await self._call("listWhaleTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})
        return result

    @overload
    async def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListLeaderboardResponse]: ...

    @overload
    async def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListLeaderboardResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_leaderboard(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        strategy: Literal["category_focused", "diversified", "high_activity", "mixed", "two_sided", "unclassified"] | None = None,
        sort: Literal["rank", "grade", "volume", "predictions", "pnl", "win_rate", "edge"] | None = None,
        dir: Literal["asc", "desc"] | None = None,
        activity: Literal["all", "active", "inactive"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListLeaderboardResponse] | ApiResponse[NotModifiedResponse]:
        """Get trader leaderboard.

        ``GET /api/v1/leaderboard`` (operationId ``listLeaderboard``).

        Returns ranked traders (grades S/A/B), by default in the board's own order: score
        descending, with a fixed tiebreak so the order never changes between reads of one
        ranking generation. sort, dir and activity reorder and scope the same wallets the way
        the site's leaderboard does (since 2026-11-02, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of ranked traders to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque lbv1_ pagination cursor from a prior response. It binds the finite score/address boundary to the effective category/strategy filters, and on a sorted ...
            category: Filter by category: a sport or esports bucket, matched case-insensitively. League values fold into their sport (NBA and NCAAB into Basketball, NFL into ...
            strategy: Filter by observed trading style. Current styles: two_sided, category_focused, high_activity, diversified, mixed, unclassified. Current styles count the ...
            sort: Order of the list, the sort columns of the site's leaderboard (/skill-leaderboard). rank (default) is the board's own order, the rank the site and the trader ...
            dir: Direction of sort. Omitted, each sort reads in its natural direction: rank 1 first for rank (asc), largest first for every other sort (desc). The opposite ...
            activity: Limit the list to wallets by recent trading, the site leaderboard's split. active: the wallet's last trade, as its current grade recorded it and aged to today, ...
        """
        result: ApiResponse[ListLeaderboardResponse] | ApiResponse[NotModifiedResponse] = await self._call("listLeaderboard", path_params={}, query={"limit": limit, "cursor": cursor, "category": category, "strategy": strategy, "sort": sort, "dir": dir, "activity": activity}, if_none_match=if_none_match)
        return result

    @overload
    async def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayResponse]: ...

    @overload
    async def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_pick_of_the_day(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "summary"] | None = None,
        pick_id: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayResponse] | ApiResponse[NotModifiedResponse]:
        """Get today's or a past day's Pick of the Day.

        ``GET /api/v1/pick-of-the-day`` (operationId ``getPickOfTheDay``).

        Returns entitled published picks for the current product day, or for the past product
        day named by `date`. Pro includes five selections in total: the designated free
        selection and the first four non-free selections in publication order. Max opens every
        available selection, up to twenty-five. A day ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            date: A product day (America/New_York) in YYYY-MM-DD format, on or before today. Omit it, or send today, for the current read. A past day with no published pick ...
            view: full (default) is the whole recorded set: every pick with its holders, lead backer, sports context, thesis and entry_authorization, and the top-level copy of ...
            pick_id: One entitled published pick of the day, by its stable decimal-string pick_id. The body carries that pick once, as picks[0], beside state, pick_date and ...
        """
        result: ApiResponse[GetPickOfTheDayResponse] | ApiResponse[NotModifiedResponse] = await self._call("getPickOfTheDay", path_params={}, query={"date": date, "view": view, "pick_id": pick_id}, if_none_match=if_none_match)
        return result

    @overload
    async def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayArchiveResponse]: ...

    @overload
    async def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayArchiveResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_pick_of_the_day_archive(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayArchiveResponse] | ApiResponse[NotModifiedResponse]:
        """Get the Pick of the Day track record.

        ``GET /api/v1/pick-of-the-day/archive`` (operationId ``getPickOfTheDayArchive``).

        Returns published picks that have not been withdrawn, with their outcome, modeled
        return, unit score, closing-line value, and cumulative record. Resolved game details and
        results are public. For unauthorized unresolved selections, game identity, category,
        image, publication time, and backed facts ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: full (default) is every row with every field, plus days and hit_rate with its per-pick series. summary returns view, hit_rate without series, one page of short ...
            limit: Rows per page of picks, 1 to 200, default 50. An integer outside that range is clamped into it, like every list limit, and X-Effective-Query reports the limit ...
            cursor: The page.next_cursor of the previous page: the rows after it, newest first. A cursor is a position in the record, so a pick published while you page does not ...
        """
        result: ApiResponse[GetPickOfTheDayArchiveResponse] | ApiResponse[NotModifiedResponse] = await self._call("getPickOfTheDayArchive", path_params={}, query={"view": view, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayStatsResponse]: ...

    @overload
    async def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayStatsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_pick_of_the_day_stats(
        self,
        *,
        view: Literal["full", "summary"] | None = None,
        sections: list[Literal["hit_rate", "series", "market_expectations", "outcome_stats", "days", "categories", "sports", "tiers", "months", "price_bands", "market_types", "total_sides", "streaks", "records", "voids"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayStatsResponse] | ApiResponse[NotModifiedResponse]:
        """Get the Pick of the Day track-record breakdown.

        ``GET /api/v1/pick-of-the-day/stats`` (operationId ``getPickOfTheDayStats``).

        The figures behind the stats page, computed from the same rows the archive publishes:
        the hit rate, the win rate the market expected at publication, flat-stake outcome stats
        (drawdown, rolling form, profit factor, concentration), and buckets by day, sport,
        category, access group, month, entry-price ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: full (default) is every section. summary returns view, sections and every section except the five that grow with the record: series, days, categories, months ...
            sections: Exactly the sections to return, in the body's order whatever the request order. Repeatable and comma-separated: hit_rate, series, market_expectations, ...
        """
        result: ApiResponse[GetPickOfTheDayStatsResponse] | ApiResponse[NotModifiedResponse] = await self._call("getPickOfTheDayStats", path_params={}, query={"view": view, "sections": sections}, if_none_match=if_none_match)
        return result

    @overload
    async def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayLedgerResponse]: ...

    @overload
    async def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayLedgerResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_pick_of_the_day_ledger(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayLedgerResponse] | ApiResponse[NotModifiedResponse]:
        """Get the Pick of the Day commitment ledger.

        ``GET /api/v1/pick-of-the-day/ledger`` (operationId ``getPickOfTheDayLedger``).

        Returns the pre-game commitment for every published pick, so the public track record can
        be checked by someone who was not watching when the pick dropped. One entry per
        (pick_date, pick_rank), ascending by pick_date then pick_rank, in one of three states.
        `sealed` is an unresolved pick: the hash, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetPickOfTheDayLedgerResponse] | ApiResponse[NotModifiedResponse] = await self._call("getPickOfTheDayLedger", path_params={}, query={}, if_none_match=if_none_match)
        return result

    async def list_trending_wallets(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        window: Literal["7d", "30d"] | None = None,
    ) -> ApiResponse[ListTrendingWalletsResponse]:
        """List trending wallets.

        ``GET /api/v1/leaderboard/trending`` (operationId ``listTrendingWallets``).

        Returns wallets ranked by Polymarket weekly/monthly P&L (Polymarket-only discovery),
        with opaque page-cursor pagination. trending_pnl_usd and the by-PNL row order come from
        Polymarket's canonical leaderboard (data-
        api.polymarket.com/v2/leaderboard?time_period=week|month&sort_by=PNL), not a locally ...

        Query parameters:
            limit: Polymarket's weekly leaderboard caps the ranked set at 50 wallets; requests above 50 still return at most 50. Out-of-range values are clamped to 1..50.
            cursor: Opaque pagination cursor from a previous response, bound to its effective limit, window and ranked-board generation. A changed board or request scope returns ...
            window: Trailing window.
        """
        result: ApiResponse[ListTrendingWalletsResponse] = await self._call("listTrendingWallets", path_params={}, query={"limit": limit, "cursor": cursor, "window": window})
        return result

    @overload
    async def list_leaderboard_leagues(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[ListLeaderboardLeaguesResponse]: ...

    @overload
    async def list_leaderboard_leagues(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[ListLeaderboardLeaguesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_leaderboard_leagues(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListLeaderboardLeaguesResponse] | ApiResponse[NotModifiedResponse]:
        """List the leagues that have a leaderboard.

        ``GET /api/v1/leaderboard/leagues`` (operationId ``listLeaderboardLeagues``).

        Every league with its own skill leaderboard, grouped by sport, most ranked wallets
        first. Each row's `sport` and `slug` are the `{sport}` path segment and `league` value
        of GET /api/v1/leaderboard/sports/{sport}. A league is listed once its edge sort ranks
        at least `min_ranked` wallets. 503 ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[ListLeaderboardLeaguesResponse] | ApiResponse[NotModifiedResponse] = await self._call("listLeaderboardLeagues", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetSportLeaderboardResponse]: ...

    @overload
    async def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetSportLeaderboardResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_sport_leaderboard(
        self,
        sport: str,
        *,
        league: str | None = None,
        sort: Literal["edge", "pnl", "win_rate"] | None = None,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetSportLeaderboardResponse] | ApiResponse[NotModifiedResponse]:
        """Get a sport or league leaderboard.

        ``GET /api/v1/leaderboard/sports/{sport}`` (operationId ``getSportLeaderboard``).

        One sport's skill leaderboard, or with `league` one league's, the board the site's sport
        pages show. Wallets need `min_resolved` resolved markets in the sport or league.
        `sort=edge` (the default) ranks `edge_skill`, the edge over the price paid pulled toward
        the board's `edge_average` by how much ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            league: A league slug of the sport, for example premier-league or cs2, from GET /api/v1/leaderboard/leagues. Omit it for the sport board.
            sort: Ranking axis. Any other value returns 400 bad_request with error.param=sort.
            limit: Rows to return from the top of the board. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[GetSportLeaderboardResponse] | ApiResponse[NotModifiedResponse] = await self._call("getSportLeaderboard", path_params={"sport": sport}, query={"league": league, "sort": sort, "limit": limit}, if_none_match=if_none_match)
        return result

    @overload
    async def list_category_leaders(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[ListCategoryLeadersResponse]: ...

    @overload
    async def list_category_leaders(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[ListCategoryLeadersResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_category_leaders(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListCategoryLeadersResponse] | ApiResponse[NotModifiedResponse]:
        """List every category's top edge leaders.

        ``GET /api/v1/leaderboard/categories`` (operationId ``listCategoryLeaders``).

        Every sports and esports category's top three edge leaders in one read, the board the
        site's categories index shows. In each category, wallets are ranked as GET
        /api/v1/leaderboard/categories/{slug} ranks them, by the 95% lower bound of their edge
        over the price they paid; only wallets whose lower ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[ListCategoryLeadersResponse] | ApiResponse[NotModifiedResponse] = await self._call("listCategoryLeaders", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetCategoryLeaderboardResponse]: ...

    @overload
    async def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetCategoryLeaderboardResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_category_leaderboard(
        self,
        slug: str,
        *,
        active_within: Literal["all", "7d", "30d", "90d"] | None = None,
        min_events: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetCategoryLeaderboardResponse] | ApiResponse[NotModifiedResponse]:
        """Get a category's edge leaderboard.

        ``GET /api/v1/leaderboard/categories/{slug}`` (operationId ``getCategoryLeaderboard``).

        One sports or esports category's edge leaderboard, the board the site's category pages
        show. Wallets are ranked by edge_lower_bound, the 95% lower bound of their edge over the
        price they paid in the category, counted over independent events (independent_events
        breaks ties, then the wallet). Only ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            active_within: Keep wallets that traded in the category within this window. all (the default) keeps every ranked wallet.
            min_events: Independent events a wallet needs in the category to be listed. The site offers 0, 50, 100 and 250. Clamped to 0..1000000.
            limit: Maximum number of leaders to return. Out-of-range values are clamped to 1..100.
            cursor: Opaque cel_ pagination cursor from a prior response. It binds the lower-bound/independent-event/wallet boundary to the committed category-skill ranking and to ...
        """
        result: ApiResponse[GetCategoryLeaderboardResponse] | ApiResponse[NotModifiedResponse] = await self._call("getCategoryLeaderboard", path_params={"slug": slug}, query={"active_within": active_within, "min_events": min_events, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    async def search_markets(
        self,
        *,
        q: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        category: str | None = None,
    ) -> ApiResponse[SearchMarketsResponse]:
        """Search markets.

        ``GET /api/v1/markets/search`` (operationId ``searchMarkets``).

        Search prediction markets by keyword. Returns one representative market per matching
        event, preferring the market whose title is q, then a winner market over a spread, total
        or prop, with status, category, platform metadata and the event_slug. Cursor pagination
        advances over grouped market results ...

        Query parameters:
            q: Required. Search query. Must be 2-512 characters before whitespace trimming and hold at least 2 letters or digits after trimming; a query with fewer letters or digits ...
            limit: Maximum number of matching markets to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response's next_cursor.
            status: Filter by market status. A market is closed once Polymarket has closed trading or it has resolved, and active otherwise; all returns both.
            category: Filter by category. Sports and esports only (#27411): a category outside them returns 400 bad_request with param category and names the accepted buckets. The ...
        """
        result: ApiResponse[SearchMarketsResponse] = await self._call("searchMarkets", path_params={}, query={"q": q, "limit": limit, "cursor": cursor, "status": status, "category": category})
        return result

    async def search_content(
        self,
        *,
        q: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[SearchContentResponse]:
        """Search editorial content.

        ``GET /api/v1/content/search`` (operationId ``searchContent``).

        Search 0xinsider editorial content by keyword. Returns backend-owned learn, glossary,
        comparison, research, and trading-strategy items with canonical URLs. Opaque ranking
        scores are not exposed.

        Query parameters:
            q: Required. Search query. Must be 1-256 characters before whitespace trimming and non-empty after trimming.
            limit: Maximum content items to return. Out-of-range values are clamped to 1..50.
        """
        result: ApiResponse[SearchContentResponse] = await self._call("searchContent", path_params={}, query={"q": q, "limit": limit})
        return result

    @overload
    async def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSettledMarketsResponse]: ...

    @overload
    async def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSettledMarketsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_settled_markets(
        self,
        *,
        since: str | None = None,
        sports_market_type: str | None = None,
        league: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSettledMarketsResponse] | ApiResponse[NotModifiedResponse]:
        """List settled game markets since a time.

        ``GET /api/v1/markets/settled`` (operationId ``listSettledMarkets``).

        Game markets Polymarket settled, as 0xinsider recorded them, oldest first by
        (settlement.observed_at, settlement_id): one row per market per settled state, the
        object the market_settled webhook delivers as data. It is the webhook's pull side: catch
        up after downtime from since, or poll with ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            since: RFC 3339 time, required without cursor. Rows whose settlement.observed_at is at or after it. With cursor, the cursor's position replaces it.
            sports_market_type: Comma-separated provider market types to keep, case-insensitive: moneyline, spreads, totals, a prop type; at most 64. Omitted: moneyline, or with cursor the ...
            league: Comma-separated leagues to keep, as the rows' league reports them (nba, epl, or pga for PGA Tour golf); at most 32, each starting with a letter and holding no ...
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque stl_v1_ cursor from next_cursor. It replaces since and keeps the filters it was issued for: a sports_market_type or league sent with it must match them, ...
        """
        result: ApiResponse[ListSettledMarketsResponse] | ApiResponse[NotModifiedResponse] = await self._call("listSettledMarkets", path_params={}, query={"since": since, "sports_market_type": sports_market_type, "league": league, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ExploreMarketsResponse]: ...

    @overload
    async def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ExploreMarketsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def explore_markets(
        self,
        *,
        category: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        platform: Literal["polymarket"] | None = None,
        sort: Literal["trending", "hot", "expiring", "large_trades", "whales", "volume", "newest"] | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        q: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ExploreMarketsResponse] | ApiResponse[NotModifiedResponse]:
        """Explore markets.

        ``GET /api/v1/markets/explore`` (operationId ``exploreMarkets``).

        Browse whale-active titled markets with category, platform, status, and keyword filters.
        Explore is Polymarket-only: the platform parameter is accepted for backward-
        compatibility but every request returns Polymarket markets. Paginates visible discovery
        entries rather than raw market rows, returns ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            status: Filter by market status. A market is closed once Polymarket has closed trading or it has resolved, and active otherwise; all returns both.
            platform: Filter by source platform. Explore is Polymarket-only; polymarket is the only supported value and the parameter is accepted for backward-compatibility but does ...
            sort: Sort order for the discovery feed. `large_trades` ranks by large-trade activity; `whales` is its deprecated spelling and selects the same order until its ...
            cursor: Opaque pagination cursor from the previous response.
            limit: Page size. Out-of-range values are clamped to 1..48.
            q: Keyword search against market titles. At most 64 characters before whitespace trimming.
        """
        result: ApiResponse[ExploreMarketsResponse] | ApiResponse[NotModifiedResponse] = await self._call("exploreMarkets", path_params={}, query={"category": category, "status": status, "platform": platform, "sort": sort, "cursor": cursor, "limit": limit, "q": q}, if_none_match=if_none_match)
        return result

    @overload
    async def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse]: ...

    @overload
    async def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_smart_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse]:
        """List ranked sharp-money flows (deprecated alias).

        ``GET /api/v1/markets/smart-money-flows`` (operationId ``listSmartMoneyFlows``).

        Ranks sports and esports markets (#27306) by absolute net S/A/B-grade whale flow over a
        requested timeframe. Use this discovery endpoint to answer where sharp money is flowing
        before drilling into a specific market with /api/v1/market/{condition_id}/flow.
        Pagination is anchored by an opaque cursor ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp, normalized effective filters, ranking and aggregate collection ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
            condition_id: Only this market's flow: an exact raw provider condition_id. Cannot be combined with event_slug (400). An unknown market returns an empty list.
            event_slug: Only the markets of one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse] = await self._call("listSmartMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    @overload
    async def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse]: ...

    @overload
    async def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_sharp_money_flows(
        self,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        category: str | None = None,
        platform: Literal["polymarket", "all"] | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        direction: Literal["YES", "NO"] | None = None,
        condition_id: str | None = None,
        event_slug: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse]:
        """List ranked sharp-money flows.

        ``GET /api/v1/markets/sharp-money-flows`` (operationId ``listSharpMoneyFlows``).

        Canonical path for ranked sharp-money flows; /api/v1/markets/smart-money-flows remains
        live as a deprecated byte-identical alias of it. Ranks sports and esports markets
        (#27306) by absolute net S/A/B-grade whale flow over a requested timeframe. Use this
        discovery endpoint to answer where sharp ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp, normalized effective filters, ranking and aggregate collection ...
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
            condition_id: Only this market's flow: an exact raw provider condition_id. Cannot be combined with event_slug (400). An unknown market returns an empty list.
            event_slug: Only the markets of one game: every market of the game behind this event slug, the moneyline, spreads, totals and props, as GET ...
        """
        result: ApiResponse[ListSmartMoneyFlowsResponse] | ApiResponse[NotModifiedResponse] = await self._call("listSharpMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction, "condition_id": condition_id, "event_slug": event_slug}, if_none_match=if_none_match)
        return result

    async def get_coverage(
        self,
    ) -> ApiResponse[GetCoverageResponse]:
        """Which reads the API serves for Polymarket.

        ``GET /api/v1/coverage`` (operationId ``getCoverage``).

        Unauthenticated discovery endpoint that declares which V1 data surfaces the API serves
        for Polymarket, the one venue it covers. Every capability reports supported. Coverage is
        sports and esports markets only (#27299): a market outside them answers 404 not_found
        with error.reason ...
        """
        result: ApiResponse[GetCoverageResponse] = await self._call("getCoverage", path_params={}, query={})
        return result

    async def get_platforms(
        self,
    ) -> ApiResponse[GetCoverageResponse]:
        """Get platform capability matrix.

        ``GET /api/v1/platforms`` (operationId ``getPlatforms``).

        Deprecated since #16315: use GET /api/v1/coverage, which serves the same body. This path
        stays live until its sunset on 2027-02-01 (#29351) and answers with Deprecation, Sunset
        and successor Link headers; from that date it answers 410 Gone with error.code
        endpoint_retired. Unauthenticated discovery ...
        """
        result: ApiResponse[GetCoverageResponse] = await self._call("getPlatforms", path_params={}, query={})
        return result

    @overload
    async def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketHoldersResponse]: ...

    @overload
    async def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketHoldersResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_market_holders(
        self,
        condition_id: str,
        *,
        outcome: Literal["yes", "no", "all"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketHoldersResponse] | ApiResponse[NotModifiedResponse]:
        """List a market's graded holders.

        ``GET /api/v1/market/{condition_id}/holders`` (operationId ``getMarketHolders``).

        The graded holder roster of one market, the list a Pick of the Day shows for its market,
        for any Polymarket market: every S/A/B wallet with open shares on either outcome, from a
        complete provider holder scan, each with its shares, Polymarket's own currentValue for
        the leg, its grade, its win record ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            outcome: Keep holders netting one side. `all` (default) lists both.
            min_grade: Narrow within the graded cohort: `S` keeps S, `A` keeps S and A, `B` (default) keeps S, A and B. `C`, `D` and `F` are rejected with 400: the route lists the ...
            limit: Maximum holders per page. Out-of-range values are clamped to 1..100.
            cursor: Opaque pagination cursor from the previous response's next_cursor. New cursors carry an absolute next offset bound to normalized condition_id, outcome and ...
        """
        result: ApiResponse[GetMarketHoldersResponse] | ApiResponse[NotModifiedResponse] = await self._call("getMarketHolders", path_params={"condition_id": condition_id}, query={"outcome": outcome, "min_grade": min_grade, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketTopHoldersResponse]: ...

    @overload
    async def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketTopHoldersResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_market_top_holders(
        self,
        condition_id: str,
        *,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketTopHoldersResponse] | ApiResponse[NotModifiedResponse]:
        """List a market's top holders, every grade.

        ``GET /api/v1/market/{condition_id}/top-holders`` (operationId ``getMarketTopHolders``).

        The largest holders of one market on each outcome, every grade from S to F and ungraded
        wallets included: the table the market's event page shows under Top holders. Each
        outcome lists up to 100 wallets, largest `shares` first, from Polymarket's holder board,
        with the provider's current value, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum holders per outcome. Out-of-range values are clamped to 1..100. `totals` covers the whole sample whatever the limit.
        """
        result: ApiResponse[GetMarketTopHoldersResponse] | ApiResponse[NotModifiedResponse] = await self._call("getMarketTopHolders", path_params={"condition_id": condition_id}, query={"limit": limit}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketFlowResponse]: ...

    @overload
    async def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketFlowResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_market_flow(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketFlowResponse] | ApiResponse[NotModifiedResponse]:
        """Get a market's flow and top positions.

        ``GET /api/v1/market/{condition_id}/flow`` (operationId ``getMarketFlow``).

        Canonical since #16312; GET /api/v1/market/{condition_id}/intel is its deprecated alias
        and serves the same body under object market_intel. One market's flow and top positions:
        the signed flow of every tracked large trade in the window (net_flow_usd and its YES or
        NO direction), the large-trade ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        result: ApiResponse[GetMarketFlowResponse] | ApiResponse[NotModifiedResponse] = await self._call("getMarketFlow", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketIntelResponse]: ...

    @overload
    async def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketIntelResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Literal["1h", "4h", "24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketIntelResponse] | ApiResponse[NotModifiedResponse]:
        """Get market intelligence.

        ``GET /api/v1/market/{condition_id}/intel`` (operationId ``getMarketIntel``).

        Deprecated since #16312: use GET /api/v1/market/{condition_id}/flow, which serves the
        same body under object market_flow. This path stays live until its sunset on 2027-02-01
        (#29351), keeps object market_intel, and answers with Deprecation, Sunset and successor
        Link headers; from that date it ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        result: ApiResponse[GetMarketIntelResponse] | ApiResponse[NotModifiedResponse] = await self._call("getMarketIntel", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)
        return result

    async def batch_get_market_flow(
        self,
        body: BatchGetMarketFlowBody,
    ) -> ApiResponse[BatchGetMarketFlowResponse]:
        """Batch market flow.

        ``POST /api/v1/markets/flow/batch`` (operationId ``batchGetMarketFlow``).

        Returns each market's flow and top positions for 1-25 raw provider condition_id values.
        Results preserve request order, duplicate inputs return duplicate rows, and each item is
        charged one batch item unit before execution. Do not pass prefixed mkt_ IDs; use
        market.condition_id from search or ...
        """
        result: ApiResponse[BatchGetMarketFlowResponse] = await self._call("batchGetMarketFlow", path_params={}, query={}, body=body)
        return result

    async def batch_get_market_close(
        self,
        body: BatchGetMarketCloseBody,
    ) -> ApiResponse[BatchGetMarketCloseResponse]:
        """Batch market closing lines.

        ``POST /api/v1/markets/close/batch`` (operationId ``batchGetMarketClose``).

        Returns the closing line of 1-25 sports or esports markets in one request. Each ok
        item's data is the body GET /api/v1/market/{condition_id}/close returns for that market:
        status measured with both outcome legs, pending, or unavailable with unavailable_reason,
        judged at one clock for the whole ...
        """
        result: ApiResponse[BatchGetMarketCloseResponse] = await self._call("batchGetMarketClose", path_params={}, query={}, body=body)
        return result

    async def batch_get_market_intel(
        self,
        body: BatchGetMarketFlowBody,
    ) -> ApiResponse[BatchGetMarketIntelResponse]:
        """Batch market intelligence.

        ``POST /api/v1/markets/intel/batch`` (operationId ``batchGetMarketIntel``).

        Deprecated since #16312: use POST /api/v1/markets/flow/batch, which returns the same
        items under object market_flow_batch. This path stays live until its sunset on
        2027-02-01 (#29351), keeps object market_intel_batch, and answers with Deprecation,
        Sunset and successor Link headers; from that date ...
        """
        result: ApiResponse[BatchGetMarketIntelResponse] = await self._call("batchGetMarketIntel", path_params={}, query={}, body=body)
        return result

    @overload
    async def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketSnapshotResponse]: ...

    @overload
    async def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketSnapshotResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: list[Literal["trust"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketSnapshotResponse] | ApiResponse[NotModifiedResponse]:
        """Get market live snapshot.

        ``GET /api/v1/market/{condition_id}/snapshot`` (operationId ``getMarketSnapshot``).

        Provider-first market card snapshot with canonical identity, outcome labels, cached top-
        of-book when available, liquidity, live sports context, and explicit
        freshness/unavailable states.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            expand: Include trust metadata for current_price and spread_bps. Repeatable: trust.
        """
        result: ApiResponse[GetMarketSnapshotResponse] | ApiResponse[NotModifiedResponse] = await self._call("getMarketSnapshot", path_params={"condition_id": condition_id}, query={"expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketCandlesResponse]: ...

    @overload
    async def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketCandlesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Literal["1d", "1w"] | None = None,
        from_: int | None = None,
        to: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketCandlesResponse] | ApiResponse[NotModifiedResponse]:
        """Get market OHLC price candles.

        ``GET /api/v1/market/{condition_id}/candles`` (operationId ``getMarketCandles``).

        Provider-first bucketed OHLC price candles for a market's outcome tokens, derived from
        our stored copy of the Polymarket CLOB prices-history series (the same series the
        market-detail chart renders; covers open and resolved markets). Because the stored data
        is daily, a 1d bucket typically carries ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            resolution: Bucketing granularity. 1d aggregates by UTC calendar day, 1w by ISO week (Monday 00:00 UTC start). Defaults to 1d.
            from_: Exclusive lower bound as a URL-decoded unix timestamp in seconds; points at or before this timestamp are omitted (the underlying daily snapshot read filters ...
            to: Inclusive upper bound as a URL-decoded unix timestamp in seconds; points after this timestamp are omitted. If from is also present, from must be less than or ...
        """
        result: ApiResponse[GetMarketCandlesResponse] | ApiResponse[NotModifiedResponse] = await self._call("getMarketCandles", path_params={"condition_id": condition_id}, query={"resolution": resolution, "from": from_, "to": to}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketCloseResponse]: ...

    @overload
    async def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketCloseResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_market_close(
        self,
        condition_id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketCloseResponse] | ApiResponse[NotModifiedResponse]:
        """Get a market's closing line.

        ``GET /api/v1/market/{condition_id}/close`` (operationId ``getMarketClose``).

        The closing line of one sports or esports market: the price Polymarket's own price-
        history series recorded for each outcome in the last minute bucket that ended at or
        before kickoff (the market's game start time), read once after the market settles and
        stored unchanged. outcomes[0] is the YES leg ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetMarketCloseResponse] | ApiResponse[NotModifiedResponse] = await self._call("getMarketClose", path_params={"condition_id": condition_id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListMarketTradesResponse]: ...

    @overload
    async def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListMarketTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_market_trades(
        self,
        condition_id: str,
        *,
        from_: str | None = None,
        to: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListMarketTradesResponse] | ApiResponse[NotModifiedResponse]:
        """List a market's taker fills in a time window.

        ``GET /api/v1/market/{condition_id}/trades`` (operationId ``listMarketTrades``).

        One market's taker fills of 100 USD or more, newest first by (traded_at,
        transaction_hash, log_index), from 0xinsider's own record of the exchange's on-chain
        fills. Each fill appears once: its id is the transaction hash and the log index of its
        fill event, so a walk can be deduplicated and joined ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            from_: Inclusive RFC 3339 lower bound on traded_at. Omitted or earlier than coverage.recorded_from: the walk runs to the start of the record (coverage.recorded_from). ...
            to: Exclusive RFC 3339 upper bound on traded_at. A first page ends at the earlier of to and coverage.complete_through. With cursor, it must match the cursor's.
            limit: Page size. Out-of-range values are clamped to 1..500.
            cursor: Opaque mtr_v1_ cursor from next_cursor. It continues the walk before the last fill of the previous page and keeps the market, from and to it was issued for: ...
        """
        result: ApiResponse[ListMarketTradesResponse] | ApiResponse[NotModifiedResponse] = await self._call("listMarketTrades", path_params={"condition_id": condition_id}, query={"from": from_, "to": to, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)
        return result

    @overload
    async def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetMarketWalletsInOutResponse]: ...

    @overload
    async def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetMarketWalletsInOutResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_market_wallets_in_out(
        self,
        condition_id: str,
        *,
        window: Literal["24h", "7d"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetMarketWalletsInOutResponse] | ApiResponse[NotModifiedResponse]:
        """Get a market's net buyers and sellers.

        ``GET /api/v1/market/{condition_id}/wallets-in-out`` (operationId ``getMarketWalletsInOut``).

        One market's net buyers and net sellers over the last 24 hours or 7 days, live: the body
        the 0xinsider market page's wallets in/out panel reads for a Pro viewer, from the same
        aggregate and cache (reads are cached for up to 60 seconds). A wallet's net is its buys
        minus its sells in the window ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            window: The window the nets are summed over, ending at the read's clock: 24h (the default) or 7d.
        """
        result: ApiResponse[GetMarketWalletsInOutResponse] | ApiResponse[NotModifiedResponse] = await self._call("getMarketWalletsInOut", path_params={"condition_id": condition_id}, query={"window": window}, if_none_match=if_none_match)
        return result

    @overload
    async def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSuspiciousTradesResponse]: ...

    @overload
    async def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_suspicious_trades(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse]:
        """Get suspicious trades.

        ``GET /api/v1/suspicious-trades`` (operationId ``listSuspiciousTrades``).

        Stored trades whose recorded suspicion score meets the live flag threshold. Evidence
        contains the scorer's stored signals. Cursor-paginated by suspicion score. mode=live
        (default) uses fresh cached pages; mode=stable pins pagination to one published scoring
        generation and returns cursor_expired ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of suspicious trades to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
            mode: Pagination mode. live (default) keeps the 120-second response cache; stable pins the walk to one published scoring generation and binds the cursor to the limit ...
        """
        result: ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse] = await self._call("listSuspiciousTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity, "mode": mode}, if_none_match=if_none_match)
        return result

    @overload
    async def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetSuspiciousTradeResponse]: ...

    @overload
    async def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetSuspiciousTradeResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_suspicious_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetSuspiciousTradeResponse] | ApiResponse[NotModifiedResponse]:
        """Get suspicious trade by ID.

        ``GET /api/v1/suspicious-trades/{id}`` (operationId ``getSuspiciousTrade``).

        Returns one suspicious trade by raw whale_alerts.id or the rf_-prefixed id emitted by
        list responses. A flag on a market outside sports and esports returns 404 not_found with
        error.reason=market_out_of_scope (#27305); stop requesting it. Canonical since
        2026-09-23; GET /api/v1/insider-radar/{id} is ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetSuspiciousTradeResponse] | ApiResponse[NotModifiedResponse] = await self._call("getSuspiciousTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListGamesResponse]: ...

    @overload
    async def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListGamesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_games(
        self,
        *,
        sport: str | None = None,
        league: str | None = None,
        status: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | None = None,
        starts_after: str | None = None,
        starts_before: str | None = None,
        window: Literal["all", "now"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "settlement"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListGamesResponse] | ApiResponse[NotModifiedResponse]:
        """List covered games.

        ``GET /api/v1/games`` (operationId ``listGames``).

        One coherent game view per row: both sides with their provider ids and live scores, the
        UTC kickoff, the provider's own status, the esports series format, and the game's winner
        markets (the moneyline, or a soccer game's three 1X2 legs) with their condition ids and
        outcome token ids. Spreads, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            sport: Canonical sport bucket, case-insensitive, with - and _ read as a space: table-tennis and Table Tennis are the same bucket. Omit for every covered sport. A ...
            league: League tag, case-insensitive, as this list's coverage.leagues spells it (GET /api/v1/coverage lists no leagues): nfl, epl, cs2, euroleague, cbb, cwbb. ...
            status: Keep only games in this state. ended, cancelled and postponed also list finished games that have left the live board, read from their stored records, for ...
            starts_after: RFC 3339 instant. Keep only games whose kickoff is at or after it. Games with no published kickoff are excluded whenever either bound is set. With a finished ...
            starts_before: RFC 3339 instant. Keep only games whose kickoff is at or before it. Must be at or after starts_after.
            window: Which games to read. all, the default, lists the whole covered catalog, which can start with games the provider still holds open weeks after kickoff. now lists ...
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque gms_v1_ cursor from next_cursor. It pins the page position (kickoff and event_slug), not a snapshot: the catalog is live, so a game added or removed ...
            expand: sharp_money adds each game's sharp_money, the GameSharpMoney object GET /api/v1/games/{event_slug}/sharp-money returns, read from the sport board's cached ...
        """
        result: ApiResponse[ListGamesResponse] | ApiResponse[NotModifiedResponse] = await self._call("listGames", path_params={}, query={"sport": sport, "league": league, "status": status, "starts_after": starts_after, "starts_before": starts_before, "window": window, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    async def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetGameResponse]: ...

    @overload
    async def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetGameResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_game(
        self,
        event_slug: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetGameResponse] | ApiResponse[NotModifiedResponse]:
        """Get one game.

        ``GET /api/v1/games/{event_slug}`` (operationId ``getGame``).

        The same game object GET /api/v1/games returns, for one event_slug, including soccer 1X2
        home, draw and away market sides and draw_offered. The slug is the identity the
        live_sports_updated webhook pulse carries, so a receiver can read the full game straight
        from a pulse. A slug outside the ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetGameResponse] | ApiResponse[NotModifiedResponse] = await self._call("getGame", path_params={"event_slug": event_slug}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListGameMarketsResponse]: ...

    @overload
    async def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListGameMarketsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_game_markets(
        self,
        event_slug: str,
        *,
        sports_market_type: str | None = None,
        status: Literal["active", "closed", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        expand: list[Literal["sharp_money", "quotes", "trading_terms"]] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListGameMarketsResponse] | ApiResponse[NotModifiedResponse]:
        """List a game's markets.

        ``GET /api/v1/games/{event_slug}/markets`` (operationId ``listGameMarkets``).

        Every stored Polymarket market of one event_slug: the moneyline, spreads, totals, team
        totals, half and quarter lines, player props and the rest, plus the markets of the
        event's child events (a soccer game's exact score, halftime result and more-markets
        events), each with its own event_slug. The ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            sports_market_type: Comma-separated provider market types to keep, case-insensitive: spreads, totals, points, first_half_totals. Omitted keeps every type. An unknown type returns ...
            status: active, closed or all. closed means the provider closed the market or it resolved.
            limit: Page size. Out-of-range values are clamped to 1..100.
            cursor: Opaque gmk_v1_ cursor from next_cursor, sent with the same filters. It pins the page position (sports_market_type, line, condition_id), not a snapshot. A ...
            expand: sharp_money adds each row's sharp_money: the game page's per-line split, side USD and S, A and B wallet counts per outcome. One read for the event whatever the ...
        """
        result: ApiResponse[ListGameMarketsResponse] | ApiResponse[NotModifiedResponse] = await self._call("listGameMarkets", path_params={"event_slug": event_slug}, query={"sports_market_type": sports_market_type, "status": status, "limit": limit, "cursor": cursor, "expand": expand}, if_none_match=if_none_match)
        return result

    @overload
    async def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetGameSharpMoneyResponse]: ...

    @overload
    async def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetGameSharpMoneyResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_game_sharp_money(
        self,
        event_slug: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetGameSharpMoneyResponse] | ApiResponse[NotModifiedResponse]:
        """Get one game's sharp money.

        ``GET /api/v1/games/{event_slug}/sharp-money`` (operationId ``getGameSharpMoney``).

        Where the graded money sits on a whole game, in one read: the S, A and B grade wallets'
        USD on each outcome (home, away and, for a 1X2 game, draw) summed across the game's
        markets, each outcome's integer share, the leader and wallet counts by grade, with the
        backend's verdict on the split. It is ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetGameSharpMoneyResponse] | ApiResponse[NotModifiedResponse] = await self._call("getGameSharpMoney", path_params={"event_slug": event_slug}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListGameTradesResponse]: ...

    @overload
    async def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListGameTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_game_trades(
        self,
        event_slug: str,
        *,
        limit: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListGameTradesResponse] | ApiResponse[NotModifiedResponse]:
        """List a game's trades.

        ``GET /api/v1/games/{event_slug}/trades`` (operationId ``listGameTrades``).

        A game's newest fills across every market in it, newest first and live: the moneyline,
        spreads, totals and every prop, player props included. The same rows the 0xinsider game
        page's activity list shows a Pro viewer, read from the same live stream. Every fill, not
        only large ones: GET ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Newest fills to return. Out-of-range values are clamped to 1..200.
        """
        result: ApiResponse[ListGameTradesResponse] | ApiResponse[NotModifiedResponse] = await self._call("listGameTrades", path_params={"event_slug": event_slug}, query={"limit": limit}, if_none_match=if_none_match)
        return result

    async def get_game_holders(
        self,
        event_slug: str,
        *,
        condition_ids: list[str] | None = None,
        limit: int | None = None,
    ) -> ApiResponse[GetGameHoldersResponse]:
        """Get a game's holders.

        ``GET /api/v1/games/{event_slug}/holders`` (operationId ``getGameHolders``).

        The S, A and B graded holders of up to 25 markets of one game in one call. Each item is
        GET /api/v1/market/{condition_id}/holders for one market, unfiltered and cut to limit,
        with the same market, scan and totals beside it. Pass condition_ids from GET
        /api/v1/games/{event_slug}/markets; a market ...

        Query parameters:
            condition_ids: Required. 1 to 25 condition_id values of this game's markets, comma-separated. The key may also repeat (condition_ids=a&condition_ids=b). A raw provider condition_id or ...
            limit: Holders per market. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[GetGameHoldersResponse] = await self._call("getGameHolders", path_params={"event_slug": event_slug}, query={"condition_ids": condition_ids, "limit": limit})
        return result

    @overload
    async def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ListSuspiciousTradesResponse]: ...

    @overload
    async def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_insider_radar(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        min_suspicion: float | None = None,
        severity: Literal["flag", "watch"] | None = None,
        mode: Literal["live", "stable"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse]:
        """Get insider radar flags.

        ``GET /api/v1/insider-radar`` (operationId ``listInsiderRadar``).

        Deprecated alias of GET /api/v1/suspicious-trades (2026-09-23), kept live until its
        sunset on 2027-02-01 (#29351); responses carry Deprecation, Sunset and a Link
        rel="successor-version" to it, and from that date the path answers 410 Gone with
        error.code endpoint_retired. Stored trades whose ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            limit: Maximum number of radar flags to return. Out-of-range values are clamped to 1..100.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
            mode: Pagination mode. live (default) keeps the 120-second response cache; stable pins the walk to one published scoring generation and binds the cursor to the limit ...
        """
        result: ApiResponse[ListSuspiciousTradesResponse] | ApiResponse[NotModifiedResponse] = await self._call("listInsiderRadar", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity, "mode": mode}, if_none_match=if_none_match)
        return result

    @overload
    async def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetInsiderRadarFlagResponse]: ...

    @overload
    async def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetInsiderRadarFlagResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetInsiderRadarFlagResponse] | ApiResponse[NotModifiedResponse]:
        """Get insider radar flag by ID.

        ``GET /api/v1/insider-radar/{id}`` (operationId ``getInsiderRadarFlag``).

        Deprecated alias of GET /api/v1/suspicious-trades/{id} (2026-09-23), kept live until its
        sunset on 2027-02-01 (#29351); responses carry Deprecation, Sunset and a Link
        rel="successor-version" to it, and from that date the path answers 410 Gone with
        error.code endpoint_retired. The envelope keeps ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetInsiderRadarFlagResponse] | ApiResponse[NotModifiedResponse] = await self._call("getInsiderRadarFlag", path_params={"id": id}, query={}, if_none_match=if_none_match)
        return result

    async def get_event_replay_since(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        trader: str | None = None,
        condition_id: str | None = None,
        min_grade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | None = None,
        min_size: float | str | None = None,
        expand: list[Literal["trade"]] | None = None,
    ) -> ApiResponse[GetEventReplaySinceResponse]:
        """Replay public large-trade events.

        ``GET /api/v1/events/feed/since`` (operationId ``getEventReplaySince``).

        Returns durable public large-trade events strictly after an opaque cursor, in commit
        order: events are ordered by the position at which their write became visible to every
        reader (whale_alerts.inserted_xid), then by whale_alerts.id, and a page never reaches
        past the oldest write transaction still ...

        Query parameters:
            cursor: Opaque event replay cursor returned as next_cursor by a prior response. The cursor maps to the global (whale_alerts.inserted_xid, whale_alerts.id) commit-order ...
            limit: Maximum durable public whale-trade events to return. Out-of-range values are clamped to 1..100.
            trader: Only this wallet's trades: a wallet address, trd_-prefixed trader id or username resolved against the traders table. Bound to the cursor: a cursor issued under ...
            condition_id: Only trades on this market: the raw provider condition_id or its mkt_-prefixed id. Bound to the cursor.
            min_grade: Only trades by wallets at this grade or better (S best), read from the wallet's newest ranking at request time; a wallet with no grade never passes. For the ...
            min_grade_at_trade: Only trades whose grade_at_trade, the grade the wallet held when the trade filled, is at this grade or better (S best). Only a trade whose grade at the fill is ...
            min_size: Only trades of at least this USD amount. Decimal and scientific query spellings normalize exactly to cents, rounding half away from zero; maximum 1e15 USD. ...
            expand: Repeatable. trade adds the public trade read to every event (the object GET /api/v1/whale-trades/{id} returns for it), from one query per page, so a page of ...
        """
        result: ApiResponse[GetEventReplaySinceResponse] = await self._call("getEventReplaySince", path_params={}, query={"cursor": cursor, "limit": limit, "trader": trader, "condition_id": condition_id, "min_grade": min_grade, "min_grade_at_trade": min_grade_at_trade, "min_size": min_size, "expand": expand})
        return result

    async def list_webhooks(
        self,
    ) -> ApiResponse[ListWebhooksResponse]:
        """List builder webhook destinations.

        ``GET /api/v1/webhooks`` (operationId ``listWebhooks``).

        Returns webhook destinations owned by the authenticated API key user. Deleted endpoints
        are omitted; an endpoint paused with PATCH or disabled after consecutive failures is
        listed with status disabled. Subscribable event_types and their payload shapes are
        described by GET /api/v1/webhooks/events. ...
        """
        result: ApiResponse[ListWebhooksResponse] = await self._call("listWebhooks", path_params={}, query={})
        return result

    async def create_webhook(
        self,
        body: CreateWebhookRequest,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Create a builder webhook destination.

        ``POST /api/v1/webhooks`` (operationId ``createWebhook``).

        Creates a pending HTTPS webhook destination. The response includes one-time
        signing_secret and verification.token values. Deliveries are not sent until the endpoint
        is verified, and verification requires the destination to answer 2xx to a signed
        webhook.verification challenge (see POST ...
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("createWebhook", path_params={}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    async def list_webhook_events(
        self,
    ) -> ApiResponse[ListWebhookEventsResponse]:
        """List webhook event catalog.

        ``GET /api/v1/webhooks/events`` (operationId ``listWebhookEvents``).

        Self-describing catalog of every webhook event type: its description, data payload
        shape, and whether it is active (has a firing producer) or dormant (subscribable but not
        yet delivered; no event type is dormant today). The catalog is identical for every
        authenticated key and exposes no ...
        """
        result: ApiResponse[ListWebhookEventsResponse] = await self._call("listWebhookEvents", path_params={}, query={})
        return result

    async def list_webhook_deliveries(
        self,
        id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
    ) -> ApiResponse[ListWebhookDeliveriesResponse]:
        """List webhook delivery log.

        ``GET /api/v1/webhooks/{id}/deliveries`` (operationId ``listWebhookDeliveries``).

        Recent delivery attempts for one webhook destination owned by the authenticated API key
        user, newest first, with opaque cursor pagination. Returns 404 (identical to an unknown
        id) when the endpoint is not owned by the caller, so a non-owner cannot tell an owned-
        but-empty log apart from someone ...

        Query parameters:
            cursor: Opaque pagination cursor returned as next_cursor by a prior response. Omit to fetch the newest page.
            limit: Maximum delivery rows to return per page. Out-of-range values are clamped to 1..100.
        """
        result: ApiResponse[ListWebhookDeliveriesResponse] = await self._call("listWebhookDeliveries", path_params={"id": id}, query={"cursor": cursor, "limit": limit})
        return result

    async def redeliver_webhook_delivery(
        self,
        id: str,
        delivery_id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[RedeliverWebhookDeliveryResponse]:
        """Redeliver a dead-lettered webhook delivery.

        ``POST /api/v1/webhooks/{id}/deliveries/{delivery_id}/redeliver`` (operationId ``redeliverWebhookDelivery``).

        Returns one dead_letter delivery to the delivery queue with a fresh attempt budget:
        status becomes pending, attempt_count resets to 0, and next_attempt_at is now, so the
        delivery worker claims it like any queued delivery, under the same per-owner and per-
        origin concurrency limits. Use it after a ...
        """
        result: ApiResponse[RedeliverWebhookDeliveryResponse] = await self._call("redeliverWebhookDelivery", path_params={"id": id, "delivery_id": delivery_id}, query={}, idempotency_key=idempotency_key)
        return result

    async def get_webhook(
        self,
        id: str,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Get one builder webhook destination.

        ``GET /api/v1/webhooks/{id}`` (operationId ``getWebhook``).

        Returns one webhook destination owned by the authenticated API key user.
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("getWebhook", path_params={"id": id}, query={})
        return result

    async def update_webhook(
        self,
        id: str,
        body: UpdateWebhookRequest,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Update a builder webhook destination.

        ``PATCH /api/v1/webhooks/{id}`` (operationId ``updateWebhook``).

        Updates name, HTTPS URL, event types, or enabled state. URL changes force
        pending_verification and return a new verification token; the new destination must
        answer 2xx to the signed webhook.verification challenge before deliveries resume. A URL
        change returns 409 with ...
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("updateWebhook", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    async def delete_webhook(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Disable a builder webhook destination.

        ``DELETE /api/v1/webhooks/{id}`` (operationId ``deleteWebhook``).

        Soft-deletes a webhook destination owned by the authenticated API key user. Existing
        delivery audit rows remain retained.
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("deleteWebhook", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    async def verify_webhook(
        self,
        id: str,
        body: VerifyWebhookRequest,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Verify a builder webhook destination.

        ``POST /api/v1/webhooks/{id}/verify`` (operationId ``verifyWebhook``).

        Activates a pending webhook destination. Two conditions must both hold: the one-time
        verification token matches and has not expired, AND the destination answers 2xx to a
        signed challenge this operation POSTs to the endpoint's stored url. The challenge body
        is ...
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("verifyWebhook", path_params={"id": id}, query={}, body=body)
        return result

    async def prepare_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Prepare a staged builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/prepare`` (operationId ``prepareWebhookSecret``).

        Creates a pending signing secret while the current secret remains active. Deploy the
        returned one-time signing_secret to the receiver before calling activate. The response
        exposes secret_rotation.status=pending; an existing pending secret is returned again so
        a lost response can be recovered safely.
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("prepareWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    async def activate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Activate a staged builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/activate`` (operationId ``activateWebhookSecret``).

        Promotes the prepared signing secret to current, returns it once, and signs every
        delivery with both the new and previous secrets for one hour. Call retire after the
        receiver has completed its rollout. The current secret remains available through the
        existing immediate rotate-secret route for ...
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("activateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    async def retire_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Retire the previous builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret/retire`` (operationId ``retireWebhookSecret``).

        Ends the one-hour dual-signature overlap and removes the previous signing secret from
        future delivery authorization. Call this after the receiver accepts the activated
        secret. The operation is idempotent and does not return signing_secret.
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("retireWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    async def rotate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookResponse]:
        """Rotate a builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret`` (operationId ``rotateWebhookSecret``).

        Rotates the endpoint signing secret and returns the new signing_secret once in the
        response. Returns 409 with error.reason=webhook_delivery_in_progress while a live
        delivery freezes the current signing nonce; retry after it completes.
        """
        result: ApiResponse[CreateWebhookResponse] = await self._call("rotateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)
        return result

    @overload
    async def get_health(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetHealthResponse]: ...

    @overload
    async def get_health(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetHealthResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_health(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetHealthResponse] | ApiResponse[NotModifiedResponse]:
        """Health check.

        ``GET /api/v1/health`` (operationId ``getHealth``).

        Returns API health status. No authentication required. Limited to 120 requests per
        minute per IP.

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetHealthResponse] | ApiResponse[NotModifiedResponse] = await self._call("getHealth", path_params={}, query={}, if_none_match=if_none_match)
        return result

    async def create_mcp_json_rpc_response(
        self,
        body: CreateMcpJsonRpcResponseBody,
    ) -> ApiResponse[CreateMcpJsonRpcResponseResponse]:
        """Remote MCP endpoint (JSON-RPC).

        ``POST /api/v1/mcp`` (operationId ``createMcpJsonRpcResponse``).

        Model Context Protocol (MCP) Streamable HTTP transport. Accepts one JSON-RPC 2.0 request
        or notification. ID-bearing initialize, ping, tools/list, and tools/call requests (and
        server/discover on revision 2026-07-28) receive one same-ID JSON-RPC response; an
        unknown method, or a notification method ...
        """
        result: ApiResponse[CreateMcpJsonRpcResponseResponse] = await self._call("createMcpJsonRpcResponse", path_params={}, query={}, body=body)
        return result

    async def get_reports(
        self,
        *,
        granularity: Literal["daily", "weekly", "monthly"] | None = None,
        period: str | None = None,
    ) -> ApiResponse[GetReportsResponse]:
        """Unified report snapshot (granularity selector).

        ``GET /api/v1/reports`` (operationId ``getReports``).

        Unified convenience route (#4975) that consolidates the three singular report routes.
        Dispatches to the exact per-granularity cap (daily 50, weekly 100, monthly 200) and date
        window the legacy /api/v1/reports/{daily,weekly,monthly} routes use, so the response
        body is byte-identical to the matching ...

        Query parameters:
            granularity: Required. Report granularity selector.
            period: Required. Period token for the granularity. daily: UTC date YYYY-MM-DD. weekly: ISO week YYYY-WW for a durable canonical snapshot, or a from,to YYYY-MM-DD pair for an ...
        """
        result: ApiResponse[GetReportsResponse] = await self._call("getReports", path_params={}, query={"granularity": granularity, "period": period})
        return result

    async def get_daily_report_snapshot(
        self,
        *,
        date: str | None = None,
    ) -> ApiResponse[GetReportsResponse]:
        """Daily report snapshot.

        ``GET /api/v1/reports/daily`` (operationId ``getDailyReportSnapshot``).

        Returns a dated daily whale-activity report snapshot with source_range, snapshot.status,
        completeness, and reconciliation metadata. Report whale volume is local whale-alert
        activity volume, not provider lifetime trader volume.

        Query parameters:
            date: Required. UTC report date in YYYY-MM-DD format, from 2024-03-01 (the first day report data covers) through tomorrow UTC. Any other date returns 400 bad_request with ...
        """
        result: ApiResponse[GetReportsResponse] = await self._call("getDailyReportSnapshot", path_params={}, query={"date": date})
        return result

    async def get_weekly_report_snapshot(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        week: str | None = None,
    ) -> ApiResponse[GetReportsResponse]:
        """Weekly report snapshot.

        ``GET /api/v1/reports/weekly`` (operationId ``getWeeklyReportSnapshot``).

        Returns a weekly whale-activity report snapshot. Pass an ISO YYYY-WW token for a durable
        canonical snapshot, or an exact from/to UTC range of at most 31 inclusive days for an
        ephemeral response. The response identifies closed ranges as final and current ranges as
        rolling.

        Query parameters:
            from_: UTC source-range start in YYYY-MM-DD format; required with to. Together with to, selects an exact ephemeral range of at most 31 inclusive UTC days. A start ...
            to: UTC source-range end in YYYY-MM-DD format; required with from. Together with from, selects an exact ephemeral range of at most 31 inclusive UTC days. An end ...
            week: ISO week selector in YYYY-WW format; alternative to from/to. Selects a durable canonical snapshot. A week that ends before 2024-03-01, the first day report ...
        """
        result: ApiResponse[GetReportsResponse] = await self._call("getWeeklyReportSnapshot", path_params={}, query={"from": from_, "to": to, "week": week})
        return result

    async def get_monthly_report_snapshot(
        self,
        *,
        month: str | None = None,
    ) -> ApiResponse[GetReportsResponse]:
        """Monthly report snapshot.

        ``GET /api/v1/reports/monthly`` (operationId ``getMonthlyReportSnapshot``).

        Returns a UTC monthly whale-activity report snapshot with source_range, completeness,
        and reconciliation metadata.

        Query parameters:
            month: Required. UTC report month in YYYY-MM format. A month that ends before 2024-03-01, the first day report data covers, or starts after tomorrow UTC returns 400 bad_request ...
        """
        result: ApiResponse[GetReportsResponse] = await self._call("getMonthlyReportSnapshot", path_params={}, query={"month": month})
        return result

    @overload
    async def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[GetResolutionReportResponse]: ...

    @overload
    async def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[GetResolutionReportResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_resolution_report(
        self,
        *,
        date: str | None = None,
        view: Literal["full", "totals"] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetResolutionReportResponse] | ApiResponse[NotModifiedResponse]:
        """Get the daily resolution report.

        ``GET /api/v1/reports/resolutions`` (operationId ``getResolutionReport``).

        One UTC day's resolved markets: how often the side the profitable (S, A and B grade)
        wallets held won, beside how often every qualifying wallet's side won, one vote each.
        `markets` lists each market they held a position in, with the consensus side, its
        confidence, and the full roster of wallets, ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            date: Required. UTC report date in YYYY-MM-DD format, no later than today UTC. Any other value returns 400 bad_request with error.param=date.
            view: `totals` returns the counts without `markets`. Any other value than full or totals returns 400 bad_request with error.param=view.
        """
        result: ApiResponse[GetResolutionReportResponse] | ApiResponse[NotModifiedResponse] = await self._call("getResolutionReport", path_params={}, query={"date": date, "view": view}, if_none_match=if_none_match)
        return result

    async def get_trader_export_snapshot(
        self,
        address: str,
    ) -> ApiResponse[GetTraderExportSnapshotResponse]:
        """Trader export snapshot metadata.

        ``GET /api/v1/trader/{address}/export`` (operationId ``getTraderExportSnapshot``).

        Returns export source-range, completeness, volume reconciliation, row-count estimate,
        and large-export policy for one trader. To download the full dataset programmatically,
        POST to this same path to submit an async export job (json | ndjson | csv), then poll
        the status route and follow the download ...
        """
        result: ApiResponse[GetTraderExportSnapshotResponse] = await self._call("getTraderExportSnapshot", path_params={"address": address}, query={})
        return result

    async def submit_trader_export(
        self,
        address: str,
        *,
        format: Literal["json", "ndjson", "csv"] | None = None,
        fresh: bool | None = None,
    ) -> ApiResponse[TraderExportJob]:
        """Submit a trader dataset export job.

        ``POST /api/v1/trader/{address}/export`` (operationId ``submitTraderExport``).

        Queues an async export of the trader's full dataset in the requested format (json
        default, ndjson, or csv) and returns the job resource. Poll the status route at
        poll_after_s until terminal is true, then follow the download route while status is
        'ready' (until expires_at, 24 hours from submit). ...

        Query parameters:
            format: Output serialization. json = full envelope document (default); ndjson = full envelope as line 1 then one trade object per line; csv = flat trades rows only.
            fresh: true: do not reuse a finished, running or reconciling job; only a queued job is reused, so the file is a snapshot read after this submit. Consumes quota when ...
        """
        result: ApiResponse[TraderExportJob] = await self._call("submitTraderExport", path_params={"address": address}, query={"format": format, "fresh": fresh})
        return result

    async def get_trader_export_status(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> ApiResponse[TraderExportJob]:
        """Poll a trader export job.

        ``GET /api/v1/trader/{address}/export/status`` (operationId ``getTraderExportStatus``).

        Returns the job resource for a submitted export: status (queued | running |
        cancel_requested | reconcile_required | ready | failed | expired | cancelled), terminal,
        next_action and poll_after_s, the lifecycle timestamps, the retention window
        (expires_at) and, once the file is written, data_as_of ...

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        result: ApiResponse[TraderExportJob] = await self._call("getTraderExportStatus", path_params={"address": address}, query={"job_id": job_id})
        return result

    async def cancel_trader_export(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> ApiResponse[TraderExportJob]:
        """Cancel a trader export job.

        ``POST /api/v1/trader/{address}/export/cancel`` (operationId ``cancelTraderExport``).

        Cancels a submitted export and returns the job resource, the same shape the status route
        returns. A queued job reads cancelled at once and no worker will start it. A running job
        reads cancel_requested until the worker reaches its next safe point, then cancelled: the
        worker checks every 5 seconds ...

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        result: ApiResponse[TraderExportJob] = await self._call("cancelTraderExport", path_params={"address": address}, query={"job_id": job_id})
        return result

    async def download_trader_export(
        self,
        address: str,
        *,
        job_id: int | None = None,
    ) -> AsyncDownload:
        """Download a finished trader export.

        ``GET /api/v1/trader/{address}/export/download`` (operationId ``downloadTraderExport``).

        Redirects (302) to a presigned URL lasting at most one hour and no later than the job's
        expires_at for the finished export file while the job status is 'ready' and expires_at
        has not passed. The file is gzip-compressed and served with the format's Content-Type
        (application/json, ...

        Returns an ``AsyncDownload``: the redirect is followed once, without the credential, and
        the file is streamed. Iterate it, ``asave(path)`` it for its SHA-256, or ``aread()`` it
        (bounded); ``aclose()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.

        Query parameters:
            job_id: Required. Export job id returned by the submit route.
        """
        return await self._download("downloadTraderExport", path_params={"address": address}, query={"job_id": job_id})

    async def get_usage(
        self,
    ) -> ApiResponse[Usage]:
        """Inspect current API usage without spending primary request quota.

        ``GET /api/v1/usage`` (operationId ``getUsage``).

        Returns the authenticated caller sliding-window request budget, UTC-day usage and
        monthly quota. This control-plane endpoint remains available for a valid credential
        after paid data access lapses and does not increment the primary Redis rate-limit
        counter, monthly quota or API usage table; it ...
        """
        result: ApiResponse[Usage] = await self._call("getUsage", path_params={}, query={})
        return result

    async def get_market_context_markdown(
        self,
        condition_id: str,
    ) -> ApiResponse[str]:
        """Get market context (Markdown).

        ``GET /api/v1/market/{condition_id}/context.md`` (operationId ``getMarketContextMarkdown``).

        Authenticated, self-contained Polymarket market evidence document. Renders the same
        typed data as the market snapshot with trust included: identity, outcome labels and
        tokens, cached quotes, liquidity, live sports, and per-source freshness or unavailable
        reasons. Provider text is encoded as ...
        """
        result: ApiResponse[str] = await self._call("getMarketContextMarkdown", path_params={"condition_id": condition_id}, query={})
        return result

    async def get_account_identity(
        self,
    ) -> ApiResponse[AccountIdentity]:
        """Identify the authenticated account and credential.

        ``GET /api/v1/me`` (operationId ``getAccountIdentity``).

        Returns caller-owned account and credential IDs, credential validity, paid-data
        entitlement and approved scopes. Null scopes mean full legacy developer-key access.
        Valid credentials can use this control-plane diagnostic path after paid access lapses;
        data routes still require active paid access. ...
        """
        result: ApiResponse[AccountIdentity] = await self._call("getAccountIdentity", path_params={}, query={})
        return result

    async def submit_whale_dataset(
        self,
        body: SubmitWhaleDatasetBody,
    ) -> ApiResponse[WhaleDatasetJob]:
        """Create an immutable whale dataset.

        ``POST /api/v1/datasets/whale-trades`` (operationId ``submitWhaleDataset``).

        Extract at most 1,000,000 rows and 256 MiB uncompressed; exceeding either bound fails
        the job and publishes no partial file. Window and filters freeze on admission; rows and
        source facts freeze on one worker database snapshot. NDJSON uses exact decimal strings,
        with no current grade or market ...
        """
        result: ApiResponse[WhaleDatasetJob] = await self._call("submitWhaleDataset", path_params={}, query={}, body=body)
        return result

    async def get_whale_dataset_status(
        self,
        job_id: str,
    ) -> ApiResponse[WhaleDatasetJob]:
        """Read a whale dataset job.

        ``GET /api/v1/datasets/whale-trades/{job_id}`` (operationId ``getWhaleDatasetStatus``).

        Read queued, running, cancel_requested, ready, failed, reconcile_required, expired or
        cancelled. Poll only while next_action is poll, after poll_after_s. Ready manifests
        contain count, content and compressed SHA-256, schema, filters, source, horizon, expiry
        and replay continuation. Deltas do not ...
        """
        result: ApiResponse[WhaleDatasetJob] = await self._call("getWhaleDatasetStatus", path_params={"job_id": job_id}, query={})
        return result

    async def download_whale_dataset(
        self,
        job_id: str,
    ) -> AsyncDownload:
        """Download an immutable whale dataset.

        ``GET /api/v1/datasets/whale-trades/{job_id}/download`` (operationId ``downloadWhaleDataset``).

        Download only a ready artifact; status handles failure and cancellation. Retired
        artifacts return 410 at serving time. Paid export scope; jobs are private to the
        credential owner. Shares the 20/day owner export quota and fair worker admission with
        trader exports; datasets also have a combined ...

        Returns an ``AsyncDownload``: the redirect is followed once, without the credential, and
        the file is streamed. Iterate it, ``asave(path)`` it for its SHA-256, or ``aread()`` it
        (bounded); ``aclose()`` it when done. A redirect or transfer fault raises
        ``DownloadError``; the API's own errors raise ``OxinsiderApiError``.
        """
        return await self._download("downloadWhaleDataset", path_params={"job_id": job_id}, query={})

    async def cancel_whale_dataset(
        self,
        job_id: str,
    ) -> ApiResponse[WhaleDatasetJob]:
        """Cancel a whale dataset job.

        ``POST /api/v1/datasets/whale-trades/{job_id}/cancel`` (operationId ``cancelWhaleDataset``).

        Cancel queued jobs immediately and request running jobs stop at their next safe point.
        Repeating cancel converges on the current state; cancellation after the completion fence
        leaves the artifact ready. Paid export scope; jobs are private to the credential owner.
        Shares the 20/day owner export ...
        """
        result: ApiResponse[WhaleDatasetJob] = await self._call("cancelWhaleDataset", path_params={"job_id": job_id}, query={})
        return result

    @overload
    async def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[GetPickOfTheDayLedgerEntryResponse]: ...

    @overload
    async def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[GetPickOfTheDayLedgerEntryResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_pick_of_the_day_ledger_entry(
        self,
        pick_id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[GetPickOfTheDayLedgerEntryResponse] | ApiResponse[NotModifiedResponse]:
        """Read a pick proof by stable id.

        ``GET /api/v1/pick-of-the-day/ledger/{pick_id}`` (operationId ``getPickOfTheDayLedgerEntry``).

        Public read of one published pick by its stable decimal-string pick_id. Same proof
        gating, canonical bytes, ETag and integrity failures as the ledger. Invalid ids return
        400; absent or unpublished picks return 404. Withdrawal from recommendations or the
        archive does not remove a published ledger ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[GetPickOfTheDayLedgerEntryResponse] | ApiResponse[NotModifiedResponse] = await self._call("getPickOfTheDayLedgerEntry", path_params={"pick_id": pick_id}, query={}, if_none_match=if_none_match)
        return result

    async def create_webhook_verification_attempt(
        self,
        id: str,
        body: CreateWebhookVerificationAttemptRequest,
        *,
        idempotency_key: str | None = None,
    ) -> ApiResponse[CreateWebhookVerificationAttemptResponse]:
        """Admit asynchronous webhook verification.

        ``POST /api/v1/webhooks/{id}/verification-attempts`` (operationId ``createWebhookVerificationAttempt``).

        Additive asynchronous consent flow; the legacy POST /verify keeps its synchronous
        200/422 behavior and retry policy. Commits one durable attempt and returns 202 without
        awaiting DNS or the receiver. Send the original verification_token. Optional
        Idempotency-Key replays the original admission ...
        """
        result: ApiResponse[CreateWebhookVerificationAttemptResponse] = await self._call("createWebhookVerificationAttempt", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)
        return result

    async def get_webhook_verification_attempt(
        self,
        id: str,
        attempt_id: str,
    ) -> ApiResponse[CreateWebhookVerificationAttemptResponse]:
        """Read webhook verification attempt status.

        ``GET /api/v1/webhooks/{id}/verification-attempts/{attempt_id}`` (operationId ``getWebhookVerificationAttempt``).

        Fresh primary-database status for one attempt owned by the authenticated account and
        webhook. queued/running means consent is pending; only verified activates the unchanged
        endpoint after receiver 2xx. failed/cancelled/expired are terminal. Polling never issues
        a challenge or restarts work. At ...
        """
        result: ApiResponse[CreateWebhookVerificationAttemptResponse] = await self._call("getWebhookVerificationAttempt", path_params={"id": id, "attempt_id": attempt_id}, query={})
        return result

    @overload
    async def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[ComboFillsResponse]: ...

    @overload
    async def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[ComboFillsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def list_combo_fills(
        self,
        *,
        result: str | None = None,
        legs: str | None = None,
        min_stake: int | None = None,
        min_multiplier: int | None = None,
        grades: str | None = None,
        sports: str | None = None,
        sort: Literal["recent", "largest", "payout"] | None = None,
        window: Literal["24h", "7d", "all"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        offset: int | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[ComboFillsResponse] | ApiResponse[NotModifiedResponse]:
        """List combo fills.

        ``GET /api/v1/combos/fills`` (operationId ``listComboFills``).

        Returns live Polymarket combo taker fills with exact decimal-string economics, wallet
        identities, grades, legs, conjunction results, and ingest coverage. Requires an active
        Pro or Max API key. Listing includes executions with price at most 0.95; use combo
        detail for complete history. Sports and ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            result: CSV of pending, won, or lost; all clears the filter. Unknown results appear only in unfiltered lists.
            legs: CSV of 2, 3, 4, or 5+; all clears the filter. A combo matches any named pick count.
            min_stake: Minimum collateral in whole USDC.
            min_multiplier: 0 disables the filter; otherwise use 2..1000000. Minimum shares per dollar at execution.
            grades: CSV of S, A, B, C, D, F; all clears the filter. Ungraded wallets do not match.
            sports: CSV of nfl, ncaaf, nba, wnba, baseball, hockey, soccer, tennis, table-tennis, esports, mma, boxing, golf, cricket, f1, pickleball; all clears the filter. ...
            sort: Recent is newest first; largest ranks collateral; payout ranks buy-fill shares and excludes sells.
            window: Defaults to all for recent and 24h for largest or payout.
            limit: Page size. Integer values outside the range are clamped to 1..200.
            cursor: Exclusive block_number:log_index cursor for recent only; send the returned next_cursor unchanged.
            offset: Offset for ranked largest or payout ordering; use returned next_offset.
        """
        result: ApiResponse[ComboFillsResponse] | ApiResponse[NotModifiedResponse] = await self._call("listComboFills", path_params={}, query={"result": result, "legs": legs, "min_stake": min_stake, "min_multiplier": min_multiplier, "grades": grades, "sports": sports, "sort": sort, "window": window, "limit": limit, "cursor": cursor, "offset": offset}, if_none_match=if_none_match)
        return result

    @overload
    async def get_combos_summary(
        self,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[CombosSummaryResponse]: ...

    @overload
    async def get_combos_summary(
        self,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[CombosSummaryResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_combos_summary(
        self,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[CombosSummaryResponse] | ApiResponse[NotModifiedResponse]:
        """Get live combo count.

        ``GET /api/v1/combos/summary`` (operationId ``getCombosSummary``).

        Returns the stored count of traded combos whose YES conjunction remains pending, with
        its computation timestamp. Sports and esports only (#27449): a combo with a leg outside
        them is not counted. Requires an active Pro or Max API key. The count is refreshed by
        the ingest owner at most every five ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[CombosSummaryResponse] | ApiResponse[NotModifiedResponse] = await self._call("getCombosSummary", path_params={}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: None = None,
    ) -> ApiResponse[ComboResponse]: ...

    @overload
    async def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: str | None,
    ) -> ApiResponse[ComboResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_combo(
        self,
        condition_id: str,
        *,
        if_none_match: str | None = None,
    ) -> ApiResponse[ComboResponse] | ApiResponse[NotModifiedResponse]:
        """Get combo detail.

        ``GET /api/v1/combos/{condition_id}`` (operationId ``getCombo``).

        Returns one Polymarket combo with its legs, conjunction result, all-time trade totals,
        newest 100 taker fills, lifecycle totals, and ingest coverage. Requires an active Pro or
        Max API key. Detail retains execution history above the listing price cap. A malformed
        combo ID returns 400; an unknown ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.
        """
        result: ApiResponse[ComboResponse] | ApiResponse[NotModifiedResponse] = await self._call("getCombo", path_params={"condition_id": condition_id}, query={}, if_none_match=if_none_match)
        return result

    @overload
    async def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: None = None,
    ) -> ApiResponse[EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse]: ...

    @overload
    async def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: str | None,
    ) -> ApiResponse[EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse] | ApiResponse[NotModifiedResponse]: ...

    async def get_edge_hunter(
        self,
        *,
        view: Literal["board", "signals", "observations"] | None = None,
        category: str | None = None,
        cohort: Literal["wider_holder", "in_play", "emerging_pile"] | None = None,
        admission: Literal["most_held_48h", "most_held_48h_by_type"] | None = None,
        min_grade: Literal["S", "A", "B"] | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        horizon_hours: int | None = None,
        kind: Literal["sports", "esports"] | None = None,
        sports: list[str] | None = None,
        leagues: list[str] | None = None,
        market_types: list[str] | None = None,
        condition_ids: list[str] | None = None,
        event_slugs: list[str] | None = None,
        series_slugs: list[str] | None = None,
        if_none_match: str | None = None,
    ) -> ApiResponse[EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse] | ApiResponse[NotModifiedResponse]:
        """Get Edge Hunter.

        ``GET /api/v1/edge-hunter`` (operationId ``getEdgeHunter``).

        Max-only canonical Edge Hunter API with board, signals and observations views. An active
        Pro credential receives 403 forbidden with reason max_plan_required. Default board
        admission and ordering remain compatible: B grade floor, 30-row cap, 48-hour kickoff
        horizon, full Max projection and both ...

        Pass ``if_none_match`` with the previous ``etag`` to make the read conditional: a 304
        then returns ``NotModifiedResponse`` and your cached body is still current.

        Query parameters:
            view: Response mode. board preserves the full quoted board; signals exposes ranked records and category evidence; observations exposes cohort measurements and ...
            category: Legacy canonical bucket alias, now accepted in every view. Provider aliases canonicalize: NFL reaches Football and EPL reaches Soccer. Use leagues for a ...
            cohort: Required for view=observations; wider_holder, in_play or emerging_pile. Rejected for board and signals. wider_holder covers pregame markets that view=signals ...
            admission: Opt-in admission rule for view=observations with cohort=wider_holder; rejected for every other view and cohort. most_held_48h returns the most-held selection ...
            min_grade: Board and signals: S, A or B, default B. Requires a piled-side holder at the selected grade floor or better, without removing other holders. Rejected for ...
            limit: Board row cap defaults to 30 and clamps integer values to 1..30; total counts selected admitted rows before the cap. Signals and observations page size ...
            cursor: Opaque canonical Edge Hunter cursor from next_cursor. Bound to view, every normalized selection axis, grade/horizon where applicable, source snapshot and ...
            horizon_hours: Kickoff window for board (default 48) or signals (default 12). Integer values clamp to 1..48. Rejected for observations, whose pre-game universe is fixed at 48 ...
            kind: All views: sports excludes the Esports bucket; esports selects only Esports. Omit for both. Combines with other selections using AND. Selected reads echo ...
            sports: Canonical sport buckets, including Esports and Table Tennis, matched case-insensitively. Unknown names and league aliases such as NFL are rejected in sports; ...
            leagues: Normalized machine/provider league identities, such as nfl, cfb, nba, epl, cs2, lol, dota2 or valorant. Known wire/tag aliases normalize; other provider keys ...
            market_types: Exact provider sports_market_type values. This is an open provider taxonomy, distinct from exact market IDs. Read market_context.market_type; missing selected ...
            condition_ids: Exact market selections. Raw provider condition IDs and the existing mkt_-prefixed aliases normalize to raw IDs. Unknown well-formed IDs return an empty ...
            event_slugs: Exact provider event slugs. Use event_slug returned on the row; no title or slug-prefix guessing. All views. Repeat this query key or put comma-separated ...
            series_slugs: Exact provider series slugs. Read market_context.series_slug; a missing selected series excludes the row. All views. Repeat this query key or put ...
        """
        result: ApiResponse[EdgeHunterBoardResponse | EdgeHunterSignalsResponse | EdgeHunterObservationsResponse] | ApiResponse[NotModifiedResponse] = await self._call("getEdgeHunter", path_params={}, query={"view": view, "category": category, "cohort": cohort, "admission": admission, "min_grade": min_grade, "limit": limit, "cursor": cursor, "horizon_hours": horizon_hours, "kind": kind, "sports": sports, "leagues": leagues, "market_types": market_types, "condition_ids": condition_ids, "event_slugs": event_slugs, "series_slugs": series_slugs}, if_none_match=if_none_match)
        return result

