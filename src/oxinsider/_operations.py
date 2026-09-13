"""Generated from the 0xinsider OpenAPI document by scripts/generate.py. Do not edit."""

from __future__ import annotations

from typing import Any, NamedTuple


OPENAPI_VERSION = "1.0.0"


class Operation(NamedTuple):
    method: str
    path: str
    streaming: bool = False


OPERATIONS: dict[str, Operation] = {
    "getApiDiscovery": Operation("GET", "/api/v1", streaming=False),
    "redirectApiOpenapiSpec": Operation("GET", "/api/v1/openapi.json", streaming=False),
    "getTrader": Operation("GET", "/api/v1/trader/{address}", streaming=False),
    "getTraderContextMarkdown": Operation("GET", "/api/v1/trader/{address}/context.md", streaming=False),
    "getTraderContext": Operation("GET", "/api/v1/trader/{address}/context", streaming=False),
    "batchGetTraders": Operation("POST", "/api/v1/traders/batch", streaming=False),
    "getPositionTimeline": Operation("GET", "/api/v1/trader/{address}/position-timeline", streaming=False),
    "getTraderPnl": Operation("GET", "/api/v1/trader/{address}/pnl", streaming=False),
    "getPositionTimelineById": Operation("GET", "/api/v1/traders/{trader}/position-timeline", streaming=False),
    "listPositions": Operation("GET", "/api/v1/positions", streaming=False),
    "listLargePositions": Operation("GET", "/api/v1/large-positions", streaming=False),
    "listWhaleTrades": Operation("GET", "/api/v1/whale-trades", streaming=False),
    "listWhaleTradeHistory": Operation("GET", "/api/v1/whale-trades/history", streaming=False),
    "getWhaleTrade": Operation("GET", "/api/v1/whale-trades/{id}", streaming=False),
    "listWhaleTradeCounterpartyExecutions": Operation("GET", "/api/v1/whale-trades/{id}/counterparties/executions", streaming=False),
    "listWhaleTradeCounterpartyMakers": Operation("GET", "/api/v1/whale-trades/{id}/counterparties/executions/{execution_id}/makers", streaming=False),
    "listLeaderboard": Operation("GET", "/api/v1/leaderboard", streaming=False),
    "getPickOfTheDay": Operation("GET", "/api/v1/pick-of-the-day", streaming=False),
    "getPickOfTheDayArchive": Operation("GET", "/api/v1/pick-of-the-day/archive", streaming=False),
    "listTrendingWallets": Operation("GET", "/api/v1/leaderboard/trending", streaming=False),
    "searchMarkets": Operation("GET", "/api/v1/markets/search", streaming=False),
    "searchContent": Operation("GET", "/api/v1/content/search", streaming=False),
    "exploreMarkets": Operation("GET", "/api/v1/markets/explore", streaming=False),
    "listSmartMoneyFlows": Operation("GET", "/api/v1/markets/smart-money-flows", streaming=False),
    "listSharpMoneyFlows": Operation("GET", "/api/v1/markets/sharp-money-flows", streaming=False),
    "listSportsEdgeSignals": Operation("GET", "/api/v1/sports-edge-signals", streaming=False),
    "listSportsEdgeObservations": Operation("GET", "/api/v1/sports-edge-observations", streaming=False),
    "getPlatforms": Operation("GET", "/api/v1/platforms", streaming=False),
    "getMarketIntel": Operation("GET", "/api/v1/market/{condition_id}/intel", streaming=False),
    "batchGetMarketIntel": Operation("POST", "/api/v1/markets/intel/batch", streaming=False),
    "getMarketSnapshot": Operation("GET", "/api/v1/market/{condition_id}/snapshot", streaming=False),
    "getMarketCandles": Operation("GET", "/api/v1/market/{condition_id}/candles", streaming=False),
    "listInsiderRadar": Operation("GET", "/api/v1/insider-radar", streaming=False),
    "getInsiderRadarFlag": Operation("GET", "/api/v1/insider-radar/{id}", streaming=False),
    "getStream": Operation("GET", "/api/v1/stream", streaming=True),
    "getEventReplaySince": Operation("GET", "/api/v1/events/feed/since", streaming=False),
    "listWebhooks": Operation("GET", "/api/v1/webhooks", streaming=False),
    "createWebhook": Operation("POST", "/api/v1/webhooks", streaming=False),
    "listWebhookEvents": Operation("GET", "/api/v1/webhooks/events", streaming=False),
    "listWebhookDeliveries": Operation("GET", "/api/v1/webhooks/{id}/deliveries", streaming=False),
    "getWebhook": Operation("GET", "/api/v1/webhooks/{id}", streaming=False),
    "updateWebhook": Operation("PATCH", "/api/v1/webhooks/{id}", streaming=False),
    "deleteWebhook": Operation("DELETE", "/api/v1/webhooks/{id}", streaming=False),
    "verifyWebhook": Operation("POST", "/api/v1/webhooks/{id}/verify", streaming=False),
    "rotateWebhookSecret": Operation("POST", "/api/v1/webhooks/{id}/rotate-secret", streaming=False),
    "getHealth": Operation("GET", "/api/v1/health", streaming=False),
    "openMcpEventStream": Operation("GET", "/api/v1/mcp", streaming=True),
    "createMcpJsonRpcResponse": Operation("POST", "/api/v1/mcp", streaming=False),
    "getReports": Operation("GET", "/api/v1/reports", streaming=False),
    "getDailyReportSnapshot": Operation("GET", "/api/v1/reports/daily", streaming=False),
    "getWeeklyReportSnapshot": Operation("GET", "/api/v1/reports/weekly", streaming=False),
    "getMonthlyReportSnapshot": Operation("GET", "/api/v1/reports/monthly", streaming=False),
    "getTraderExportSnapshot": Operation("GET", "/api/v1/trader/{address}/export", streaming=False),
    "submitTraderExport": Operation("POST", "/api/v1/trader/{address}/export", streaming=False),
    "getTraderExportStatus": Operation("GET", "/api/v1/trader/{address}/export/status", streaming=False),
    "downloadTraderExport": Operation("GET", "/api/v1/trader/{address}/export/download", streaming=False),
    "getUsage": Operation("GET", "/api/v1/usage", streaming=False),
}


