"""Generated from the 0xinsider OpenAPI document by scripts/generate.py. Do not edit.

Every documented request body, response envelope and schema, as a ``TypedDict``.
They are annotations over the plain decoded JSON: an operation returns the
dictionary the API sent, unchanged, and these say what is in it. Nothing is
validated, converted or copied at runtime, so reading one costs nothing.

What the shapes promise, and what they deliberately do not:

* A key in the document's ``required`` list is a required key here. A key that
  is not is optional: the API omits it rather than sending null, and a missing
  key is not a zero. Read one with ``.get()`` and handle the absence.
* ``| None`` means the key is present and its value can be JSON null. Omitted
  and null are different facts; neither is a zero.
* An ``enum`` the API returns is typed ``Literal[...] | str``: the documented
  values are there for an editor to complete, and a value the API adds after
  this release is not a type error. An ``enum`` you SEND is a strict
  ``Literal``, so a typo fails before it spends a request. A ``const`` is exact,
  which is what lets a union narrow on it (``entry["state"] == "sealed"``).
* Keys the API adds after this release are in the dictionary at runtime, as
  received. A type checker will not know them: read one through
  ``client.request(...)``, which is typed ``Any``, or ``cast`` the value.

These are deferred annotations (PEP 563) written in the ``X | None`` form, so
nothing here is evaluated at import on any supported Python. Resolving them at
runtime with ``typing.get_type_hints`` needs Python 3.10 or newer; reading the
dictionaries does not.

``oxinsider._provenance.OPENAPI_SHA256`` identifies the document these were
generated from.
"""

from __future__ import annotations

from typing import Any, Literal, TypedDict, Union

__all__ = [
    "AccountIdentity",
    "AccountIdentityData",
    "AccountIdentityDataEntitlement",
    "AgentRegistration",
    "AgentRegistrationLiveAccess",
    "AgentRegistrationSandbox",
    "ApiDiscovery",
    "ApiErrorBody",
    "BatchGetMarketFlowBody",
    "BatchGetMarketFlowResponse",
    "BatchGetMarketIntelResponse",
    "BatchGetTradersBody",
    "BatchGetTradersResponse",
    "BatchMarketFlowItem",
    "BatchRateLimitMeta",
    "BatchResponseMeta",
    "BatchTraderItem",
    "Candle",
    "CategorySkillModelReadiness",
    "CategorySkillV2",
    "ContentSearchResult",
    "CounterpartyAnalysis",
    "CounterpartyExecution",
    "CounterpartyMakerPage",
    "CounterpartyMatchBreakdown",
    "CounterpartyParticipant",
    "CreateMcpJsonRpcResponseBody",
    "CreateMcpJsonRpcResponseResponse",
    "CreateMcpJsonRpcResponseResponseError",
    "CreateWebhookRequest",
    "CreateWebhookResponse",
    "DataQuality",
    "DataQualityGroup",
    "EventReplayEvent",
    "EventReplayEventPayload",
    "EventReplayFreshness",
    "EventReplayMeta",
    "EventReplayMetaCompleteness",
    "EventReplayMetaReplay",
    "EventReplayMetaReplayFilters",
    "EventReplayMetaRetention",
    "EventReplaySource",
    "ExactDecimal",
    "ExploreEntry",
    "ExploreFacetValue",
    "ExploreFacets",
    "ExploreGroup",
    "ExploreMarket",
    "ExploreMarketFreshness",
    "ExploreMarketScoreComponents",
    "ExploreMarketsResponse",
    "ExploreStandalone",
    "ExportCompleteness",
    "ExportCounts",
    "ExportSourceRange",
    "ExportVolumeReconciliation",
    "FreshnessFailure",
    "Game",
    "GameCompetitor",
    "GameCoverage",
    "GameFreshness",
    "GameMarket",
    "GameMarketPriceBindingProvenance",
    "GameMarketPriceCompetitor",
    "GameMarketPriceIncomplete",
    "GameMarketPriceInvalid",
    "GameMarketPricePaired",
    "GameMarketPrices",
    "GameMarketProviderPrices",
    "GameStatus",
    "GamesCoverage",
    "GetApiDiscoveryResponse",
    "GetCoverageResponse",
    "GetEventReplaySinceResponse",
    "GetGameResponse",
    "GetHealthResponse",
    "GetHealthResponseData",
    "GetHealthResponseDataSubsystems",
    "GetHealthResponseDataSubsystemsBackgroundJobs",
    "GetInsiderRadarFlagResponse",
    "GetLargeTradeResponse",
    "GetMarketCandlesResponse",
    "GetMarketFlowResponse",
    "GetMarketHoldersResponse",
    "GetMarketIntelResponse",
    "GetMarketSnapshotResponse",
    "GetPickOfTheDayArchiveResponse",
    "GetPickOfTheDayLedgerResponse",
    "GetPickOfTheDayResponse",
    "GetPositionTimelineResponse",
    "GetReportsResponse",
    "GetSuspiciousTradeResponse",
    "GetTraderCategoryRecordsResponse",
    "GetTraderContextResponse",
    "GetTraderExportSnapshotResponse",
    "GetTraderGradeAtResponse",
    "GetTraderPnlResponse",
    "GetTraderResponse",
    "GetWhaleTradeResponse",
    "HolderCategoryEvidence",
    "LargeExportPolicy",
    "LargeExportPolicyV1Async",
    "LargePosition",
    "LargePositionHoldingsItem",
    "LargePositionMarket",
    "LargePositionTrader",
    "LargeTrade",
    "LargeTradeDetail",
    "LargeTradeHistoryMeta",
    "LargeTradeHistoryMetaCompleteness",
    "LargeTradeHistoryMetaSource",
    "LargeTradeMarket",
    "LargeTradeSubscriptionFilters",
    "LargeTradeTrader",
    "LeaderboardEntry",
    "ListGamesResponse",
    "ListLargePositionsResponse",
    "ListLargeTradeCounterpartyExecutionsResponse",
    "ListLargeTradeCounterpartyMakersResponse",
    "ListLargeTradeHistoryResponse",
    "ListLargeTradesResponse",
    "ListLeaderboardResponse",
    "ListPositionsResponse",
    "ListPositionsResponseSnapshot",
    "ListPreGameSideObservationsResponse",
    "ListPreGameSidesResponse",
    "ListSmartMoneyFlowsResponse",
    "ListSuspiciousTradesResponse",
    "ListTrendingWalletsResponse",
    "ListWebhookDeliveriesResponse",
    "ListWebhookEventsResponse",
    "ListWebhooksResponse",
    "ListWhaleTradeHistoryResponse",
    "ListWhaleTradesResponse",
    "MarketCandles",
    "MarketFlow",
    "MarketFlowMarket",
    "MarketFlowSharpMoney",
    "MarketFlowSharpMoneyTopPositionsItem",
    "MarketFlowSmartMoney",
    "MarketHolder",
    "MarketHolderCategoryWinRecord",
    "MarketHoldersMarket",
    "MarketHoldersScan",
    "MarketHoldersSideGrades",
    "MarketHoldersTotals",
    "MarketSearchResult",
    "MarketSnapshot",
    "MarketSnapshotFreshness",
    "MarketSnapshotLiquidity",
    "MarketSnapshotMarket",
    "MarketSnapshotOutcomesItem",
    "MarketSnapshotSports",
    "MarketSnapshotTopOfBook",
    "MarketSnapshotTrust",
    "NotModifiedResponse",
    "OutcomeCandles",
    "PickHolder",
    "PickHolderCategoryWinRecord",
    "PickOfTheDay",
    "PickOfTheDayArchive",
    "PickOfTheDayArchiveDay",
    "PickOfTheDayArchiveEntry",
    "PickOfTheDayCommitmentPayload",
    "PickOfTheDayHitRate",
    "PickOfTheDayHitRateSeriesItem",
    "PickOfTheDayLedger",
    "PickOfTheDayLedgerEntry",
    "PickOfTheDayLedgerOpenedEntry",
    "PickOfTheDayLedgerSealedEntry",
    "PickOfTheDayLedgerUncommittedEntry",
    "PickOfTheDayQualifyingExpert",
    "PickOfTheDayUncommittedPayload",
    "PickSportsContext",
    "PickSportsTeam",
    "PickTrust",
    "PlatformCapabilities",
    "PlatformCapabilityStatus",
    "Platforms",
    "PlatformsPlatforms",
    "Position",
    "PositionExact",
    "PositionMarket",
    "PositionTimelineEvent",
    "PositionTrader",
    "PotdEntryAuthorization",
    "PreGameSide",
    "PreGameSideCategorySkill",
    "PreGameSideFunnelReport",
    "PreGameSideObservation",
    "PreGameSideSportFunnelReport",
    "ProofPendingPickSlot",
    "RedeliverWebhookDeliveryResponse",
    "RegisterAgentResponse",
    "ReportPayload",
    "ReportPayloadTopLargeTradesItem",
    "ReportReconciliation",
    "ReportSnapshot",
    "ReportSourceRange",
    "ResponseMeta",
    "ResponseMetaCategorySkillStatusCounts",
    "ScheduledPickSlot",
    "ScoreCell",
    "ScoreFormat",
    "SearchContentResponse",
    "SearchMarketsResponse",
    "SmartMoneyFlowMarket",
    "SmartMoneyFlowMarketMarket",
    "SmartMoneyFlowMarketSharpMoney",
    "SmartMoneyFlowMarketSmartMoney",
    "SnapshotCompleteness",
    "SnapshotState",
    "SuspiciousTrade",
    "SuspiciousTradeMarket",
    "SuspiciousTradeScores",
    "SuspiciousTradeTrader",
    "Trader",
    "TraderCategoryRecord",
    "TraderCategoryRecords",
    "TraderContext",
    "TraderContextPositionSummary",
    "TraderEsportsGameRecord",
    "TraderExportArtifactManifest",
    "TraderExportCategoryWatermark",
    "TraderExportGeneration",
    "TraderExportJob",
    "TraderExportJobData",
    "TraderExportJobDataArtifact",
    "TraderExportPnlWatermark",
    "TraderExportPositionWatermark",
    "TraderExportSnapshot",
    "TraderExportSourceWatermarks",
    "TraderExportTradeWatermark",
    "TraderGradeAt",
    "TraderGradeAtObservation",
    "TraderPnl",
    "TraderPnlExact",
    "TraderQuantMetrics",
    "TraderStats",
    "TraderStatsExact",
    "TraderStrategy",
    "TraderTrust",
    "TrendingWallet",
    "TrendingWalletDailyPnlSeriesItem",
    "TrustCompleteness",
    "TrustFreshness",
    "TrustMetadata",
    "TrustReconciliation",
    "TrustSource",
    "UpdateWebhookRequest",
    "Usage",
    "UsageData",
    "UsageDataDailyUsage",
    "UsageDataMonthlyQuota",
    "UsageDataRateLimit",
    "VerifyWebhookRequest",
    "WebhookDelivery",
    "WebhookEndpoint",
    "WebhookEventDescriptor",
    "WebhookEventType",
    "WebhookRetryPolicy",
    "WebhookSecretRotation",
    "WebhookStatus",
    "WebhookVerification",
]


class _NotModifiedResponseRequired(TypedDict):
    object: Literal["not_modified"]
    # Always None: a 304 carries no body, and the cached one you already hold is still current.
    data: None


class NotModifiedResponse(_NotModifiedResponseRequired, total=False):
    """What an operation returns when ``if_none_match`` matched and the API answered 304.

    Keep the body you cached; ``etag`` is the validator to send on the next
    read. ``client.with_response.<method>(...)`` reports the same as
    ``.not_modified``.
    """

    etag: str | None


class GetApiDiscoveryResponse(TypedDict):
    object: Literal["api_discovery"]
    data: ApiDiscovery
    meta: ResponseMeta


class ApiDiscovery(TypedDict):
    # Canonical API origin for public V1 requests. Format: uri.
    api_base_url: str
    # Full agent-readable API reference. Format: uri.
    docs_url: str
    # Canonical web-origin OpenAPI JSON document. Format: uri.
    openapi_url: str
    # Unauthenticated API health endpoint. Format: uri.
    health_url: str
    authentication: Literal["Bearer API key required for data endpoints; discovery (/api/v1), health, coverage (/api/v1/coverage, and its deprecated alias /api/v1/platforms), the Pick of the Day commitment ledger (/api/v1/pick-of-the-day/ledger), and the MCP handshake (initialize, ping, tools/list on /api/v1/mcp) are public. A 401 carries WWW-Authenticate with the resource_metadata URL."]
    # RFC 9728 protected-resource metadata for the API origin: the document every V1 401 names in its WWW-
    # Authenticate challenge (resource, bearer_methods_supported, resource_documentation). The remote MCP server
    # has its own ...
    protected_resource_metadata_url: str
    # The complete authenticated route index: one entry per authenticated route this spec documents, in "<METHOD>
    # <path>" form, not a representative subset. GET /api/v1 is the unauthenticated entrypoint an agent hits
    # first, ...
    authenticated_routes: list[str]


class _ResponseMetaRequired(TypedDict):
    # Unique request ID (req_ prefix). The same value as the X-Request-Id response header, the request's usage
    # accounting row and its log lines.
    request_id: str
    cached: bool
    # Advisory request weight (relative compute cost). 1 for simple reads; higher for heavier endpoints. Not a
    # credit/price.
    cost: int


class ResponseMeta(_ResponseMetaRequired, total=False):
    # Cache age in seconds. Omitted when the response was not cached, and also when it was cached but its age
    # cannot be established (an entry stored before its cache carried a computed instant). Never a placeholder: an
    # ...
    cache_age_s: int
    # Committed PostgreSQL-owned leaderboard generation for the returned rows and cursor. Present on GET
    # /api/v1/leaderboard; omitted on endpoints that do not read this ranking.
    ranking_generation: int
    # Authoritative RFC3339 timestamp from cache_generations.updated_at for ranking_generation. It is read in the
    # same repeatable-read snapshot as the leaderboard rows and is not request time, cache write time, or row ...
    ranking_as_of: str
    # Which path produced the team-directional read on this response. Only present on endpoints that compute one
    # (today: GET /api/v1/sports-edge-signals). "live" means the read RAN. "degraded" means it FAILED, so nothing
    # was ...
    directional_source: Literal["live", "degraded"] | str
    # Which ranking-data path produced this response. Only present on endpoints that can degrade a ranking (today:
    # GET /api/v1/sports-edge-signals). "live" is the normal path (the current holder pile from the provider
    # batch); ...
    ranking_source: Literal["live", "db_only"] | str
    # Whole filtered snapshot category-evidence status before pagination. Operational live always remains partial
    # source coverage.
    category_skill_source: Literal["live", "partial", "degraded", "unavailable"] | str
    category_skill_model_version: str
    category_skill_taxonomy_version: str
    category_skill_platform: Literal["polymarket"]
    category_skill_scope: Literal["observed_goldsky_primary_taker_fill"]
    category_skill_source_coverage: Literal["partial_whale_threshold_fills", "graded_wallet_fills"] | str
    # Format: date-time.
    category_skill_observation_started_at: str
    # Whole-model operational readiness captured with the category model snapshot. Present on category-enriched
    # responses even when the filtered signal list is empty. When true, category_skill_source is degraded and ...
    category_skill_model_operationally_degraded: bool
    category_skill_status_counts: ResponseMetaCategorySkillStatusCounts
    # SHA-256 of the funded signal membership/order/rank/cursor vector immediately before category-skill
    # enrichment. Sports-edge-signals only.
    category_skill_base_payload_hash: str
    # Independent SHA-256 recomputation over the same base fields immediately after category-skill enrichment.
    # Equality with category_skill_base_payload_hash proves shadow enrichment did not change funded inputs. ...
    category_skill_enriched_base_payload_hash: str


class ResponseMetaCategorySkillStatusCounts(TypedDict):
    live: int
    insufficient: int
    stale: int
    unknown: int
    degraded: int


class RegisterAgentResponse(TypedDict):
    object: Literal["agent_registration"]
    data: AgentRegistration
    meta: ResponseMeta


class AgentRegistration(TypedDict):
    """A sandbox key and the path to live access (#13959). Nothing is stored: the key cannot be listed or
    revoked and does not expire. Register again for a new one."""
    # The sandbox key. Send it as Authorization: Bearer <api_key> to the sandbox. The last 8 hex characters are a
    # checksum (the first 4 bytes of SHA-256 over the rest of the key), so the sandbox can tell a mistyped key
    # from a ...
    api_key: str
    # Always false: this key never reaches live data.
    livemode: Literal[False]
    environment: Literal["sandbox"]
    # Format: date-time.
    created_at: str
    sandbox: AgentRegistrationSandbox
    # What live data needs, and where each credential comes from. Both need a person: an account with an active
    # Pro subscription.
    live_access: AgentRegistrationLiveAccess


class AgentRegistrationSandbox(TypedDict):
    # The sandbox V1 base URL. Every documented operation answers here with example data, except GET
    # /api/v1/stream: a Server-Sent Events stream is a live connection rather than a body, so the sandbox answers
    # it with 400. ...
    api_base_url: str
    # A read to send with the key. Format: uri.
    first_request_url: str
    # The OpenAPI document, served by the sandbox. Format: uri.
    openapi_url: str


class AgentRegistrationLiveAccess(TypedDict):
    """What live data needs, and where each credential comes from. Both need a person: an account with an
    active Pro subscription."""
    # The production V1 base URL. Format: uri.
    api_base_url: str
    # What a live credential needs, in one sentence.
    requirement: str
    # Where a signed-in Pro user creates a live key (oxi_sk_live_). Format: uri.
    api_keys_url: str
    # RFC 8414 authorization server metadata, for an OAuth 2.1 grant the user approves. Format: uri.
    oauth_authorization_server_metadata_url: str
    # RFC 7591 dynamic client registration for public OAuth clients. Format: uri.
    oauth_registration_endpoint: str
    # The Pro plan. Format: uri.
    pricing_url: str
    # The authentication walkthrough for agents. Format: uri.
    auth_guide_url: str


class GetTraderResponse(TypedDict):
    object: Literal["trader"]
    data: Trader
    meta: ResponseMeta


class _TraderRequired(TypedDict):
    # Prefixed ID (trd_...).
    id: str
    address: str
    pnl: TraderPnl
    stats: TraderStats
    # Data age and coverage for this trader body. Always present. Its five groups are sync (traders.last_synced,
    # covering pnl.total, pnl.realized, stats.markets_traded, stats.win_rate, stats.daily_win_rate, last_active,
    # ...
    data_quality: DataQuality


class Trader(_TraderRequired, total=False):
    username: str
    grade: Literal["S", "A", "B", "C", "D", "F"] | str
    # Hot-streak tier (trailing-7d cross-sectional percentile); a separate axis from the all-time grade. Omitted
    # when there is no recent activity.
    streak_tier: Literal["hot", "rising", "neutral", "cooling", "cold"] | str
    score: float
    # Capital-normalized forecasting score: the cohort percentile (0-100) of the EB-shrunk calibration edge.
    # Omitted when the forecasting signal is unavailable; never replaced with zero.
    forecast_score: float
    # Share of forecast_score supported by the trader's own resolved-market record rather than the cohort prior: n
    # / (n + 30). Omitted when forecast_score is unavailable.
    forecast_evidence: float
    rank: int
    strategy: TraderStrategy
    # Per-category performance breakdown (expand=categories or expand[]=categories). Omitted unless expanded.
    # Object keyed by category name; each value is the precomputed trader_rankings.category_ranks payload (rank,
    # ...
    category_strengths: dict[str, Any]
    # Curated advanced risk/performance metrics (expand=quant_metrics or expand[]=quant_metrics). Omitted unless
    # expanded and backed by a computed row strictly under six hours old; a missing row, NULL computed_at, or age
    # of ...
    quant_metrics: TraderQuantMetrics
    # Format: date-time.
    last_active: str
    # Format: date-time.
    synced_at: str
    # synced, unknown, or pending.
    sync_status: str
    # Field-level trust metadata. Present only when expand=trust or expand[]=trust is requested.
    trust: TraderTrust
    # Current evidence for observed and known categories (expand=categories or expand[]=categories). Omitted
    # unless expanded. Includes insufficient, stale, unknown and degraded rows; absence of a category is not proof
    # of ...
    category_records: list[CategorySkillV2]
    category_skill_model: CategorySkillModelReadiness


class TraderPnl(TypedDict, total=False):
    total: float
    # For pnl.realized, expand=trust marks a matching native accounting snapshot as computed: native Polymarket
    # realized P&L plus credited maker and taker rebates, with fees already included. The exact numeric value is
    # ...
    realized: float
    unrealized: float
    # DEPRECATED, never sent. The local pnl_7d rollup over-counted P&L (#5416 class) and is no longer emitted.
    # Read the provider-native weekly window from GET /api/trader/{address}/profile-summary instead.
    last_7d: float
    # DEPRECATED, never sent. The local pnl_30d rollup over-counted P&L (#5416 class) and is no longer emitted.
    # Read the provider-native monthly window from GET /api/trader/{address}/profile-summary instead.
    last_30d: float
    # Additive lossless counterpart. Omitted when the trusted native realized-P&L source is unavailable; existing
    # numeric fields keep their display-safe v1 semantics.
    exact: TraderPnlExact


class TraderPnlExact(TypedDict):
    """Lossless counterparts for trader P&L values. The object is omitted when no trusted native
    realized-P&L snapshot is available."""
    # Native Polymarket realized P&L plus credited maker and taker rebates, with fees included, from the trusted
    # matching `trader_trading_pnl.net_realized_pnl` snapshot.
    realized: ExactDecimal


class ExactDecimal(TypedDict):
    """A lossless decimal atom rendered from the canonical NUMERIC or provider value. The value is a
    decimal string and must be parsed with a decimal library; it is never a display string and must not
    be converted through a binary float. `scale` is the source decimal scale. The field is omitted when
    its source is unavailable."""
    # Plain decimal text at full source precision, including a minus sign for negative values and trailing zeros
    # when the source scale carries them. Parse as an arbitrary-precision decimal.
    value: str
    # Unit of the value, such as `USD`, `USD/share`, or `shares`.
    unit: str
    # Number of digits after the decimal point in `value`'s source atom.
    scale: int
    # Backend-owned source or derivation basis. Treat it as provenance, not as a display label.
    basis: str


class TraderStats(TypedDict, total=False):
    markets_traded: int
    win_rate: float
    daily_win_rate: float
    # Full-history both-sides USD cash volume from Polymarket user-volume. Omitted without a verified observation;
    # never leaderboard shares. Its observation time is published as the volume group in data_quality and as ...
    total_volume: float
    # Additive lossless counterpart to `total_volume`. Omitted when the verified provider observation is
    # unavailable.
    exact: TraderStatsExact


class TraderStatsExact(TypedDict):
    """Lossless counterparts for trader statistics. The object is omitted when the verified provider
    observation is unavailable."""
    # Full-history both-sides Polymarket user-volume atom from the verified `trader_usd_volume` observation.
    total_volume: ExactDecimal


class TraderStrategy(TypedDict, total=False):
    strategy_type: str
    description: str
    confidence: float


class TraderQuantMetrics(TypedDict):
    """Curated advanced risk/performance metrics (expand=quant_metrics or expand[]=quant_metrics). Omitted
    unless expanded and backed by a computed row strictly under six hours old; a missing row, NULL
    computed_at, or age of exactly six hours or more is stale and omitted. Provider-input changes may
    intentionally lag inside the bounded six-hour window. When present, all listed fields are present
    (each is a number or null); null means insufficient trade history and must not be treated as 0. The
    fixed field shape is unchanged."""
    # Composite skill score, 0-100. smart_score = clamp(0, 100, 30*sharpe_percentile_fraction +
    # 20*profit_factor_percentile_fraction + 20*edge_consistency_percentile_fraction + 10*min(1,
    # return_on_capital/2) + ...
    smart_score: float | None
    # Copyability score, 0-100. Same base as smart_score minus penalties for traits that make a strategy hard to
    # replicate: -20 if fewer than 50 markets traded, -15 if positions are highly concentrated, -15 if position
    # sizing ...
    copy_score: float | None
    # Sharpe ratio over the trailing 30 days (risk-adjusted return; higher is better). Magnitude can be large for
    # small samples. null when insufficient history.
    sharpe_30d: float | None
    # Sharpe ratio over the trailing 7 days (risk-adjusted return; higher is better). null when insufficient
    # history.
    sharpe_7d: float | None
    # Gross profit divided by gross loss; greater than 1 is profitable. Capped at 1000 when there are effectively
    # no losses. null when insufficient history.
    profit_factor: float | None
    # Stability of the trader's edge over time, 0-1 (higher is more consistent). null when insufficient history.
    edge_consistency: float | None
    # Cross-sectional percentile rank of the trader's Sharpe ratio versus all traders, 0-100. null when
    # insufficient history.
    sharpe_percentile: float | None
    # Cross-sectional percentile rank of profit factor versus all traders, 0-100. null when insufficient history.
    pf_percentile: float | None
    # Cross-sectional percentile rank of edge consistency versus all traders, 0-100. null when insufficient
    # history.
    consistency_percentile: float | None


class _DataQualityRequired(TypedDict):
    # fresh when every group is fresh, unavailable when every group is unavailable, and partial in every other
    # case.
    status: Literal["fresh", "partial", "unknown", "untracked", "unavailable"] | str
    # One entry per field group. Entries may be added in later releases, so match on group rather than on position
    # or length.
    field_groups: list[DataQualityGroup]


class DataQuality(_DataQualityRequired, total=False):
    """Compact data age and coverage for a response body, always present on the operations that publish it.
    Read status and as_of to decide whether to use the body at all, and field_groups to see which part
    is weak. Everything here comes from stored observation clocks, so a cached body reports the same
    ages a freshly computed one does: meta.cached and meta.cache_age_s stay the only transport-time
    facts and neither makes this block newer. The per-field audit object is still available through
    expand=trust; this is the default summary of the same question."""
    # The oldest as_of among the groups that carry one: the age of the weakest clock this body rests on. Omitted
    # when no group carries a clock. Format: date-time.
    as_of: str


class _DataQualityGroupRequired(TypedDict):
    # Stable snake_case group name. Names are additive across releases, so match on the ones you know and ignore
    # the rest.
    group: str
    # The table and column that write this group, named so the verdict can be audited (for example
    # trader_rankings.computed_at).
    owner: str
    # fresh: served, and as_of carries this group's real observation or computation clock. partial: some of the
    # group's fields are served and some are missing. unknown: served, and this read has no clock for it, so no
    # age may ...
    status: Literal["fresh", "partial", "unknown", "untracked", "unavailable"] | str


class DataQualityGroup(_DataQualityGroupRequired, total=False):
    """One group of response fields that share a writer and therefore share a clock."""
    # When this group's values were observed or computed. Omitted whenever the read cannot measure it, and never
    # filled with the serialization time, the cache time, or another group's clock. Format: date-time.
    as_of: str
    # Why the status is not fresh. Omitted when it is.
    reason: str


class TraderTrust(TypedDict):
    """Field-level trust metadata returned only when GET /api/v1/trader/{address} includes expand=trust."""
    total_pnl: TrustMetadata
    realized_pnl: TrustMetadata
    unrealized_pnl: TrustMetadata
    markets_traded: TrustMetadata
    win_rate: TrustMetadata
    daily_win_rate: TrustMetadata
    total_volume: TrustMetadata
    grade: TrustMetadata
    score: TrustMetadata
    forecast_score: TrustMetadata
    forecast_evidence: TrustMetadata
    rank: TrustMetadata
    streak_tier: TrustMetadata
    strategy: TrustMetadata
    category_strengths: TrustMetadata
    quant_metrics: TrustMetadata
    last_active: TrustMetadata
    synced_at: TrustMetadata
    sync_status: TrustMetadata
    category_records: TrustMetadata
    category_skill_model: TrustMetadata


class TrustMetadata(TypedDict):
    """Shared source/freshness/reconciliation/completeness metadata for public API values that may be
    cached, stale, partial, computed, or provider-unavailable. Unavailable provider values must be
    represented with explicit metadata instead of fabricated zeros or empty arrays."""
    source: TrustSource
    freshness: TrustFreshness
    reconciliation: TrustReconciliation
    completeness: TrustCompleteness


class _TrustSourceRequired(TypedDict):
    kind: Literal["provider", "database", "cache", "computed", "client_input", "unavailable"] | str
    # Provider, table/read-model, cache, or service that owns the value.
    owner: str


class TrustSource(_TrustSourceRequired, total=False):
    """Source metadata for a trust-critical value. Providers and DB/read models own business truth; clients
    should not infer missing provider facts from titles, slugs, zeros, or empty arrays."""
    # Provider field, DB column, or computed field name when applicable.
    field: str


class _TrustFreshnessRequired(TypedDict):
    status: Literal["fresh", "refreshing", "stale", "not_live", "unknown", "unavailable"] | str


class TrustFreshness(_TrustFreshnessRequired, total=False):
    """Freshness metadata for a trust-critical value. This is separate from transport cache fields in
    ResponseMeta."""
    # Format: date-time.
    as_of: str
    max_age_s: int


class _TrustReconciliationRequired(TypedDict):
    status: Literal["provider_backed", "db_mirror", "computed", "partial", "not_applicable", "unavailable"] | str


class TrustReconciliation(_TrustReconciliationRequired, total=False):
    """How provider-owned facts were reconciled with stored/read-model values."""
    detail: str


class _TrustCompletenessRequired(TypedDict):
    status: Literal["complete", "partial", "not_computed", "not_applicable", "unavailable"] | str


class TrustCompleteness(_TrustCompletenessRequired, total=False):
    """Whether the described value or result set is complete for its stated contract."""
    detail: str


class CategorySkillV2(TypedDict):
    """Forward-only category evidence from observed Polymarket taker fills. Status is category eligibility,
    not a global letter grade or a guarantee of positive edge. Scores are probability differences.
    Unknown and degraded rows withhold scores. Coverage is partial; observation counts are not lifetime
    market counts."""
    status: Literal["live", "insufficient", "stale", "unknown", "degraded"] | str
    model_version: str
    taxonomy_version: str | None
    platform: Literal["polymarket"]
    scope: Literal["observed_goldsky_primary_taker_fill"]
    source_coverage: Literal["partial_whale_threshold_fills", "graded_wallet_fills"] | str
    canonical_category: str
    # Format: date-time.
    as_of: str
    # Format: date-time.
    source_last_success_at: str | None
    # Format: date-time.
    observation_started_at: str
    # Format: date-time.
    latest_observation_at: str | None
    independent_event_count: int
    resolved_condition_count: int
    unresolved_observation_count: int
    edge_mean: float | None
    edge_sd: float | None
    edge_se: float | None
    edge_lower_95: float | None
    brier_event_avg: float | None


class CategorySkillModelReadiness(TypedDict):
    """Model-wide readiness, read in the same database snapshot as category_records. Individual category
    rows retain their own status."""
    status: Literal["live", "insufficient", "stale", "unknown", "degraded"] | str
    model_version: str
    taxonomy_version: str
    # Format: date-time.
    observation_started_at: str
    # Format: date-time.
    as_of: str
    # Format: date-time.
    source_last_success_at: str | None


class GetTraderGradeAtResponse(TypedDict):
    object: Literal["trader_grade_at"]
    data: TraderGradeAt
    meta: ResponseMeta


class TraderGradeAt(TypedDict):
    # Prefixed trader id (trd_<wallet>).
    id: str
    # Resolved wallet address, lowercased.
    address: str
    # Requested event or decision time. Format: date-time.
    as_of: str
    # graded has a proven grade; ungraded is a proven null grade; unknown has no valid historical observation.
    status: Literal["graded", "ungraded", "unknown"] | str
    # Grade only when status is graded; null otherwise.
    grade: Literal["S", "A", "B", "C", "D", "F"] | str | None
    # First proven visibility instant for this trader. Null when no observation exists. Earlier times remain
    # unknown. Format: date-time.
    available_from: str | None
    # Proof row when status is graded or ungraded. Null when history is unknown.
    observation: TraderGradeAtObservation | None


class TraderGradeAtObservation(TypedDict):
    """Proof row when status is graded or ungraded. Null when history is unknown."""
    # Immutable grade_forward_history observation id. Format: int64.
    id: int
    # Previous immutable observation id when retained. A later grade change supersedes that observation but never
    # erases it; this link does not assert why the grade changed. Format: int64.
    previous_observation_id: int | None
    # Lower bound: the grade writer had started the transition at this instant. Format: date-time.
    observed_at: str
    # Upper bound: a later snapshot confirmed the observation was committed. This is not an exact commit
    # timestamp. Format: date-time.
    published_by: str
    # Writer-proven model family, such as grading-v4. Null when unknown.
    model_version: str | None
    # Exact writer build SHA when recorded. Null on old and non-model observations.
    model_build_sha: str | None
    # Database-clock upper bound on when the grading pass read its cohort inputs. Not the event time or source
    # freshness of every input; null when unknown. Format: date-time.
    source_observed_by: str | None


class GetTraderContextResponse(TypedDict):
    object: Literal["trader_context"]
    data: TraderContext
    meta: ResponseMeta


class _TraderContextRequired(TypedDict):
    trader: Trader
    # RFC3339 freshness of the OPEN-position-level data: when a position_summary is present this mirrors its as_of
    # byte-for-byte (latest /positions snapshot, else last completed sync) -- the open-position freshness clock,
    # ...
    data_as_of: str | None
    # Human-readable statement of the point-in-time snapshot semantics (data_as_of is the open-position clock --
    # the latest /positions snapshot, else the last completed sync; the snapshot advances only open positions, so
    # ...
    freshness_note: str


class TraderContext(_TraderContextRequired, total=False):
    # Aggregate position and P&L coverage for the trader. Omitted entirely (key absent, never null) when the
    # trader is not in the local database or native net economics is unavailable. Realized fields remain numbers
    # when ...
    position_summary: TraderContextPositionSummary


class TraderContextPositionSummary(TypedDict):
    """Aggregate position and P&L coverage for the trader. Omitted entirely (key absent, never null) when
    the trader is not in the local database or native net economics is unavailable. Realized fields
    remain numbers when present, including a genuine zero."""
    # Provider markets_traded count when known; null when the provider total is unavailable.
    markets_total: int | None
    # Markets with locally synced position rows.
    markets_synced: int
    # Synced markets that have resolved.
    markets_resolved: int
    # Synced markets still open with residual value (open positions with current value > 0).
    markets_open: int
    # markets_synced divided by markets_total when the provider total is known (capped at 1.0); 0.0-1.0. When
    # markets_total is unknown or not positive (null, 0, or negative), this is 1.0 if any markets are synced (else
    # 0.0), ...
    sync_coverage: float
    # Native net realized P&L (USD) including credited rebates, minus the stored realized component of open
    # positions with positive current value. Rebates are credited to the account, not to a position, so every
    # credited ...
    synced_realized_pnl: float
    # Native net realized P&L (USD) including credited rebates, read directly from the accounting snapshot.
    # Position sync_coverage is separate from this accounting basis.
    total_realized_pnl: float
    # Mark-to-market unrealized P&L (USD) on open positions.
    unrealized_mtm: float
    # Cost basis (USD) currently tied up in open positions.
    cost_basis_locked: float
    # Win rate as a percentage (0-100): resolved_wins over resolved_decided. A resolved market that settled at
    # exactly zero realized P&L (a void, a refund, a fully hedged position) is neither a win nor a loss and is not
    # in ...
    resolved_win_rate: float | None
    # Resolved markets that settled at positive realized P&L: the win-rate numerator. Additive; null only on a
    # summary cached before the field existed.
    resolved_wins: int | None
    # Resolved markets that settled at a non-zero realized P&L: the win-rate denominator. At most
    # markets_resolved; the difference is markets settled at exactly zero or with an unknown P&L. Additive; null
    # only on a summary ...
    resolved_decided: int | None
    # RFC3339 freshness of the served OPEN-position data: the trader's latest /positions snapshot, else the last
    # completed sync. The snapshot advances ONLY open positions, so read this as the open-position freshness clock
    # -- ...
    as_of: str | None


class _BatchGetTradersBodyRequired(TypedDict):
    # Trader identities to resolve in input order.
    traders: list[str]


class BatchGetTradersBody(_BatchGetTradersBodyRequired, total=False):
    # Shared expand flags applied to every trader item.
    expand: list[Literal["strategy", "categories", "quant_metrics", "trust"]]


class BatchGetTradersResponse(TypedDict):
    object: Literal["trader_batch"]
    data: list[BatchTraderItem]
    meta: BatchResponseMeta


class _BatchTraderItemRequired(TypedDict):
    # Zero-based request index. Duplicate inputs keep separate result rows.
    index: int
    input: str
    status: Literal["ok", "error"] | str


class BatchTraderItem(_BatchTraderItemRequired, total=False):
    data: Trader
    error: ApiErrorBody


class _ApiErrorBodyRequired(TypedDict):
    # FROZEN: an existing value never changes meaning. request_timeout (408, #16146) was added the way
    # insufficient_scope was: the handler did not answer inside the server's 30-second timeout. Retry-After and
    # retry_at ride on ...
    code: Literal["bad_request", "invalid_api_key", "subscription_required", "forbidden", "insufficient_scope", "not_found", "account_locked", "rate_limited", "rate_limit_unavailable", "internal_error", "request_timeout"] | str
    message: str


class ApiErrorBody(_ApiErrorBodyRequired, total=False):
    doc_url: str
    param: str
    # The recommended next retry instant (RFC3339). Present on every retryable error (reason=pick_not_released,
    # code=rate_limited including reason=monthly_quota_exceeded, code=rate_limit_unavailable, ...
    retry_at: str
    freshness: FreshnessFailure
    # ADDITIVE (#7209). The specific, actionable cause behind `code`, when there is one more specific than the
    # code itself. `code` keeps its published values, so existing clients are unaffected; new clients branch on
    # ...
    reason: Literal["cursor_expired", "unknown_endpoint", "pick_not_released", "trader_not_tracked", "read_model_warming", "database_unavailable", "request_accounting_unavailable", "idempotency_in_progress", "webhook_delivery_in_progress", "webhook_secret_rotation_not_prepared", "webhook_secret_rotation_overlap_active", "sandbox_api_key", "api_key_in_query", "subscription_inactive", "monthly_quota_exceeded", "invalid_query", "unknown_query_parameter", "invalid_path", "invalid_body", "unsupported_media_type", "payload_too_large", "method_not_allowed", "ip_rate_limited", "ip_throttled", "export_expired", "freshness_ceiling_unsatisfied"] | str


class _FreshnessFailureRequired(TypedDict):
    # The caller's requested whole-response freshness ceiling in seconds. Format: int64.
    max_age_s: int
    # The trader body's whole-response data-quality status. Only fresh can satisfy max_age_s.
    data_quality_status: Literal["fresh", "partial", "unknown", "untracked", "unavailable"] | str


class FreshnessFailure(_FreshnessFailureRequired, total=False):
    # Age in seconds of the oldest stored data_quality.as_of clock, when one is available. Format: int64.
    actual_age_s: int
    # The oldest stored data-quality clock used to calculate actual_age_s, when one is available. Format: date-
    # time.
    as_of: str


class BatchResponseMeta(TypedDict):
    # Unique request ID (req_ prefix). The same value as the X-Request-Id response header, the request's usage
    # accounting row and its log lines.
    request_id: str
    cached: bool
    total_items: int
    successful_items: int
    failed_items: int
    # Number of batch item units reserved before execution.
    request_cost: int
    rate_limit: BatchRateLimitMeta


class BatchRateLimitMeta(TypedDict):
    basis: Literal["batch_items_per_minute"]
    limit: int
    remaining: int
    # Unix timestamp when the batch item window resets.
    reset: int


class _GetPositionTimelineResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[PositionTimelineEvent]
    has_more: bool
    meta: ResponseMeta