class OperationsMixin:
    """One method per documented operation. Each returns the decoded JSON body."""

    def _call(self, operation_id: str, **kwargs: Any) -> Any:  # pragma: no cover - provided by Client
        raise NotImplementedError

    def get_api_discovery(
        self,
    ) -> Any:
        """API discovery.

        ``GET /api/v1`` (operationId ``getApiDiscovery``).

        Unauthenticated API-origin discovery document pointing agents to the canonical API base
        URL, full docs, web-origin OpenAPI spec, health check, and the COMPLETE index of
        authenticated data routes. data.authenticated_routes is the whole authenticated route
        surface, not a sample: it carries every ...
        """
        return self._call("getApiDiscovery", path_params={}, query={})

    def redirect_api_openapi_spec(
        self,
    ) -> Any:
        """Redirect to the canonical OpenAPI spec.

        ``GET /api/v1/openapi.json`` (operationId ``redirectApiOpenapiSpec``).

        Unauthenticated API-origin compatibility redirect to the canonical web-origin OpenAPI
        JSON document at https://0xinsider.com/api/v1/openapi.json.
        """
        return self._call("redirectApiOpenapiSpec", path_params={}, query={})

    def get_trader(
        self,
        address: str,
        *,
        expand: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Get trader intelligence.

        ``GET /api/v1/trader/{address}`` (operationId ``getTrader``).

        Returns a trader's grade (S through F; ranked about 95% by realized profit, with
        calibration, track record, and consistency as a tie-breaker and proven-trader
        guardrails), P&L, win rate, and optional strategy/category data. The path accepts either
        an Ethereum wallet address, a known trader ...

        Query parameters:
            expand: Include heavy fields and trust metadata. Repeatable: strategy, categories, quant_metrics, trust.
        """
        return self._call("getTrader", path_params={"address": address}, query={"expand": expand}, if_none_match=if_none_match)

    def get_trader_context_markdown(
        self,
        address: str,
    ) -> Any:
        """Get trader context (Markdown).

        ``GET /api/v1/trader/{address}/context.md`` (operationId ``getTraderContextMarkdown``).

        Returns a single human- and LLM-readable Markdown briefing for one trader: identity,
        grade, P&L, position coverage, and freshness. The path accepts an Ethereum wallet
        address (0x...), a known trader username, or a trd_-prefixed trader ID emitted by this
        API. Unknown traders still return 200 with a ...
        """
        return self._call("getTraderContextMarkdown", path_params={"address": address}, query={})

    def get_trader_context(
        self,
        address: str,
        *,
        if_none_match: str | None = None,
    ) -> Any:
        """Get trader context (JSON).

        ``GET /api/v1/trader/{address}/context`` (operationId ``getTraderContext``).

        Returns a single structured context object for one trader: the full trader profile (same
        shape as GET /api/v1/trader/{address}) plus a position_summary (sync coverage and
        realized/unrealized P&L rollups, with an as_of open-position freshness clock), the
        data_as_of freshness timestamp (the ...
        """
        return self._call("getTraderContext", path_params={"address": address}, query={}, if_none_match=if_none_match)

    def batch_get_traders(
        self,
        body: Any,
    ) -> Any:
        """Batch trader intelligence.

        ``POST /api/v1/traders/batch`` (operationId ``batchGetTraders``).

        Returns trader intelligence for 1-25 wallet addresses or known usernames. Results
        preserve request order, duplicate inputs return duplicate rows, and each item is charged
        one batch item unit before execution. Unknown trader lookups return data with
        sync_status "unknown" matching the single trader ...
        """
        return self._call("batchGetTraders", path_params={}, query={}, body=body)

    def get_position_timeline(
        self,
        address: str,
        *,
        condition_id: Any = None,
        limit: Any = None,
        cursor: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Get a trader's position timeline for one market.

        ``GET /api/v1/trader/{address}/position-timeline`` (operationId ``getPositionTimeline``).

        Returns stored Polymarket fills for one tracked trader in one market, newest first, with
        outcome-specific running_amount and running_avg_price including earlier stored fills
        before pagination. The {address} segment accepts the same identity shapes as the plural
        alias: wallet, username, ...

        Query parameters:
            condition_id: Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        return self._call("getPositionTimeline", path_params={"address": address}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)

    def get_trader_pnl(
        self,
        address: str,
    ) -> Any:
        """Get trader P&L time series.

        ``GET /api/v1/trader/{address}/pnl`` (operationId ``getTraderPnl``).

        Returns a trader's daily P&L time series and pre-derived stats from the precomputed
        daily_pnl read model: entries (daily cumulative P&L), period stats (all/90d/30d/7d),
        monthly aggregation, per-year totals, and the drawdown series. Reads the refreshed read
        model, not a per-request equity replay. A ...
        """
        return self._call("getTraderPnl", path_params={"address": address}, query={})

    def get_position_timeline_by_id(
        self,
        trader: str,
        *,
        condition_id: Any = None,
        limit: Any = None,
        cursor: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Get a trader's position timeline (unified identity resolver).

        ``GET /api/v1/traders/{trader}/position-timeline`` (operationId ``getPositionTimelineById``).

        Unified trader-timeline route (#4975). {trader} accepts all five identity shapes - 0x...
        wallet, username, trd_-prefixed trader id, bare integer id, and @username (a username
        lookup only, for all-digit usernames) - resolved by the single shared trader-identity
        resolver. Returns stored Polymarket ...

        Query parameters:
            condition_id: Market condition_id. One timeline per (trader, market).
            limit: Maximum number of timeline events to return.
            cursor: Pagination cursor from previous response's next_cursor.
        """
        return self._call("getPositionTimelineById", path_params={"trader": trader}, query={"condition_id": condition_id, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)

    def list_positions(
        self,
        *,
        limit: Any = None,
        cursor: Any = None,
        min_size: Any = None,
        category: Any = None,
        min_grade: Any = None,
        side: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """List current positions (positions-board feed).

        ``GET /api/v1/positions`` (operationId ``listPositions``).

        Returns the current positions-board feed backed by the wallet_positions mirror. Ordered
        by current_value_usd DESC with deterministic (wallet, condition_id, outcome_index)
        tiebreakers. Pre-reconcile rows (current_value_usd IS NULL) are excluded. Cursor-
        paginated. Every filter pushes into SQL.

        Query parameters:
            limit: Maximum number of current positions to return.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum current position value in USD.
            category: Exact match against provider-backed market_canonical.category.
            min_grade: Minimum trader grade allowlist. `A` matches S and A; `B` matches S, A, B; etc.
            side: Filter by the binary outcome side. `yes` maps to outcome_index=0, `no` to outcome_index=1.
        """
        return self._call("listPositions", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "side": side}, if_none_match=if_none_match)

    def list_large_positions(
        self,
        *,
        limit: Any = None,
        cursor: Any = None,
        min_size: Any = None,
        category: Any = None,
        min_grade: Any = None,
        condition_id: Any = None,
    ) -> Any:
        """List large positions.

        ``GET /api/v1/large-positions`` (operationId ``listLargePositions``).

        Returns the largest current open positions from graded traders, value-descending, with
        opaque cursor pagination. Polymarket-only by design: the large-positions scanner filters
        platform = 'polymarket' (backend/crates/large-positions/src/scanner.rs), so only
        Polymarket rows are scanned and an unknown ...

        Query parameters:
            limit: Maximum number of large positions to return.
            cursor: Opaque pagination cursor from a previous response.
            min_size: Minimum position value in USD.
            category: One RFC 4180 CSV record of exact current provider-backed market_canonical.category values. Legacy unquoted lists such as NBA,WNBA remain valid; values ...
            min_grade: Minimum trader grade.
            condition_id: Scope to one market. Accepts the raw provider condition_id or the mkt_-prefixed market id (round-trips a value from a list response). Polymarket-only; an ...
        """
        return self._call("listLargePositions", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "condition_id": condition_id})

    def list_whale_trades(
        self,
        *,
        limit: Any = None,
        cursor: Any = None,
        min_size: Any = None,
        category: Any = None,
        min_grade: Any = None,
        suspicious_only: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """List whale trades.

        ``GET /api/v1/whale-trades`` (operationId ``listWhaleTrades``).

        Returns recent large trades with signal scoring and persisted suspicion facts. Filter by
        size, category, trader grade, or persisted suspicion. Filters are applied before
        pagination, and every request uses SQL-backed limit + 1 pagination so has_more and
        next_cursor reflect the filtered result set. ...

        Query parameters:
            limit: Maximum number of recent large trades to return.
            cursor: Pagination cursor from previous response's next_cursor.
            min_size: Minimum trade size in USD.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade.
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
        """
        return self._call("listWhaleTrades", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "category": category, "min_grade": min_grade, "suspicious_only": suspicious_only}, if_none_match=if_none_match)

    def list_whale_trade_history(
        self,
        *,
        limit: Any = None,
        cursor: Any = None,
        min_size: Any = None,
        condition_id: Any = None,
        trader: Any = None,
        category: Any = None,
        min_grade: Any = None,
        suspicious_only: Any = None,
        platform: Any = None,
        from_: Any = None,
        to: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Replay historical whale trades.

        ``GET /api/v1/whale-trades/history`` (operationId ``listWhaleTradeHistory``).

        Returns historical whale trades from local whale_alerts rows, not request-time provider
        fetches. Filter by condition_id, trader, category, minimum grade, persisted suspicion,
        platform, and RFC3339 from/to windows. All filters are pushed into SQL before LIMIT,
        every request uses SQL-backed limit + 1 ...

        Query parameters:
            limit: Maximum number of historical large trades to return.
            cursor: Pagination cursor from previous response's next_cursor. Prefix: wth_. URL-encode when replaying as a query parameter.
            min_size: Minimum trade size in USD.
            condition_id: Exact raw provider condition_id. Unknown markets return an empty list.
            trader: Trader wallet address, timestamp-suffixed wallet alias, or username resolved against the traders table. Unknown traders return an empty list.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            min_grade: Minimum trader grade.
            suspicious_only: When true, return only rows with persisted suspicion_score >= 60. The filter is applied before SQL-backed limit + 1 pagination.
            platform: Filter by whale_alerts.platform. all is equivalent to omitted.
            from_: Inclusive RFC3339 lower bound on whale_alerts.traded_at.
            to: Exclusive RFC3339 upper bound on whale_alerts.traded_at. Must be after from when both are present.
        """
        return self._call("listWhaleTradeHistory", path_params={}, query={"limit": limit, "cursor": cursor, "min_size": min_size, "condition_id": condition_id, "trader": trader, "category": category, "min_grade": min_grade, "suspicious_only": suspicious_only, "platform": platform, "from": from_, "to": to}, if_none_match=if_none_match)

    def get_whale_trade(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> Any:
        """Get whale trade by ID.

        ``GET /api/v1/whale-trades/{id}`` (operationId ``getWhaleTrade``).

        Returns one whale trade by raw whale_alerts.id or the wt_-prefixed id emitted by list
        and history responses.
        """
        return self._call("getWhaleTrade", path_params={"id": id}, query={}, if_none_match=if_none_match)

    def list_whale_trade_counterparty_executions(
        self,
        id: str,
        *,
        snapshot_id: Any = None,
        cursor: Any = None,
        limit: Any = None,
    ) -> Any:
        """Page counterparty executions.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions`` (operationId ``listWhaleTradeCounterpartyExecutions``).

        Returns a bounded execution page from the immutable snapshot emitted by whale-trade
        detail. A stale or changed snapshot returns a cursor-expired error so clients restart
        from detail.

        Query parameters:
            snapshot_id: Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of counterparty execution rows to return.
        """
        return self._call("listWhaleTradeCounterpartyExecutions", path_params={"id": id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})

    def list_whale_trade_counterparty_makers(
        self,
        id: str,
        execution_id: str,
        *,
        snapshot_id: Any = None,
        cursor: Any = None,
        limit: Any = None,
    ) -> Any:
        """Page maker counterparties.

        ``GET /api/v1/whale-trades/{id}/counterparties/executions/{execution_id}/makers`` (operationId ``listWhaleTradeCounterpartyMakers``).

        Returns a bounded maker-wallet page for one exact execution. Percentages keep the
        complete execution denominator across pages.

        Query parameters:
            snapshot_id: Counterparty snapshot ID from the whale trade detail response.
            cursor: Opaque cursor from the previous response's next_cursor.
            limit: Maximum number of maker rows to return.
        """
        return self._call("listWhaleTradeCounterpartyMakers", path_params={"id": id, "execution_id": execution_id}, query={"snapshot_id": snapshot_id, "cursor": cursor, "limit": limit})

    def list_leaderboard(
        self,
        *,
        limit: Any = None,
        cursor: Any = None,
        category: Any = None,
        strategy: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Get trader leaderboard.

        ``GET /api/v1/leaderboard`` (operationId ``listLeaderboard``).

        Returns ranked traders (grades S/A/B) sorted by score descending. Supports cursor
        pagination and optional category/strategy filters.

        Query parameters:
            limit: Maximum number of ranked traders to return.
            cursor: Opaque lbv1_ pagination cursor from a prior response. It binds the finite score/address boundary to the committed leaderboard generation and the effective ...
            category: Filter by category. Values are matched to canonical category buckets: political variants (Elections, Global Politics, U.S. Politics, ...) fold into Politics, ...
            strategy: Filter by ML-detected strategy type. Values come from backend/crates/analytics/src/trader_analysis/classification/decision_tree.rs and are matched exactly ...
        """
        return self._call("listLeaderboard", path_params={}, query={"limit": limit, "cursor": cursor, "category": category, "strategy": strategy}, if_none_match=if_none_match)

    def get_pick_of_the_day(
        self,
        *,
        if_none_match: str | None = None,
    ) -> Any:
        """Get today's Pick of the Day.

        ``GET /api/v1/pick-of-the-day`` (operationId ``getPickOfTheDay``).

        Returns the published picks for the current product day. Pro tier. `picks` holds up to
        six ranked picks. Each pick carries the backed side, the pre-game price, the $100
        return, the sharp-money holders, the grade, and a thesis. The price is frozen before
        kickoff. A prior day's pick never appears ...
        """
        return self._call("getPickOfTheDay", path_params={}, query={}, if_none_match=if_none_match)

    def get_pick_of_the_day_archive(
        self,
        *,
        if_none_match: str | None = None,
    ) -> Any:
        """Get the Pick of the Day track record.

        ``GET /api/v1/pick-of-the-day/archive`` (operationId ``getPickOfTheDayArchive``).

        Returns every published pick with its outcome, unit score, closing-line value, and the
        rolling hit rate. Resolved picks are public. A pending pick's backed side appears only
        for an authenticated Pro key. Each row carries a CLV value or the reason it was not
        measured. Coverage divides measured rows ...
        """
        return self._call("getPickOfTheDayArchive", path_params={}, query={}, if_none_match=if_none_match)

    def list_trending_wallets(
        self,
        *,
        limit: Any = None,
        cursor: Any = None,
        window: Any = None,
    ) -> Any:
        """List trending wallets.

        ``GET /api/v1/leaderboard/trending`` (operationId ``listTrendingWallets``).

        Returns wallets ranked by Polymarket weekly/monthly P&L (Polymarket-only discovery),
        with opaque page-cursor pagination. trending_pnl_usd and the by-PNL row order come from
        Polymarket's canonical leaderboard (data-
        api.polymarket.com/v1/leaderboard?timePeriod=week|month&orderBy=PNL), not a locally ...

        Query parameters:
            limit: Polymarket's weekly leaderboard caps the ranked set at 50 wallets; requests above 50 still return at most 50.
            cursor: Opaque pagination cursor from a previous response.
            window: Trailing window.
        """
        return self._call("listTrendingWallets", path_params={}, query={"limit": limit, "cursor": cursor, "window": window})

    def search_markets(
        self,
        *,
        q: Any = None,
        limit: Any = None,
        cursor: Any = None,
        status: Any = None,
        category: Any = None,
    ) -> Any:
        """Search markets.

        ``GET /api/v1/markets/search`` (operationId ``searchMarkets``).

        Search prediction markets by keyword. Returns representative market matches with status,
        category, and platform metadata. Cursor pagination advances over grouped market results
        rather than raw sub-market rows.

        Query parameters:
            q: Search query. Must be 1-512 characters before whitespace trimming and non-empty after trimming.
            limit: Maximum number of matching markets to return.
            cursor: Pagination cursor from previous response's next_cursor.
            status: Filter by market status.
            category: Filter by category.
        """
        return self._call("searchMarkets", path_params={}, query={"q": q, "limit": limit, "cursor": cursor, "status": status, "category": category})

    def search_content(
        self,
        *,
        q: Any = None,
        limit: Any = None,
    ) -> Any:
        """Search editorial content.

        ``GET /api/v1/content/search`` (operationId ``searchContent``).

        Search 0xinsider editorial content by keyword. Returns backend-owned learn, glossary,
        comparison, research, and trading-strategy items with canonical URLs. Opaque ranking
        scores are not exposed.

        Query parameters:
            q: Search query. Must be 1-256 characters before whitespace trimming and non-empty after trimming.
            limit: Maximum content items to return.
        """
        return self._call("searchContent", path_params={}, query={"q": q, "limit": limit})

    def explore_markets(
        self,
        *,
        category: Any = None,
        status: Any = None,
        platform: Any = None,
        sort: Any = None,
        cursor: Any = None,
        limit: Any = None,
        q: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Explore markets.

        ``GET /api/v1/markets/explore`` (operationId ``exploreMarkets``).

        Browse whale-active titled markets with category, platform, status, and keyword filters.
        Explore is Polymarket-only: the platform parameter is accepted for backward-
        compatibility but every request returns Polymarket markets. Paginates visible discovery
        entries rather than raw market rows, returns ...

        Query parameters:
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            status: Filter by market status.
            platform: Filter by source platform. Explore is Polymarket-only; polymarket is the only supported value and the parameter is accepted for backward-compatibility but does ...
            sort: Sort order for the discovery feed.
            cursor: Opaque pagination cursor from the previous response.
            limit: Page size.
            q: Keyword search against market titles. At most 64 characters before whitespace trimming.
        """
        return self._call("exploreMarkets", path_params={}, query={"category": category, "status": status, "platform": platform, "sort": sort, "cursor": cursor, "limit": limit, "q": q}, if_none_match=if_none_match)

    def list_smart_money_flows(
        self,
        *,
        timeframe: Any = None,
        limit: Any = None,
        cursor: Any = None,
        category: Any = None,
        platform: Any = None,
        min_grade: Any = None,
        direction: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """List ranked smart-money flows.

        ``GET /api/v1/markets/smart-money-flows`` (operationId ``listSmartMoneyFlows``).

        Ranks markets by absolute net S/A/B-grade whale flow over a requested timeframe. Use
        this discovery endpoint to answer where smart money is flowing before drilling into a
        specific market with /api/v1/market/{condition_id}/intel. Pagination is anchored by an
        opaque cursor carrying the first page ...

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp plus the last row's absolute net flow and condition_id.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
        """
        return self._call("listSmartMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction}, if_none_match=if_none_match)

    def list_sharp_money_flows(
        self,
        *,
        timeframe: Any = None,
        limit: Any = None,
        cursor: Any = None,
        category: Any = None,
        platform: Any = None,
        min_grade: Any = None,
        direction: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """List ranked sharp-money flows.

        ``GET /api/v1/markets/sharp-money-flows`` (operationId ``listSharpMoneyFlows``).

        Canonical alias of /api/v1/markets/smart-money-flows, which remains live but deprecated.
        Ranks markets by absolute net S/A/B-grade whale flow over a requested timeframe. Use
        this discovery endpoint to answer where sharp money is flowing before drilling into a
        specific market with ...

        Query parameters:
            timeframe: Lookback window for grade-filtered whale flow aggregation.
            limit: Page size.
            cursor: Opaque cursor from previous response's next_cursor. Encodes the first-page as_of timestamp plus the last row's absolute net flow and condition_id.
            category: Filter by market category (case-insensitive). A canonical bucket name (e.g. Basketball) matches every provider member that folds into it (NBA, WNBA, NCAAB); a ...
            platform: Filter by source platform. all is a request-side no-op.
            min_grade: Minimum latest trader grade included in the flow. Default B means S/A/B only; unranked traders are excluded.
            direction: Optional post-aggregate flow direction filter.
        """
        return self._call("listSharpMoneyFlows", path_params={}, query={"timeframe": timeframe, "limit": limit, "cursor": cursor, "category": category, "platform": platform, "min_grade": min_grade, "direction": direction}, if_none_match=if_none_match)

    def list_sports_edge_signals(
        self,
        *,
        category: Any = None,
        limit: Any = None,
        cursor: Any = None,
        horizon_hours: Any = None,
        min_grade: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """List ranked pre-game sports-edge signals.

        ``GET /api/v1/sports-edge-signals`` (operationId ``listSportsEdgeSignals``).

        Pro-tier. Ranked list of upcoming pre-game sports markets (moneyline + props) where
        graded (S/A/B) sharp money is piled on one side, each row carrying signal_created_at
        (the UTC time its immutable snapshot was computed), the piled side, its grade
        distribution, kickoff, piled-side Polymarket CLOB ...

        Query parameters:
            category: Optional canonical sport bucket filter (e.g. Basketball, Tennis, Soccer). A raw provider value (NBA) resolves to its canonical bucket. A non-sport category ...
            limit: Page size.
            cursor: Opaque cursor from a previous response's next_cursor. Encodes the snapshot anchor plus the last row's directional_rank_score, conviction_score, smart_score and ...
            horizon_hours: Kickoff ceiling in hours from now; the floor is now (only games not yet started). Clamped to 1..48.
            min_grade: Minimum trader grade required on the piled side. Only S, A, B are accepted (the piled-side grade distribution is S/A/B only; C, D, F return 400). Default B ...
        """
        return self._call("listSportsEdgeSignals", path_params={}, query={"category": category, "limit": limit, "cursor": cursor, "horizon_hours": horizon_hours, "min_grade": min_grade}, if_none_match=if_none_match)

    def list_sports_edge_observations(
        self,
        *,
        cohort: Any = None,
        category: Any = None,
        limit: Any = None,
        cursor: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """List observation-only sports-edge cohorts.

        ``GET /api/v1/sports-edge-observations`` (operationId ``listSportsEdgeObservations``).

        Pro-tier. Measures three explicitly observation-only Polymarket sports cohorts without
        changing or feeding GET /api/v1/sports-edge-signals: wider_holder measures pre-game
        holder piles outside the funded route's exact raw signals admission, including recent-
        flow rows rejected by its event, bucket, ...

        Query parameters:
            cohort: Observation cohort. wider_holder measures pre-game holder piles outside the funded route's exact raw signals admission. in_play admits only provider-confirmed ...
            category: Optional canonical sport bucket. Omitted or blank selects all registered sports. Raw provider categories resolve through the canonical taxonomy, including ...
            limit: Page size.
            cursor: Server-authenticated opaque seo_v2_ cursor from next_cursor. Pins snapshot_as_of, cohort, rank, and condition_id; pre-deploy unsigned seo_ cursors are ...
        """
        return self._call("listSportsEdgeObservations", path_params={}, query={"cohort": cohort, "category": category, "limit": limit, "cursor": cursor}, if_none_match=if_none_match)

    def get_platforms(
        self,
    ) -> Any:
        """Get platform capability matrix.

        ``GET /api/v1/platforms`` (operationId ``getPlatforms``).

        Unauthenticated discovery endpoint that declares which V1 intelligence surfaces are
        supported, partial, or unsupported per provider platform.
        """
        return self._call("getPlatforms", path_params={}, query={})

    def get_market_intel(
        self,
        condition_id: str,
        *,
        timeframe: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Get market intelligence.

        ``GET /api/v1/market/{condition_id}/intel`` (operationId ``getMarketIntel``).

        Smart money flow analysis for a specific market — net flow direction, whale trade count,
        buy/sell volumes, and top graded trader positions.

        Query parameters:
            timeframe: Lookback window for whale flow aggregation.
        """
        return self._call("getMarketIntel", path_params={"condition_id": condition_id}, query={"timeframe": timeframe}, if_none_match=if_none_match)

    def batch_get_market_intel(
        self,
        body: Any,
    ) -> Any:
        """Batch market intelligence.

        ``POST /api/v1/markets/intel/batch`` (operationId ``batchGetMarketIntel``).

        Returns smart-money market intelligence for 1-25 raw provider condition_id values.
        Results preserve request order, duplicate inputs return duplicate rows, and each item is
        charged one batch item unit before execution. Do not pass prefixed mkt_ IDs; use
        market.condition_id from search or explore.
        """
        return self._call("batchGetMarketIntel", path_params={}, query={}, body=body)

    def get_market_snapshot(
        self,
        condition_id: str,
        *,
        expand: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Get market live snapshot.

        ``GET /api/v1/market/{condition_id}/snapshot`` (operationId ``getMarketSnapshot``).

        Provider-first market card snapshot with canonical identity, outcome labels, cached top-
        of-book when available, liquidity, live sports context, and explicit
        freshness/unavailable states.

        Query parameters:
            expand: Include trust metadata for current_price and spread_bps. Repeatable: trust.
        """
        return self._call("getMarketSnapshot", path_params={"condition_id": condition_id}, query={"expand": expand}, if_none_match=if_none_match)

    def get_market_candles(
        self,
        condition_id: str,
        *,
        resolution: Any = None,
        from_: Any = None,
        to: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Get market OHLC price candles.

        ``GET /api/v1/market/{condition_id}/candles`` (operationId ``getMarketCandles``).

        Provider-first bucketed OHLC price candles for a market's outcome tokens, derived from
        the stored token_price_snapshots series (the same series the market-detail chart
        renders; covers open and resolved markets). Because the stored data is daily, a 1d
        bucket typically carries one point so its ...

        Query parameters:
            resolution: Bucketing granularity. 1d aggregates by UTC calendar day, 1w by ISO week (Monday 00:00 UTC start). Defaults to 1d.
            from_: Exclusive lower bound as a unix timestamp in seconds; points at or before this timestamp are omitted (the underlying daily snapshot read filters bucket_start > ...
            to: Inclusive upper bound as a unix timestamp in seconds; points after this timestamp are omitted.
        """
        return self._call("getMarketCandles", path_params={"condition_id": condition_id}, query={"resolution": resolution, "from": from_, "to": to}, if_none_match=if_none_match)

    def list_insider_radar(
        self,
        *,
        limit: Any = None,
        cursor: Any = None,
        min_suspicion: Any = None,
        severity: Any = None,
        if_none_match: str | None = None,
    ) -> Any:
        """Get insider radar flags.

        ``GET /api/v1/insider-radar`` (operationId ``listInsiderRadar``).

        Stored trades whose recorded suspicion score meets the live flag threshold. Evidence
        contains the scorer's stored signals. Cursor-paginated by suspicion score.

        Query parameters:
            limit: Maximum number of radar flags to return.
            cursor: Pagination cursor from previous response.
            min_suspicion: Minimum suspicion score (0-100). The live flag floor of 60 also applies.
            severity: Compatible filter. flag selects live threshold crossings. watch returns no rows because no live watch policy exists.
        """
        return self._call("listInsiderRadar", path_params={}, query={"limit": limit, "cursor": cursor, "min_suspicion": min_suspicion, "severity": severity}, if_none_match=if_none_match)

    def get_insider_radar_flag(
        self,
        id: str,
        *,
        if_none_match: str | None = None,
    ) -> Any:
        """Get insider radar flag by ID.

        ``GET /api/v1/insider-radar/{id}`` (operationId ``getInsiderRadarFlag``).

        Returns one suspicious-trading radar flag by raw whale_alerts.id or the rf_-prefixed id
        emitted by list responses.
        """
        return self._call("getInsiderRadarFlag", path_params={"id": id}, query={}, if_none_match=if_none_match)

    def get_event_replay_since(
        self,
        *,
        cursor: Any = None,
        limit: Any = None,
    ) -> Any:
        """Replay public whale-trade intelligence events.

        ``GET /api/v1/events/feed/since`` (operationId ``getEventReplaySince``).

        Returns durable public whale-trade intelligence events strictly after an opaque cursor
        backed by whale_alerts.id. This is a separate API-key contract from the browser/session
        /api/events/feed stream: browser-only and private alert, following, radar, and position
        patch events are excluded until they ...

        Query parameters:
            cursor: Opaque event replay cursor returned as next_cursor by a prior response. The cursor maps to whale_alerts.id and is valid across backend replicas. Omit to fetch ...
            limit: Maximum durable public whale-trade events to return.
        """
        return self._call("getEventReplaySince", path_params={}, query={"cursor": cursor, "limit": limit})

    def list_webhooks(
        self,
    ) -> Any:
        """List builder webhook destinations.

        ``GET /api/v1/webhooks`` (operationId ``listWebhooks``).

        Returns webhook destinations owned by the authenticated API key user. Disabled endpoints
        are omitted. Subscribable event_types and their payload shapes are described by GET
        /api/v1/webhooks/events. Four subscribable event types are Pro-only and only deliver to
        API keys on an active Pro ...
        """
        return self._call("listWebhooks", path_params={}, query={})

    def create_webhook(
        self,
        body: Any,
        *,
        idempotency_key: str | None = None,
    ) -> Any:
        """Create a builder webhook destination.

        ``POST /api/v1/webhooks`` (operationId ``createWebhook``).

        Creates a pending HTTPS webhook destination. The response includes one-time
        signing_secret and verification.token values. Deliveries are not sent until the endpoint
        is verified, and verification requires the destination to answer 2xx to a signed
        webhook.verification challenge (see POST ...
        """
        return self._call("createWebhook", path_params={}, query={}, body=body, idempotency_key=idempotency_key)

    def list_webhook_events(
        self,
    ) -> Any:
        """List webhook event catalog.

        ``GET /api/v1/webhooks/events`` (operationId ``listWebhookEvents``).

        Self-describing catalog of every webhook event type: its description, data payload
        shape, and whether it is active (has a firing producer) or dormant (subscribable but not
        yet delivered). The catalog is identical for every authenticated key and exposes no
        owner-scoped data. Pro-only event types ...
        """
        return self._call("listWebhookEvents", path_params={}, query={})

    def list_webhook_deliveries(
        self,
        id: str,
        *,
        cursor: Any = None,
        limit: Any = None,
    ) -> Any:
        """List webhook delivery log.

        ``GET /api/v1/webhooks/{id}/deliveries`` (operationId ``listWebhookDeliveries``).

        Recent delivery attempts for one webhook destination owned by the authenticated API key
        user, newest first, with opaque cursor pagination. Returns 404 (identical to an unknown
        id) when the endpoint is not owned by the caller, so a non-owner cannot tell an owned-
        but-empty log apart from someone ...

        Query parameters:
            cursor: Opaque pagination cursor returned as next_cursor by a prior response. Omit to fetch the newest page.
            limit: Maximum delivery rows to return per page.
        """
        return self._call("listWebhookDeliveries", path_params={"id": id}, query={"cursor": cursor, "limit": limit})

    def get_webhook(
        self,
        id: str,
    ) -> Any:
        """Get one builder webhook destination.

        ``GET /api/v1/webhooks/{id}`` (operationId ``getWebhook``).

        Returns one webhook destination owned by the authenticated API key user.
        """
        return self._call("getWebhook", path_params={"id": id}, query={})

    def update_webhook(
        self,
        id: str,
        body: Any,
        *,
        idempotency_key: str | None = None,
    ) -> Any:
        """Update a builder webhook destination.

        ``PATCH /api/v1/webhooks/{id}`` (operationId ``updateWebhook``).

        Updates name, HTTPS URL, event types, or enabled state. URL changes force
        pending_verification and return a new verification token; the new destination must
        answer 2xx to the signed webhook.verification challenge before deliveries resume. A URL
        change returns 409 with ...
        """
        return self._call("updateWebhook", path_params={"id": id}, query={}, body=body, idempotency_key=idempotency_key)

    def delete_webhook(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> Any:
        """Disable a builder webhook destination.

        ``DELETE /api/v1/webhooks/{id}`` (operationId ``deleteWebhook``).

        Soft-deletes a webhook destination owned by the authenticated API key user. Existing
        delivery audit rows remain retained.
        """
        return self._call("deleteWebhook", path_params={"id": id}, query={}, idempotency_key=idempotency_key)

    def verify_webhook(
        self,
        id: str,
        body: Any,
    ) -> Any:
        """Verify a builder webhook destination.

        ``POST /api/v1/webhooks/{id}/verify`` (operationId ``verifyWebhook``).

        Activates a pending webhook destination. Two conditions must both hold: the one-time
        verification token matches and has not expired, AND the destination answers 2xx to a
        signed challenge this operation POSTs to the endpoint's stored url. The challenge body
        is ...
        """
        return self._call("verifyWebhook", path_params={"id": id}, query={}, body=body)

    def rotate_webhook_secret(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
    ) -> Any:
        """Rotate a builder webhook signing secret.

        ``POST /api/v1/webhooks/{id}/rotate-secret`` (operationId ``rotateWebhookSecret``).

        Rotates the endpoint signing secret and returns the new signing_secret once in the
        response. Returns 409 with error.reason=webhook_delivery_in_progress while a live
        delivery freezes the current signing nonce; retry after it completes.
        """
        return self._call("rotateWebhookSecret", path_params={"id": id}, query={}, idempotency_key=idempotency_key)

    def get_health(
        self,
        *,
        if_none_match: str | None = None,
    ) -> Any:
        """Health check.

        ``GET /api/v1/health`` (operationId ``getHealth``).

        Returns API health status. No authentication required. Limited to 120 requests per
        minute per IP.
        """
        return self._call("getHealth", path_params={}, query={}, if_none_match=if_none_match)

    def create_mcp_json_rpc_response(
        self,
        body: Any,
        *,
        token: Any = None,
    ) -> Any:
        """Remote MCP endpoint (JSON-RPC).

        ``POST /api/v1/mcp`` (operationId ``createMcpJsonRpcResponse``).

        Model Context Protocol (MCP) Streamable HTTP transport. Accepts a JSON-RPC 2.0 request
        and returns a JSON-RPC response. Supported methods: initialize,
        notifications/initialized, ping, tools/list, tools/call. Remote MCP exposes 33 read-only
        tools for public V1 read operations: get_leaderboard, ...

        Query parameters:
            token: Legacy API-key query parameter for exact /api/v1/mcp only. Every other protected V1 route rejects it. Prefer Authorization: Bearer <token> or the stdio package ...
        """
        return self._call("createMcpJsonRpcResponse", path_params={}, query={"token": token}, body=body)

    def get_reports(
        self,
        *,
        granularity: Any = None,
        period: Any = None,
    ) -> Any:
        """Unified report snapshot (granularity selector).

        ``GET /api/v1/reports`` (operationId ``getReports``).

        Unified convenience route (#4975) that consolidates the three singular report routes.
        Dispatches to the exact per-granularity cap (daily 50, weekly 100, monthly 200) and date
        window the legacy /api/v1/reports/{daily,weekly,monthly} routes use, so the response
        body is byte-identical to the matching ...

        Query parameters:
            granularity: Report granularity selector.
            period: Period token for the granularity. daily: UTC date YYYY-MM-DD. weekly: ISO week YYYY-WW, or a from,to YYYY-MM-DD pair. monthly: UTC month YYYY-MM.
        """
        return self._call("getReports", path_params={}, query={"granularity": granularity, "period": period})

    def get_daily_report_snapshot(
        self,
        *,
        date: Any = None,
    ) -> Any:
        """Daily report snapshot.

        ``GET /api/v1/reports/daily`` (operationId ``getDailyReportSnapshot``).

        Returns a dated daily whale-activity report snapshot with source_range, snapshot.status,
        completeness, and reconciliation metadata. Report whale volume is local whale-alert
        activity volume, not provider lifetime trader volume.

        Query parameters:
            date: UTC report date in YYYY-MM-DD format.
        """
        return self._call("getDailyReportSnapshot", path_params={}, query={"date": date})

    def get_weekly_report_snapshot(
        self,
        *,
        from_: Any = None,
        to: Any = None,
        week: Any = None,
    ) -> Any:
        """Weekly report snapshot.

        ``GET /api/v1/reports/weekly`` (operationId ``getWeeklyReportSnapshot``).

        Returns a weekly whale-activity report snapshot. Pass either from/to UTC dates or an ISO
        YYYY-WW week token. The response identifies closed ranges as final and current ranges as
        rolling.

        Query parameters:
            from_: UTC source-range start in YYYY-MM-DD format; required with to.
            to: UTC source-range end in YYYY-MM-DD format; required with from.
            week: ISO week selector in YYYY-WW format; alternative to from/to.
        """
        return self._call("getWeeklyReportSnapshot", path_params={}, query={"from": from_, "to": to, "week": week})

    def get_monthly_report_snapshot(
        self,
        *,
        month: Any = None,
    ) -> Any:
        """Monthly report snapshot.

        ``GET /api/v1/reports/monthly`` (operationId ``getMonthlyReportSnapshot``).

        Returns a UTC monthly whale-activity report snapshot with source_range, completeness,
        and reconciliation metadata.

        Query parameters:
            month: UTC report month in YYYY-MM format.
        """
        return self._call("getMonthlyReportSnapshot", path_params={}, query={"month": month})

    def get_trader_export_snapshot(
        self,
        address: str,
    ) -> Any:
        """Trader export snapshot metadata.

        ``GET /api/v1/trader/{address}/export`` (operationId ``getTraderExportSnapshot``).

        Returns export source-range, completeness, volume reconciliation, row-count estimate,
        and large-export policy for one trader. To download the full dataset programmatically,
        POST to this same path to submit an async export job (json | ndjson | csv), then poll
        the status route and follow the download ...
        """
        return self._call("getTraderExportSnapshot", path_params={"address": address}, query={})

    def submit_trader_export(
        self,
        address: str,
        *,
        format: Any = None,
    ) -> Any:
        """Submit a trader dataset export job.

        ``POST /api/v1/trader/{address}/export`` (operationId ``submitTraderExport``).

        Queues an async export of the trader's full dataset in the requested format (json
        default, ndjson, or csv) and returns the job. Poll the status route, then follow the
        download route once status is 'ready'. Quotas are the per-user daily and per-address
        hourly export caps, keyed on the API key owner ...

        Query parameters:
            format: Output serialization. json = full envelope document (default); ndjson = full envelope as line 1 then one trade object per line; csv = flat trades rows only.
        """
        return self._call("submitTraderExport", path_params={"address": address}, query={"format": format})

    def get_trader_export_status(
        self,
        address: str,
        *,
        job_id: Any = None,
    ) -> Any:
        """Poll a trader export job.

        ``GET /api/v1/trader/{address}/export/status`` (operationId ``getTraderExportStatus``).

        Returns the current state of a submitted export job (queued | running | ready | failed)
        for the authenticated API key.

        Query parameters:
            job_id: Export job id returned by the submit route.
        """
        return self._call("getTraderExportStatus", path_params={"address": address}, query={"job_id": job_id})

    def download_trader_export(
        self,
        address: str,
        *,
        job_id: Any = None,
    ) -> Any:
        """Download a finished trader export.

        ``GET /api/v1/trader/{address}/export/download`` (operationId ``downloadTraderExport``).

        Redirects (302) to a short-lived presigned URL for the finished export file once the job
        status is 'ready'. The file is gzip-compressed and served with the format's Content-Type
        (application/json, application/x-ndjson, or text/csv). Returns 400 while the job is not
        yet ready (poll the status route ...

        Query parameters:
            job_id: Export job id returned by the submit route.
        """
        return self._call("downloadTraderExport", path_params={"address": address}, query={"job_id": job_id})

    def get_usage(
        self,
    ) -> Any:
        """Inspect current API usage without spending primary request quota.

        ``GET /api/v1/usage`` (operationId ``getUsage``).

        Returns the authenticated caller sliding-window request budget and UTC-day usage. This
        endpoint is authenticated and does not increment the primary Redis rate-limit counter or
        log itself into the API usage table; it is separately throttled at 100 reads/minute per
        user to protect the usage-count ...
        """
        return self._call("getUsage", path_params={}, query={})