class GetPositionTimelineResponse(_GetPositionTimelineResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; the key is absent when it does not.
    total: int


class PositionTimelineEvent(TypedDict):
    # Prefixed ID (pe_...).
    id: str
    # ISO 8601 timestamp of the on-chain fill. Format: date-time.
    event_timestamp: str
    # From the taker's perspective.
    action: Literal["buy", "sell"] | str
    outcome_side: Literal["yes", "no"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for this outcome; null when unavailable
    # (e.g. unsynced markets).
    token_id: str | None
    # Signed share delta (+ on buy, − on sell).
    amount_delta: float
    # Fill price in USDC per share, in [0,1].
    price: float
    # Positive USDC notional of the fill.
    usdc_notional: float
    # Polygon transaction hash of the fill.
    tx_hash: str
    # Cumulative signed stored-fill amount for this outcome after this fill, including older pages. Stable across
    # limits/cursors for unchanged source history. Excludes split, merge, redemption and neg-risk activity; not
    # ...
    running_amount: float
    # Cumulative buy-weighted average of stored fills for this outcome, including older pages; not provider
    # current-position avgPrice. Sells do not change this value. 0 when no stored buys have occurred yet.
    running_avg_price: float


class GetTraderCategoryRecordsResponse(TypedDict):
    object: Literal["trader_category_records"]
    data: TraderCategoryRecords
    meta: ResponseMeta


class TraderCategoryRecords(TypedDict):
    # Prefixed trader id (trd_<wallet>).
    id: str
    # Resolved wallet address, lowercased.
    address: str
    # Which sample the counts come from: every settled market in the category, at any position size.
    # category_strengths on the trader endpoint reads the floored calibration sample instead, so the two differ in
    # both ...
    basis: Literal["settled_markets_all_sizes"]
    # Decided markets a category needs before win_rate is served. Published so a caller can apply its own sample
    # rule to the raw counts.
    min_decided_for_win_rate: int
    # When the served records were last rebuilt (RFC3339, Z): the newest stamp among every row served, game rows
    # included, which the daily rebuild writes in one transaction. Null when the wallet has no record at all.
    # Format: ...
    computed_at: str | None
    # One entry per canonical category with at least one decided market, ordered by decided descending then
    # category. A category with no decided market is omitted. The Esports entry carries its per-game records in
    # games.
    records: list[TraderCategoryRecord]


class _TraderCategoryRecordRequired(TypedDict):
    # Canonical category bucket, for example Soccer, Esports, Tennis. Esports is one bucket, and the Esports
    # record carries its per-game records in games.
    category: str
    # Markets in this category the wallet closed with a profit.
    wins: int
    # Markets it closed with a profit or a loss. A market that resolved at exactly zero P&L is in neither count,
    # so this is not the wallet's market count in the category.
    decided: int
    # wins / decided in [0,1], truncated to four decimals. Null when status is not_enough_data.
    win_rate: float | None
    # measured: decided cleared min_decided_for_win_rate and win_rate carries the rate. not_enough_data: the
    # counts are real but the sample is under the floor, so no percent is published. A failed read is an error
    # response, ...
    status: Literal["measured", "not_enough_data"] | str


class TraderCategoryRecord(_TraderCategoryRecordRequired, total=False):
    # The wallet's record per esports title, busiest first. Present only on the Esports record, and only when the
    # wallet has a settled market in at least one title; absent on every other category and on an Esports record
    # ...
    games: list[TraderEsportsGameRecord]


class TraderEsportsGameRecord(TypedDict):
    # The game, by the same name every holder chip carries in category_win_rate_game: LoL, CS2, Dota 2, Valorant,
    # Call of Duty, Honor of Kings, Mobile Legends: Bang Bang, Overwatch, Rainbow Six Siege, Rocket League or ...
    game: str
    # The Polymarket series slug the record is keyed on: league-of-legends, counter-strike, dota-2, valorant,
    # call-of-duty, honor-of-kings, mobile-legends-bang-bang, overwatch, rainbow-six-siege, rocket-league or
    # starcraft-2. ...
    series_slug: str
    # Markets in this game the wallet closed with a profit.
    wins: int
    # Markets in this game it closed with a profit or a loss. A subset of the parent Esports record's decided: the
    # two are read from the same daily rebuild.
    decided: int
    # wins / decided in [0,1], truncated to four decimals. Null when status is not_enough_data.
    win_rate: float | None
    # The same rule as the parent record: measured when decided cleared min_decided_for_win_rate, not_enough_data
    # when the counts are real but the sample is under the floor. A chip on a market in this game shows this row's
    # ...
    status: Literal["measured", "not_enough_data"] | str


class GetTraderPnlResponse(TypedDict):
    object: Literal["trader_pnl"]
    data: TraderPnl
    meta: ResponseMeta


class _ListPositionsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[Position]
    # Writer-backed age and coverage for this page; it is part of the representation and the ETag, while transport
    # cache facts remain in meta.
    data_quality: DataQuality
    has_more: bool
    meta: ResponseMeta


class ListPositionsResponse(_ListPositionsResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; the key is absent when it does not.
    total: int
    # Present only with consistency=snapshot. Dates the frozen response rows, not the provider's underlying
    # observations.
    snapshot: ListPositionsResponseSnapshot


class _PositionRequired(TypedDict):
    # Composite prefixed ID `pos_<wallet>:<condition_id>:<outcome_index>`.
    id: str
    # Provider discriminator. Polymarket only.
    platform: Literal["polymarket"]
    # Lowercased proxy wallet address.
    wallet: str
    # Binary outcome side. Non-binary positions are not surfaced on V1.
    side: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for this outcome; null when unavailable
    # (e.g. unsynced markets).
    token_id: str | None
    # Live share count from the wallet_positions mirror.
    shares: float
    # Current mark-to-market value in USD (always non-null on V1 — pre-reconcile rows are excluded).
    current_value_usd: float
    # Backend-computed staleness bucket derived from last_reconciled_at.
    freshness: Literal["fresh", "refreshing", "stale", "unknown"] | str
    trader: PositionTrader
    market: PositionMarket


class Position(_PositionRequired, total=False):
    # Volume-weighted entry price for this leg.
    avg_price: float
    initial_value_usd: float
    # Unrealized P&L for the open position (Polymarket `cashPnl`).
    cash_pnl: float
    # Closed-leg P&L rolled up (Polymarket `realizedPnl`).
    realized_pnl: float
    # Additive lossless source atoms for the display-safe position fields. Parse every `value` with decimal-safe
    # arithmetic; never recover exact values from the numeric twins.
    exact: PositionExact
    # Max updated_at across mirror legs for this pair. Format: date-time.
    last_reconciled_at: str


class _PositionExactRequired(TypedDict):
    shares: ExactDecimal
    current_value_usd: ExactDecimal


class PositionExact(_PositionExactRequired, total=False):
    """Lossless position atoms from `wallet_positions`. `shares` and `current_value_usd` are required when
    this object is present; other source values are omitted when the mirror has no verified value."""
    cost_basis_usd: ExactDecimal
    # Exact derived price: `wallet_positions.cost_basis_usd / wallet_positions.shares`.
    avg_price: ExactDecimal
    initial_value_usd: ExactDecimal
    cash_pnl: ExactDecimal
    realized_pnl: ExactDecimal


class _PositionTraderRequired(TypedDict):
    # Prefixed ID (`trd_...`).
    id: str
    address: str
    # True when 0xinsider first recorded the wallet within the new-wallet threshold (30 days). This public V1
    # field is first-seen recency, not the wallet's on-chain age.
    is_new_wallet: bool


class PositionTrader(_PositionTraderRequired, total=False):
    username: str
    grade: Literal["S", "A", "B", "C", "D", "F"] | str
    # Percentage 0-100.
    win_rate: float
    pnl: float
    markets: int
    wallet_age_days: float


class _PositionMarketRequired(TypedDict):
    # Prefixed ID (`mkt_...`).
    id: str
    condition_id: str
    title: str


class PositionMarket(_PositionMarketRequired, total=False):
    slug: str
    event_slug: str
    # Provider-backed market_canonical category.
    category: str
    # Provider-reported outcome label (e.g. team name for sports). Separate from `side` because provider labels
    # can diverge from the binary Yes/No axis.
    outcome_label: str
    # Format: date-time.
    end_date: str


class ListPositionsResponseSnapshot(TypedDict):
    """Present only with consistency=snapshot. Dates the frozen response rows, not the provider's
    underlying observations."""
    # Format: date-time.
    as_of: str
    # Format: date-time.
    expires_at: str
    row_count: int


class _ListLargePositionsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[LargePosition]
    has_more: bool
    meta: ResponseMeta


class ListLargePositionsResponse(_ListLargePositionsResponseRequired, total=False):
    # Opaque cursor for the next page; absent on the last page.
    next_cursor: str
    # Total ranked rows when the read model exposes a count; may be absent.
    total: int


class _LargePositionRequired(TypedDict):
    # Composite prefixed ID `pos_<wallet>:<condition_id>:<outcome_index>`.
    id: str
    # Provider discriminator. Always polymarket.
    platform: Literal["polymarket"]
    # Whether the wallet holds shares on both outcomes of this market.
    is_two_sided: bool
    # Every outcome the wallet holds, primary first. holdings[0] restates the top-level per-outcome fields; a
    # further entry is a leg those fields do not describe. No amount here is a share-proportional slice of a both-
    # sides ...
    holdings: list[LargePositionHoldingsItem]
    # Live share count for this position.
    share_count: float
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for this outcome; null when unavailable
    # (e.g. unsynced markets).
    token_id: str | None
    # Legs collapsed into this representative row for one (wallet, event, outcome side) group. 1 means standalone.
    event_leg_count: int
    # Format: date-time.
    first_seen_at: str
    # Format: date-time.
    last_updated_at: str
    trader: LargePositionTrader
    market: LargePositionMarket


class LargePosition(_LargePositionRequired, total=False):
    # Provider currentValue in USD for the outcome named by outcome_label / token_id, and for that outcome only.
    # An absent key means the provider supplied no value for this leg, not a zero position. combined_value_usd
    # carries ...
    total_size_usd: float
    # Provider unrealized mark-to-market P&L (Polymarket cashPnl) for that same one outcome. An absent key means
    # unavailable, not break-even.
    position_unrealized_pnl: float
    # The wallet's currentValue across every outcome it holds in this market. Equals total_size_usd unless
    # is_two_sided is true, and is the value the feed ranked this row by.
    combined_value_usd: float
    # The wallet's unrealized P&L across every outcome it holds in this market. Equals position_unrealized_pnl
    # unless is_two_sided is true.
    combined_unrealized_pnl: float
    # Volume-weighted entry price.
    avg_entry_price: float
    # Latest provider mark price for the position's token.
    current_price: float
    # Backend-resolved outcome label (provider outcome, else Yes/No from the binary index).
    outcome_label: str
    # Sum of the collapsed sibling legs' own holding values for this (wallet, event) group; equals total_size_usd
    # when event_leg_count = 1, and omitted when any member's value is unknown.
    event_total_value_usd: float


class _LargePositionHoldingsItemRequired(TypedDict):
    # 0 = Yes, 1 = No.
    outcome_index: int
    # Polymarket CLOB token id for this outcome; null for an unsynced market.
    token_id: str | None
    # Shares held on this outcome.
    share_count: float


class LargePositionHoldingsItem(_LargePositionHoldingsItemRequired, total=False):
    # The market's label for this outcome.
    outcome_label: str
    # Provider average entry price for this outcome.
    avg_entry_price: float
    # Provider mark price for this outcome.
    current_price: float
    # Provider currentValue for this outcome. An absent key means unavailable, not zero.
    value_usd: float
    # Provider unrealized P&L for this outcome. An absent key means unavailable, not break-even.
    unrealized_pnl: float


class _LargePositionTraderRequired(TypedDict):
    # Prefixed ID (`trd_...`).
    id: str
    address: str


class LargePositionTrader(_LargePositionTraderRequired, total=False):
    username: str
    grade: Literal["S", "A", "B", "C", "D", "F"] | str
    win_rate: float
    # Trader lifetime realized P&L across all markets.
    pnl: float
    markets_traded: int


class _LargePositionMarketRequired(TypedDict):
    # Prefixed ID (`mkt_...`).
    id: str
    condition_id: str


class LargePositionMarket(_LargePositionMarketRequired, total=False):
    title: str
    slug: str
    event_slug: str
    category: str


class _ListLargeTradesResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[LargeTrade]
    # Writer-backed age and coverage for this page; it is part of the representation and the ETag, while transport
    # cache facts remain in meta.
    data_quality: DataQuality
    has_more: bool
    meta: ResponseMeta


class ListLargeTradesResponse(_ListLargeTradesResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; absent (or null) when it does not.
    total: int


class _LargeTradeRequired(TypedDict):
    # Prefixed ID (wt_...).
    id: str
    # Format: date-time.
    traded_at: str
    size_usd: float
    side: Literal["BUY", "SELL"] | str
    # Traded outcome label (e.g. "Yes"/"No"/team name), resolved provider-first from the trade's outcome_index
    # against market_canonical (index 0 -> yes, 1 -> no). Distinct axis from side (BUY/SELL): side is the trade
    # ...
    outcome: str | None
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the traded outcome; null when
    # unavailable (e.g. unsynced markets) and for a Polymarket trade recorded before 2026-04-02T00:00:00Z, where
    # the traded ...
    token_id: str | None
    price: float
    # Current 0.0–1.0 review score, computed at request time from the trade's size, the trader's win rate today, a
    # bonus when a trader with a win rate above 55% trades at a price below 30¢, and the trade's age now. A higher
    # ...
    review_score: float
    # Current 0.0–1.0 review score, computed at request time from the trader's win rate today and the trade's age
    # now. Deprecated (#16311): `review_score` is the canonical spelling and carries the same value; this key
    # stays ...
    signal_score: float
    # 0.0–1.0 review score written once when the trade row is inserted, from the trader's statistics at that
    # moment. Populated from 2026-08-03T11:59Z; older rows return null and are never backfilled, because a
    # backfill could ...
    recorded_review_score: float | None
    # 0.0–1.0 review score written once when the trade row is inserted; null before 2026-08-03T11:59Z. Deprecated
    # (#16311): `recorded_review_score` is the canonical spelling and carries the same value; this key stays on
    # the ...
    recorded_signal_score: float | None
    # Persisted live suspicion score from the scorer. Null when the row has no persisted score.
    suspicion_score: int | None
    # Persisted scorer track. Null when a legacy row has no stored track label.
    suspicion_track: Literal["whale", "fresh_conviction", "sliced_position"] | str | None
    trader: LargeTradeTrader
    market: LargeTradeMarket


class LargeTrade(_LargeTradeRequired, total=False):
    # This fill's size relative to its market: size_usd divided by a market volume figure recorded at or after the
    # trade, so the value always falls between 0 and 1 inclusive. A $10,000 fill is 0.00005 of a $200M market and
    # ...
    market_volume_share: float


class _LargeTradeTraderRequired(TypedDict):
    id: str
    address: str
    # The grade the trader held when the trade happened, from recorded grade history (recorded from
    # 2026-09-19T23:00Z). Null unless grade_at_trade_status is graded. Never today's grade projected backward.
    grade_at_trade: Literal["S", "A", "B", "C", "D", "F"] | str | None
    # graded: grade_at_trade holds the recorded grade. ungraded: the trader was recorded without a grade at that
    # moment. unknown: no record covers the moment, which is every trade before 2026-09-19T23:00Z and a trade that
    # ...
    grade_at_trade_status: Literal["graded", "ungraded", "unknown"] | str


class LargeTradeTrader(_LargeTradeTraderRequired, total=False):
    username: str
    # The trader's grade today, on every row however old. For what the grade was when the trade happened, read
    # grade_at_trade.
    grade: str


class _LargeTradeMarketRequired(TypedDict):
    id: str
    condition_id: str
    title: str


class LargeTradeMarket(_LargeTradeMarketRequired, total=False):
    slug: str
    # Provider-backed market_canonical category.
    category: str


class _ListWhaleTradesResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[LargeTrade]
    # Writer-backed age and coverage for this page; it is part of the representation and the ETag, while transport
    # cache facts remain in meta.
    data_quality: DataQuality
    has_more: bool
    meta: ResponseMeta


class ListWhaleTradesResponse(_ListWhaleTradesResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; the key is absent when it does not.
    total: int


class _ListLargeTradeHistoryResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[LargeTrade]
    # Writer-backed age and coverage for this page; it is part of the representation and the ETag, while transport
    # cache facts remain in meta.
    data_quality: DataQuality
    has_more: bool
    meta: LargeTradeHistoryMeta


class ListLargeTradeHistoryResponse(_ListLargeTradeHistoryResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; the key is absent when it does not.
    total: int


class _LargeTradeHistoryMetaRequired(TypedDict):
    # Unique request ID (req_ prefix). The same value as the X-Request-Id response header, the request's usage
    # accounting row and its log lines.
    request_id: str
    cached: bool
    source: LargeTradeHistoryMetaSource
    completeness: LargeTradeHistoryMetaCompleteness


class LargeTradeHistoryMeta(_LargeTradeHistoryMetaRequired, total=False):
    # Cache age in seconds; the key is absent when the response was not cached.
    cache_age_s: int


class LargeTradeHistoryMetaSource(TypedDict):
    kind: Literal["local_replay"]
    table: Literal["whale_alerts"]
    provider_fetch_at_request_time: Literal[False]


class LargeTradeHistoryMetaCompleteness(TypedDict):
    status: Literal["best_effort"]
    # Explains that local replay completeness can vary by market and time window.
    reason: str


class _ListWhaleTradeHistoryResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[LargeTrade]
    # Writer-backed age and coverage for this page; it is part of the representation and the ETag, while transport
    # cache facts remain in meta.
    data_quality: DataQuality
    has_more: bool
    meta: LargeTradeHistoryMeta


class ListWhaleTradeHistoryResponse(_ListWhaleTradeHistoryResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; absent (or null) when it does not.
    total: int


class GetLargeTradeResponse(TypedDict):
    object: Literal["large_trade"]
    data: LargeTradeDetail
    meta: ResponseMeta


class LargeTradeDetail(LargeTrade):
    counterparty_analysis: CounterpartyAnalysis


class _CounterpartyAnalysisRequired(TypedDict):
    status: Literal["available", "partial", "unavailable"] | str
    execution_count: int
    available_execution_count: int
    unavailable_execution_count: int
    executions: list[CounterpartyExecution]


class CounterpartyAnalysis(_CounterpartyAnalysisRequired, total=False):
    unavailable_reason: str
    # Deterministic immutable membership snapshot for this detail response.
    snapshot_id: str
    # Stable digest binding page cursors to one snapshot and execution set.
    analysis_id: str
    # Stable cursor after the last execution included in the bounded inline page.
    executions_next_cursor: str


class _CounterpartyExecutionRequired(TypedDict):
    execution_id: str
    exchange_family: Literal["ctf_v2", "neg_risk_ctf_v2"] | str
    transaction_hash: str
    orders_matched_log_index: int
    taker: CounterpartyParticipant
    makers: list[CounterpartyParticipant]


class CounterpartyExecution(_CounterpartyExecutionRequired, total=False):
    # Stable cursor after the last maker included in the bounded inline page.
    makers_next_cursor: str


class _CounterpartyParticipantRequired(TypedDict):
    counterparty_key: str
    # Lowercase Polygon wallet from the exact OrderFilled log.
    execution_wallet: str
    identity_status: Literal["resolved", "infrastructure", "unavailable"] | str
    maker_fill_count: int
    # Exact decimal shares.
    filled_shares: str
    # Exact decimal USDC amount.
    filled_usdc: str
    # Participant share of the exact execution, from 0 through 100.
    share_pct: str
    match_breakdown: list[CounterpartyMatchBreakdown]


class CounterpartyParticipant(_CounterpartyParticipantRequired, total=False):
    resolved_user_id: str
    wallet_family: str
    resolution_block: int
    resolution_source: str
    display_name: str
    grade: str
    # Latest nonfuture recorded wallet-wide trade time for the tracked trader supplying this participant's grade.
    # Omitted when unavailable; not the receipt time or the owner EOA's activity. Trader context is read with the
    # ...
    last_traded_at: str
    # 0xinsider profile path segment for this participant, present only when the execution wallet has a tracked
    # trader: `@<username>` when that username resolves to the trader alone, otherwise the trader's lowercase
    # wallet. ...
    profile_segment: str


class CounterpartyMatchBreakdown(TypedDict):
    match_type: Literal["COMPLEMENTARY", "MINT", "MERGE"] | str
    maker_fill_count: int
    # Exact decimal shares.
    filled_shares: str


class GetWhaleTradeResponse(TypedDict):
    object: Literal["whale_trade"]
    data: LargeTradeDetail
    meta: ResponseMeta


class ListLargeTradeCounterpartyExecutionsResponse(TypedDict):
    object: Literal["counterparty_analysis"]
    data: CounterpartyAnalysis
    meta: ResponseMeta


class ListLargeTradeCounterpartyMakersResponse(TypedDict):
    object: Literal["counterparty_maker_page"]
    data: CounterpartyMakerPage
    meta: ResponseMeta


class _CounterpartyMakerPageRequired(TypedDict):
    analysis_id: str
    snapshot_id: str
    execution_id: str
    items: list[CounterpartyParticipant]


class CounterpartyMakerPage(_CounterpartyMakerPageRequired, total=False):
    # Cursor bound to the analysis, execution, last full-denominator share total, and wallet.
    next_cursor: str


class _ListLeaderboardResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[LeaderboardEntry]
    has_more: bool
    meta: ResponseMeta


class ListLeaderboardResponse(_ListLeaderboardResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; the key is absent when it does not.
    total: int


class _LeaderboardEntryRequired(TypedDict):
    id: str
    address: str
    platform: str


class LeaderboardEntry(_LeaderboardEntryRequired, total=False):
    username: str
    grade: str
    # Hot-streak tier (trailing-7d cross-sectional percentile); a separate axis from the all-time grade. Omitted
    # when there is no recent activity.
    streak_tier: Literal["hot", "rising", "neutral", "cooling", "cold"] | str
    score: float
    # All-time P&L in USD (total_pnl), including unrealized open positions. Kept for back-compat; prefer
    # realized_pnl for the banked figure.
    pnl: float
    # Native realized P&L plus credited maker and taker rebates in USD, with fees already included. The exact
    # numeric value is truncated toward zero to cents before JSON conversion. Wallets without a native snapshot
    # retain ...
    realized_pnl: float
    # Full-history both-sides USD cash volume from a verified Polymarket user-volume observation. Omitted without
    # coverage.
    volume: float
    markets_traded: int
    # The wallet's win rate across ALL categories, not the filtered one. ?category= decides WHICH wallets are
    # listed (the wallet must be ranked in that category); it does not rescope this field, so a soccer-filtered
    # list ...
    win_rate: float
    strategy_type: str
    # Format: date-time.
    last_active: str


class GetPickOfTheDayResponse(TypedDict):
    object: Literal["pick_of_the_day"]
    data: PickOfTheDay
    meta: ResponseMeta


class _PickOfTheDayRequired(TypedDict):
    # Always 'full' for an authenticated Pro key.
    state: Literal["full"]


class PickOfTheDay(_PickOfTheDayRequired, total=False):
    # The pick's local publication date (YYYY-MM-DD). Format: date.
    pick_date: str
    # Stable 1-based slot within the product day's ranked picks.
    pick_rank: int
    # The complete ranked picks for this product day, ordered by pick_rank. Thin days contain fewer items; the
    # selector never fabricates rows.
    picks: list[PickOfTheDay]
    # Number of items in `picks`: the proof-readable picks. Picks held in `proof_pending_picks` are not counted.
    pick_count: int
    # Same-day picks selected but not yet released, ordered by pick_rank. Additive and optional: present only
    # while at least one unreleased slot exists. Each slot exposes only its rank and schedule -- no market
    # identity ...
    scheduled_picks: list[ScheduledPickSlot]
    # Human-readable matchup (e.g. "Portugal vs. Uzbekistan").
    matchup: str
    # Frozen canonical calibration/report bucket (e.g. "Basketball", "MMA", or "Soccer"). Existing semantics are
    # unchanged; presentation consumers should prefer display_category when present.
    category: str
    # Frozen public presentation category. For supported Polymarket sports this is the exact verified provider
    # event identity: an official league (e.g. "WNBA" or "UFC"), the esports title (e.g. "CS2", "LoL", "Dota 2" or
    # ...
    display_category: str
    # Provider platform (e.g. "polymarket").
    platform: str
    # The pick's stored release instant. Normally the current provider kickoff minus one hour; an operator may
    # override it. The actual publish instant can trail it because of worker or claim delay. Format: date-time.
    release_at: str
    # True only before the pick's stored release instant (a pre-release embargo flag); effectively always false on
    # a served, already-published pick. To detect that the backed game has kicked off, use `game_started`.
    is_locked: bool
    # True once the backed game's kickoff has passed (kickoff <= now). When true the snapshotted pre-game price is
    # no longer actionable. Absent for a legacy pick with no stored kickoff (treat as not-started).
    game_started: bool
    # Settlement outcome of the backed side; 'pending' until the market resolves.
    outcome: Literal["pending", "win", "loss", "void"] | str
    # Pre-formatted SETTLEMENT STATUS for display: "Win" / "Loss" / "Void" / "Pending" -- the outcome enum above
    # as a label. Convenience only; outcome is the source value. NOTE: this is the win/loss STATUS, not the backed
    # ...
    outcome_display: str
    # The backed side phrased as a bet: a team for a moneyline (e.g. "Portugal"), the handicap line for a spread
    # (e.g. "Belgium (-2.5)"), or "{team} to advance" for a knockout advancement market (e.g. "Spain to advance").
    pick_outcome_label: str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the backed outcome; omitted when
    # unavailable (e.g. unsynced markets).
    token_id: str
    # The backed side phrased as a bet (e.g. "Portugal to win").
    position: str
    # One-line summary of which side sharp money is backing. Required on every item in `picks`: a current-day
    # published pick whose required holder proof is not safely readable is listed in `proof_pending_picks` instead
    # of ...
    side_summary: str
    # Public V1 compatibility count of S/A sharp-money wallets on the backed side. The first-party/internal
    # current policy counts S/A/B; historical rows retain their frozen policy's count. Required on every item in
    # `picks`: a ...
    sharp_wallet_count: int
    # Deprecated spelling of sharp_wallet_count, emitted beside it with the same value and never removed. Public
    # V1 compatibility count of S/A sharp-money wallets on the backed side. The first-party/internal current
    # policy ...
    smart_wallet_count: int
    # Best public V1-compatible S/A sharp-money grade on the backed side. The first-party/internal current policy
    # can select B, but a current B-only grade is omitted by the stable V1 adapter. Historical rows retain their
    # ...
    top_grade: str
    # Deprecated (#7170): no longer populated for picks selected on/after the calibration-edge change; omitted
    # (absent) for new picks (the field uses skip_serializing_if, so a null value is dropped from the JSON rather
    # than ...
    category_edge_pct: float
    # Deprecated (#7170): no longer populated for picks selected on/after the calibration-edge change; omitted
    # (absent) for new picks (the field uses skip_serializing_if, so a null value is dropped from the JSON rather
    # than ...
    category_edge_sample: int
    # Recency-weighted graded-flow magnitude in USD; omitted when <= 0. Canonical key since #16308; smart_usd is
    # its deprecated spelling, emitted beside it with the same value.
    sharp_usd: float
    # Deprecated spelling of sharp_usd, emitted beside it with the same value and never removed. Recency-weighted
    # graded-flow magnitude in USD; omitted when <= 0.
    smart_usd: float
    # Frozen pre-game probability (0..1) for the backed side, written once at publication. It is the Polymarket
    # CLOB order book midpoint at release, not an executed fill: a buyer lifts the ask, so a subscriber's own
    # entry is ...
    backed_price: float
    # Full-only disclosure when backed_price was recovered from provider history within 30 seconds before
    # publication. Render beside the price. Absent for ordinary publication captures and teasers; this is a
    # historical ...
    entry_price_note: str
    # Pre-formatted backed_price as cents-on-the-dollar odds, to ONE decimal: "62.0c" / "99.9c". Never rounded to
    # a whole cent -- a 99.9c favorite is not a 100c certainty. Convenience only; backed_price is the source
    # value. ...
    odds_display: str
    # The flat stake the published record puts on every pick, in USD: 1000 since 2026-09-22 (it was 100 before).
    # Present exactly when return_usd is, so a reader never has to know the stake from anywhere else.
    stake_usd: float
    # Gross return of stake_usd at the frozen midpoint price (stake_usd / backed_price). A real fill pays the ask,
    # so an executed stake usually returns a little less. Omitted with backed_price.
    return_usd: float
    # The same return on a literal $100 (100 / backed_price), kept for compatibility: the field predates stake_usd
    # and its name promises the $100 basis, so a client that scales it to its own stake stays right. Present
    # exactly ...
    return_per_100: float
    # Pre-formatted return_usd as USD with cents and thousands separators: "$1,612.90" / "$12,500.00". The GROSS
    # return (the stake included), so it carries no sign. Convenience only; return_usd is the source value.
    # Omitted ...
    payout_display: str
    # Pre-formatted PROFIT on the stake -- return_usd minus stake_usd, i.e. the payout net of what you put in --
    # as a signed USD string: "+$612.90". Distinct from payout_display, which is gross. Omitted when return_usd
    # is.
    profit_display: str
    # Backend-owned CLV capture disposition. "pending" means no capture decision exists yet; terminal provider or
    # quality statuses remain distinguishable. The raw close price and timestamp are never serialized.
    clv_status: str
    # Backend-owned CLV evidence basis. `frozen_displayed_entry` uses the persisted displayed entry.
    # `historical_provider_entry` uses a known-CLOB point at or before publication.
    # `historical_provider_price_match` requires the ...
    clv_basis: str
    # Closing-line value toward the backed side, computed as (close / entry - 1) * 100. The basis-specific
    # provider p entry must match the stored display; historical_provider_price_match also requires source
    # provenance to ...
    clv_pct: float
    # Backend-formatted signed CLV percentage, present exactly when clv_pct is present.
    clv_display: str
    # Backend-owned CLV formula text with the entry probability, close probability, and rounded result. Provider
    # timestamps remain private.
    clv_explanation: str
    # Net return for the pick in stake units (return_usd / stake_usd - 1); one unit is one stake_usd stake, and
    # the figure is the same under any stake size. Omitted when the outcome is not valued.
    unit_score: float
    # Backend-formatted signed unit score, present exactly when unit_score is present.
    unit_score_display: str
    # First-party/internal backed-side sharp-money dollar consensus as a fraction 0..1: the share of current-
    # policy sharp dollars on the backed side. Omitted on current public V1 rows when the B-inclusive value has no
    # ...
    sharp_pct: float
    # Market-implied probability of the backed side as a fraction 0..1 (equals backed_price), re-exposed alongside
    # sharp_pct for the WHY breakdown.
    market_pct: float
    # First-party/internal consensus edge = sharp_pct - market_pct, the conviction-vs-price gap (how much more of
    # the current-policy sharp money sits on this side than the price implies). Omitted on current public V1 rows
    # ...
    consensus_edge_pct: float
    # First-party/internal team-directional commitment read at selection time: the fraction (0..1) of the backed
    # side's current-policy graded sharp-money DOLLARS held by wallets read one-way rather than hedged: no
    # opposite ...
    directional_confidence: float
    # Graded backed-side holders read as one-way-committed on this game.
    one_way_holder_count: int
    # Graded backed-side holders read as HEDGED across the game's markets.
    hedged_holder_count: int
    # The one-way holders' share of the backed-side graded dollars (the confidence's numerator).
    one_way_graded_usd: float
    # Backed-side graded dollars the confidence is measured against (its denominator).
    total_graded_usd: float
    # The qualifying category expert whose sport-specific record and real position earned this pick its top
    # selection tier. The first-party/internal current policy admits S/A/B; public V1 exposes a compatible S/A
    # expert and ...
    qualifying_expert: PickOfTheDayQualifyingExpert
    trust: PickTrust
    # Public V1 S/A compatibility count on the backed side (equals the adapted sharp_wallet_count). The first-
    # party/internal current policy counts S/A/B. Historical rows retain their frozen policy's count.
    traders: int
    # Raw backed-side sharp-money USD frozen at generation. This is the Sharp USD value, not the recency-weighted
    # sharp_usd which decays. Omitted on current public V1 rows when the B-inclusive value has no reconstructible
    # S/A ...
    backed_sharp_usd: float
    # Bounded S/A compatibility projection of the frozen sharp-money holders on the backed side. Current full
    # payloads expose the complete S/A/B roster in display_holders; historical rows can retain their earlier
    # frozen shape.
    holders: list[PickHolder]
    # Full-only complete provider-confirmed S/A/B holder roster for the current Pick of the Day backing policy.
    # Omitted for teaser, no-pick, and historical rows whose frozen holder proof predates this policy. Each entry
    # may ...
    display_holders: list[PickHolder]
    # Exact S/A sharp-money proof count on the backed side. The current display_holders roster can be longer
    # because it also carries B-grade sharp-money holders.
    holder_count: int
    # Optional editorial note attached to the pick.
    editorial_note: str
    # Required truthful thesis. With at least one profitable-wallet holder: Profitable wallets hold
    # {pick_outcome_label}[, led by a grade-{top_grade} trader]. Without holder backing: 0xInsider's Pick of the
    # Day is ...
    thesis: str
    # Canonical web market URL.
    market_url: str
    # The canonical /event game-page slug (one neutral page per game); omitted when the game has no neutral event
    # page.
    event_slug: str
    # Backend-resolved /event destination slug for this pick's source market; its absence is an authoritative no-
    # link decision.
    event_link_slug: str
    # Provider-first sports context for the pick's market (team logos, league branding, live score). Full-state
    # only; omitted when the pick is not a team-sports market.
    sports_context: PickSportsContext
    # Risk disclaimer shown with every pick.
    disclaimer: str
    # Published same-day picks whose holder proof is not readable yet, ordered by pick_rank. Additive and
    # optional: present only while at least one such pick exists. While present, `picks` carries only the proof-
    # readable ...
    proof_pending_picks: list[ProofPendingPickSlot]
    # Frozen admission classification, full payload only. The specialist lane exempts two probability rejects and
    # adds no rank bonus. Historical rows remain standard.
    selection_lane: Literal["standard", "longshot_specialist"] | str
    # Optional full-only authorization for newly issued policy-7 picks; omitted for legacy or unissued picks and
    # teasers. It remains historical after expiry.
    entry_authorization: PotdEntryAuthorization


class ScheduledPickSlot(TypedDict):
    """One same-day pick that is selected but not yet released: its stable slot rank plus the backend-owned
    release and kickoff instants. Deliberately minimal -- no matchup, category, platform, side, price,
    or holder fields exist on this shape before release."""
    # Stable 1-based slot within the product day's ranked picks. The slot keeps this rank when it releases.
    pick_rank: int
    # The slot's scheduled release instant, normally the current provider kickoff minus one hour. The actual
    # publish can trail it by bounded worker delay. Format: date-time.
    release_at: str
    # The backed game's current kickoff instant. Format: date-time.
    kickoff: str


class _PickOfTheDayQualifyingExpertRequired(TypedDict):
    # Wallet address of the qualifying expert.
    address: str
    # Provider display name, or null for an unnamed wallet.
    name: str | None
    # 0xinsider grade letter. The first-party/internal current Pick of the Day policy counts S, A, and B; public
    # V1 exposes only the compatible S/A expert.
    grade: str | None
    # The canonical sport bucket the win rate was measured over (for example Basketball). Can be BROADER than the
    # pick's display_category, which names an exact league such as NBA — label the rate with this field, never
    # with ...
    canonical_category: str
    # Share of this wallet's resolved markets in canonical_category whose realized P&L came out positive, as a
    # 0..1 fraction. Above 0.60 by construction for a source=v1 expert; null for an expert who qualified on the
    # ...
    win_rate: float | None
    # Resolved markets in canonical_category behind win_rate. At least 10 by construction for a source=v1 expert;
    # null with win_rate.
    n_resolved: int | None
    # Polymarket's own currentValue for this wallet on the backed outcome, in USD, as of selection. At least 1000
    # by construction through gate policy v7; the standard floor is 500 from v8. From gate policy v5 the floor is
    # ...
    position_usd: float
    # When the skill read model behind the evidence was last rebuilt: trader_category_stats.computed_at for a
    # source=v1 expert, category_skill_v2_current.as_of for a source=v2 expert. Format: date-time.
    stats_computed_at: str


class PickOfTheDayQualifyingExpert(_PickOfTheDayQualifyingExpertRequired, total=False):
    """The qualifying category expert whose sport-specific record and real position earned this pick its
    top selection tier. The first-party/internal current policy admits S/A/B; public V1 exposes a
    compatible S/A expert and omits a current-policy B-grade expert: a candidate backed by one outranks
    every candidate without one. Present only on the full payload. Omitted when no wallet qualified on
    the backed side, on picks generated before the field existed, and on the first-party web teaser,
    which withholds all backed-side evidence. Frozen at SELECTION time — the wallet's position can move
    before the ..."""
    # Current expert policy 10 does not require a category-skill v2 specialist in any sport; in every sport a
    # specialist raises the candidate's rank tier rather than gating it. Standard specialists need a positive ...
    source: Literal["v1", "v2"] | str
    # 95% lower bound of the wallet's mean calibration edge over the market price in canonical_category, in
    # probability units (0.08 is 8 points). Positive by construction for a v2 expert; present on a v1 expert only
    # when the ...
    edge_lower_95: float
    # Point estimate behind edge_lower_95.
    edge_mean: float
    # Independent canonical events behind the edge. At least 10 by construction for a v2 expert.
    independent_event_count: int
    # The same wallet's currentValue on the OTHER outcome of this market, in USD, as of selection. Present from
    # gate policy v5, when the floor moved to net exposure; a wallet long both sides does not qualify. Absent on
    # picks ...
    opposite_position_usd: float
    # Present from expert policy 6. Current expert policy 10 retains the longshot requirement of live v2 only,
    # with a positive lower bound over a large sample, large net backed value and no meaningful opposite value.
    # ...
    lane: Literal["standard", "longshot_specialist"] | str
    # Answered, spread-gated, index-scoped backed probability frozen only on a specialist exception.
    lane_probability: float
    # Canonical provider probability pair branch; absent on standard experts.
    lane_probability_source: Literal["p"]


class PickTrust(TypedDict):
    """Field-level trust metadata for the full Pick of the Day payload. Present on the full shape only
    (omitted on the teaser and the no-pick state, because whether a specialist backs the pick is itself
    backed-side evidence). Unlike TraderTrust it is not gated behind expand=trust: it carries one member
    on an endpoint that returns a single object per day."""
    # Provenance of the frozen qualifying category expert. source.kind=database with
    # reconciliation.status=db_mirror means the evidence deserialized, still satisfies every frozen selection
    # gate, and is being served. On that ...
    qualifying_expert: TrustMetadata


class _PickHolderRequired(TypedDict):
    address: str
    name: str | None
    # All-time trader grade (S, A, B, C, D, F).
    grade: str | None
    shares: float


class PickHolder(_PickHolderRequired, total=False):
    # 0xinsider profile path segment this wallet links to: `@<username>` when that username resolves to this
    # wallet alone, otherwise the lowercase wallet. Percent-encode the part after `@` and append to ...
    profile_segment: str
    # This wallet's win rate in the pick's canonical category bucket (the pick's `category` field, e.g. Basketball
    # -- label the rate with it, never with the narrower `display_category` league, except when ...
    category_win_rate: float
    # The two counts `category_win_rate` is the ratio of, read from the same row: `wins / decided` equals the
    # rate. Counts every resolved Polymarket market the wallet traded in the pick's canonical category (or in its
    # game, ...
    category_win_record: PickHolderCategoryWinRecord
    # For an esports pick, the game `category_win_rate` and `category_win_record` were measured in, by the same
    # name the pick's `display_category` uses for it: `LoL`, `CS2`, `Dota 2`, `Valorant`, `Call of Duty`, `Honor
    # of ...
    category_win_rate_game: str
    # Why `category_win_rate` is present or absent on a `display_holders` entry: `measured` (rate present),
    # `not_enough_data` (the wallet is below the resolved-market floor of 5 in the category), or `unavailable`
    # (the ...
    category_win_rate_status: Literal["measured", "not_enough_data", "unavailable"] | str
    # Days since this wallet's first trade. Stamped at serve time from the wallet's current trader record, never
    # frozen with the pick. The five badge fields are present together, and only for a wallet that carries at
    # least ...
    wallet_age_days: float | None
    # True when the wallet's first trade was under 30 days ago. Stamped at serve time from the wallet's current
    # trader record, never frozen with the pick. The five badge fields are present together, and only for a wallet
    # that ...
    is_new_wallet: bool
    # Distinct markets this wallet has traded. Stamped at serve time from the wallet's current trader record,
    # never frozen with the pick. The five badge fields are present together, and only for a wallet that carries
    # at least ...
    markets_traded: int | None
    # True when the wallet has traded 10,000 or more distinct markets, the breadth floor 0xinsider uses to mark
    # automated wallets. It is a breadth rule, not proof of automation. Stamped at serve time from the wallet's
    # current ...
    is_bot: bool
    # The wallet's X handle from its Polymarket profile, normalized to 1-15 characters of [A-Za-z0-9_] with no
    # `@`. Link it as `https://x.com/<handle>`. Stamped at serve time from the wallet's current trader record,
    # never ...
    x_username: str | None
    category_evidence: HolderCategoryEvidence


class PickHolderCategoryWinRecord(TypedDict):
    """The two counts `category_win_rate` is the ratio of, read from the same row: `wins / decided` equals
    the rate. Counts every resolved Polymarket market the wallet traded in the pick's canonical category
    (or in its game, when `category_win_rate_game` is present), at any position size; the counts are
    rebuilt daily. Present only with `category_win_rate_status` = `measured`; absent otherwise and on
    payloads predating the field."""
    # Resolved markets in the category that this wallet closed with a profit.
    wins: int
    # Resolved markets in the category that this wallet closed with a profit or a loss. A market resolved at zero
    # realized P&L is in neither count.
    decided: int


class _HolderCategoryEvidenceRequired(TypedDict):
    status: Literal["live", "insufficient", "stale", "unknown", "degraded"] | str


class HolderCategoryEvidence(_HolderCategoryEvidenceRequired, total=False):
    """Current category evidence, independent of the global grade. Pick of the Day stamps only the served
    display roster; frozen entry snapshots remain unchanged."""
    canonical_category: str
    skill: CategorySkillV2


class _PickSportsContextRequired(TypedDict):
    # League or competition display name (e.g. "Premier League").
    league_name: str | None
    # League logo URL (provider-owned).
    league_logo: str | None
    # The team mapped to the market's YES outcome, or the parent-event home/first team when event_matchup is true.
    yes_team: PickSportsTeam | None
    # The team mapped to the market's NO outcome, or the parent-event away/second team when event_matchup is true.
    no_team: PickSportsTeam | None
    # Always present. True when the two teams are the parent-event match identity for a teamless binary leg (e.g.
    # a draw, totals, or prop market), not the market's own outcomes.
    event_matchup: bool


class PickSportsContext(_PickSportsContextRequired, total=False):
    """Provider-first sports context for a Pick of the Day market: team crests, league branding, and live
    score. Team logos and league logo are provider-owned (Polymarket /teams crests for clubs, country
    flags for national teams and tennis players); no local derivation."""
    # Provider-owned event taxonomy from Gamma eventMetadata, joined in league · serie · tournament order with
    # blanks and case-insensitive duplicates removed. Separate from league_name; omitted when the provider does
    # not ...
    competition_label: str
    # Provider game identifier (Polymarket Gamma gameId); omitted when the provider supplies none.
    game_id: int
    # Present only alongside event_matchup: the event team the binary leg is about (provider group_item_title
    # matched to a matchup team, e.g. Belgium for "Will Belgium win?"), i.e. the winner on a Yes resolution.
    # Omitted for ...
    event_subject_team: PickSportsTeam
    # The two teams as a single whole-game label, joined "<home> – <away>" (en-dash) in provider display order
    # (e.g. "Portugal – Uzbekistan"). Composed server-side from the provider team names (no title/slug parsing).
    # Present ...
    matchup_title: str


class _PickSportsTeamRequired(TypedDict):
    # Team display label as it appears on the market outcome (e.g. "Portugal").
    label: str | None
    # Abbreviated team label (e.g. "POR").
    short_label: str | None
    # Full team or competitor name (e.g. "Portugal national football team").
    full_name: str | None
    # Provider team identifier (Polymarket /teams id).
    provider_id: int | None
    # Team crest or flag URL. Provider-owned for most teams (Polymarket /teams crest for clubs, country flag for
    # national teams and tennis players). A club with a vendored crest carries it instead, served same-origin as a
    # ...
    logo: str | None
    # Team brand color as a hex string (provider-owned).
    color: str | None
    # Win-loss record as a display string (e.g. "12-4").
    record: str | None
    # Live or final score as a display string when the game is in play or settled.
    score: str | None


class PickSportsTeam(_PickSportsTeamRequired, total=False):
    """A single sports team or competitor in a Pick of the Day market's sports context. Identity and score
    fields are provider-owned and nullable. The structured score fields (`sets`, `format`, `sets_won`)
    and the tennis fields (`headshot`, `tour`) are backend-owned and are OMITTED rather than null when
    they do not apply, so a consumer must treat an absent key and a null the same way."""
    # Tennis player headshot URL, served same-origin. Present only for a tennis competitor the headshot resolver
    # matched; absent for team sports and for unmatched players, where `logo` stays the fallback.
    headshot: str
    # Tennis tour this competitor belongs to. Present for every tennis entry whether or not `headshot` resolved,
    # so a consumer can tell a tennis player with no photo from a non-tennis team. Absent for every other sport.
    # Only ...
    tour: Literal["atp", "wta", "itf"] | str
    # Per-set score cells for this side, in set order. Backend-owned: render these rather than parsing `score`.
    # Omitted entirely when the provider score is not a structured multi-set match or could not be parsed, so an
    # absent ...
    sets: list[ScoreCell]
    format: ScoreFormat
    # Completed sets won by this side. Present only when both sides expose the same set columns, so a partially
    # parsed scoreline reports no tally rather than a misleading one.
    sets_won: int


class _ScoreCellRequired(TypedDict):
    # Games won in this set.
    games: int


class ScoreCell(_ScoreCellRequired, total=False):
    """One side's score in a single set. The verbatim provider text stays on the team's `score` string;
    this is the parsed form."""
    # Tiebreak points won in this set. Omitted when the set had no tiebreak; absence and zero are different.
    tiebreak: int


# Shape the provider score string was parsed into. `two_side` is one aggregate per side (basketball `105-98`),
# `multi_set` is per-set columns (tennis `6-7(5-7), 6-0, 1-0`), `esports_series` is a maps/sets/format triplet
# (`000-000|2-0|Bo3`). Omitted when the score could not be parsed.
ScoreFormat = Union[Literal["two_side", "multi_set", "esports_series"], str]


class _ProofPendingPickSlotRequired(TypedDict):
    # Stable 1-based slot within the product day's ranked picks. The pick keeps this rank once its proof is
    # readable and it moves into `picks`.
    pick_rank: int
    # The pick's stored release instant. Format: date-time.
    release_at: str
    # Recommended next read: 30 seconds ahead while pre-game proof is warming, one hour ahead for a post-kickoff
    # pending legacy row that only settlement can make readable. Schedule against it instead of polling. Format:
    # ...
    retry_at: str


class ProofPendingPickSlot(_ProofPendingPickSlotRequired, total=False):
    """One PUBLISHED same-day pick whose holder proof is not readable yet: its stable slot rank, the
    release and kickoff instants, and the instant before which a retry cannot succeed. Every item in
    `picks` carries its full required shape, so a pick that cannot meet it is listed here instead of
    being served with missing fields or a synthetic zero."""
    # The backed game's frozen kickoff instant; absent for a legacy row without one. Format: date-time.
    kickoff: str


class PotdEntryAuthorization(TypedDict):
    """Policy-7 issuance binds one condition, selected token, outcome, canonical event and sport. Reuse the
    same authorization across public/private discovery and retries. Require a new account-size
    executable book and current market eligibility; this frozen reference does not prove current
    liquidity or positive expected value. Absence or expiry cannot authorize a new automated entry."""
    version: Literal[1]
    # Format: uuid.
    authorization_id: str
    policy_version: Literal[7]
    condition_id: str
    token_id: str
    outcome_index: Literal[0, 1] | int
    # Canonical sport bucket, not display_category.
    category: str
    # Exact provider parent event ID, or provider event ID when no parent exists.
    canonical_event_id: str
    # Immutable decimal limit: first fresh selected-token ask plus 0.02, floored to the provider tick below 1.
    # Fees excluded. Never a calibrated fair probability.
    max_entry_price: str
    reference_best_ask: str
    reference_book_hash: str
    # Format: date-time.
    reference_book_at: str
    # Format: date-time.
    issued_at: str
    # Original provider kickoff ceiling. Never extended on retry. Format: date-time.
    expires_at: str


class GetPickOfTheDayArchiveResponse(TypedDict):
    object: Literal["pick_of_the_day_archive"]
    data: PickOfTheDayArchive
    meta: ResponseMeta


class PickOfTheDayArchive(TypedDict):
    # Every published Pick of the Day, newest first by pick_date and then pick_rank within each product day.
    picks: list[PickOfTheDayArchiveEntry]
    # One entry per product day that has a published pick, newest first, in the same order as picks. Each carries
    # that day's net units, accumulated in the same backend pass and behind the same visibility gate as ...
    days: list[PickOfTheDayArchiveDay]
    hit_rate: PickOfTheDayHitRate


class _PickOfTheDayArchiveEntryRequired(TypedDict):
    # The pick's local publication date (YYYY-MM-DD). Format: date.
    pick_date: str
    # Human-readable matchup (e.g. "Portugal vs. Uzbekistan").
    matchup: str
    # Frozen canonical calibration/report bucket (e.g. "Basketball", "MMA", or "Soccer"). Existing semantics are
    # unchanged; presentation consumers should prefer display_category when present.
    category: str
    # Settlement outcome of the backed side; 'pending' until the market resolves.
    outcome: Literal["pending", "win", "loss", "void"] | str


class PickOfTheDayArchiveEntry(_PickOfTheDayArchiveEntryRequired, total=False):
    # Stable 1-based slot within the product day's ranked picks.
    pick_rank: int
    # Frozen public presentation category. For supported Polymarket sports this is the exact verified provider
    # event identity: an official league (e.g. "WNBA" or "UFC"), the esports title (e.g. "CS2", "LoL", "Dota 2" or
    # ...
    display_category: str
    # Provider (Polymarket Gamma) market thumbnail URL (markets.image); omitted (not null) when the market has no
    # image. Public regardless of the backed-side gate, so present for pending rows too.
    image_url: str
    # The backed side's outcome label. Omitted for a still-pending pick when the request is not from an
    # authenticated Pro key.
    pick_outcome_label: str
    # Best public V1-compatible S/A sharp-money grade on the backed side; a current B-only grade is omitted by the
    # stable V1 adapter, while historical rows retain their frozen policy's grade. Omitted when no sharp-money ...
    top_grade: str
    # Pre-formatted settlement status for display: "Win" / "Loss" / "Void" / "Pending" -- the outcome enum above
    # as a label, from the same formatter the pick payload's outcome_display uses. Convenience only; outcome is
    # the ...
    outcome_display: str
    # The flat stake this row was valued at, in USD: 1000 since 2026-09-22 (100 before). Every row of the record
    # is valued at the current stake, including picks published before the change. Present exactly when return_usd
    # is.
    stake_usd: float
    # Gross return of stake_usd on this resolved pick: a win returns stake_usd / backed_price, a loss returns 0, a
    # void refunds stake_usd. A loss always returns 0 (the whole stake is lost regardless of price). The operand
    # is ...
    return_usd: float
    # The same return on a literal $100 (a win returns 100 / backed_price, a loss 0, a void 100), kept for
    # compatibility: the field predates stake_usd and its name promises the $100 basis. Present exactly when
    # return_usd is.
    return_per_100: float
    # Pre-formatted return_usd as USD with cents: "$2,000.00". Present exactly when return_usd is -- it is
    # formatted from that already-gated value -- so it is omitted for a still-pending pick, an unpriced win, and
    # any pick ...
    payout_display: str
    # Frozen price of the backed side (0..1) that return_usd and return_per_100 were computed from: on a win,
    # stake_usd / backed_price equals return_usd. It is the Polymarket CLOB order book midpoint at release, frozen
    # ...
    backed_price: float
    # Closing-line value toward the backed side, computed as (close / entry - 1) * 100. Omitted when the row is
    # gated, ineligible, or not measured.
    clv_pct: float
    # Backend-formatted signed CLV percentage, present exactly when clv_pct is present.
    clv_display: str
    # Entry operand of clv_pct: the frozen pick probability the close is compared against. It equals backed_price,
    # which CLV eligibility requires. Present exactly when clv_pct is.
    clv_entry_price: float
    # Close operand of clv_pct: the last valid Polymarket probability before the close bound (kickoff, or the
    # first instant the live feed reported the game in progress when that came earlier). Present exactly when
    # clv_pct is; ...
    clv_close_price: float
    # Whether CLV applies. A visible resolved pick published after kickoff is not_applicable.
    clv_applicability: Literal["applicable", "not_applicable"] | str
    # Backend-owned CLV text. A measured row names the entry, then the close, then the formula (close / entry - 1)
    # x 100 and its rounded result; otherwise it gives the reason CLV does not apply or is unavailable.
    clv_explanation: str
    # Exact backend CLV capture disposition for this visible row. Pending and terminal provider or quality
    # statuses are distinguishable; capture timestamps are never serialized, while a measured row's entry and
    # close prices ...
    clv_status: str
    # Backend-owned CLV evidence basis. Source-null price-match bases preserve unknown original provenance.
    # `historical_provider_nearby_price_match` requires a matching Polymarket point within five minutes before
    # publication.
    clv_basis: str
    # Net return for this pick in stake units (return_usd / stake_usd - 1), where one unit is one stake_usd stake;
    # the same figure under any stake size. Omitted when the backed side is withheld or the pick is not valued.
    unit_score: float
    # Backend-formatted signed unit score, present exactly when unit_score is present.
    unit_score_display: str


class _PickOfTheDayArchiveDayRequired(TypedDict):
    # The product day (YYYY-MM-DD). Format: date.
    date: str
    # Published picks on the day: wins + losses + void + pending.
    picks: int
    # Picks on the day that resolved as a win, counted by the same pass as hit_rate.wins, so the day entries sum
    # to the headline record.
    wins: int
    # Picks on the day that resolved as a loss, counted by the same pass as hit_rate.losses.
    losses: int
    # Picks on the day that resolved void (stake refunded).
    void: int
    # Picks on the day not yet resolved. A day whose picks are all pending is a real 0-0 day with pending > 0, not
    # a missing record.
    pending: int


class PickOfTheDayArchiveDay(_PickOfTheDayArchiveDayRequired, total=False):
    # Net units over the day's visible, valued, decided (win/loss) picks: the same population staked_usd runs
    # over. Omitted when the day has not scored -- every pick still pending, every pick void, or a price-gated
    # current ...
    unit_score: float
    # unit_score pre-formatted as signed units to two decimals (for example +1.24u or -2.00u), by the same
    # formatter the per-pick unit_score_display and hit_rate.unit_score_display use. Present exactly when
    # unit_score is; ...
    unit_score_display: str
    # win when every decided pick on the day won, loss when every one lost, over at least three decided (win or
    # loss) picks with nothing pending. Omitted for every other day. A void is not a result: it neither lifts a
    # day ...
    sweep: Literal["win", "loss"] | str


class _PickOfTheDayHitRateRequired(TypedDict):
    # Number of decided picks that won.
    wins: int
    # Number of decided picks that lost.
    losses: int
    # Number of decided picks (wins + losses); excludes void and pending.
    decided: int
    # Rolling hit rate as a percentage (wins / decided * 100, to 1 decimal); 0 when none are decided.
    pct: float
    # Number of picks that resolved void (excluded from the hit rate).
    void: int
    # Number of picks still pending resolution (excluded from the hit rate).
    pending: int
    # Cumulative profit (USD) of a stake_usd-per-pick strategy over visible valued decided picks: a priced win
    # pays stake_usd/backed_price - stake_usd, every visible loss pays -stake_usd independent of price, and a void
    # pays ...
    net_profit_usd: float
    # Total staked (USD) = stake_usd * count of visible valued decided picks: every visible loss plus every priced
    # win. Void, unpriced wins, and current non-Insider rows whose price is gated are excluded.
    staked_usd: float
    # Return on the staked amount as a percentage (net_profit_usd / staked_usd * 100, to 1 decimal); 0 when
    # nothing is staked.
    roi_pct: float
    # Pre-formatted net profit for display, e.g. "+$100" / "-$40". Whole dollars, signed, round-then-signed so a
    # rounds-to-zero record reads "+$0" (never "-$0"). Convenience only; net_profit_usd is the source value.
    net_profit_display: str
    # Pre-formatted ROI for display, e.g. "+8.3%" / "-20.0%". One decimal, signed, round-then-signed so a rounds-
    # to-zero record reads "+0.0%" (never "-0.0%"). Convenience only; roi_pct is the source value.
    roi_display: str
    # Pre-formatted win rate for display, e.g. "92.3%". One decimal, unsigned. Convenience only; pct is the source
    # value.
    win_rate_display: str
    # Visible resolved archive rows with no CLV capture disposition yet.
    clv_pending: int
    # Visible resolved archive rows with a terminal non-measured CLV disposition.
    clv_unavailable: int
    # Aggregate CLV state. Counts remain available for mixed measured/pending/unavailable populations.
    clv_state: Literal["measured", "pending", "unavailable", "not_applicable", "none"] | str
    # Visible resolved archive rows with valid basis-specific CLV entry evidence. Known-source bases require CLOB
    # provenance; historical_provider_price_match instead requires source provenance to remain null and the latest
    # ...
    clv_eligible: int
    # Every visible resolved archive row, including post-kickoff picks. A price-gated current row is excluded
    # until its backed side becomes visible.
    clv_total: int
    # Eligible resolved public rows with a measured Polymarket CLOB close.
    clv_measured: int
    # Visible resolved rows published before kickoff. This is the CLV coverage denominator.
    clv_applicable: int
    # Visible resolved rows published after kickoff. These rows remain public but do not enter coverage.
    clv_not_applicable: int
    # Measured public rows where close is strictly greater than entry.
    clv_beats_close: int
    # Measured public rows where close exactly equals entry.
    clv_ties: int


class PickOfTheDayHitRate(_PickOfTheDayHitRateRequired, total=False):
    # The flat stake every money figure here assumes, in USD: 1000 since 2026-09-22 (100 before). Always present.
    stake_usd: float
    # Cumulative net return in stake units over the same valued win/loss population as net_profit_usd.
    unit_score: float
    # Backend-formatted signed cumulative unit score, for example "+1.25u". Omitted when no valued settled pick
    # contributes to the aggregate.
    unit_score_display: str
    # Measured divided by clv_applicable as a percentage. Omitted when clv_applicable is zero.
    clv_coverage_pct: float
    # Backend-formatted measured/clv_applicable coverage percentage.
    clv_coverage_display: str
    # Backend-owned coverage count text, including the excluded post-kickoff count.
    clv_coverage_explanation: str
    # Arithmetic mean of per-pick ratio CLV, (close / entry - 1) * 100. A cheap entry weighs more here than a
    # favorite, so the headline average is clv_avg_pp; this field is kept for continuity. Suppressed until at
    # least five ...
    clv_avg_pct: float
    # Backend-formatted signed average CLV percentage, present when clv_avg_pct is present.
    clv_avg_display: str
    # Arithmetic mean of the measured closing-line move in percentage points, (close - entry) * 100, so every pick
    # counts on the same scale. The headline CLV average. Covers the same measured rows as clv_avg_pct and is ...
    clv_avg_pp: float
    # Backend-formatted signed average in percentage points, for example "+0.4 pp"; a value that rounds to zero
    # reads "0.0 pp". Present when clv_avg_pp is present.
    clv_avg_pp_display: str
    # Cumulative track-record series, one point per decided (win/loss) pick in ascending pick_date order (void and
    # pending add no point). A non-valued decided row carries cumulative profit forward while advancing hit rate.
    # ...
    series: list[PickOfTheDayHitRateSeriesItem]


class PickOfTheDayHitRateSeriesItem(TypedDict):
    # The decided pick's publish date (YYYY-MM-DD). Format: date.
    date: str
    # Running cumulative stake_usd-per-pick profit (USD) through this pick; valued losses and priced wins are
    # booked, while a non-valued decided row carries profit forward unchanged.
    net_profit_usd: float
    # Running rolling hit rate (wins / decided * 100, to 1 decimal) through this pick.
    hit_rate_pct: float


class GetPickOfTheDayLedgerResponse(TypedDict):
    object: Literal["pick_of_the_day_ledger"]
    data: PickOfTheDayLedger
    meta: ResponseMeta


class PickOfTheDayLedger(TypedDict):
    """The commitment ledger: every published pick, ascending, in the state its commitment is actually in.
    The counts are derived from entries in the same pass that builds it."""
    # One entry per published (pick_date, pick_rank), ascending by pick_date then pick_rank.
    entries: list[PickOfTheDayLedgerEntry]
    # Number of entries, all states included.
    entry_count: int
    # Entries committed to and not yet settled.
    sealed_count: int
    # Entries committed to and verifiable now.
    opened_count: int
    # Entries carrying no commitment, so provable by nothing: the honest size of the unprovable part of the
    # record. It only stops growing; no pick is ever retro-sealed.
    uncommitted_count: int


class PickOfTheDayLedgerSealedEntry(TypedDict):
    """A published pick that has not settled. Carries the commitment and nothing that states a side or a
    price: no nonce, no payload, no outcome. Publishable the instant the pick releases."""
    state: Literal["sealed"]
    # ET product day the pick belongs to (YYYY-MM-DD). Format: date.
    pick_date: str
    # 1-based daily slot within the product day.
    pick_rank: int
    # sha256(canonical_json(payload) || nonce), lowercase hex, no 0x prefix. Publishable the moment the pick
    # releases: without the nonce it is not invertible.
    commitment_hash: str
    # The construction the hash was taken with, stated in the response so a verifier never has to guess the
    # serialization.
    commitment_algo: Literal["sha256(canonical_json(payload)||nonce)"]
    # When the hash was frozen. Always strictly before kickoff: a pick that reaches kickoff unsealed stays
    # unsealed forever, because a seal written after the game started would be a backdated proof. Format: date-
    # time.
    sealed_at: str
    # The frozen provider kickoff in the canonical payload form: whole seconds, UTC, literal Z. This exact string
    # reappears inside payload.kickoff when the pick opens. Format: date-time.
    kickoff: str
    # The pick's public page. Format: uri.
    permalink: str


class PickOfTheDayLedgerOpenedEntry(TypedDict):
    """A settled pick whose commitment is open: the nonce plus the exact payload the hash was taken over.
    Concatenate the payload bytes as received with the decoded nonce and sha256 them to reproduce
    commitment_hash."""
    state: Literal["opened"]
    # ET product day the pick belongs to (YYYY-MM-DD). Format: date.
    pick_date: str
    # 1-based daily slot within the product day.
    pick_rank: int
    # sha256(canonical_json(payload) || nonce), lowercase hex, no 0x prefix. Publishable the moment the pick
    # releases: without the nonce it is not invertible.
    commitment_hash: str
    # The 32-byte nonce the hash was taken over, lowercase hex, no 0x prefix. Secret while the pick is live: a
    # pick payload is low entropy, so a published nonce on a live pick would hand out the backed side.
    commitment_nonce: str
    # The construction the hash was taken with, stated in the response so a verifier never has to guess the
    # serialization.
    commitment_algo: Literal["sha256(canonical_json(payload)||nonce)"]
    # When the hash was frozen. Always strictly before kickoff: a pick that reaches kickoff unsealed stays
    # unsealed forever, because a seal written after the game started would be a backdated proof. Format: date-
    # time.
    sealed_at: str
    # When outcome was LAST written to a settled value, or null when that instant is unknown. It moves with a
    # corrected market re-mapping an already-settled pick, while commitment_hash stays untouched -- which is how a
    # mirror ...
    resolved_at: str | None
    # The frozen provider kickoff in the canonical payload form: whole seconds, UTC, literal Z. This exact string
    # reappears inside payload.kickoff when the pick opens. Format: date-time.
    kickoff: str
    payload: PickOfTheDayCommitmentPayload
    # How the pick settled. Never pending: a pending pick is a sealed entry.
    outcome: Literal["win", "loss", "void"] | str
    # Frozen matchup, for a reader.
    matchup: str
    # Frozen canonical sport bucket used for selection calibration (Basketball, MMA), not the exact public league
    # identity; the archive owns that.
    category: str
    # The pick's public page. Format: uri.
    permalink: str


class PickOfTheDayCommitmentPayload(TypedDict):
    """The frozen identity of the pick, exactly as the hash was taken over it. Served byte for byte as it
    was hashed -- keys sorted by UTF-8 byte value, no insignificant whitespace -- so a verifier
    concatenates and hashes with nothing to reconstruct. Property order below is the wire order. The
    outcome is deliberately NOT part of it: surviving a corrected outcome unchanged is the case the
    commitment exists for. Worked example: ..."""
    # Frozen pre-game price of the backed side, 0..1, as the plain decimal text of the stored NUMERIC at full
    # stored precision, trailing zeros included. A string, never a number: a float round-trip would change the
    # bytes and ...
    backed_price: str
    # Provider condition id of the backed market.
    condition_id: str
    # Frozen provider kickoff, whole seconds, UTC, literal Z. Fixed precision, never a shortest-lossless
    # rendering. Format: date-time.
    kickoff: str
    # ET product day (YYYY-MM-DD). Format: date.
    pick_date: str
    # Index of the backed outcome within the market.
    pick_outcome_index: Literal[0, 1] | int
    # Frozen display label of the backed outcome.
    pick_outcome_label: str
    # 1-based daily slot.
    pick_rank: int
    # Provider platform.
    platform: str


class PickOfTheDayLedgerUncommittedEntry(TypedDict):
    """A published pick with no commitment: it predates the scheme, or it reached kickoff unsealed. Nothing
    here is evidence of WHEN the pick was made. It is emitted rather than skipped, because a ledger with
    holes where the unprovable picks were would silently flatter the record. Once the pick settles,
    payload names its market, side and price, so the outcome can still be checked against the market's
    own resolution."""
    state: Literal["uncommitted"]
    # ET product day the pick belongs to (YYYY-MM-DD). Format: date.
    pick_date: str
    # 1-based daily slot within the product day.
    pick_rank: int
    # Always true: this pick has no commitment and never will.
    pre_commitment: Literal[True]
    # How the pick settled, or pending.
    outcome: Literal["pending", "win", "loss", "void"] | str
    # Frozen matchup, for a reader.
    matchup: str
    # Frozen canonical sport bucket used for selection calibration (Basketball, MMA), not the exact public league
    # identity; the archive owns that.
    category: str
    # When outcome was LAST written to a settled value, or null when that instant is unknown. It moves with a
    # corrected market re-mapping an already-settled pick, while commitment_hash stays untouched -- which is how a
    # mirror ...
    resolved_at: str | None
    # The pick's market, side and price once it has settled; null while it is pending, and null for a settled pick
    # whose stored row lacks one of these columns. Not hashed: nothing was committed over these values, which is
    # ...
    payload: PickOfTheDayUncommittedPayload | None
    # The pick's public page. Format: uri.
    permalink: str


class PickOfTheDayUncommittedPayload(TypedDict):
    """A settled uncommitted pick's market, side and price. The same eight fields as
    PickOfTheDayCommitmentPayload, in the same key order, so a settled pick's side and price sit under
    payload whatever the entry's state. It is NOT a commitment: no hash was taken over it before the
    game, and it proves nothing about when the pick was made."""
    # Frozen pre-game price of the backed side, 0..1, as the plain decimal text of the stored NUMERIC at full
    # stored precision, trailing zeros included -- rendered exactly as the commitment payload renders it.
    backed_price: str
    # Provider condition id of the backed market.
    condition_id: str
    # Frozen provider kickoff, UTC, literal Z; null when no kickoff was frozen. Whole seconds render exactly as
    # the commitment payload does; a sub-second instant keeps its fraction rather than being truncated, since
    # nothing ...
    kickoff: str | None
    # ET product day (YYYY-MM-DD). Format: date.
    pick_date: str
    # Index of the backed outcome within the market.
    pick_outcome_index: Literal[0, 1] | int
    # Frozen display label of the backed outcome.
    pick_outcome_label: str
    # 1-based daily slot.
    pick_rank: int
    # Provider platform.
    platform: str


# One ledger entry. Read `state` to know which shape you have; the three are disjoint.
PickOfTheDayLedgerEntry = Union[PickOfTheDayLedgerSealedEntry, PickOfTheDayLedgerOpenedEntry, PickOfTheDayLedgerUncommittedEntry]


class _ListTrendingWalletsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[TrendingWallet]
    has_more: bool
    meta: ResponseMeta


class ListTrendingWalletsResponse(_ListTrendingWalletsResponseRequired, total=False):
    # Opaque cursor for the next page; absent on the last page.
    next_cursor: str
    # Total ranked rows when the read model exposes a count; may be absent.
    total: int


class _TrendingWalletRequired(TypedDict):
    # Prefixed trader ID (`trd_...`).
    id: str
    address: str
    # 1-based rank within the full ranked set (stable across pages).
    rank: int
    # Real provider platform; surfaced, never coerced. Polymarket only.
    platform: Literal["polymarket"]
    # Polymarket weekly/monthly P&L for the wallet in USD, taken from Polymarket's canonical leaderboard (data-
    # api.polymarket.com/v1/leaderboard?timePeriod=week|month&orderBy=PNL). This is the ranking axis and the rows
    # are ...
    trending_pnl_usd: float
    window_markets_traded: int
    # Distinct in-window UTC trade days from our trades (0 if the winner is not in our DB).
    window_trade_days: int
    # Shape-only daily P&L sparkline across the window, derived from Polymarket's documented user-pnl cumulative
    # curve (GET /v2/user-pnl) converted to per-day deltas. It conveys the trend of the curve only and is NOT ...
    daily_pnl_series: list[TrendingWalletDailyPnlSeriesItem]


class TrendingWallet(_TrendingWalletRequired, total=False):
    username: str
    # Official Polymarket avatar URL (profileImage).
    profile_image_url: str
    # Both-sides cash volume over the window in USD, from Polymarket GET /v2/user-volume (volume_usdc). Omitted
    # when Polymarket served no volume for the wallet: an absent observation, never zero. Polymarket tracks volume
    # in ...
    window_volume_usd: float
    # Both-sides traded volume over the window in SHARES, from the Polymarket leaderboard row, whose own schema
    # states the figure is never USD. Omitted when the row carried none.
    window_volume_shares: float
    # All-time trader grade; a separate axis from streak_tier. Led by realized profit (the money actually banked,
    # about 95 percent of the grade), with forecasting calibration, risk-adjusted returns, and consistency as the
    # ...
    grade: Literal["S", "A", "B", "C", "D", "F"] | str
    # Hot-streak tier (trailing-7d cross-sectional percentile). Omitted when there is no recent activity.
    streak_tier: Literal["hot", "rising", "neutral", "cooling", "cold"] | str
    all_time_pnl_usd: float
    all_time_score: float
    # Format: date-time.
    last_synced: str


class TrendingWalletDailyPnlSeriesItem(TypedDict):
    # Format: date.
    date: str
    pnl_usd: float


class _SearchMarketsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[MarketSearchResult]
    has_more: bool
    meta: ResponseMeta


class SearchMarketsResponse(_SearchMarketsResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; the key is absent when it does not.
    total: int


class MarketSearchResult(TypedDict):
    id: str
    condition_id: str
    title: str
    slug: str | None
    category: str | None
    platform: str | None
    status: Literal["active", "closed"] | str


class _SearchContentResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[ContentSearchResult]
    has_more: Literal[False]
    meta: ResponseMeta


class SearchContentResponse(_SearchContentResponseRequired, total=False):
    # Omitted because content search is a bounded one-page result.
    next_cursor: str
    # Absent because content search is a bounded relevance result and does not run a count query.
    total: int


class ContentSearchResult(TypedDict):
    # Backend-owned stable editorial content identifier.
    content_id: str
    # Editorial content kind.
    kind: Literal["learn", "glossary", "comparison", "research", "strategy"] | str
    # Backend-owned content slug.
    slug: str
    # Editorial title.
    title: str
    # Search-result excerpt.
    excerpt: str
    # Canonical first-party content URL.
    url: str


class _ExploreMarketsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[ExploreEntry]
    has_more: bool
    facets: ExploreFacets
    meta: ResponseMeta


class ExploreMarketsResponse(_ExploreMarketsResponseRequired, total=False):
    next_cursor: str
    # Total matching visible entries after grouping. Present on the first page and omitted on cursor pages.
    total: int
    # When this response body was computed. Present whenever the body came from, or was just written to, the 60s
    # explore cache. Pair it with fresh_for_seconds to derive how much longer the body may be reused: ...
    computed_at: str
    # How long the body computed at computed_at is good for, in seconds. Deliberately not pre-subtracted: a cached
    # body cannot carry a number that changes while it sits in the cache. Excluded from the ETag validator.
    fresh_for_seconds: int


class ExploreGroup(TypedDict):
    type: Literal["group"]
    event_slug: str
    parent_title: str
    image: str | None
    platform: str | None
    category: str | None
    # Markets in the event cluster, ranked by volume with condition_id as the tie-breaker. The selected
    # representative is retained within the 12-market cap.
    markets: list[ExploreMarket]
    rep_volume: float | None
    # Canonical key since #16304; rep_whales is its deprecated spelling, emitted beside it with the same value.
    rep_large_trades: int | None
    rep_whales: int | None


class _ExploreMarketRequired(TypedDict):
    id: str
    condition_id: str
    # Non-empty market title.
    title: str
    # Provider-native market slug.
    slug: str | None
    # First-party market page slug used for internal links.
    url_slug: str | None
    image: str | None
    icon: str | None
    category: str | None
    platform: str | None
    status: Literal["active", "closed"] | str
    volume: float | None
    liquidity: float | None
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value.
    large_trade_count: int | None
    whale_trade_count: int | None
    # Canonical key since #16304; whale_distinct_wallets is its deprecated spelling, emitted beside it with the
    # same value.
    large_trade_distinct_wallets: int | None
    whale_distinct_wallets: int | None
    # Canonical key since #16304; whale_total_usd is its deprecated spelling, emitted beside it with the same
    # value.
    large_trade_total_usd: float | None
    whale_total_usd: float | None
    # Canonical key since #16304; whale_last_trade_at is its deprecated spelling, emitted beside it with the same
    # value. Format: date-time.
    large_trade_last_at: str | None
    # Format: date-time.
    whale_last_trade_at: str | None
    # Format: date-time.
    end_date: str | None
    # Format: date-time.
    created_at: str | None
    outcome_yes: str | None
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the YES outcome; null when unavailable
    # (e.g. unsynced markets).
    token_id_yes: str | None
    outcome_no: str | None
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the NO outcome; null when unavailable
    # (e.g. unsynced markets).
    token_id_no: str | None
    event_slug: str | None
    smart_score: float | None
    smart_count: int | None
    smart_label: str | None
    # Display label for the YES/outcome_index=0 side, enriched from provider outcome metadata when available.
    outcome_yes_label: str | None
    # Display label for the NO/outcome_index=1 side, enriched from provider outcome metadata when available.
    outcome_no_label: str | None
    # Provider-owned YES/outcome_index=0 identifier when available for trade-ticket wiring.
    outcome_yes_provider_id: int | None
    # Provider-owned NO/outcome_index=1 identifier when available for trade-ticket wiring.
    outcome_no_provider_id: int | None
    open_interest: float | None
    oi_change_pct: float | None
    price_points: list[list[float]] | None
    no_price_points: list[list[float]] | None
    last_price: float | None
    no_last_price: float | None
    change_pct_24h: float | None
    no_change_pct_24h: float | None
    # Backend-owned deterministic market discovery score used by the hot sort.
    discover_score: float | None


class ExploreMarket(_ExploreMarketRequired, total=False):
    score_components: ExploreMarketScoreComponents
    freshness: ExploreMarketFreshness


class ExploreMarketScoreComponents(TypedDict):
    volume_signal: float | None
    # Canonical key since #16304; whale_signal is its deprecated spelling, emitted beside it with the same value.
    large_trade_signal: float | None
    whale_signal: float | None
    liquidity_signal: float | None
    recency_signal: float | None
    # Canonical key since #16308; smart_money_signal is its deprecated spelling, emitted beside it with the same
    # value.
    sharp_money_signal: float | None
    # Deprecated spelling of sharp_money_signal; emitted beside it with the same value and never removed.
    smart_money_signal: float | None
    price_move_signal: float | None
    missing_price_penalty: float


class ExploreMarketFreshness(TypedDict):
    enrichment_status: Literal["available", "unavailable"] | str
    price_status: Literal["available", "unavailable"] | str


class ExploreStandalone(TypedDict):
    type: Literal["standalone"]
    market: ExploreMarket


ExploreEntry = Union[ExploreGroup, ExploreStandalone]


class ExploreFacets(TypedDict):
    categories: list[ExploreFacetValue]
    platforms: list[ExploreFacetValue]


class ExploreFacetValue(TypedDict):
    value: str
    label: str
    count: int


class _ListSmartMoneyFlowsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[SmartMoneyFlowMarket]
    has_more: bool
    meta: ResponseMeta


class ListSmartMoneyFlowsResponse(_ListSmartMoneyFlowsResponseRequired, total=False):
    next_cursor: str
    total: int


class SmartMoneyFlowMarket(TypedDict):
    market: SmartMoneyFlowMarketMarket
    # Sharp-money flow aggregate for the market (canonical; smart_money is a deprecated byte-identical alias).
    sharp_money: SmartMoneyFlowMarketSharpMoney
    # Deprecated alias of sharp_money; byte-identical and retained for backward compatibility.
    smart_money: SmartMoneyFlowMarketSmartMoney
    timeframe: str


class SmartMoneyFlowMarketMarket(TypedDict):
    id: str
    condition_id: str
    title: str | None
    slug: str | None
    category: str | None
    platform: str | None


class _SmartMoneyFlowMarketSharpMoneyRequired(TypedDict):
    net_flow_usd: float
    direction: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the net-flow direction outcome; null
    # when unavailable (e.g. unsynced markets).
    token_id: str | None
    whale_trade_count: int
    buy_volume_usd: float
    sell_volume_usd: float


class SmartMoneyFlowMarketSharpMoney(_SmartMoneyFlowMarketSharpMoneyRequired, total=False):
    """Sharp-money flow aggregate for the market (canonical; smart_money is a deprecated byte-identical
    alias)."""
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value.
    large_trade_count: int


class _SmartMoneyFlowMarketSmartMoneyRequired(TypedDict):
    net_flow_usd: float
    direction: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the net-flow direction outcome; null
    # when unavailable (e.g. unsynced markets).
    token_id: str | None
    whale_trade_count: int
    buy_volume_usd: float
    sell_volume_usd: float


class SmartMoneyFlowMarketSmartMoney(_SmartMoneyFlowMarketSmartMoneyRequired, total=False):
    """Deprecated alias of sharp_money; byte-identical and retained for backward compatibility."""
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value.
    large_trade_count: int


class _ListPreGameSidesResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[PreGameSide]
    has_more: bool
    meta: ResponseMeta


class ListPreGameSidesResponse(_ListPreGameSidesResponseRequired, total=False):
    next_cursor: str
    total: int


class PreGameSide(TypedDict):
    """One ranked pre-game sports market where graded sharp money is piled on one side, with required-
    status shadow category evidence from partial forward-observed Polymarket fills."""
    # The side profitable wallets hold, as a provider-backed display label. Canonical spelling of piled_side
    # (#16310), same value: when provider group context is unavailable it may remain a bare Yes/No/Over/Under, so
    # do not ...
    side: str | None
    # UTC time at which the snapshot that ranked this row was computed. Canonical spelling of signal_created_at
    # (#16310), same value. Format: date-time.
    ranked_at: str
    # Grade-weighted holders times the share of their money on the side: (5*s + 4*a + 3*b) * sharp_pct. Canonical
    # spelling of conviction_score (#16310), same value.
    backing_score: float
    # Signed share of graded money on the side, (yes_usd - no_usd)/(yes_usd + no_usd) in [-1, 1] (side-yes
    # positive, side-no negative). Canonical spelling of smart_score (#16309, #16310), same value.
    side_share: float | None
    # Polymarket condition id.
    condition_id: str
    # UTC time at which the immutable signal snapshot was computed. Every row from one snapshot shares this value;
    # it is not provider market creation time and is not rewritten at request time. Deprecated (#16310):
    # `ranked_at` ...
    signal_created_at: str
    # Polymarket CLOB token id (ERC1155 asset id, decimal string) for the PILED outcome; null when unavailable.
    token_id: str | None
    # Canonical sport bucket (e.g. Basketball, Tennis); null when the raw category has no canonical mapping.
    category: str | None
    # Raw provider category as stored (e.g. NBA, EPL).
    raw_category: str | None
    title: str | None
    event_slug: str | None
    # Kickoff (UTC). In the future at SNAPSHOT time and within the requested horizon; because the response is
    # served from a shared snapshot cached up to the ~180s TTL, a served kickoff can be up to ~180s in the past
    # relative ...
    game_start_time: str | None
    # Nullable provider-backed piled-outcome display label. When provider group context is unavailable, it may
    # remain a bare Yes/No/Over/Under; do not use it alone as participant identity. Deprecated (#16310): `side` is
    # the ...
    piled_side: str | None
    # Provider binary-column selector: 0 selects outcome_yes/token_id_yes; 1 selects outcome_no/token_id_no. It
    # does not identify home/away or a participant. Use piled_side together with title/event context for display.
    piled_outcome_index: int
    # Piled-side dollar concentration backed_usd / (yes_usd + no_usd), in (0.5, 1] for a real pile; null when
    # there is no sharp USD.
    sharp_pct: float | None
    # Raw piled-side sharp-money USD.
    backed_sharp_usd: float
    # S-grade graded holders on the piled side.
    s_count: int
    # A-grade graded holders on the piled side.
    a_count: int
    # B-grade graded holders on the piled side.
    b_count: int
    # Piled-side graded holder count (s_count + a_count + b_count).
    graded_holders: int
    # Best grade present on the piled side; null when none.
    top_grade: Literal["S", "A", "B"] | str | None
    # Canonical sharp-money score (yes_usd - no_usd)/(yes_usd + no_usd) in [-1, 1] (piled-yes positive, piled-no
    # negative); a lower-order ranking tiebreak (after directional_rank_score and conviction_score). Deprecated
    # ...
    smart_score: float | None
    # Market volume (USD).
    volume: float | None
    # Aggregate recent flow direction on the market; null when unavailable.
    net_side: Literal["BUY", "SELL"] | str | None
    # Grade-weighted pile score (5*s + 4*a + 3*b) * sharp_pct; the raw conviction input to the ranking (see
    # directional_rank_score). Deprecated (#16310): `backing_score` is the canonical spelling and carries the same
    # value; ...
    conviction_score: float
    # Piled-side graded holders read one-way: their fresh open legs across the signal game's markets (cross-market
    # within the one game; moneyline+spread family only) all back the same team, or, when the market's holder scan
    # ...
    one_way_holder_count: int | None
    # Piled-side graded holders classified HEDGED across the game by fresh legs (they back two or more distinct
    # teams). A wallet long both outcomes of this market is not one-way and not counted here. Null when the
    # directional ...
    hedged_holder_count: int | None
    # Piled-side graded USD held by one-way wallets (share-weighted allocation of backed_sharp_usd). Null when the
    # directional read was not computed or classified nobody.
    one_way_graded_usd: float | None
    # One-way fraction of the piled graded dollars, in [0, 1] -- the metric orthogonal to sharp_pct. Stale,
    # unknown, hedged, and two-sided dollars dilute it toward zero (conservative). Null when the directional read
    # was not ...
    directional_confidence: float | None
    # The ranking key, descending: conviction_score * (1 + 0.25 * directional_confidence). Equals conviction_score
    # when the directional read is null/zero, so signals without the read rank exactly as before.
    directional_rank_score: float
    category_skill: PreGameSideCategorySkill
    # 1-based rank within the (min_grade-filtered) ranked result.
    rank: int


class PreGameSideCategorySkill(TypedDict):
    """Shadow-only category evidence over the full uncapped piled-side S/A/B holder allocation. It never
    changes signal membership, ordering, routing, or sizing."""
    status: Literal["live", "insufficient", "stale", "unknown", "degraded"] | str
    model_version: str
    taxonomy_version: str | None
    platform: Literal["polymarket"]
    scope: Literal["observed_goldsky_primary_taker_fill"]
    source_coverage: Literal["partial_whale_threshold_fills", "graded_wallet_fills"] | str
    # Format: date-time.
    observation_started_at: str
    # Format: date-time.
    as_of: str
    canonical_category: str | None
    eligible_holders: int
    covered_holders: int
    backed_sharp_usd: float | None
    covered_backed_usd: float | None
    coverage_pct: float | None
    weighted_edge_mean: float | None
    weighted_holder_lower_mean: float | None
    specialist_backed_usd: float | None
    specialist_backed_usd_pct: float | None
    largest_holder_backed_usd_pct: float | None
    minimum_holder_event_count: int | None


class _ListPreGameSideObservationsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[PreGameSideObservation]
    has_more: bool
    # Completion time of the shared observation snapshot pinned by the cursor. Format: date-time.
    snapshot_as_of: str
    # True when an operational failure or unknown provider-board, holder, directional, reconciliation, or internal
    # completeness state made this snapshot partial. This is snapshot-wide and can retain degradation that the ...
    degraded: bool
    funnel: PreGameSideFunnelReport
    meta: ResponseMeta


class ListPreGameSideObservationsResponse(_ListPreGameSideObservationsResponseRequired, total=False):
    next_cursor: str


class PreGameSideObservation(TypedDict):
    """One explicitly observation-only holder-pile measurement. It is evidence for cohort evaluation, not
    an execution instruction, and is isolated from the funded sports-edge-signals route."""
    # The side profitable wallets hold, as a provider-backed display label. Canonical spelling of piled_side
    # (#16310), same value: when provider group context is unavailable it may remain a bare Yes/No/Over/Under, so
    # do not ...
    side: str | None
    # Grade-weighted holder-pile score before directional enrichment. Canonical spelling of conviction_score
    # (#16310), same value.
    backing_score: float
    # Signed share of graded money on the side, in [-1, 1]. Canonical spelling of smart_score (#16309, #16310),
    # same value.
    side_share: float
    # Raw Polymarket condition id.
    condition_id: str
    # Provider-backed Polymarket CLOB token id for the piled outcome. Rows without a verified token terminate
    # before emission.
    token_id: str
    # Canonical sport bucket.
    category: Literal["Basketball", "Football", "Baseball", "Hockey", "MMA", "Boxing", "Soccer", "Cricket", "Golf", "Tennis", "Esports", "Racing", "Table Tennis", "Pickleball"] | str
    # Raw provider category as stored.
    raw_category: str | None
    # Provider-backed market title.
    title: str
    event_slug: str | None
    # Provider event id when available.
    event_id: str | None
    # Provider parent-event id used as the first event-cap identity when available.
    parent_event_id: str | None
    # Provider-backed kickoff time in UTC. Format: date-time.
    game_start_time: str
    # UTC instant when this row finished provider/holder evaluation. Format: date-time.
    observed_at: str
    # Source cohort or additive projection view. emerging_pile is projected from wider_holder after source
    # computation, overlaps its funnel denominator, and uses the source row's directional evidence.
    cohort: Literal["wider_holder", "in_play", "emerging_pile"] | str
    # Always true. This row must not be routed to an order executor.
    observation_only: Literal[True]
    # Nullable provider-backed piled-outcome display label. When provider group context is unavailable, it may
    # remain a bare Yes/No/Over/Under; do not use it alone as participant identity. Deprecated (#16310): `side` is
    # the ...
    piled_side: str | None
    # Provider binary-column selector: 0 selects outcome_yes/token_id_yes; 1 selects outcome_no/token_id_no. It
    # does not identify home/away or a participant. Use piled_side together with title/event context for display.
    piled_outcome_index: Literal[0, 1] | int
    # Provider-backed implied price for the piled outcome at observation time.
    backed_price: float
    # Piled-side graded-holder dollar concentration.
    sharp_pct: float
    # Raw graded-holder USD on the piled outcome.
    backed_sharp_usd: float
    s_count: int
    a_count: int
    b_count: int
    # Piled-side S/A/B holder count.
    graded_holders: int
    top_grade: Literal["S", "A", "B"] | str
    # Canonical signed holder-pile score. Deprecated (#16310): `side_share` is the canonical spelling and carries
    # the same value; this key stays on the wire.
    smart_score: float
    # Strictly positive stored market volume in USD. Missing, zero, or non-finite volume terminates as
    # invalid_market and is never emitted as an observation.
    volume: float
    # Grade-weighted holder-pile score before directional enrichment. Deprecated (#16310): `backing_score` is the
    # canonical spelling and carries the same value; this key stays on the wire.
    conviction_score: float
    # Whether the provider holder page came from the shared cache or a live provider read.
    provider_read_source: Literal["cached", "live"] | str
    # True only when neither provider outcome holder page hit the top-100 scan bound. False means the pile is a
    # positive lower bound and cannot satisfy a future capital-promotion gate.
    holder_scan_complete: bool
    # Proven provider holder observation time. A warm cache hit uses only the original provider completion time
    # from its companion metadata, never cache-read time. Null, malformed, future, or stale holder time fails in-
    # play ...
    holder_snapshot_at: str | None
    # Truthful state of the directional read, which classifies each graded holder by its fresh synced legs across
    # the game's markets and, when holder_scan_complete is true, by Polymarket's currentValue on both outcomes of
    # ...
    directional_status: Literal["available", "unknown_ungrouped", "unknown_stale", "unavailable"] | str
    one_way_holder_count: int | None
    hedged_holder_count: int | None
    one_way_graded_usd: float | None
    directional_confidence: float | None
    # Default cohort ordering key: conviction_score * (1 + 0.25 * directional_confidence), or conviction_score
    # when confidence is null.
    directional_rank_score: float
    # 1-based rank within this observation cohort and snapshot.
    rank: int


class PreGameSideFunnelReport(TypedDict):
    """Per-sport accountable funnel for the full observation snapshot, returned on every page."""
    sports: list[PreGameSideSportFunnelReport]


class PreGameSideSportFunnelReport(TypedDict):
    """Independent sports-board supply plus stored-universe terminal accounting for one canonical sport."""
    sport: Literal["Basketball", "Football", "Baseball", "Hockey", "MMA", "Boxing", "Soccer", "Cricket", "Golf", "Tennis", "Esports", "Racing", "Table Tennis", "Pickleball"] | str
    # Unique condition ids independently visible on the provider-first sports board.
    board_input: int
    # Whether the always-applicable live-board source completed as available. False can mean a completed source
    # failure (board_source_unavailable) or live-board work missing an internal configured-scope deadline or the
    # outer ...
    board_live_available: bool
    # Whether a provider-backed upcoming-board source is configured and applicable for this sport. False means not
    # applicable, not provider failure.
    board_upcoming_configured: bool
    # Whether every configured upcoming-board scope completed as available. False with
    # board_upcoming_configured=false means not applicable. When board_upcoming_configured is true and this flag
    # is false, read ...
    board_upcoming_available: bool
    # Why the upcoming-board source is (un)available. Board supply is one canonical-sport union: the bare category
    # owns live truth and every configured composed league scope contributes upcoming rows; folded leagues without
    # a ...
    board_upcoming_status: Literal["unknown", "not_configured", "available", "capacity_limited", "source_unavailable", "cold_unavailable", "deadline_unavailable"] | str
    # Configured upcoming scopes that did not complete as available. Values are category, a provider league tag
    # slug (nfl, cfb, nba, wnba, nhl, mls, valorant, league-of-legends, counter-strike-2, or dota-2), registry
    # when the ...
    board_upcoming_unavailable_scopes: list[Literal["category", "nfl", "cfb", "nba", "wnba", "nhl", "mls", "valorant", "league-of-legends", "counter-strike-2", "dota-2", "registry", "union", "wave"] | str]
    # Stored-universe rows plus provider-board rows missing from storage.
    input: int
    # Sparse counts over the closed 25-value terminal vocabulary: outside_horizon, resolved, provider_closed,
    # provider_excluded, invalid_market, missing_token, missing_stored_market, not_provider_live, ...
    terminals: dict[str, int]
    # Sum of every sparse terminal count.
    terminal_total: int
    # True exactly when input equals terminal_total.
    reconciled: bool


class GetCoverageResponse(TypedDict):
    object: Literal["platforms"]
    data: Platforms
    meta: ResponseMeta


class Platforms(TypedDict):
    platforms: PlatformsPlatforms


class PlatformsPlatforms(TypedDict):
    polymarket: PlatformCapabilities


class PlatformCapabilities(TypedDict):
    grade: PlatformCapabilityStatus
    pnl: PlatformCapabilityStatus
    strategy: PlatformCapabilityStatus
    timeline: PlatformCapabilityStatus
    # The large-trade feed. Canonical key since #16304; whale_signal is its deprecated spelling, emitted beside it
    # with the same value.
    large_trades: PlatformCapabilityStatus
    whale_signal: PlatformCapabilityStatus
    suspicious_trades: PlatformCapabilityStatus
    insider_radar: PlatformCapabilityStatus
    market_snapshot: PlatformCapabilityStatus


PlatformCapabilityStatus = Union[Literal["supported", "partial", "unsupported"], str]


class _GetMarketHoldersResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[MarketHolder]
    has_more: bool
    market: MarketHoldersMarket
    scan: MarketHoldersScan
    totals: MarketHoldersTotals
    meta: ResponseMeta


class GetMarketHoldersResponse(_GetMarketHoldersResponseRequired, total=False):
    # Absent on the last page.
    next_cursor: str
    # Holders matching the request's `outcome` and `min_grade` filters across every page.
    total: int


class _MarketHolderRequired(TypedDict):
    # Composite `pos_<wallet>:<condition_id>:<outcome_index>`, the same id `GET /api/v1/positions` gives this leg.
    id: str
    # `trd_`-prefixed trader id, accepted by `GET /api/v1/trader/{address}`.
    trader_id: str
    # Lowercased proxy wallet.
    address: str
    # Polymarket's public display name from the same holder snapshot; null for a private wallet, which the
    # provider redacts at the source.
    name: str | None
    # The outcome this wallet nets to. A wallet holding both outcomes is listed once, on its net side; see
    # `other_outcome_shares`.
    side: Literal["YES", "NO"] | str
    # Polymarket CLOB token id (ERC1155 asset id, decimal string) for `side`; null when the market has no stored
    # token id.
    token_id: str | None
    # All-time trader grade. This route lists the S/A/B cohort only, the same cohort a Pick of the Day roster
    # lists.
    grade: Literal["S", "A", "B"] | str | None
    # Shares held on `side`, from the complete provider scan.
    shares: float
    # Polymarket's own currentValue for this leg, in USD. Null when the snapshot predates the value map.
    current_value_usd: float | None
    # The wallet's last recorded trade anywhere, null when unknown. Format: date-time.
    last_traded_at: str | None
    # Why `category_win_rate` is present or absent: `measured` (rate present), `not_enough_data` (under the floor
    # of 5 decided markets in the category), or `unavailable` (the market has no canonical category, or the read
    # ...
    category_win_rate_status: Literal["measured", "not_enough_data", "unavailable"] | str


class MarketHolder(_MarketHolderRequired, total=False):
    # Shares on the other outcome when the wallet holds both. Absent when the wallet is one-sided.
    other_outcome_shares: float
    # This wallet's win rate in the market's canonical category (`market.category`): the share of its resolved
    # markets in that category whose realized P&L closed positive, as a 0..1 fraction. Present only with ...
    category_win_rate: float
    # The two counts `category_win_rate` is the ratio of, from the same row: `wins / decided` equals the rate.
    # Every resolved Polymarket market the wallet traded in the market's canonical category, at any position size,
    # ...
    category_win_record: MarketHolderCategoryWinRecord
    # For an esports market, the game `category_win_rate` and `category_win_record` were measured in: `LoL`,
    # `CS2`, `Dota 2`, `Valorant`, `Call of Duty`, `Honor of Kings`, `Mobile Legends: Bang Bang`, `Overwatch`,
    # `Rainbow ...
    category_win_rate_game: str
    category_evidence: HolderCategoryEvidence
    # Days since this wallet's first trade. The five badge fields are present together, only for a wallet that
    # draws at least one badge.
    wallet_age_days: float | None
    # True when the wallet's first trade was under 30 days ago.
    is_new_wallet: bool
    # Distinct markets the wallet has traded.
    markets_traded: int | None
    # True when the wallet is flagged as automated.
    is_bot: bool
    # The wallet's X handle without the @, when linked.
    x_username: str | None


class MarketHolderCategoryWinRecord(TypedDict):
    """The two counts `category_win_rate` is the ratio of, from the same row: `wins / decided` equals the
    rate. Every resolved Polymarket market the wallet traded in the market's canonical category, at any
    position size, rebuilt daily. Present only with `category_win_rate_status` = `measured`."""
    # Resolved markets in the category that this wallet closed with a profit.
    wins: int
    # Resolved markets in the category that this wallet closed with a profit or a loss. A market resolved at zero
    # realized P&L is in neither count.
    decided: int


class _MarketHoldersMarketRequired(TypedDict):
    # `mkt_`-prefixed market id.
    id: str
    condition_id: str
    title: str | None
    # The canonical category bucket `category_win_rate` is measured in.
    category: str | None
    outcome_yes: str | None
    outcome_no: str | None
    token_id_yes: str | None
    token_id_no: str | None
    # A settled market's roster is whatever the provider still lists as open; it empties as holders redeem.
    status: Literal["open", "closed", "resolved"] | str


class MarketHoldersMarket(_MarketHoldersMarketRequired, total=False):
    slug: str
    event_slug: str
    # Format: date-time.
    end_date: str


class MarketHoldersScan(TypedDict):
    # `cached`: the shared holder snapshot, at most 180 s old at compute time. `live`: the provider answered a
    # fresh complete walk for this compute.
    source: Literal["cached", "live"] | str
    # Always true on a served roster. An incomplete or unstable scan is a 503, never a partial list.
    complete: bool
    # When the provider walk that produced the holder population finished. Format: date-time.
    fetched_at: str | None
    # Every distinct wallet the complete walk saw with open shares, graded or not. The roster lists the graded
    # S/A/B subset.
    wallet_count: int


class MarketHoldersTotals(TypedDict):
    """Roster totals BEFORE any `outcome` or `min_grade` filter, so a page always knows the whole market it
    was cut from."""
    # Distinct graded wallets with net exposure; a two-sided wallet counts once.
    graded_count: int
    yes_count: int
    no_count: int
    yes_shares: float
    no_shares: float
    # Polymarket currentValue summed over the graded wallets netting YES.
    yes_usd: float
    # Polymarket currentValue summed over the graded wallets netting NO.
    no_usd: float
    yes_grades: MarketHoldersSideGrades
    no_grades: MarketHoldersSideGrades


class MarketHoldersSideGrades(TypedDict):
    s: int
    a: int
    b: int


class GetMarketFlowResponse(TypedDict):
    object: Literal["market_flow"]
    data: MarketFlow
    meta: ResponseMeta


class MarketFlow(TypedDict):
    market: MarketFlowMarket
    # Outcome-aware flow from all tracked whale trades in the window, without a grade filter. BUY YES and SELL NO
    # add net exposure; BUY NO and SELL YES subtract it. Gross buy/sell volumes count both outcomes. Top positions
    # ...
    sharp_money: MarketFlowSharpMoney
    # Deprecated alias of sharp_money; byte-identical and retained for backward compatibility.
    smart_money: MarketFlowSmartMoney
    timeframe: str


class MarketFlowMarket(TypedDict):
    id: str
    condition_id: str
    title: str
    slug: str | None
    category: str | None
    platform: str | None


class _MarketFlowSharpMoneyRequired(TypedDict):
    net_flow_usd: float
    direction: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the net-flow direction outcome; null
    # when unavailable (e.g. unsynced markets).
    token_id: str | None
    whale_trade_count: int
    buy_volume_usd: float
    sell_volume_usd: float
    top_positions: list[MarketFlowSharpMoneyTopPositionsItem]
    # Age of the oldest stored position snapshot behind top_positions: the minimum wallet sync clock over the
    # positions this body publishes. The roster is a stored read rather than a live one, and graded wallets sit on
    # ...
    oldest_snapshot_as_of: str | None


class MarketFlowSharpMoney(_MarketFlowSharpMoneyRequired, total=False):
    """Outcome-aware flow from all tracked whale trades in the window, without a grade filter. BUY YES and
    SELL NO add net exposure; BUY NO and SELL YES subtract it. Gross buy/sell volumes count both
    outcomes. Top positions are separately graded. Direction uses unrounded net: negative is NO,
    otherwise YES; the zero tie-break is not conviction. Canonical; smart_money is a deprecated byte-
    identical alias."""
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value.
    large_trade_count: int


class MarketFlowSharpMoneyTopPositionsItem(TypedDict):
    id: str
    address: str
    username: str | None
    grade: str | None
    side: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for this outcome; null when unavailable
    # (e.g. unsynced markets).
    token_id: str | None
    size_usd: float


class _MarketFlowSmartMoneyRequired(TypedDict):
    net_flow_usd: float
    direction: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the net-flow direction outcome; null
    # when unavailable (e.g. unsynced markets).
    token_id: str | None
    whale_trade_count: int
    buy_volume_usd: float
    sell_volume_usd: float
    top_positions: list[MarketFlowSharpMoneyTopPositionsItem]
    # Age of the oldest stored position snapshot behind top_positions: the minimum wallet sync clock over the
    # positions this body publishes. The roster is a stored read rather than a live one, and graded wallets sit on
    # ...
    oldest_snapshot_as_of: str | None


class MarketFlowSmartMoney(_MarketFlowSmartMoneyRequired, total=False):
    """Deprecated alias of sharp_money; byte-identical and retained for backward compatibility."""
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value.
    large_trade_count: int


class GetMarketIntelResponse(TypedDict):
    object: Literal["market_intel"]
    data: MarketFlow
    meta: ResponseMeta


class _BatchGetMarketFlowBodyRequired(TypedDict):
    # Market condition IDs to resolve in input order.
    condition_ids: list[str]


class BatchGetMarketFlowBody(_BatchGetMarketFlowBodyRequired, total=False):
    # Lookback window used for flow and trade-count context.
    timeframe: Literal["1h", "4h", "24h", "7d"]


class BatchGetMarketFlowResponse(TypedDict):
    object: Literal["market_flow_batch"]
    data: list[BatchMarketFlowItem]
    meta: BatchResponseMeta


class _BatchMarketFlowItemRequired(TypedDict):
    # Zero-based request index. Duplicate inputs keep separate result rows.
    index: int
    input: str
    status: Literal["ok", "error"] | str


class BatchMarketFlowItem(_BatchMarketFlowItemRequired, total=False):
    data: MarketFlow
    error: ApiErrorBody


class BatchGetMarketIntelResponse(TypedDict):
    object: Literal["market_intel_batch"]
    data: list[BatchMarketFlowItem]
    meta: BatchResponseMeta


class GetMarketSnapshotResponse(TypedDict):
    object: Literal["market_snapshot"]
    data: MarketSnapshot
    meta: ResponseMeta


class _MarketSnapshotRequired(TypedDict):
    market: MarketSnapshotMarket
    outcomes: list[MarketSnapshotOutcomesItem]
    liquidity: MarketSnapshotLiquidity
    sports: MarketSnapshotSports
    freshness: MarketSnapshotFreshness


class MarketSnapshot(_MarketSnapshotRequired, total=False):
    # Price and spread trust metadata. Present only when expand=trust or expand[]=trust is requested.
    trust: MarketSnapshotTrust


class MarketSnapshotMarket(TypedDict):
    id: str
    condition_id: str
    provider: str
    title: str | None
    slug: str | None
    page_slug: str | None
    event_slug: str | None
    category: str | None
    status: Literal["active", "closed"] | str
    description: str | None
    image: str | None
    # Polymarket series slug from the canonical identity row, null when unavailable. A sports series identifies a
    # league and must not be used as a per-matchup grouping key.
    series_slug: str | None
    market_type: str | None
    market_result: str | None
    # Format: date-time.
    created_at: str | None
    # Format: date-time.
    end_date: str | None
    # Format: date-time.
    resolved_at: str | None


class _MarketSnapshotOutcomesItemRequired(TypedDict):
    side: Literal["yes", "no"] | str
    label: str
    top_of_book: MarketSnapshotTopOfBook


class MarketSnapshotOutcomesItem(_MarketSnapshotOutcomesItemRequired, total=False):
    token_id: str
    current_price: float


class _MarketSnapshotTopOfBookRequired(TypedDict):
    status: Literal["available", "unavailable"] | str
    source: str


class MarketSnapshotTopOfBook(_MarketSnapshotTopOfBookRequired, total=False):
    best_bid: float
    best_ask: float
    spread_bps: int
    bid_depth_usdc: float
    ask_depth_usdc: float
    reason: str


class MarketSnapshotLiquidity(TypedDict):
    source: str
    volume_usd: float | None
    liquidity_usd: float | None
    volume_24h_usd: float | None
    # Always null. Polymarket snapshot prices come from outcome top-of-book midpoints.
    last_price: float | None


class _MarketSnapshotSportsRequired(TypedDict):
    status: Literal["fresh", "stale", "not_live", "unavailable"] | str
    source: str


class MarketSnapshotSports(_MarketSnapshotSportsRequired, total=False):
    live_match_key: str
    live_league_key: str
    # Live-score period and elapsed may be omitted when unavailable (older responses use null). A score entry may
    # omit full_name when it equals team; fall back to team. Distinct aliases and score admission markers are ...
    live_score: dict[str, Any]
    reason: str


class MarketSnapshotFreshness(TypedDict):
    market_data: MarketSnapshotFreshness
    top_of_book: MarketSnapshotFreshness
    # Freshness requires the dedicated two-second post-publication marker to match the retained vintage and non-
    # invalidated data timestamp; timestamp presence alone is insufficient. as_of records compute start, so ...
    live_sports: MarketSnapshotFreshness


class MarketSnapshotTrust(TypedDict):
    """Price and spread trust metadata returned only when GET /api/v1/market/{condition_id}/snapshot
    includes expand=trust."""
    current_price: TrustMetadata
    spread_bps: TrustMetadata


class GetMarketCandlesResponse(TypedDict):
    object: Literal["market_candles"]
    data: MarketCandles
    meta: ResponseMeta


class MarketCandles(TypedDict):
    """Provider-first bucketed OHLC price candles for a market's outcome tokens, derived from the stored
    token_price_snapshots series (covers open and resolved markets)."""
    # Market condition id the candles were read for.
    condition_id: str
    # Bucketing granularity that produced these candles.
    resolution: Literal["1d", "1w"] | str
    # One entry per present provider token (YES first, then NO); empty when no tokens have been fetched yet.
    outcomes: list[OutcomeCandles]


class OutcomeCandles(TypedDict):
    """One outcome token's bucketed candle series."""
    # Provider CLOB token id the candles were read for.
    token_id: str
    # Canonical side label.
    outcome: Literal["YES", "NO"] | str
    # OHLC candles for this outcome token, ascending by bucket start.
    candles: list[Candle]


class Candle(TypedDict):
    """One bucketed OHLC price candle. Prices are in provider [0, 1] units, truncated to 4 decimals at the
    rendering edge."""
    # Bucket-start unix epoch (seconds): UTC midnight for 1d, the ISO-week Monday's UTC midnight for 1w. Format:
    # int64.
    t: int
    # Open price in provider [0, 1] units (first observed point in the bucket).
    o: float
    # High price in provider [0, 1] units (max observed in the bucket).
    h: float
    # Low price in provider [0, 1] units (min observed in the bucket).
    l: float
    # Close price in provider [0, 1] units (last observed point in the bucket).
    c: float


class _ListSuspiciousTradesResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[SuspiciousTrade]
    has_more: bool
    meta: ResponseMeta


class ListSuspiciousTradesResponse(_ListSuspiciousTradesResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; the key is absent when it does not.
    total: int


class SuspiciousTrade(TypedDict):
    # Prefixed ID (rf_...).
    id: str
    # Stored score that met the live flag threshold.
    suspicion_score: float
    # The live scorer persists one threshold class.
    severity: Literal["flag"]
    trader: SuspiciousTradeTrader
    market: SuspiciousTradeMarket
    scores: SuspiciousTradeScores
    # Stored whale_alerts.suspicion_signals JSON from the scorer.
    evidence: Any
    # Stored trade timestamp. Format: date-time.
    created_at: str


class SuspiciousTradeTrader(TypedDict):
    id: str
    address: str
    username: str | None


class SuspiciousTradeMarket(TypedDict):
    id: str
    condition_id: str
    # Canonical market question when available.
    title: str | None


class SuspiciousTradeScores(TypedDict):
    # Null because the live scorer does not record this component.
    timing: float | None
    # Null because the live scorer does not record this component.
    edge: float | None
    # Numeric evidence.size when recorded; otherwise null.
    size: float | None
    # Numeric evidence.fresh when recorded; otherwise null.
    fresh_wallet: float | None


class GetSuspiciousTradeResponse(TypedDict):
    object: Literal["suspicious_trade"]
    data: SuspiciousTrade
    meta: ResponseMeta


class _ListGamesResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[Game]
    has_more: bool
    # When this read assembled the catalog. Per-source vintage is on each game's freshness. Format: date-time.
    as_of: str
    coverage: GamesCoverage
    meta: ResponseMeta


class ListGamesResponse(_ListGamesResponseRequired, total=False):
    # Pass as cursor for the next page. Present only when has_more is true.
    next_cursor: str


class _GameRequired(TypedDict):
    object: Literal["game"]
    # The game's identity, for example mlb-mil-cin-2026-06-22. The same key the live_sports_updated webhook pulse
    # carries and the same key /api/v1/games/{event_slug} takes.
    event_slug: str
    status: GameStatus
    # Both sides, in the provider's own order. For a team league the provider lists the home side first. Empty
    # when the provider identified neither side.
    competitors: list[GameCompetitor]
    # Whether one of this game's markets pays on a draw. Read this instead of assuming a two-outcome moneyline.
    draw_offered: bool
    # Every market this read linked to the game, ordered by condition_id.
    markets: list[GameMarket]
    freshness: GameFreshness
    coverage: GameCoverage
    # The game's page on 0xinsider.
    url: str


class Game(_GameRequired, total=False):
    """One sports or esports game: both sides, its schedule, provider status, linked Polymarket markets and
    their available provider moneyline price states. Assembled from the same provider-first live and
    upcoming projections the site's boards use, with no request-time provider fan-out."""
    # The provider's Gamma gameId, as a string. Omitted when the canonical owner has no single value for this
    # slug: the provider stamps one gameId across an event's derivative siblings, so an ambiguous read is reported
    # as ...
    game_id: str
    # The canonical sport bucket, for example Soccer or Table Tennis. Omitted when neither the board scope nor the
    # provider category names one.
    sport: str
    # The league tag, for example nfl or epl. Omitted for a sport served as one whole bucket with no league scope.
    league: str
    # The provider's event title. Omitted when the provider sent none.
    title: str
    # Kickoff in UTC, as the provider supplied it. Omitted when the provider published none; coverage.schedule
    # then reads unavailable. Format: date-time.
    scheduled_at: str
    # The esports series length, for example Bo3. Omitted for everything else.
    series_format: str


class _GameStatusRequired(TypedDict):
    # scheduled: kickoff is ahead or the provider still calls it scheduled. live: the provider reports it in play.
    # paused: halftime or a provider-reported break. ended: the provider reported a final, an award or a forfeit.
    # ...
    state: Literal["scheduled", "live", "paused", "ended", "postponed", "cancelled", "suspended", "delayed", "unknown"] | str
    # Whether the game is over. Always present.
    ended: bool


class GameStatus(_GameStatusRequired, total=False):
    """Where the game is in its own life, as the provider reports it. A postponement, a cancellation and a
    suspension each keep their own state, so a client can tell a game that will be played later from one
    that never will be."""
    # The provider status folded onto one vocabulary across leagues. unknown means the provider sent a value this
    # API has no meaning for; provider_status keeps that value verbatim. Omitted when no live-score frame carries
    # a ...
    match_status: Literal["scheduled", "in_progress", "halftime", "penalty_shootout", "delayed", "suspended", "final", "final_overtime", "final_shootout", "awarded", "forfeit", "not_necessary", "postponed", "cancelled", "unknown"] | str
    # The provider's status string, verbatim. Omitted when the provider sent none.
    provider_status: str
    # The provider's period label, for example Q3, End Q2 or T5. Omitted when the provider sent none.
    period: str
    # The game clock as the provider spells it, never reformatted. Omitted when the provider sent none.
    clock: str
    # The provider's own in-play flag. Omitted when no live-score frame exists, which is not the same as false.
    live: bool


class _GameCompetitorRequired(TypedDict):
    # The competitor's name as the provider gives it.
    name: str


class GameCompetitor(_GameCompetitorRequired, total=False):
    """One side of the game."""
    # The provider's league-scoped competitor id, as a string. Omitted when the provider has not identified this
    # side; coverage.competitors then reads labels.
    provider_id: str
    # Provider crest or logo URL. Omitted when there is none.
    logo: str
    # The provider's score for this side, verbatim. A string because the provider sends one: a set score, a map
    # score and a run total are not all integers. Omitted when no live-score frame carries a score.
    score: str
    # The provider's season record for this side, for example 12-4. Omitted when the provider sent none.
    record: str


class _GameMarketRequired(TypedDict):
    # The mkt_-prefixed market id every other V1 response uses.
    id: str
    # The raw provider condition id.
    condition_id: str
    # Always polymarket.
    platform: str


class GameMarket(_GameMarketRequired, total=False):
    """One Polymarket market linked to this game."""
    # The provider's market slug. Omitted when the provider sent none.
    slug: str
    # The provider's own market type, for example moneyline or spread. Omitted when the provider sent none. Not an
    # enum: the provider owns this vocabulary and adds to it.
    sports_market_type: str
    # Which side of the game this market's YES leg pays. draw is a real value: a 1X2 market's third leg is not a
    # competitor. Omitted when the provider ids do not classify the leg, which is not the same as other.
    side: Literal["home", "away", "draw", "other"] | str
    # The provider's label for the YES outcome. Omitted when the provider sent none.
    outcome_yes: str
    # The provider's label for the NO outcome. Omitted when the provider sent none.
    outcome_no: str
    # Polymarket CLOB token ids in the provider's own outcome-index order. Omitted when the provider has published
    # none for this market.
    outcome_token_ids: list[str]
    # Default provider moneyline state. Omitted when this market has no classified moneyline projection;
    # incomplete and invalid projections remain explicit.
    prices: GameMarketPrices


class GameMarketPrices(TypedDict):
    """Provider-owned moneyline state with the observation clock that can be compared with game freshness."""
    provider: GameMarketProviderPrices
    # Board cache vintage for Gamma or the older CLOB leg clock. Null when no reliable clock is available; never a
    # Gamma-authored timestamp. Format: date-time.
    observed_at: str | None
    # The clock used for observed_at. board_snapshot is this service’s cache observation, not a provider source
    # timestamp.
    observation_source: Literal["board_snapshot", "clob_display"] | str


class GameMarketPricePaired(TypedDict):
    """A validated provider moneyline pair bound to the two competitors."""
    state: Literal["paired"]
    competitor_a: GameMarketPriceCompetitor
    competitor_b: GameMarketPriceCompetitor
    # Whether competitor A is the provider YES leg.
    competitor_a_is_yes: bool
    binding_provenance: GameMarketPriceBindingProvenance


class _GameMarketPriceCompetitorRequired(TypedDict):
    # The provider competitor label.
    label: str
    # Unrounded provider price in [0, 1].
    price: float
    # Which provider price observation supplies this leg.
    price_provenance: Literal["gamma_outcome_prices", "clob_display"] | str


class GameMarketPriceCompetitor(_GameMarketPriceCompetitorRequired, total=False):
    """One competitor-bound provider moneyline price. No YES/NO inference is required."""
    # The provider competitor id when identity is available. Format: int64.
    provider_id: int


# How the existing sports-board writer bound prices to competitors.
GameMarketPriceBindingProvenance = Union[Literal["provider_ids", "exact_labels", "containment_labels", "elimination"], str]


class _GameMarketPriceIncompleteRequired(TypedDict):
    state: Literal["incomplete"]
    reason: Literal["outcome_prices_missing", "outcome_price_leg_missing", "zero_price_sentinel", "display_price_pair_unavailable", "outcome_identity_unavailable", "final_score_unavailable"] | str


class GameMarketPriceIncomplete(_GameMarketPriceIncompleteRequired, total=False):
    """The provider moneyline pair is incomplete; no numeric pair is invented."""
    # Whether competitor A is the provider YES leg.
    competitor_a_is_yes: bool
    # The provider competitor id when identity is available. Format: int64.
    competitor_a_provider_id: int
    # The provider competitor id when identity is available. Format: int64.
    competitor_b_provider_id: int
    binding_provenance: GameMarketPriceBindingProvenance


class _GameMarketPriceInvalidRequired(TypedDict):
    state: Literal["invalid"]
    reason: Literal["team_cardinality", "outcome_cardinality", "price_cardinality", "non_finite_price", "out_of_range_price", "non_complementary_prices", "ambiguous_identity", "final_identity_mismatch"] | str


class GameMarketPriceInvalid(_GameMarketPriceInvalidRequired, total=False):
    """The provider moneyline pair is invalid; no numeric pair is invented."""
    # Whether competitor A is the provider YES leg.
    competitor_a_is_yes: bool
    # The provider competitor id when identity is available. Format: int64.
    competitor_a_provider_id: int
    # The provider competitor id when identity is available. Format: int64.
    competitor_b_provider_id: int
    binding_provenance: GameMarketPriceBindingProvenance


GameMarketProviderPrices = Union[GameMarketPricePaired, GameMarketPriceIncomplete, GameMarketPriceInvalid]


class _GameFreshnessRequired(TypedDict):
    # Which board half produced this game.
    source: Literal["live", "upcoming"] | str
    # Whether that half returned a truthful source body for this read.
    source_status: Literal["ok", "unavailable"] | str
    # Whether that half had a source body at all. not_applicable means the sport has no configured source for that
    # half.
    source_availability: Literal["available", "unavailable", "not_applicable"] | str
    # Freshness of the cached source body, never inferred from the response clock or the row count.
    source_freshness: Literal["fresh", "stale", "unknown", "not_applicable"] | str
    # Whether a reader should be told these rows are behind. This applies the half's own servable-age bar (15 s
    # live, 120 s upcoming), which is not the same as source_freshness: a live board whose scores are seconds old
    # reads ...
    delayed: bool


class GameFreshness(_GameFreshnessRequired, total=False):
    """How current this game's facts are. Independent per source: the board half that produced the game,
    and the live-score frame that produced its scores."""
    # The source body's data vintage. Omitted when the read has no vintage anchor, which is not age zero. Format:
    # date-time.
    source_observed_at: str
    # Age of source_observed_at in seconds, capped at 600. Omitted past the cap or with no anchor.
    source_age_seconds: int
    # When this game's live-score frame was observed. Omitted when there is no frame. Format: date-time.
    scores_observed_at: str
    # The provider's own frame clock. Omitted when the frame carries none. Format: date-time.
    scores_source_at: str


class GameCoverage(TypedDict):
    """What this game's read actually supplied, so a client branches on coverage instead of on a missing
    key."""
    # available when a live-score frame supplied this game's scores.
    scores: Literal["available", "unavailable"] | str
    # provider_ids when every side carries a provider id, labels when only the provider's names identify them,
    # unavailable when neither exists. Do not join on names when this reads labels.
    competitors: Literal["provider_ids", "labels", "unavailable"] | str
    # available when the provider supplied a kickoff.
    schedule: Literal["available", "unavailable"] | str


class GamesCoverage(TypedDict):
    """What this deployment covers, published with every page so a client never has to guess whether an
    empty list means no games or no coverage."""
    # Canonical sport buckets served, sorted.
    sports: list[str]
    # League tags served, sorted.
    leagues: list[str]
    # Scopes whose source half was unavailable for this read, as <sport>:<half>. Empty means every scope answered.
    sources_unavailable: list[str]


class GetGameResponse(TypedDict):
    object: Literal["game"]
    data: Game
    # When this read assembled the catalog. Per-source vintage is on freshness. Format: date-time.
    as_of: str
    meta: ResponseMeta


class GetInsiderRadarFlagResponse(TypedDict):
    object: Literal["radar_flag"]
    data: SuspiciousTrade
    meta: ResponseMeta


class GetEventReplaySinceResponse(TypedDict):
    object: Literal["event_replay"]
    data: list[EventReplayEvent]
    has_more: bool
    next_cursor: str
    meta: EventReplayMeta


class _EventReplayEventRequired(TypedDict):
    # Opaque event identity: the ef_-encoded whale_alerts.id, stable across cursor formats. Deduplicate on this,
    # never on cursor or sequence.
    id: str
    type: Literal["whale_trades_inserted"]
    # Cursor positioned at this event: its (inserted_xid, id) commit-order position. Store the page's next_cursor
    # to continue; this one resumes from exactly this event.
    cursor: str
    # whale_alerts.id of the event. Not monotonic across a replay: events arrive in commit order, so a lower id
    # can follow a higher one when its write finished later. Order and resume by cursor, deduplicate by id.
    sequence: int
    # Format: date-time.
    published_at: str
    # What the event announces. Every field is present on every event; a field added later is additive, so a
    # client tolerates keys it does not know.
    payload: EventReplayEventPayload
    source: EventReplaySource
    freshness: EventReplayFreshness


class EventReplayEvent(_EventReplayEventRequired, total=False):
    # Present only with expand=trade: the base trade fields for this row, read at request time from one query per
    # page. GET /api/v1/large-trades/{id} adds counterparty_analysis; replay does not include it. traded_at, side,
    # ...
    trade: LargeTrade | None


class EventReplayEventPayload(TypedDict):
    """What the event announces. Every field is present on every event; a field added later is additive, so
    a client tolerates keys it does not know.

    The API sends keys beyond the ones listed here; read them from the value as a plain mapping
    (``cast(dict[str, Any], value)``)."""
    # Whale trades this event announces. One event is minted per stored whale trade, so this is 1.
    count: int
    # The raw whale_alerts.id of the trade, the same number as sequence. GET /api/v1/whale-trades/{id} accepts it
    # and returns the trade with its wallet, grade, size, price and market.
    whale_alert_id: int
    # The Polymarket condition id of the market the trade was in.
    condition_id: str
    # 0xinsider's numeric id for the wallet's trader row. It is not the trd_ id, which is derived from the
    # address; read the address and grade from the whale trade.
    trader_id: int
    # Provider discriminator. Polymarket only.
    platform: Literal["polymarket"]


class EventReplaySource(TypedDict):
    kind: Literal["local_durable_replay"]
    producer_family: Literal["whale_trades"]
    owner: Literal["whale_alerts"]
    provider_fetch_at_request_time: Literal[False]


class EventReplayFreshness(TypedDict):
    status: Literal["observed"]
    # Format: date-time.
    observed_at: str


class _EventReplayMetaRequired(TypedDict):
    # Unique request ID (req_ prefix). The same value as the X-Request-Id response header, the request's usage
    # accounting row and its log lines.
    request_id: str
    cached: bool
    # Advisory request weight (relative compute cost). 1 for simple reads; higher for heavier endpoints. Not a
    # credit/price.
    cost: int
    replay: EventReplayMetaReplay
    retention: EventReplayMetaRetention
    completeness: EventReplayMetaCompleteness


class EventReplayMeta(_EventReplayMetaRequired, total=False):
    cache_age_s: int


class _EventReplayMetaReplayRequired(TypedDict):
    # The request cursor in canonical form (an id-only cursor is re-encoded), or the zero position when omitted.
    from_cursor: str
    # Identical to next_cursor. After a full page, the cursor of the last event; after a page that is not full,
    # the commit horizon itself, since every row below it, matching or not, has been examined. An empty page
    # therefore ...
    to_cursor: str
    # whale_alerts.id component of the request cursor (0 when omitted).
    from_sequence: int
    # whale_alerts.id of the last event on this page, or from_sequence when the page is empty. Can sit below the
    # position next_cursor encodes after a page that is not full.
    to_sequence: int
    # Events are ordered by the position at which their write became visible (whale_alerts.inserted_xid), then by
    # whale_alerts.id, and a page is bounded by the oldest write transaction still open when it was read. Before
    # ...
    ordering: Literal["commit_visibility_then_id_asc"]
    # True when committed whale-trade rows newer than this page's commit-visibility horizon exist. They are held
    # until every older write transaction has finished and are served on a later request, so a caught_up page with
    # ...
    pending_beyond_horizon: bool
    # The expansions applied to every event on this page; empty when none.
    expand: list[Literal["trade"]]


class EventReplayMetaReplay(_EventReplayMetaReplayRequired, total=False):
    # The effective filter set this page ran with and next_cursor is bound to. Absent on an unfiltered walk.
    filters: EventReplayMetaReplayFilters


class EventReplayMetaReplayFilters(TypedDict, total=False):
    """The effective filter set this page ran with and next_cursor is bound to. Absent on an unfiltered
    walk."""
    # The trader parameter as given.
    trader: str
    # The raw provider condition id after mkt_ is stripped.
    condition_id: str
    min_grade: Literal["S", "A", "B", "C", "D", "F"] | str
    min_size: float


class EventReplayMetaRetention(TypedDict):
    status: Literal["durable_database"]
    retained_events: int
    cursor_expired: Literal[False]


class EventReplayMetaCompleteness(TypedDict):
    # complete: the page carries every durable event matching the filters after the cursor below the commit
    # horizon, up to limit. caught_up: nothing matching after the cursor is visible below the horizon; read ...
    status: Literal["complete", "caught_up"] | str
    reason: str


class _ListWebhooksResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[WebhookEndpoint]
    has_more: bool
    meta: ResponseMeta


class ListWebhooksResponse(_ListWebhooksResponseRequired, total=False):
    next_cursor: str
    total: int


class _WebhookEndpointRequired(TypedDict):
    # Format: int64.
    id: int
    object: Literal["webhook"]
    name: str
    # Format: uri.
    url: str
    event_types: list[WebhookEventType]
    trade_filters: LargeTradeSubscriptionFilters
    status: WebhookStatus
    # Format: date-time.
    verified_at: str | None
    # Format: date-time.
    verification_token_expires_at: str
    failure_count: int
    # Format: date-time.
    created_at: str
    # Format: date-time.
    updated_at: str
    retry_policy: WebhookRetryPolicy
    secret_rotation: WebhookSecretRotation


class WebhookEndpoint(_WebhookEndpointRequired, total=False):
    # Returned only on create, immediate rotate-secret, staged rotate-secret/prepare, or staged rotate-
    # secret/activate. Never returned by list, get, update, delete, verify, or retire.
    signing_secret: str
    verification: WebhookVerification


WebhookEventType = Union[Literal["large_trade_inserted_v2", "large_trades_inserted", "whale_trades_inserted", "live_sports_updated", "trader_synced", "whale_trader_synced", "large_positions_updated", "wallet_grade_changed", "suspicious_trade_flagged", "insider_radar_flag_raised", "sharp_money_flow_detected", "smart_money_flow_detected", "export_job_ready", "export_job_failed", "export_job_expired", "export_job_cancelled"], str]


class LargeTradeSubscriptionFilters(TypedDict, total=False):
    """All present fields narrow large_trade_inserted_v2 delivery. Grade is observed at publication;
    ungraded trades do not match min_grade. An empty object matches every large trade."""
    # Raw provider condition ID or mkt_-prefixed market ID.
    condition_id: str
    # Polymarket wallet address; matching is case-insensitive.
    wallet: str
    # S is best; ungraded trades do not match.
    min_grade: Literal["S", "A", "B", "C", "D", "F"] | str
    # Positive USD notional as an exact decimal string.
    min_size_usd: str


WebhookStatus = Union[Literal["pending_verification", "active", "disabled"], str]


class WebhookRetryPolicy(TypedDict):
    max_attempts: Literal[8]
    terminal_status: Literal["dead_letter"]
    # Total wait from a delivery's first failed attempt to its last retry: 60, 120, 240, 480, 960, 1920 and 3600
    # seconds. A delivery still failing after that is dead_letter.
    retry_horizon_seconds: Literal[7380]
    # Consecutive failed attempts, across all of this endpoint's deliveries, after which the endpoint is disabled
    # and its queued deliveries are dead-lettered. Any successful attempt resets the count.
    disable_after_consecutive_failures: Literal[8]


class WebhookSecretRotation(TypedDict):
    # idle when no staged rotation exists, pending after prepare, and overlap after activate while both signing
    # secrets are accepted.
    status: Literal["idle", "pending", "overlap"] | str
    # When the previous signing secret stops being emitted and accepted. null outside the overlap phase. Format:
    # date-time.
    overlap_expires_at: str | None


class WebhookVerification(TypedDict):
    # One-time verification token returned only on create or URL change. Pass it to POST
    # /api/v1/webhooks/{id}/verify, which activates the endpoint only when the destination also answers the signed
    # webhook.verification ...
    token: str
    # Format: date-time.
    expires_at: str


class _CreateWebhookRequestRequired(TypedDict):
    name: str
    # Public HTTPS callback URL on the default port 443. Local, private, and internal targets are rejected, as is
    # any explicit port other than 443 and any URL carrying credentials. Each user's URLs are unique after ...
    url: str
    event_types: list[WebhookEventType]


class CreateWebhookRequest(_CreateWebhookRequestRequired, total=False):
    trade_filters: LargeTradeSubscriptionFilters


class CreateWebhookResponse(TypedDict):
    object: Literal["webhook"]
    data: WebhookEndpoint
    meta: ResponseMeta


class _ListWebhookEventsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[WebhookEventDescriptor]
    has_more: bool
    meta: ResponseMeta


class ListWebhookEventsResponse(_ListWebhookEventsResponseRequired, total=False):
    next_cursor: str
    total: int


class WebhookEventDescriptor(TypedDict):
    """Self-describing entry in the webhook event catalog: the event type a subscriber lists in
    event_types, when it fires, the data payload shape, and whether it currently fires (active) or is
    reserved (dormant, subscribable but not yet delivered). Pro-only event types (large_trades_inserted,
    whale_trades_inserted, wallet_grade_changed, suspicious_trade_flagged, insider_radar_flag_raised,
    sharp_money_flow_detected, smart_money_flow_detected) only deliver to API keys on an active Pro
    subscription. Export lifecycle event types (export_job_ready, export_job_failed, export_job_expired,
    ..."""
    id: WebhookEventType
    # One-line description of when the event fires.
    description: str
    # Short description of the data payload object's shape.
    payload_shape: str
    # active: the event has a firing producer callsite. dormant: advertised and subscribable, but does not yet
    # enqueue any delivery.
    status: Literal["active", "dormant"] | str


class _ListWebhookDeliveriesResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[WebhookDelivery]
    has_more: bool
    meta: ResponseMeta


class ListWebhookDeliveriesResponse(_ListWebhookDeliveriesResponseRequired, total=False):
    next_cursor: str
    total: int


class _WebhookDeliveryRequired(TypedDict):
    # Format: int64.
    id: int
    object: Literal["webhook_delivery"]
    # Stable event id for this delivery; identical across retries of the same logical event.
    event_id: str
    event_type: WebhookEventType
    # Delivery lifecycle state (e.g. pending, delivered, dead_letter).
    status: str
    # Number of delivery attempts made so far.
    attempt_count: int
    # When the next delivery attempt is due, for a delivery whose status is pending or retry. null while an
    # attempt is in flight (processing) and once the delivery is terminal (delivered or dead_letter). Format:
    # date-time.
    next_attempt_at: str | None
    # Why next_attempt_at was scheduled: receiver_retry_after for an accepted Retry-After on a 408, 429, or 5xx
    # response; transient_failure for a network or ordinary transient retry; permanent_or_auth_failure for another
    # ...
    retry_schedule_reason: Literal["receiver_retry_after", "transient_failure", "permanent_or_auth_failure", "manual_redelivery", "configuration_changed"] | str | None
    # Format: date-time.
    created_at: str


class WebhookDelivery(_WebhookDeliveryRequired, total=False):
    """Owner-scoped view of one webhook delivery attempt. Deliberately omits the request body and the
    endpoint signing secret: a delivery log never re-exposes the payload or any secret material."""
    # HTTP status code of the most recent delivery attempt. Omitted until a response (or transport error) has been
    # recorded.
    last_response_status: int
    # Short description of the most recent delivery failure. Omitted when the last attempt succeeded or none has
    # failed.
    last_error: str
    # When the delivery was first accepted by the destination. Omitted until a delivery succeeds. Format: date-
    # time.
    delivered_at: str


class RedeliverWebhookDeliveryResponse(TypedDict):
    object: Literal["webhook_delivery"]
    data: WebhookDelivery
    meta: ResponseMeta


class UpdateWebhookRequest(TypedDict, total=False):
    name: str
    # Replacement public HTTPS callback URL on the default port 443, validated and checked for uniqueness exactly
    # like the create url. HTTPS scheme/host case, trailing DNS dots and port 443 normalize; path/query case is
    # ...
    url: str
    event_types: list[WebhookEventType]
    trade_filters: LargeTradeSubscriptionFilters
    enabled: bool


class VerifyWebhookRequest(TypedDict):
    # The one-time token returned on create or on a url change. It is necessary but not sufficient: the
    # destination must also answer the signed webhook.verification challenge with a 2xx.
    verification_token: str


class GetHealthResponse(TypedDict):
    object: Literal["health"]
    data: GetHealthResponseData
    meta: ResponseMeta


class GetHealthResponseData(TypedDict, total=False):
    status: Literal["ok", "degraded", "down", "maintenance"] | str
    db: bool
    cache: bool
    subsystems: GetHealthResponseDataSubsystems


class GetHealthResponseDataSubsystems(TypedDict):
    # Whether the webhook outbox schema validated on this probe. false lowers status to degraded. true during a
    # maintenance window, when nothing is probed.
    webhook_compatibility: bool
    # Public-safe aggregate status for expected background job successful-completion heartbeats. Does not expose
    # Redis keys, job names, raw errors, provider payloads, wallet addresses, or condition IDs.
    background_jobs: GetHealthResponseDataSubsystemsBackgroundJobs


class GetHealthResponseDataSubsystemsBackgroundJobs(TypedDict):
    """Public-safe aggregate status for expected background job successful-completion heartbeats. Does not
    expose Redis keys, job names, raw errors, provider payloads, wallet addresses, or condition IDs."""
    status: Literal["ok", "degraded", "down", "not_checked"] | str
    checked: bool
    total: int
    healthy: int
    stale: int
    missing: int
    invalid: int
    unconfigured: int
    # Heavy-periodic jobs that are stale/missing/invalid while the heavy executor is disabled
    # (heavy_pipeline_control.executor_mode != 'active'), so this binary does not dispatch them. Observable but
    # expected; they never ...
    paused: int


class _CreateMcpJsonRpcResponseBodyRequired(TypedDict):
    # JSON-RPC protocol version; this server accepts 2.0.
    jsonrpc: Literal["2.0"]
    # MCP method to invoke.
    method: Literal["initialize", "notifications/initialized", "notifications/cancelled", "ping", "tools/list", "tools/call"]


class CreateMcpJsonRpcResponseBody(_CreateMcpJsonRpcResponseBodyRequired, total=False):
    # Request identifier echoed exactly in one JSON-RPC response; supported notifications omit it and receive an
    # empty HTTP 202.
    id: str | float | None
    # Method-specific MCP parameters.
    params: dict[str, Any]


class _CreateMcpJsonRpcResponseResponseRequired(TypedDict):
    jsonrpc: Literal["2.0"]
    id: str | float | None


class CreateMcpJsonRpcResponseResponse(_CreateMcpJsonRpcResponseResponseRequired, total=False):
    result: dict[str, Any]
    error: CreateMcpJsonRpcResponseResponseError


class CreateMcpJsonRpcResponseResponseError(TypedDict):
    code: int
    message: str


class GetReportsResponse(TypedDict):
    object: Literal["report_snapshot"]
    data: ReportSnapshot
    meta: ResponseMeta


class ReportSnapshot(TypedDict):
    kind: Literal["daily", "weekly", "monthly"] | str
    # Format: date-time.
    generated_at: str
    source_range: ReportSourceRange
    snapshot: SnapshotState
    completeness: SnapshotCompleteness
    reconciliation: ReportReconciliation
    report: ReportPayload


class ReportSourceRange(TypedDict):
    # Format: date.
    start_date: str
    # Format: date.
    end_date: str
    timezone: Literal["UTC"]


class SnapshotState(TypedDict):
    # Immutable content version for a durable report identity; 0 for an ephemeral explicit weekly from/to range.
    # Format: int64.
    version: int
    # durable for canonical daily, ISO-week, and monthly snapshot identities; ephemeral for explicit weekly
    # from/to ranges, which are recomputed within a bounded 31-day window and never persisted.
    storage: Literal["durable", "ephemeral"] | str
    # final only for a body whose source read started at or after final_after (the UTC close of the range plus the
    # whale-trade ingestion budget). rolling for a live range and for a closed range still inside that budget:
    # such ...
    status: Literal["final", "rolling"] | str
    # Format: date-time.
    generated_at: str
    # For a rolling body, the UTC date on which a final body can first be built (the date of final_after); null
    # once final. Format: date.
    mutable_until: str | None
    # Whether the source range has ended on the UTC calendar. Closing is not finality: a closed range is rolling
    # until final_after.
    period_closed: bool
    # The instant a source read must start at or after to produce a final body: the range's UTC close plus 7,530
    # s, the whale-trade ingestion budget (p95 block lag gate plus the projection retry budget). Format: date-
    # time.
    final_after: str
    # When this body's source read started, the clock finality is judged on. null for a body stored before that
    # clock was recorded. Format: date-time.
    source_read_started_at: str | None


class _SnapshotCompletenessRequired(TypedDict):
    # complete only on a final body (snapshot.status final). partial for a live range and for a closed range whose
    # body was read before final_after; reason says which. empty when the range has no whale activity.
    status: Literal["complete", "partial", "empty"] | str
    reason: str
    expected_days: int
    covered_days_with_whale_activity: int


class SnapshotCompleteness(_SnapshotCompletenessRequired, total=False):
    # Canonical key since #16304; covered_days_with_whale_activity is its deprecated spelling, emitted beside it
    # with the same value.
    covered_days_with_large_trade_activity: int


class ReportReconciliation(TypedDict):
    volume_kind: Literal["local_whale_activity_volume"]
    # Where the whale volume in this report is read from: the column name `whale_alerts.usdc_notional_num`,
    # followed in parentheses by the reconciliation note the server attaches to it. The server has always sent the
    # note ...
    whale_volume_source: str
    notes: str


class ReportPayload(TypedDict):
    # Canonical key since #16304; total_whale_trades is its deprecated spelling, emitted beside it with the same
    # value.
    total_large_trades: int | None
    total_whale_trades: int | None
    # Canonical key since #16304; total_whale_volume is its deprecated spelling, emitted beside it with the same
    # value.
    total_large_trade_volume: float | None
    total_whale_volume: float | None
    biggest_trade_size: float | None
    active_traders: int | None
    # Canonical key since #16304; top_whale_trades is its deprecated spelling, emitted beside it with the same
    # value.
    top_large_trades: list[ReportPayloadTopLargeTradesItem] | None
    top_whale_trades: list[ReportPayloadTopLargeTradesItem] | None
    categories: list[dict[str, Any]] | None
    # Counts of current grades for distinct Polymarket traders with at least one whale alert in the report's
    # source date range. The grade is the current projection at snapshot materialization time, not a historical
    # grade at ...
    grade_distribution: list[dict[str, Any]] | None


class ReportPayloadTopLargeTradesItem(TypedDict):
    # Provider outcome label for the traded side.
    outcome: str | None
    # Trade direction (BUY or SELL), not the outcome side.
    side: str | None
    # Market title.
    title: str | None
    # Trade size in USD.
    size: float | None
    # Trade price in provider [0, 1] units.
    price: float | None
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the traded outcome; null when
    # unavailable (e.g. unsynced markets).
    token_id: str | None
    # Whale trade id. Format: int64.
    id: int | None
    # Trade timestamp (UTC). Format: date-time.
    trade_time: str | None
    # Provider market category.
    market_category: str | None
    # Venue: polymarket.
    platform: str | None
    # Trader display name, when known.
    name: str | None
    # Trader pseudonym, when no display name is known.
    pseudonym: str | None
    # Trader grade (S-F) at snapshot time.
    trader_grade: str | None


class GetTraderExportSnapshotResponse(TypedDict):
    object: Literal["trader_export_snapshot"]
    data: TraderExportSnapshot
    meta: ResponseMeta


class TraderExportSnapshot(TypedDict):
    address: str
    # Format: date-time.
    generated_at: str
    source_range: ExportSourceRange
    completeness: ExportCompleteness
    reconciliation: ExportVolumeReconciliation
    counts: ExportCounts
    large_export_policy: LargeExportPolicy


class ExportSourceRange(TypedDict):
    # Format: date.
    first_pnl_date: str | None
    # Format: date.
    last_pnl_date: str | None
    # Format: date-time.
    latest_trade_at: str | None
    # Format: date-time.
    latest_market_activity_at: str | None


class ExportCompleteness(TypedDict):
    status: Literal["complete", "partial", "empty"] | str
    reason: str
    sync_coverage: float


class ExportVolumeReconciliation(TypedDict):
    # Verified full-history both-sides USD cash volume. Null without coverage; the local activity numerator may
    # cover only a subset of history.
    provider_lifetime_volume: float | None
    exported_activity_volume: float
    exported_market_cost_basis: float
    provider_activity_volume_gap: float | None
    activity_volume_coverage: float | None


class ExportCounts(TypedDict):
    pnl_days: int
    exported_markets: int
    estimated_trade_rows: int
    estimated_size_mb: float


class LargeExportPolicy(TypedDict):
    mode: Literal["v1_async_export"]
    current_internal_route: str
    # Programmatic API-key-gated export routes (submit/status/download/cancel) and supported formats (json,
    # ndjson, csv).
    v1_async: LargeExportPolicyV1Async
    direct_streaming: dict[str, Any]
    async_job: dict[str, Any]
    rate_limit: dict[str, Any]


class LargeExportPolicyV1Async(TypedDict, total=False):
    """Programmatic API-key-gated export routes (submit/status/download/cancel) and supported formats
    (json, ndjson, csv)."""
    # POST route template to submit an export job. fresh=true asks for a snapshot read after the submit instead of
    # reusing a finished one.
    submit_route: str
    # GET route template to poll job status.
    status_route: str
    # GET route template that 302-redirects to the file.
    download_route: str
    # POST route template to cancel a queued or running job.
    cancel_route: str
    # Supported ?format= values.
    formats: list[Literal["json", "ndjson", "csv"] | str]
    # Possible job status values.
    status_values: list[Literal["queued", "running", "ready", "failed", "reconcile_required", "expired", "cancel_requested", "cancelled"] | str]
    # How long a finished export is retained before expiry.
    retention: str


class TraderExportJob(TypedDict):
    object: Literal["trader_export_job"]
    data: TraderExportJobData
    meta: ResponseMeta


class _TraderExportJobDataRequired(TypedDict):
    # Format: int64.
    job_id: int
    # queued: accepted, not started. running: the worker is streaming rows. reconcile_required: the upload
    # finished but the storage completion answer was lost; the hourly reconciler reads the object back and moves
    # the job to ...
    status: Literal["queued", "running", "ready", "failed", "reconcile_required", "expired", "cancel_requested", "cancelled"] | str
    format: Literal["json", "ndjson", "csv"] | str
    # Format: int64.
    total_trades: int | None
    # Format: int64.
    processed_trades: int | None
    # Format: int64.
    file_size: int | None
    error: str | None
    # True when status never changes again (ready, failed, expired, cancelled). Stop polling.
    terminal: bool
    # What to do next: poll the status route after poll_after_s, follow the download route, or submit a new
    # export. Published beside status so a status value added later does not strand a client.
    next_action: Literal["poll", "download", "resubmit"] | str
    # Format: date-time.
    created_at: str
    # When the worker last claimed the job; null while queued. Format: date-time.
    started_at: str | None
    # When the file became downloadable. null before ready, and on jobs finalized before this field existed.
    # Format: date-time.
    ready_at: str | None
    # Format: date-time.
    failed_at: str | None
    # The retention window: 24 hours from submit. A ready file downloads until this instant; a job that has not
    # reached ready by it fails. A reused job (200 on submit) keeps its original window. Format: date-time.
    expires_at: str
    # When the job became expired; null until then. Format: date-time.
    expired_at: str | None
    # What the file is a snapshot of: the trader's served-data clock (the latest position refresh, else the last
    # completed sync) when the file was written; the same value as export_metadata.data_as_of inside the file.
    # null ...
    data_as_of: str | None
    # When the owner asked to cancel the job; null otherwise. Set on every cancelled job, including one cancelled
    # while queued. While status is cancel_requested this is the instant the worker was asked to stop. Format: ...
    cancel_requested_at: str | None
    # When the job reached cancelled; null until then. Format: date-time.
    cancelled_at: str | None
    # Worker claims so far.
    attempt: int
    # The job fails when attempt reaches this.
    max_attempts: int


class TraderExportJobData(_TraderExportJobDataRequired, total=False):
    # Seconds to wait before polling again. Absent when terminal. 5 while queued, running or cancel_requested; 300
    # while reconcile_required, the cadence that state can change at.
    poll_after_s: int
    # Present only while status is ready: the stored object's identity, so a client can check the download it
    # receives.
    artifact: TraderExportJobDataArtifact


class TraderExportJobDataArtifact(TypedDict):
    """Present only while status is ready: the stored object's identity, so a client can check the download
    it receives."""
    # Stable identity for this completed export artifact; unchanged when a temporary download URL is renewed.
    artifact_id: str
    # The storage ETag of the object.
    etag: str | None
    # Bytes on the wire (gzip); file_size is the decompressed size. Format: int64.
    compressed_size_bytes: int | None
    content_type: Literal["application/json", "application/x-ndjson", "text/csv"] | str
    content_encoding: Literal["gzip"]
    # Immutable manifest for artifacts generated with manifest support; null on historical artifacts written
    # before this contract.
    manifest: TraderExportArtifactManifest | None


class TraderExportArtifactManifest(TypedDict):
    # Version of the artifact manifest contract.
    manifest_version: str
    # Serialization used for the decompressed content.
    format: Literal["json", "ndjson", "csv"] | str
    # Stable schema identifier for the selected serialization.
    schema_version: Literal["trader-export-json-v1", "trader-export-ndjson-v1", "trader-export-csv-v1"] | str
    # Sections represented by the artifact. JSON and NDJSON carry the full envelope and trades; CSV carries trade
    # rows only.
    coverage: Literal["full_envelope_and_trades", "trades_only"] | str
    generation: TraderExportGeneration
    # Number of trade rows written. Format: int64.
    row_count: int
    # Exact byte count of the decompressed content stream clients receive. Format: int64.
    content_size_bytes: int
    # Lowercase SHA-256 of the decompressed content bytes.
    content_sha256: str
    # Exact byte count of the gzip-compressed bytes stored by the object provider. Format: int64.
    compressed_size_bytes: int
    # Lowercase SHA-256 of the stored gzip bytes; the multipart ETag is not used as this checksum.
    compressed_sha256: str


class TraderExportGeneration(TypedDict):
    # Opaque generation identity selected for the coherent read snapshot. Format: uuid.
    id: str
    # Format: date-time.
    selected_at: str
    consistency: Literal["repeatable_read"]
    source_watermarks: TraderExportSourceWatermarks


class TraderExportSourceWatermarks(TypedDict):
    positions: TraderExportPositionWatermark
    pnl: TraderExportPnlWatermark
    categories: TraderExportCategoryWatermark
    trades: TraderExportTradeWatermark


class TraderExportPositionWatermark(TypedDict):
    source: str
    coverage: str
    # Format: int64.
    generation: int | None
    # Format: date-time.
    data_as_of: str | None


class TraderExportPnlWatermark(TypedDict):
    source: str
    coverage: str
    # Format: int64.
    revision: int | None
    # Format: date-time.
    observed_at: str | None


class TraderExportCategoryWatermark(TypedDict):
    source: str
    coverage: str
    # Format: date-time.
    publication_fence: str | None
    # Format: date-time.
    data_as_of: str | None


class TraderExportTradeWatermark(TypedDict):
    source: str
    coverage: str
    # Format: int64.
    rows: int
    # Format: date.
    first_activity_date: str | None


class Usage(TypedDict):
    object: Literal["usage"]
    data: UsageData
    meta: ResponseMeta


class UsageData(TypedDict):
    rate_limit: UsageDataRateLimit
    # UTC-day usage count. Current V1 has no daily hard cap, so limit and remaining are null rather than
    # synthesized.
    daily_usage: UsageDataDailyUsage
    # The monthly request quota (#16111): where the account stands against the requests Pro includes per UTC
    # calendar month. Reading it here spends nothing. null only when the month's count could not be read for this
    # response.
    monthly_quota: UsageDataMonthlyQuota | None


class UsageDataRateLimit(TypedDict):
    used: int
    limit: int
    remaining: int
    reset_at: int
    window_seconds: int


class UsageDataDailyUsage(TypedDict):
    """UTC-day usage count. Current V1 has no daily hard cap, so limit and remaining are null rather than
    synthesized."""
    used: int
    limit: int | None
    remaining: int | None
    reset_at: int
    window_seconds: int


class UsageDataMonthlyQuota(TypedDict):
    """The monthly request quota (#16111): where the account stands against the requests Pro includes per
    UTC calendar month. Reading it here spends nothing. null only when the month's count could not be
    read for this response."""
    # Admitted requests so far this UTC calendar month.
    used: int
    # Requests Pro includes per UTC calendar month.
    limit: int
    remaining: int
    # Unix seconds: the first instant of the next UTC calendar month.
    reset_at: int
    # Unix seconds: from when request limit + 1 is refused for an account the quota binds.
    enforced_from: int
    # Whether requests over this account's ceiling are refused right now: false before enforced_from and for an
    # admin account.
    binding: bool
    # Pay as you go is on: requests over the quota keep answering and bill on a monthly invoice, up to ceiling.
    pay_as_you_go: bool
    # The most requests this account is admitted in a UTC calendar month once enforcement has begun: limit, or
    # 1,000,000 with pay as you go on. null for an admin account, which no number stops. Additive since
    # 2026-09-22.
    ceiling: int | None


class AccountIdentity(TypedDict):
    object: Literal["account"]
    data: AccountIdentityData
    meta: ResponseMeta


class AccountIdentityData(TypedDict):
    user_id: int
    credential_id: int
    credential_kind: Literal["api_key", "oauth_grant"] | str
    # The credential is currently valid; revoked, expired or unknown credentials are rejected.
    credential_status: Literal["active"]
    entitlement: AccountIdentityDataEntitlement
    # Approved OAuth scopes; null for full developer-key access.
    scopes: list[str] | None


class AccountIdentityDataEntitlement(TypedDict):
    paid_data_access: Literal["active", "lapsed"] | str
    # When paid data access is lapsed, the caller should renew the subscription; otherwise null.
    recovery_action: Literal["renew_subscription"] | None
