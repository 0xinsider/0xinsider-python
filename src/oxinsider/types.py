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
    "BatchGameHoldersItem",
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
    "CategoryLeader",
    "CategorySkillModelReadiness",
    "CategorySkillV2",
    "Combo",
    "ComboCoverage",
    "ComboCoverageCursor",
    "ComboDetail",
    "ComboFill",
    "ComboFillsResponse",
    "ComboLeg",
    "ComboLegMarket",
    "ComboLifecycleStats",
    "ComboLiveCount",
    "ComboResponse",
    "ComboTotals",
    "ComboWindowStats",
    "CombosSummary",
    "CombosSummaryResponse",
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
    "CreateWebhookVerificationAttemptRequest",
    "CreateWebhookVerificationAttemptResponse",
    "DataQuality",
    "DataQualityGroup",
    "EdgeHunterBoard",
    "EdgeHunterBoardResponse",
    "EdgeHunterCategorySkill",
    "EdgeHunterFunnelReport",
    "EdgeHunterMarketContext",
    "EdgeHunterObservation",
    "EdgeHunterObservationCoverage",
    "EdgeHunterObservationDegradationReason",
    "EdgeHunterObservationDeparture",
    "EdgeHunterObservationTerminalReason",
    "EdgeHunterObservationsResponse",
    "EdgeHunterOutcome",
    "EdgeHunterParticipant",
    "EdgeHunterPrice",
    "EdgeHunterRankedSignal",
    "EdgeHunterRow",
    "EdgeHunterSelection",
    "EdgeHunterSignal",
    "EdgeHunterSignalsResponse",
    "EdgeHunterSportFunnelReport",
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
    "GameHoldersItem",
    "GameMarket",
    "GameMarketLiquidity",
    "GameMarketPriceBindingProvenance",
    "GameMarketPriceCompetitor",
    "GameMarketPriceIncomplete",
    "GameMarketPriceInvalid",
    "GameMarketPricePaired",
    "GameMarketPrices",
    "GameMarketProviderPrices",
    "GameSharpMoney",
    "GameSharpMoneyOutcomesItem",
    "GameSharpMoneyVerdict11",
    "GameSharpMoneyVerdict12",
    "GameSharpMoneyVerdict13",
    "GameSharpMoneyVerdict14",
    "GameSharpMoneyVerdict15",
    "GameSharpMoneyVerdict16",
    "GameSharpMoneyVerdict17",
    "GameSharpMoneyVerdict18",
    "GameStatus",
    "GameTrade",
    "GameTradeMarket",
    "GameTradeTrader",
    "GameVolume",
    "GamesCoverage",
    "GetApiDiscoveryResponse",
    "GetCategoryLeaderboardResponse",
    "GetCoverageResponse",
    "GetEventReplaySinceResponse",
    "GetGameHoldersResponse",
    "GetGameResponse",
    "GetGameSharpMoneyResponse",
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
    "GetMarketTopHoldersResponse",
    "GetMarketWalletsInOutResponse",
    "GetPickOfTheDayArchiveResponse",
    "GetPickOfTheDayLedgerEntryResponse",
    "GetPickOfTheDayLedgerResponse",
    "GetPickOfTheDayResponse",
    "GetPickOfTheDayStatsResponse",
    "GetPositionTimelineResponse",
    "GetReportsResponse",
    "GetResolutionReportResponse",
    "GetSportLeaderboardResponse",
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
    "LargeExportPolicyAsyncJob",
    "LargeExportPolicyDirectStreaming",
    "LargeExportPolicyRateLimit",
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
    "LeaderboardLeagues",
    "LeaderboardLeaguesLeaguesItem",
    "LeaderboardPriceEdge",
    "ListCategoryLeadersResponse",
    "ListGameMarketsResponse",
    "ListGameMarketsResponseDataItem",
    "ListGameMarketsResponseDataItemOutcomesItem",
    "ListGameMarketsResponseDataItemSharpMoney",
    "ListGameMarketsResponseDataItemSharpMoneyOutcomesItem",
    "ListGameMarketsResponseFamiliesItem",
    "ListGameTradesResponse",
    "ListGamesResponse",
    "ListLargePositionsResponse",
    "ListLargeTradeCounterpartyExecutionsResponse",
    "ListLargeTradeCounterpartyMakersResponse",
    "ListLargeTradeHistoryResponse",
    "ListLargeTradesResponse",
    "ListLeaderboardLeaguesResponse",
    "ListLeaderboardResponse",
    "ListPositionsResponse",
    "ListPositionsResponseSnapshot",
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
    "MarketHoldersSideGradeUsd",
    "MarketHoldersSideGrades",
    "MarketHoldersTotals",
    "MarketSearchResult",
    "MarketSnapshot",
    "MarketSnapshotFreshness",
    "MarketSnapshotLiquidity",
    "MarketSnapshotMarket",
    "MarketSnapshotOutcomesItem",
    "MarketSnapshotSports",
    "MarketSnapshotSportsLiveScore",
    "MarketSnapshotTopOfBook",
    "MarketSnapshotTrust",
    "MarketTopHolder",
    "MarketTopHolders",
    "MarketTopHoldersTotals",
    "MarketWalletsInOut",
    "MarketWalletsInOutNetBuyersItem",
    "MarketWalletsInOutSummary",
    "NotModifiedResponse",
    "OutcomeCandles",
    "PickHolder",
    "PickHolderCategoryWinRecord",
    "PickLeadBacker",
    "PickOfTheDay",
    "PickOfTheDayArchive",
    "PickOfTheDayArchiveDay",
    "PickOfTheDayArchiveEntry",
    "PickOfTheDayCommitmentPayload",
    "PickOfTheDayCommitmentPayloadV1",
    "PickOfTheDayCommitmentPayloadV2",
    "PickOfTheDayHitRate",
    "PickOfTheDayHitRateSeriesItem",
    "PickOfTheDayLedger",
    "PickOfTheDayLedgerEntry",
    "PickOfTheDayLedgerOpenedEntry",
    "PickOfTheDayLedgerSealedEntry",
    "PickOfTheDayLedgerUncommittedEntry",
    "PickOfTheDayLockedPicksItem",
    "PickOfTheDayNoEntitledPicks",
    "PickOfTheDayQualifyingExpert",
    "PickOfTheDayStats",
    "PickOfTheDayStatsCategoriesItem",
    "PickOfTheDayStatsDaysItem",
    "PickOfTheDayStatsMarketExpectations",
    "PickOfTheDayStatsMarketExpectationsWindowsItem",
    "PickOfTheDayStatsOutcomeStats",
    "PickOfTheDayStatsOutcomeStatsConcentration",
    "PickOfTheDayStatsOutcomeStatsDrawdown",
    "PickOfTheDayStatsOutcomeStatsProfitFactor",
    "PickOfTheDayStatsOutcomeStatsRollingItem",
    "PickOfTheDayStatsRecords",
    "PickOfTheDayStatsRecordsBestDay",
    "PickOfTheDayStatsRecordsBiggestWin",
    "PickOfTheDayStatsRecordsLongestLosingDayStreak",
    "PickOfTheDayStatsRecordsSweeps",
    "PickOfTheDayStatsRecordsSweepsLatestCleanSweep",
    "PickOfTheDayStatsRecordsWinningDays",
    "PickOfTheDayStatsStreaks",
    "PickOfTheDayStatsVoidsItem",
    "PickOfTheDayUncommittedPayload",
    "PickSportsContext",
    "PickSportsTeam",
    "PlatformCapabilities",
    "PlatformCapabilityStatus",
    "Platforms",
    "PlatformsPlatforms",
    "PnlCorrection",
    "Position",
    "PositionExact",
    "PositionMarket",
    "PositionTimelineEvent",
    "PositionTrader",
    "PotdEntryAuthorization",
    "ProofPendingPickSlot",
    "RedeliverWebhookDeliveryResponse",
    "RegisterAgentResponse",
    "ReportPayload",
    "ReportPayloadCategoriesItem",
    "ReportPayloadGradeDistributionItem",
    "ReportPayloadTopLargeTradesItem",
    "ReportReconciliation",
    "ReportSnapshot",
    "ReportSourceRange",
    "ResolutionReport",
    "ResolutionReportMarketsItem",
    "ResolutionReportMarketsItemTradersItem",
    "ResolutionReportTimeBasisCounts1",
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
    "SportLeaderboard",
    "SportLeaderboardLeague1",
    "SportLeaderboardRowsItem",
    "SportLeaderboardRowsItemPriceEdge1",
    "SubmitWhaleDatasetBody",
    "SuspiciousTrade",
    "SuspiciousTradeMarket",
    "SuspiciousTradeScores",
    "SuspiciousTradeTrader",
    "TennisPoints",
    "TennisRanking",
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
    "TraderPnlInScope",
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
    "WebhookVerificationAttempt",
    "WhaleDatasetArtifactManifest",
    "WhaleDatasetContinuation",
    "WhaleDatasetFilters",
    "WhaleDatasetGeneration",
    "WhaleDatasetJob",
    "WhaleDatasetJobData",
    "WhaleDatasetJobDataArtifact",
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
    # Directional evidence provenance for Edge Hunter signals collections. The default board carries this
    # provenance in data.directional_source and omits this optional meta field.
    directional_source: Literal["live", "degraded"] | str
    # Ranking evidence provenance for Edge Hunter signals collections. The default board carries this
    # clock/provenance in data.ranking_source and omits this optional meta field.
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
    # responses even when the filtered signal list is empty. When true, category_skill_source is degraded and Edge
    # ...
    category_skill_model_operationally_degraded: bool
    category_skill_status_counts: ResponseMetaCategorySkillStatusCounts
    # SHA-256 of the funded signal membership/order/rank/cursor vector immediately before category-skill
    # enrichment. Edge Hunter signals view only.
    category_skill_base_payload_hash: str
    # Independent SHA-256 recomputation over the same base fields immediately after category-skill enrichment.
    # Equality with category_skill_base_payload_hash proves category-skill enrichment did not change funded
    # inputs. Edge ...
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
    # Sports and esports markets only since 2026-10-27 (#29830): markets_traded and win_rate come from the
    # wallet's sports and esports record (pnl.in_scope), and total_volume from its stored trade days. A wallet
    # that traded ...
    stats: TraderStats
    # Data age and coverage for this trader body. Always present. Its six groups are sync (traders.last_synced,
    # covering synced_at and sync_status; it covered last_active until 2026-11-02, #32324, and no group covers ...
    data_quality: DataQuality


class Trader(_TraderRequired, total=False):
    username: str
    grade: Literal["S", "A", "B", "C", "D", "F"] | str
    # Hot-streak tier (trailing-7d cross-sectional percentile); a separate axis from the all-time grade. Omitted
    # when there is no recent activity.
    streak_tier: Literal["hot", "rising", "neutral", "cooling", "cold"] | str
    score: float
    # Optional forecast score on the documented display scale. Null when unavailable.
    forecast_score: float
    # Optional measured forecast context. Missing values remain unavailable rather than being inferred.
    forecast_evidence: float
    rank: int
    strategy: TraderStrategy
    # Per-category rank context when expand=categories is requested. Values include available rank, category
    # totals, performance and record counts; scaled_total_pnl is a legacy alias of total_pnl. Its measurement
    # basis and ...
    category_strengths: dict[str, Any]
    # Deprecated since 2026-10-27 and never sent. These advanced risk and performance metrics covered every
    # Polymarket market of the wallet, and wallet figures cover sports and esports markets only (#29589). ...
    quant_metrics: TraderQuantMetrics
    # When the wallet last traded: its most recent recorded trade, the same value the leaderboard entry's
    # last_active carries (which re-reads it hourly). A cached body (meta.cached true) can lag a new trade by up
    # to 60 ...
    last_active: str
    # When 0xinsider last completed a sync of the wallet (traders.last_synced), dated by the sync data_quality
    # group. Not when the wallet traded: read last_active for that. Format: date-time.
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
    # Deprecated since 2026-10-27 and never sent. It was Polymarket's all-time leaderboard P&L, which covered
    # every Polymarket market of the wallet, and wallet figures cover sports and esports markets only (#29830).
    # Read ...
    total: float
    # Deprecated since 2026-10-27 and never sent. It was Polymarket's net total P&L over every Polymarket market
    # of the wallet, and wallet figures cover sports and esports markets only (#29830). Read
    # pnl.in_scope.realized_pnl.
    net_total: float
    # Deprecated since 2026-10-27 and never sent. It was the neg-risk conversion correction to the wallet-wide
    # pnl.net_total and pnl.realized (#29830). Its sports and esports part is inside pnl.in_scope.realized_pnl.
    correction: PnlCorrection
    # true while 0xinsider is still checking some of the wallet's converted neg-risk markets with a sports or
    # esports event (not yet measured, measured and not yet checked for transfers, or its latest reads keep
    # failing), so ...
    correction_pending: bool
    # Deprecated since 2026-10-27 and never sent. It was native Polymarket realized P&L over every Polymarket
    # market of the wallet, and wallet figures cover sports and esports markets only (#29830). Read ...
    realized: float
    # Unrealized (mark-to-market) P&L in USD of the wallet's open positions on its synced sports and esports
    # markets: Polymarket's cashPnl, current value minus cost, summed over the positions still held, from the ...
    unrealized: float
    # Deprecated since 2026-10-27 and never sent: its one member was the lossless counterpart of the retired
    # pnl.realized (#29830).
    exact: TraderPnlExact
    # Additive (#27311): the wallet's sports and esports record, the figure the 0xinsider profile headlines, dated
    # by the sports_record data_quality group. Omitted until 0xinsider has computed the wallet's record; absent
    # ...
    in_scope: TraderPnlInScope


class _PnlCorrectionRequired(TypedDict):
    # The correction method.
    basis: Literal["neg_risk_conversion_v1"]
    # The correction in USD. Negative when Polymarket overstates the wallet.
    amount: float
    # The newest measurement among the measured markets. Format: date-time.
    as_of: str
    # Neg-risk markets whose measurement amount sums.
    markets_measured: int


class PnlCorrection(_PnlCorrectionRequired, total=False):
    """A derived 0xinsider correction to Polymarket's P&L, never a Polymarket value. Polymarket misbooks
    neg-risk conversions, in both directions: it puts cost on placeholder YES outcomes minted by a
    conversion and never books it as a loss (negative amount), and its position records leave out shares
    the wallet really got, such as YES minted by a conversion, so it books no P&L on them (positive
    amount). Per neg-risk market the wallet converted in, 0xinsider measures Polymarket's own activity
    cash against the sum of its position P&L, and sums the difference over every measured market whose
    shares did ..."""
    # Polymarket's net realized P&L plus amount. Since 2026-10-22 the grade reads this figure's sports and esports
    # share. Omitted when Polymarket's figure is.
    realized: float
    # Polymarket's net total P&L over every Polymarket market of the wallet, plus amount. Omitted when
    # Polymarket's figure is, and on leaderboard entries.
    net_total: float
    # Measured neg-risk markets left out because shares moved in or out of the wallet by direct transfer; they
    # keep Polymarket's figure. Omitted when none.
    markets_excluded: int


class TraderPnlExact(TypedDict):
    """Deprecated since 2026-10-27 and never sent: pnl.exact held the lossless counterpart of the retired
    wallet-wide pnl.realized (#29830). The member shape below is what the object held before; it is kept
    so existing type declarations still compile."""
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


class TraderPnlInScope(TypedDict):
    """A wallet's sports and esports record (#27311). basis names the rule behind realized_pnl (#29370):
    polymarket_sports_esports_v1 is Polymarket's own realized P&L for the wallet in its sports and
    esports categories, plus the wallet's maker and taker rebates apportioned by its sports and esports
    share of its Polymarket volume (by cost while Polymarket reports no overall volume) and the in-scope
    part of any published neg-risk conversion correction; sports_esports_split_v1, used until both of
    the wallet's category figures are confirmed, is Polymarket's published wallet-wide realized P&L
    (with any ..."""
    # The rule behind realized_pnl: polymarket_sports_esports_v1 (Polymarket's sports and esports category figures
    # plus apportioned rebates) or sports_esports_split_v1 (the published realized figure split by cost). A new
    # ...
    basis: str
    # Sports and esports realized P&L in USD, display-safe. null when the split basis has no published realized
    # figure to split.
    realized_pnl: float | None
    # Sports and esports markets the wallet has traded, any status.
    markets: int
    # Of those, the settled markets: the wallet closed its position by selling out, or the market resolved. Its
    # P&L there is final.
    markets_resolved: int
    # Share of decided sports and esports markets the wallet won, 0 to 1. null with no decided market.
    win_rate: float | None
    # The wallet's markets outside sports and esports, which 0xinsider no longer lists: those it still stores,
    # those whose rows it deleted and counted, and those of other categories first traded since 2026-10-26, which
    # it ...
    markets_out_of_scope: int
    # When the record behind these figures was computed. Format: date-time.
    as_of: str


class TraderStats(TypedDict, total=False):
    """Sports and esports markets only since 2026-10-27 (#29830): markets_traded and win_rate come from the
    wallet's sports and esports record (pnl.in_scope), and total_volume from its stored trade days. A
    wallet that traded no sports or esports market never gets a record: markets_traded is 0 and win_rate
    is omitted (since 2026-10-29, #30589, #30657). A wallet that trades only combos has no record
    either: both are omitted (since 2026-10-29, #30637)."""
    # Sports and esports markets the wallet traded, any status: pnl.in_scope.markets, dated by the sports_record
    # data_quality group. Omitted until the record is computed. 0 for a wallet that traded no sports or esports
    # ...
    markets_traded: int
    # Won over decided sports and esports markets, 0 to 1: pnl.in_scope.win_rate truncated to four places, dated
    # by the sports_record data_quality group. Omitted until the record is computed, while the wallet has no
    # decided ...
    win_rate: float
    # Deprecated since 2026-10-27 and never sent. It counted mark-to-market days over every Polymarket market of
    # the wallet (#29830). Read stats.all.win_days and stats.all.loss_days from GET /api/v1/trader/{address}/pnl,
    # ...
    daily_win_rate: float
    # Sports and esports USD volume, all time: the sum of every stored trade day's in-scope volume
    # (trader_trade_daily_rollups.in_scope_volume_total), the profile's Volume traded. Dated by the volume
    # data_quality group, which ...
    total_volume: float
    # Additive lossless counterpart to `total_volume`, present exactly when it is.
    exact: TraderStatsExact


class TraderStatsExact(TypedDict):
    """Lossless counterparts for trader statistics. The object is present exactly when stats.total_volume
    is."""
    # stats.total_volume as an exact decimal: the sports and esports USD volume, the sum of every stored trade
    # day's `trader_trade_daily_rollups.in_scope_volume_total` (#29830). Polymarket's full-history wallet-wide
    # user ...
    total_volume: ExactDecimal


class _TraderStrategyRequired(TypedDict):
    # Observed trading style identifier. New rows use two_sided, category_focused, high_activity, diversified,
    # mixed, or unclassified, counted over the wallet's sports and esports markets only. Historical identifiers
    # remain ...
    strategy_type: str


class TraderStrategy(_TraderStrategyRequired, total=False):
    description: str
    confidence: float


class TraderQuantMetrics(TypedDict):
    """Deprecated since 2026-10-27 and never sent. These advanced risk and performance metrics covered
    every Polymarket market of the wallet, and wallet figures cover sports and esports markets only
    (#29589). expand=quant_metrics is still accepted and adds nothing. For the sports and esports record
    read pnl.in_scope here, and GET /api/v1/trader/{address}/pnl for its daily series. The member shape
    below is what the object held before; it is kept so existing type declarations still compile."""
    # Trader smart score on a 0..100 display scale; higher is stronger. Null when unavailable.
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
    # Share of the trader's last 30 days with realized P&L that closed positive, 0-1 (higher is more consistent).
    # A day with no realized P&L is not one of them, so the window can span months. null below 10 such days; null
    # ...
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
    # fresh when every group is fresh, unavailable when every group is unavailable, stale when every group is
    # fresh or stale and at least one is stale, and partial in every other case.
    status: Literal["fresh", "stale", "partial", "unknown", "untracked", "unavailable"] | str
    # One entry per field group. Entries may be added in later releases, so match on group rather than on position
    # or length.
    field_groups: list[DataQualityGroup]


class DataQuality(_DataQualityRequired, total=False):
    """Compact data age and coverage for a response body, always present on the operations that publish it.
    Read status and as_of to decide whether to use the body at all, and field_groups to see which part
    is weak. Everything here comes from stored observation clocks, and each clocked group is judged
    against its writer's budget when the body is served, so a cached body reports the same ages and
    verdicts a freshly computed one does: meta.cached and meta.cache_age_s stay the only transport-time
    facts and neither makes this block newer. The per-field audit object is still available through ..."""
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
    # fresh: served, as_of carries this group's real observation or computation clock, and that clock is no older
    # than max_age_s when the group carries one. stale: served and clocked, but as_of is older than max_age_s, so
    # the ...
    status: Literal["fresh", "stale", "partial", "unknown", "untracked", "unavailable"] | str


class DataQualityGroup(_DataQualityGroupRequired, total=False):
    """One group of response fields that share a writer and therefore share a clock."""
    # When this group's values were observed or computed. Omitted whenever the read cannot measure it, and never
    # filled with the serialization time, the cache time, or another group's clock. Format: date-time.
    as_of: str
    # Why the status is not fresh. Omitted when it is.
    reason: str
    # The longest gap in seconds this group's writer leaves between refreshes on its schedule: the age past which
    # the group reads stale instead of fresh. Omitted when the writer keeps no schedule its clock could fall
    # behind ...
    max_age_s: int


class _TraderTrustRequired(TypedDict):
    # Since 2026-10-27 always not_computed: pnl.total is retired and never sent (#29830). The key stays so the
    # object keeps its shape.
    total_pnl: TrustMetadata
    # Since 2026-10-27 always not_computed: pnl.realized and pnl.exact are retired and never sent (#29830). The
    # key stays so the object keeps its shape.
    realized_pnl: TrustMetadata
    # Since 2026-10-27 always not_computed: pnl.net_total is retired and never sent (#29830). The key stays so the
    # object keeps its shape.
    net_total_pnl: TrustMetadata
    unrealized_pnl: TrustMetadata
    # Computed, owned by trader_product_scope_records (markets) and dated by the record's computed_at, since
    # 2026-10-27 (#29830). For a wallet that traded no sports or esports market, which never gets a record, owned
    # by ...
    markets_traded: TrustMetadata
    # Computed, owned by trader_product_scope_records (win_rate) and dated by the record's computed_at, since
    # 2026-10-27 (#29830).
    win_rate: TrustMetadata
    # Since 2026-10-27 always not_computed: stats.daily_win_rate is retired and never sent (#29830). The key stays
    # so the object keeps its shape.
    daily_win_rate: TrustMetadata
    # Computed, owned by trader_trade_daily_rollups (in_scope_volume_total) and dated by traders.last_synced,
    # since 2026-10-27 (#29830).
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


class TraderTrust(_TraderTrustRequired, total=False):
    """Field-level trust metadata returned only when GET /api/v1/trader/{address} includes expand=trust."""
    # Deprecated since 2026-10-27 and never sent: it was present only with pnl.correction, which is retired
    # (#29830).
    pnl_correction: TrustMetadata


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
    grade: Literal["S", "A", "B", "C", "D", "F", None] | str | None
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
    # Writer-proven model family, such as grading. Null when unknown.
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
    # Aggregate position and P&L coverage for the trader, over its synced markets. markets_open, unrealized_mtm
    # and cost_basis_locked cover the open positions on sports and esports markets, each market judged when the
    # summary ...
    position_summary: TraderContextPositionSummary


class TraderContextPositionSummary(TypedDict):
    """Aggregate position and P&L coverage for the trader, over its synced markets. markets_open,
    unrealized_mtm and cost_basis_locked cover the open positions on sports and esports markets, each
    market judged when the summary is read (#32119). markets_synced, markets_resolved and the resolved
    win figures count every stored market: since 2026-10-27 (#29366) those are mostly sports and esports
    markets, but a market that moved out of sports and esports, or one stored before its category was
    known, stays in them, and sync_coverage counts every category on both sides. markets_total,
    total_realized_pnl ..."""
    # Polymarket's count of the markets the wallet traded, every category, when known; null when the provider
    # total is unavailable.
    markets_total: int | None
    # Markets with locally synced position rows.
    markets_synced: int
    # Markets outside sports and esports that the wallet traded and whose synced rows 0xinsider deleted, counted
    # when they were deleted (from 2026-10-27, #29366); 0 when none were. Not in markets_synced or any other count
    # ...
    markets_pruned: int
    # Markets outside sports and esports that the wallet first traded since 2026-10-26, which 0xinsider does not
    # store, counted as the wallet syncs (#30165); 0 when none are. Not in markets_synced, markets_pruned or any
    # other ...
    markets_unstored: int
    # Combo markets the wallet traded, as maker or taker, counted from the combo fills 0xinsider indexes from the
    # chain (#30218); 0 when it traded none. Polymarket counts each combo as one market in markets_total, and no
    # ...
    markets_combo: int
    # Synced markets the wallet has settled: it closed its position by selling out, or the market resolved. Its
    # P&L there is final.
    markets_resolved: int
    # Synced sports and esports markets still open with residual value (open positions with current value > 0); a
    # stored market of another category is left out (#32119).
    markets_open: int
    # markets_synced plus markets_pruned plus markets_unstored plus markets_combo, divided by markets_total when
    # the provider total is known (capped at 1.0); 0.0-1.0. Both sides count every category: no Polymarket count
    # of a ...
    sync_coverage: float
    # Native net realized P&L (USD) over every Polymarket market of the wallet, including credited rebates, minus
    # the stored realized component of synced open positions with positive current value. Rebates are credited to
    # the ...
    synced_realized_pnl: float
    # Native net realized P&L (USD) over every Polymarket market of the wallet, including credited rebates, read
    # directly from the accounting snapshot. For the sports and esports figure read
    # trader.pnl.in_scope.realized_pnl. ...
    total_realized_pnl: float
    # Mark-to-market unrealized P&L (USD) on open positions in synced sports and esports markets (#32119):
    # Polymarket's cashPnl summed over the positions still held, without the realized P&L of partial sells. The
    # same figure ...
    unrealized_mtm: float
    # Cost basis (USD) currently tied up in open positions in synced sports and esports markets (#32119).
    cost_basis_locked: float
    # Win rate as a percentage (0-100): resolved_wins over resolved_decided. A settled market that closed at
    # exactly zero realized P&L (a void, a refund, a fully hedged position) is neither a win nor a loss and is not
    # in the ...
    resolved_win_rate: float | None
    # Settled markets that closed at positive realized P&L: the win-rate numerator. Additive; null only on a
    # summary cached before the field existed.
    resolved_wins: int | None
    # Settled markets that closed at a non-zero realized P&L: the win-rate denominator. At most markets_resolved;
    # the difference is markets settled at exactly zero or with an unknown P&L. Additive; null only on a summary
    # ...
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
    code: Literal["bad_request", "invalid_api_key", "subscription_required", "forbidden", "insufficient_scope", "not_found", "account_locked", "rate_limited", "rate_limit_unavailable", "internal_error", "request_timeout", "endpoint_retired"] | str
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
    reason: Literal["cursor_expired", "unknown_endpoint", "pick_not_released", "trader_not_tracked", "market_out_of_scope", "read_model_warming", "database_unavailable", "request_accounting_unavailable", "idempotency_in_progress", "webhook_delivery_in_progress", "webhook_secret_rotation_not_prepared", "webhook_secret_rotation_overlap_active", "sandbox_api_key", "api_key_in_query", "subscription_inactive", "monthly_quota_exceeded", "invalid_query", "unknown_query_parameter", "invalid_path", "invalid_body", "unsupported_media_type", "payload_too_large", "method_not_allowed", "ip_rate_limited", "ip_throttled", "cold_read_limited", "export_expired", "freshness_ceiling_unsatisfied", "max_plan_required", "endpoint_retired"] | str


class _FreshnessFailureRequired(TypedDict):
    # The caller's requested whole-response freshness ceiling in seconds. Format: int64.
    max_age_s: int
    # The trader body's whole-response data-quality status. Only fresh or stale can satisfy max_age_s: the ceiling
    # replaces each writer's own budget, so a stale body inside it is answered.
    data_quality_status: Literal["fresh", "stale", "partial", "unknown", "untracked", "unavailable"] | str


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
    # The batch item budget per minute for the caller's plan: 2500 item units on Pro, 5000 on Max. The same number
    # X-Batch-RateLimit-Limit reports.
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
    # The wallet's own side of this fill: buy or sell.
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
    # True when wallet_age_days is under the new-wallet threshold (30 days), which means 0xinsider first recorded
    # the wallet in the last 30 days. False when wallet_age_days is absent. This public V1 field is first-seen ...
    is_new_wallet: bool


class PositionTrader(_PositionTraderRequired, total=False):
    username: str
    grade: Literal["S", "A", "B", "C", "D", "F"] | str
    # Sports and esports win rate as a ratio from 0 to 1 (0.62 means 62%): wins over the decided sports and
    # esports markets on the wallet's record, the same figure as pnl.in_scope.win_rate and stats.win_rate on GET
    # ...
    win_rate: float
    # Deprecated since 2026-10-27 and never sent. It was Polymarket's net total P&L over every Polymarket market
    # of the wallet, and wallet figures cover sports and esports markets only (#29953). Read ...
    pnl: float
    # The wallet's realized P&L in USD on sports and esports markets, the figure the 0xinsider profile shows: the
    # record behind pnl.in_scope.realized_pnl on GET /api/v1/trader/{address}, to cents. For a graded wallet it is
    # ...
    in_scope_realized_pnl: float
    # Sports and esports markets on the wallet's record, pnl.in_scope.markets on GET /api/v1/trader/{address}.
    # Since 2026-10-27 it no longer counts other markets (#29953). Absent when the wallet has no record.
    markets: int
    # Days since the wallet's first-seen time. For a wallet 0xinsider first recorded on or after March 21, 2026,
    # that is when 0xinsider recorded it. For a wallet recorded earlier, it is usually the wallet's first
    # Polymarket ...
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
    # Sports and esports win rate as a ratio from 0 to 1 (0.62 means 62%): wins over the decided sports and
    # esports markets on the wallet's record, the same figure as pnl.in_scope.win_rate on GET
    # /api/v1/trader/{address}. ...
    win_rate: float
    # Deprecated since 2026-10-27 and never sent. It was Polymarket's net total P&L over every Polymarket market
    # of the wallet, and wallet figures cover sports and esports markets only (#29953). Read ...
    pnl: float
    # The wallet's realized P&L in USD on sports and esports markets, the figure the 0xinsider profile shows: the
    # record behind pnl.in_scope.realized_pnl on GET /api/v1/trader/{address}, to cents. Distinct from this ...
    in_scope_realized_pnl: float
    # Sports and esports markets on the wallet's record, pnl.in_scope.markets on GET /api/v1/trader/{address}.
    # Since 2026-10-27 it no longer counts other markets (#29953). Absent when the wallet has no record.
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
    # unavailable (e.g. unsynced markets) and for a Polymarket trade recorded before 2026-04-02T00:00:00Z whose
    # traded side is ...
    token_id: str | None
    price: float
    # Current trade review score on a 0..1 scale; higher values indicate a stronger review signal. This is the
    # current response value and can differ from the recorded score. Missing measurements remain unavailable.
    review_score: float
    # Deprecated alias of review_score with the same current value and 0..1 scale. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read review_score.
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
    suspicion_track: Literal["whale", "fresh_conviction", "sliced_position", None] | str | None
    trader: LargeTradeTrader
    market: LargeTradeMarket


class LargeTrade(_LargeTradeRequired, total=False):
    # This fill's size relative to its market: its share count (size_usd / price) divided by the shares the market
    # has traded, Polymarket's recorded volume, which counts shares rather than dollars, as observed at or after
    # the ...
    market_volume_share: float


class _LargeTradeTraderRequired(TypedDict):
    id: str
    address: str
    # The grade the trader held when the trade happened, from recorded grade history (recorded from
    # 2026-09-19T23:00Z). Null unless grade_at_trade_status is graded. Never today's grade projected backward.
    grade_at_trade: Literal["S", "A", "B", "C", "D", "F", None] | str | None
    # graded: grade_at_trade holds the recorded grade. ungraded: the trader was recorded without a grade at that
    # moment. unknown: no record covers the moment, which is every trade before 2026-09-19T23:00Z and a trade that
    # ...
    grade_at_trade_status: Literal["graded", "ungraded", "unknown"] | str


class LargeTradeTrader(_LargeTradeTraderRequired, total=False):
    username: str
    # The trader's grade today, on every row however old. For what the grade was when the trade happened, read
    # grade_at_trade.
    grade: Literal["S", "A", "B", "C", "D", "F"] | str


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
    # Polymarket exchange contract that emitted the execution: `ctf_v2` the CTF Exchange v2, `neg_risk_ctf_v2` the
    # Neg Risk CTF Exchange v2, `exchange_v3` ExchangeV3, which settles Polymarket Protocol V2 binary and neg-risk
    # ...
    exchange_family: Literal["ctf_v2", "neg_risk_ctf_v2", "exchange_v3"] | str
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
    # Provider platform. Always polymarket.
    platform: Literal["polymarket"]


class LeaderboardEntry(_LeaderboardEntryRequired, total=False):
    username: str
    grade: Literal["S", "A", "B", "C", "D", "F"] | str
    # Hot-streak tier (trailing-7d cross-sectional percentile); a separate axis from the all-time grade. Omitted
    # when there is no recent activity.
    streak_tier: Literal["hot", "rising", "neutral", "cooling", "cold"] | str
    score: float
    # Deprecated since 2026-10-27 and never sent. It was Polymarket's all-time leaderboard P&L, which covered
    # every Polymarket market of the wallet, and wallet figures cover sports and esports markets only (#29971).
    # Read ...
    pnl: float
    # Deprecated since 2026-10-27 and never sent. It was native Polymarket realized P&L over every Polymarket
    # market of the wallet, and wallet figures cover sports and esports markets only (#29971). Read
    # in_scope.realized_pnl.
    realized_pnl: float
    # Deprecated since 2026-10-27 and never sent. It was the neg-risk conversion correction to the wallet-wide
    # realized_pnl (#29971). Its sports and esports part is inside in_scope.realized_pnl.
    pnl_correction: PnlCorrection
    # Deprecated since 2026-10-27 and never sent. It was full-history USD cash volume over every Polymarket market
    # of the wallet, and wallet figures cover sports and esports markets only (#29971).
    volume: float
    # Sports and esports markets on the wallet's record, the same count as in_scope.markets. Since 2026-10-27
    # (#29971); before, it counted every Polymarket market. Sent exactly when in_scope is.
    markets_traded: int
    # The wallet's sports and esports win rate, in_scope.win_rate rounded to four places. Since 2026-10-27
    # (#29971); before, it covered every Polymarket market. ?category= decides WHICH wallets are listed (the
    # wallet must be ...
    win_rate: float
    # Additive (#27859): the wallet's sports and esports record, the same object as GET /api/v1/trader/{address}
    # pnl.in_scope, as of the leaderboard's last refresh. The 0xinsider leaderboard page shows and sorts by ...
    in_scope: TraderPnlInScope
    # Additive (#32270): the wallet's edge over the price paid on its sports and esports markets, the figures the
    # 0xinsider leaderboard page's Edge column states for the row. sort=edge orders by price_edge.edge. Omitted
    # when ...
    price_edge: LeaderboardPriceEdge
    # Observed trading style identifier. New rows use two_sided, category_focused, high_activity, diversified,
    # mixed, or unclassified, counted over the wallet's sports and esports markets only. Historical identifiers
    # remain ...
    strategy_type: str
    # When the wallet last traded: its most recent recorded trade, as of the leaderboard row's last refresh, which
    # re-reads it hourly, so a new trade can take about an hour to show. It agrees with the activity filter: every
    # ...
    last_active: str


class _LeaderboardPriceEdgeRequired(TypedDict):
    # Settled sports and esports markets of $20 or more at a known entry price that the edge is measured over.
    markets: int
    # Share of those markets whose bought side won, 0-1.
    hit_rate: float
    # Mean entry price paid, 0-1.
    avg_price: float
    # hit_rate minus avg_price, full precision. The value sort=edge orders by.
    edge: float
    # Whether the edge ranks. ranked: at least 30 such markets, and the share of the decided ones that made money
    # at settlement within 10 points of the win rate over the same markets. too_few_markets: fewer than 30. ...
    status: Literal["ranked", "too_few_markets", "sample_mismatch"] | str


class LeaderboardPriceEdge(_LeaderboardPriceEdgeRequired, total=False):
    """Edge over the price paid (#32270): how often the side a wallet bought won, minus the average price
    it paid, over its settled sports and esports markets of $20 or more at a known entry price.
    Probabilities throughout: edge 0.12 is 12 percentage points. A wallet buying at 99 cents that wins
    every market has an edge of about 0.01. A market bought on both sides counts by its shares: the
    winning side's share of the shares bought is its hit, the cost over those shares its price."""
    # Why the leaderboard does not rank a ranked edge. record_incomplete: the wallet's stored sports and esports
    # record shows more profit than Polymarket reports for it, so some losing markets are likely missing. Omitted
    # when ...
    hold: Literal["record_incomplete"]


class GetPickOfTheDayResponse(TypedDict):
    object: Literal["pick_of_the_day"]
    data: PickOfTheDay | PickOfTheDayNoEntitledPicks
    meta: ResponseMeta


class _PickOfTheDayRequired(TypedDict):
    # Full success containing entitled proof-readable picks.
    state: Literal["full"]
    # Deprecated (#24157): always null. No replacement lineage was ever recorded in this field; the key stays so
    # existing V1 clients keep parsing. Identify a pick by pick_id.
    supersedes_pick_id: str | None


class PickOfTheDay(_PickOfTheDayRequired, total=False):
    # The pick's local publication date (YYYY-MM-DD). Format: date.
    pick_date: str
    # Deprecated compatibility daily release slot; use pick_id for identity and publication_order for scheduling.
    pick_rank: int
    # Published picks for this product day in the returned display order. Use pick_id for identity.
    picks: list[PickOfTheDay]
    # Number of items in `picks`: the proof-readable picks. Picks held in `proof_pending_picks` are not counted.
    pick_count: int
    # Rank-ordered entitled selections that have not released. Every row retains release_at and kickoff;
    # unauthorized scheduled ranks appear only in identity-free locked_picks.
    scheduled_picks: list[ScheduledPickSlot]
    # Human-readable matchup (e.g. "Portugal vs. Uzbekistan").
    matchup: str
    # Recorded canonical sport category. Prefer display_category for the public competition label.
    category: str
    # Frozen public presentation category. Tennis uses the provider-verified ATP or WTA tour, including Wimbledon
    # and doubles; unknown tours retain Tennis. Every men's and women's cricket competition uses Cricket. Other
    # ...
    display_category: str
    # Provider platform. Always polymarket.
    platform: Literal["polymarket"]
    # The pick's stored release instant. Use the returned timestamp; published_at records when publication
    # occurred. Format: date-time.
    release_at: str
    # True only before the pick's stored release instant (a pre-release embargo flag); effectively always false on
    # a served, already-published pick. To detect that the backed game has kicked off, use `game_started`.
    is_locked: bool
    # True once the backed game's kickoff has passed (kickoff <= now). When true the snapshotted pre-game price is
    # no longer actionable. Absent for a legacy pick with no stored kickoff (treat as not-started).
    game_started: bool
    # Whether the backed game is over according to the cached live scoreboard, read at serve time. Tells a
    # finished game from one still in play before `outcome` settles. Omitted when the pick has no event slug or no
    # ...
    game_ended: bool
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
    # S/A wallet count on the backed side in the public V1 compatibility projection.
    sharp_wallet_count: int
    # Deprecated spelling of sharp_wallet_count with the same value.
    smart_wallet_count: int
    # Best recorded S/A grade in the public V1 compatibility projection.
    top_grade: str
    # Recorded sharp-money magnitude in USD when available.
    sharp_usd: float
    # Deprecated spelling of sharp_usd with the same value.
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
    # Recorded sharp-money share as a 0..1 fraction when available. This is not a winning probability.
    sharp_pct: float
    # Recorded market-implied probability as a 0..1 fraction when available.
    market_pct: float
    # Optional recorded specialist facts on a full response. These describe the trader, not the pick's win
    # probability. Omitted when no recorded specialist is available.
    qualifying_expert: PickOfTheDayQualifyingExpert
    # Public V1 S/A wallet count on the backed side, equal to sharp_wallet_count.
    traders: int
    # Recorded aggregate backed-side position value in USD when available, not a live balance or entry cost. The
    # display_holders roster can include additional wallets; use the returned aggregate rather than summing that
    # ...
    backed_sharp_usd: float
    # Bounded S/A holder display projection from the recorded snapshot. Historical rows retain their recorded
    # display shape.
    holders: list[PickHolder]
    # Optional recorded holder roster in display order, with lead_backer first when present. Preserve the returned
    # order. The roster can include wallets outside the recorded count and aggregate fields; do not derive ...
    display_holders: list[PickHolder]
    # S/A holder count for the public V1 compatibility projection. display_holders can include additional grades.
    holder_count: int
    # Display-ready explanation of the recorded pick. Render the returned text rather than reconstructing it from
    # holder counts or grades.
    thesis: str
    # Canonical web market URL.
    market_url: str
    # Where this pick's outbound Polymarket link lands: Polymarket's own redirect answer for
    # `/event/<event_slug>`, carrying the referral tag. Omitted until that redirect has been resolved; link to the
    # event page instead when ...
    polymarket_url: str
    # The canonical /event game-page slug (one neutral page per game); omitted when the game has no neutral event
    # page.
    event_slug: str
    # Backend-resolved /event destination slug for the source market. Omitted outside full responses; null is an
    # authoritative no-link decision.
    event_link_slug: str | None
    # Provider-first sports context for the pick's market (team logos, league branding, live score). Full-state
    # only; omitted when the pick is not a team-sports market.
    sports_context: PickSportsContext
    # Risk disclaimer shown with every pick.
    disclaimer: str
    # Entitled published picks whose holder proof is unreadable, ordered by rank. Unauthorized ranks appear only
    # in locked_picks and cannot trigger proof warming. Read retry_at for the next read.
    proof_pending_picks: list[ProofPendingPickSlot]
    # Optional full-response entry authorization. Missing or expired authorization cannot authorize an automated
    # entry.
    entry_authorization: PotdEntryAuthorization
    # Unauthorized unresolved published or scheduled ranks. Contains no game, provider identity, price, or
    # identifying clock. Pro may upgrade to Max to open these ranks.
    locked_picks: list[PickOfTheDayLockedPicksItem]
    # Actionable status, including Upgrade to Max when only locked ranks are published.
    message: str
    # Stable pick row identity as decimal text. Never use a quality rank as identity.
    pick_id: str
    # Compatibility release slot. No quality claim; historic scheduling order is retained.
    publication_order: int
    # Viewer-independent free selection designation. New rows store it explicitly; historic null storage uses the
    # original free slot.
    is_free_selection: bool
    # Optional full-only lead wallet publication facts. Omitted on legacy picks or when the recorded evidence is
    # unavailable.
    lead_backer: PickLeadBacker


class ScheduledPickSlot(TypedDict):
    """An entitled same-day slot with a future scheduled release: stable identity and backend-owned
    release/kickoff instants. It leaves this list at its release instant; an unpublished slot is never a
    delayed recommendation. No matchup, category, platform, side, price, or holder fields appear before
    release. Unauthorized scheduled ranks appear only in locked_picks."""
    # Deprecated compatibility daily release slot; use pick_id for identity and publication_order for scheduling.
    pick_rank: int
    # The slot's future release instant. Remove this preview at that instant and read again for published picks; a
    # scheduled slot does not guarantee publication. Format: date-time.
    release_at: str
    # The backed game's current kickoff instant. Format: date-time.
    kickoff: str
    # Stable pick row identity as decimal text. Never use a quality rank as identity.
    pick_id: str
    # Compatibility release slot. No quality claim; historic scheduling order is retained.
    publication_order: int
    # Viewer-independent free selection designation. New rows store it explicitly; historic null storage uses the
    # original free slot.
    is_free_selection: bool
    # Deprecated (#24157): always null. No replacement lineage was ever recorded in this field; the key stays so
    # existing V1 clients keep parsing. Identify a pick by pick_id.
    supersedes_pick_id: str | None


class _PickOfTheDayQualifyingExpertRequired(TypedDict):
    # Trader wallet address.
    address: str
    # Provider display name, or null for an unnamed wallet.
    name: str | None
    # Recorded trader grade. Public V1 preserves its S/A compatibility projection.
    grade: str | None
    # The canonical sport bucket the win rate was measured over (for example Basketball). Can be BROADER than the
    # pick's display_category, which names an exact league such as NBA — label the rate with this field, never
    # with ...
    canonical_category: str
    # Share of the trader’s settled markets in canonical_category (closed by selling out, or resolved) with
    # positive realized P&L, as a 0..1 fraction. Null when not measured. This is a trader statistic, not the
    # pick’s ...
    win_rate: float | None
    # Number of settled markets behind win_rate; null when not measured.
    n_resolved: int | None
    # Recorded Polymarket position value on the backed outcome, in USD. It can change after this snapshot.
    position_usd: float
    # Timestamp of the recorded trader statistics. Format: date-time.
    stats_computed_at: str


class PickOfTheDayQualifyingExpert(_PickOfTheDayQualifyingExpertRequired, total=False):
    """Optional recorded specialist facts on a full response. These describe the trader, not the pick's win
    probability. Omitted when no recorded specialist is available."""
    # Recorded position value on the other outcome of this market, in USD. Omitted when not recorded; zero is a
    # measured value.
    opposite_position_usd: float


class _PickHolderRequired(TypedDict):
    address: str
    name: str | None
    # All-time trader grade (S, A, B, C, D, F).
    grade: str | None
    # The wallet's most recent recorded trade time, stamped at serve time from its current trader record rather
    # than frozen with the pick. Always sent; null when no trade time is recorded. Format: date-time.
    last_traded_at: str | None
    shares: float


class PickHolder(_PickHolderRequired, total=False):
    # 0xinsider profile path segment this wallet links to: `@<username>` when that username resolves to this
    # wallet alone, otherwise the lowercase wallet. Percent-encode the part after `@` and append to ...
    profile_segment: str
    # USD entry value of this wallet's position: `shares` times the pick's frozen `backed_price`. An entry
    # valuation, never a live balance or the provider's current value. Omitted when the holder snapshot has no
    # valid price.
    entry_value_usd: float
    # This wallet's win rate in the pick's canonical category bucket (the pick's `category` field, e.g. Basketball
    # -- label the rate with it, never with the narrower `display_category` league, except when ...
    category_win_rate: float
    # The two counts `category_win_rate` is the ratio of, read from the same row: `wins / decided` equals the
    # rate. Counts every settled Polymarket market the wallet traded (it closed its position by selling out, or
    # the ...
    category_win_record: PickHolderCategoryWinRecord
    # The wallet's average entry price in the pick's canonical category, as a 0..1 fraction of $1 (0.98 is 98
    # cents). Its sample is the wallet's markets in that category that resolved to a winning side, of $20 or more
    # where ...
    category_avg_price: float
    # Where `category_win_rate` and `category_win_record` were measured, by the same name the pick's
    # `display_category` uses for it: for an esports pick the game (`LoL`, `CS2`, `Dota 2`, `Valorant`, `Call of
    # Duty`, `Honor of ...
    category_win_rate_game: str
    # Why `category_win_rate` is present or absent on a `display_holders` entry: `measured` (rate present),
    # `not_enough_data` (the wallet is below the settled-market floor of 5 in the category), or `unavailable` (the
    # ...
    category_win_rate_status: Literal["measured", "not_enough_data", "unavailable", "untracked"] | str
    # Whole days since this wallet's first trade, rounded down (3.6 days reads 3), so it changes once a day, not
    # on every request, and the pick's ETag holds between requests. Stamped at serve time from the wallet's
    # current ...
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


class PickHolderCategoryWinRecord(TypedDict):
    """The two counts `category_win_rate` is the ratio of, read from the same row: `wins / decided` equals
    the rate. Counts every settled Polymarket market the wallet traded (it closed its position by
    selling out, or the market resolved) in the pick's canonical category (or in its game or league,
    when `category_win_rate_game` is present), at any position size; the counts are rebuilt daily.
    Present only with `category_win_rate_status` = `measured`; absent otherwise and on payloads
    predating the field."""
    # Settled markets in the category that this wallet closed with a profit.
    wins: int
    # Settled markets in the category that this wallet closed with a profit or a loss. A market resolved at zero
    # realized P&L is in neither count.
    decided: int


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
    score. Each team `logo` is a registered club crest or national flag as a same-origin path where one
    exists, and provider artwork otherwise."""
    # Provider-owned event taxonomy from Gamma eventMetadata, joined in league · serie · tournament order with
    # blanks and case-insensitive duplicates removed. A tennis qualifying match ends in ", Qualification",
    # including an ...
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
    # The name to show for this team or competitor, the same on every surface (e.g. "UCF Knights", "Oklahoma City
    # Thunder", "Portugal"). `label` keeps the market outcome's own spelling.
    full_name: str | None
    # Provider team identifier (Polymarket /teams id).
    provider_id: int | None
    # Team crest or flag URL. Official NFL (32), WNBA (15), NBA (30), NHL (32), and MLB (30) club crests use same-
    # origin relative paths (`/api/sports/team-logos/{league}/{abbr}.svg?v=<content hash>`); resolve relative URLs
    # ...
    logo: str | None
    # True when artwork measurements show that the team mark needs a light plate on a dark background. Vendored
    # crest verdicts are tied to the exact asset bytes; provider artwork is measured by the teams sync. Always
    # sent; ...
    logo_mark_dark: bool
    # Team brand color as a hex string (provider-owned).
    color: str | None
    # Win-loss record as a display string (e.g. "12-4").
    record: str | None
    # Live or final score as a display string when the game is in play or settled.
    score: str | None
    # True when artwork measurements show that the team mark disappears on a white background and needs a dark
    # plate there: the light-background twin of logo_mark_dark. Vendored crest verdicts are tied to the exact
    # asset ...
    logo_mark_light: bool
    # True when logo_mark_dark and logo_mark_light are both measurements of this exact logo URL, so their false
    # means the mark is legible on that background. Every vendored crest is measured; a provider logo is measured
    # once ...
    logo_mark_measured: bool


class PickSportsTeam(_PickSportsTeamRequired, total=False):
    """A single sports team or competitor in a Pick of the Day market's sports context. Identity and score
    fields are provider-owned and nullable. The structured score fields (`sets`, `format`, `sets_won`)
    and the tennis fields (`headshot`, `headshot_revision`, `tour`) are backend-owned and are OMITTED
    rather than null when they do not apply, so a consumer must treat an absent key and a null the same
    way."""
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
    # Optional monotonic photo revision for this tennis player, independent of the sports score revision. Legacy
    # stored photos start at zero. Successful new or changed image bytes advance it; source checks and attribution
    # ...
    headshot_revision: int
    # Optional latest retrieved ATP/WTA singles rank for this player. Absent for unranked, ambiguous, doubles,
    # expired, or unavailable identities. This is not rank at match time.
    ranking: TennisRanking


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


class TennisRanking(TypedDict):
    """A provider-reported ATP/WTA singles rank with independent retrieval and expiry clocks. API-Tennis
    provides no ranking publication date. Retrieval time does not establish when the tour published the
    ranking."""
    # Provider-reported singles rank.
    rank: int
    # The player ranking tour.
    tour: Literal["atp", "wta"] | str
    # The standings provider.
    source: Literal["api_tennis"]
    # Successful snapshot retrieval time in UTC, not ranking publication date. Format: date-time.
    observed_at: str
    # UTC deadline after which clients must hide this rank, including when an older game or pick response remains
    # cached. Format: date-time.
    expires_at: str


class _ProofPendingPickSlotRequired(TypedDict):
    # Deprecated compatibility daily release slot; use pick_id for identity and publication_order for scheduling.
    pick_rank: int
    # The pick's stored release instant. Format: date-time.
    release_at: str
    # Recommended next read: 30 seconds ahead while pre-game proof is warming, one hour ahead for a post-kickoff
    # pending legacy row that only settlement can make readable. Schedule against it instead of polling. Format:
    # ...
    retry_at: str
    # Stable pick row identity as decimal text. Never use a quality rank as identity.
    pick_id: str
    # Compatibility release slot. No quality claim; historic scheduling order is retained.
    publication_order: int
    # Viewer-independent free selection designation. New rows store it explicitly; historic null storage uses the
    # original free slot.
    is_free_selection: bool
    # Deprecated (#24157): always null. No replacement lineage was ever recorded in this field; the key stays so
    # existing V1 clients keep parsing. Identify a pick by pick_id.
    supersedes_pick_id: str | None


class ProofPendingPickSlot(_ProofPendingPickSlotRequired, total=False):
    """One PUBLISHED same-day pick whose holder proof is not readable yet: its stable slot rank, the
    release and kickoff instants, and the instant before which a retry cannot succeed. Every item in
    `picks` carries its full required shape, so a pick that cannot meet it is listed here instead of
    being served with missing fields or a synthetic zero."""
    # The backed game's frozen kickoff instant; absent for a legacy row without one. Format: date-time.
    kickoff: str


class PotdEntryAuthorization(TypedDict):
    """Returned entry permission bound to the named market, token and outcome. Honor the immutable
    max_entry_price and expires_at, and quote a current executable book for the actual stake. The
    submitted order price must remain within the returned limit; fills may be lower. Fees are separate,
    and this grant does not guarantee liquidity, execution or positive expected value."""
    version: Literal[1]
    # Format: uuid.
    authorization_id: str
    # Identifier for the policy recorded with this authorization. It does not replace the returned max_entry_price
    # or expires_at. Existing grants retain their recorded values.
    policy_version: Literal[7, 8] | int
    condition_id: str
    token_id: str
    outcome_index: Literal[0, 1] | int
    # Canonical sport bucket, not display_category.
    category: str
    # Exact provider parent event ID, or provider event ID when no parent exists.
    canonical_event_id: str
    # Maximum authorized order price as an exact decimal string, excluding fees. Quote a current executable book
    # for the actual stake and keep the submitted order price at or below this bound. Actual fills may be lower;
    # this ...
    max_entry_price: str
    # Selected-token best ask from the recorded reference book at issuance. This is a reference quote, not the
    # authorized order-price limit; use max_entry_price for that limit.
    reference_best_ask: str
    reference_book_hash: str
    # Format: date-time.
    reference_book_at: str
    # Format: date-time.
    issued_at: str
    # Authorization expiry timestamp. Existing grants do not extend; an expired authorization cannot authorize a
    # new automated entry. Format: date-time.
    expires_at: str


class PickOfTheDayLockedPicksItem(TypedDict):
    pick_rank: int
    required_tier: Literal["max"]


class _PickLeadBackerRequired(TypedDict):
    # Lead trader wallet address.
    address: str
    # Recorded provider display name.
    name: str | None
    # Trader grade recorded at publication.
    grade: str
    # Canonical sport of the recorded directional history.
    category: str
    # Provider-reported position value on the backed outcome at publication, in USD. It is the gross value on that
    # outcome and does not subtract shares the wallet held on the other outcome; see net_position_usd. It is not
    # the ...
    position_usd: float
    # Start time of the provider position fetch used at publication. This conservative observation clock precedes
    # completion; the position is not a live balance. Format: date-time.
    position_observed_at: str
    # Distinct directional events in the recorded category history.
    directional_event_count: int
    # Events with strictly positive native terminal P&L in the same frozen category sample as
    # directional_event_count, realized_pnl_usd and roi. Multiple market positions in one event contribute one
    # combined event result. ...
    profitable_event_count: int
    # Realized P&L over the recorded directional category sample, in USD. Excludes open positions and later
    # changes.
    realized_pnl_usd: float
    # Recorded entry basis of that directional sample, in USD; not a claim of complete trading costs or fees.
    entry_basis_usd: float
    # Realized P&L divided by recorded entry basis, as a fraction: 0.10 means 10%. This is a wallet statistic, not
    # a pick win probability.
    roi: float
    # Peak-to-trough realized P&L drawdown after each event result in the recorded sample, in USD. Excludes
    # intragame, unrealized, and account equity drawdown.
    max_realized_drawdown_usd: float
    # Timestamp when the directional history evidence was recorded, separate from the provider position snapshot
    # clock. Format: date-time.
    recorded_at: str


class PickLeadBacker(_PickLeadBackerRequired, total=False):
    """Recorded lead wallet facts on a full response when available. Position and category history are
    frozen at publication; they are not live balances or pick win probabilities."""
    # Net value of the lead's position toward the backed outcome at publication, in USD: shares held on the backed
    # outcome minus shares held on the other outcome of the same market, valued at the backed outcome's provider
    # ...
    net_position_usd: float


class _PickOfTheDayNoEntitledPicksRequired(TypedDict):
    # Only locked ranks are published for this account.
    state: Literal["none"]
    # Current product date in America/New_York (YYYY-MM-DD). Format: date.
    pick_date: str
    # Empty: no entitled proof-readable picks are returned.
    picks: list[PickOfTheDay]
    # Zero entitled proof-readable picks.
    pick_count: Literal[0]
    # Unauthorized unresolved published or scheduled ranks. Contains no game, provider identity, price, or
    # identifying clock. Pro may upgrade to Max to open these ranks.
    locked_picks: list[PickOfTheDayLockedPicksItem]
    # Actionable status, including Upgrade to Max when only locked ranks are published.
    message: str
    # Deprecated (#24157): always null. No replacement lineage was ever recorded in this field; the key stays so
    # existing V1 clients keep parsing. Identify a pick by pick_id.
    supersedes_pick_id: str | None


class PickOfTheDayNoEntitledPicks(_PickOfTheDayNoEntitledPicksRequired, total=False):
    """A successful current-day entitlement response when only unauthorized ranks have published. It
    carries an empty pick set, identity-free locked ranks and an upgrade message. Selection IDs, game
    identity, prices and unauthorized clocks are absent. Any scheduled or proof-pending rows are
    entitled rows."""
    # Rank-ordered entitled selections that have not released. Every row retains release_at and kickoff;
    # unauthorized scheduled ranks appear only in identity-free locked_picks.
    scheduled_picks: list[ScheduledPickSlot]


class GetPickOfTheDayArchiveResponse(TypedDict):
    object: Literal["pick_of_the_day_archive"]
    data: PickOfTheDayArchive
    meta: ResponseMeta


class PickOfTheDayArchive(TypedDict):
    # Published Pick of the Day selections that have not been withdrawn, newest first by pick_date and then
    # pick_rank within each product day. Withdrawn rows stay excluded after settlement.
    picks: list[PickOfTheDayArchiveEntry]
    # One entry per product day that has a published pick included in the archive, newest first, in the same order
    # as picks. Each carries that day's net units, accumulated in the same backend pass and behind the same ...
    days: list[PickOfTheDayArchiveDay]
    hit_rate: PickOfTheDayHitRate


class _PickOfTheDayArchiveEntryRequired(TypedDict):
    # The pick's local publication date (YYYY-MM-DD). Format: date.
    pick_date: str
    # Deprecated compatibility daily release slot; use pick_id for identity and publication_order for scheduling.
    pick_rank: int
    # Settlement outcome of the backed side; 'pending' until the market resolves.
    outcome: Literal["pending", "win", "loss", "void"] | str
    # Stable pick row identity as decimal text. Never use a quality rank as identity.
    pick_id: str
    # Compatibility release slot. No quality claim; historic scheduling order is retained.
    publication_order: int
    # Viewer-independent free selection designation. New rows store it explicitly; historic null storage uses the
    # original free slot.
    is_free_selection: bool
    # Deprecated (#24157): always null. No replacement lineage was ever recorded in this field; the key stays so
    # existing V1 clients keep parsing. Identify a pick by pick_id.
    supersedes_pick_id: str | None


class PickOfTheDayArchiveEntry(_PickOfTheDayArchiveEntryRequired, total=False):
    # When this selection was published, as RFC3339 UTC. Use this instant for publication feeds and timelines;
    # pick_date is the America/New_York product day, not a publication timestamp. Absent only for historical rows
    # whose ...
    published_at: str
    # Human-readable matchup (e.g. "Portugal vs. Uzbekistan").
    matchup: str
    # Frozen canonical sport bucket (e.g. "Basketball", "MMA", or "Soccer"). Existing semantics are unchanged;
    # presentation consumers should prefer display_category when present.
    category: str
    # Frozen public presentation category. Tennis uses the provider-verified ATP or WTA tour, including Wimbledon
    # and doubles; unknown tours retain Tennis. Every men's and women's cricket competition uses Cricket. Other
    # ...
    display_category: str
    # Provider (Polymarket Gamma) market thumbnail URL (markets.image); omitted (not null) when the market has no
    # image. Public regardless of the backed-side gate, so present for pending rows too.
    image_url: str
    # The backed side's outcome label. Omitted for a still-pending pick when the request is not from an
    # authenticated Pro key.
    pick_outcome_label: str
    # Recorded top grade on the backed side in the public V1 compatibility projection. Omitted when unavailable.
    # Historical values remain recorded snapshots.
    top_grade: str
    # Pre-formatted settlement status for display: "Win" / "Loss" / "Void" / "Pending" -- the outcome enum above
    # as a label, from the same formatter the pick payload's outcome_display uses. Convenience only; outcome is
    # the ...
    outcome_display: str
    # When outcome was LAST written to a settled value (RFC3339 UTC), the same instant the commitment ledger
    # publishes. It moves with a corrected market re-mapping an already-settled pick. Omitted (not null) for a
    # pending ...
    resolved_at: str
    # The flat stake this row was valued at, in USD: 1000 since 2026-09-22 (100 before). Every row of the record
    # is valued at the current stake, including picks published before the change. Present exactly when return_usd
    # is.
    stake_usd: float
    # Gross return of stake_usd on this resolved pick: a win returns stake_usd / backed_price and a loss returns
    # 0. A loss always returns 0 (the whole stake is lost regardless of price). The operand is published beside it
    # as ...
    return_usd: float
    # The same return on a literal $100 (a win returns 100 / backed_price, a loss 0), kept for compatibility: the
    # field predates stake_usd and its name promises the $100 basis. Present exactly when return_usd is.
    return_per_100: float
    # Pre-formatted return_usd as USD with cents: "$2,000.00". Present exactly when return_usd is -- it is
    # formatted from that already-gated value -- so it is omitted for a still-pending pick, a void, an unpriced
    # win, and any ...
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
    # The account or paid tier needed to open this unresolved rank.
    required_tier: Literal["account", "insider", "max"] | str
    # True for an unauthorized unresolved row. Game identity, category, image, publication clock and all backed
    # facts are omitted.
    backed_side_locked: bool


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
    # Picks on the day that resolved void: the market settled with no winner, or the game was suspended or
    # postponed and not completed within 72 hours of kickoff. A void is neither a win nor a loss and is not
    # staked, so it ...
    void: int
    # Picks on the day not yet resolved. A day whose picks are all pending is a real 0-0 day with pending > 0, not
    # a missing record.
    pending: int


class PickOfTheDayArchiveDay(_PickOfTheDayArchiveDayRequired, total=False):
    # Net units over the day's visible, valued, staked (win or loss) picks: the same population staked_usd runs
    # over. Omitted when the day has not scored -- every pick still pending or void, or a price-gated current row
    # -- ...
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
    # The flat stake every money figure here assumes, in USD: 1000 since 2026-09-22 (100 before). Always present.
    stake_usd: float
    # Cumulative profit (USD) of a stake_usd-per-pick strategy over visible valued settled picks: a priced win
    # pays stake_usd/backed_price - stake_usd, every visible loss pays -stake_usd independent of price. A void is
    # not ...
    net_profit_usd: float
    # Total staked (USD) = stake_usd * count of visible valued settled picks: every visible loss and every priced
    # win. Voids, unpriced wins and current non-Insider rows whose price is gated are excluded.
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
    # Cumulative track-record series, one point per decided (win/loss) pick in ascending pick_date order (pending
    # and void picks add no point). A non-valued decided row carries cumulative profit forward while advancing hit
    # ...
    series: list[PickOfTheDayHitRateSeriesItem]


class PickOfTheDayHitRate(_PickOfTheDayHitRateRequired, total=False):
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


class PickOfTheDayHitRateSeriesItem(TypedDict):
    # The decided pick's publish date (YYYY-MM-DD). Format: date.
    date: str
    # Running cumulative stake_usd-per-pick profit (USD) through this pick; valued losses and priced wins are
    # booked, while a non-valued decided row carries profit forward unchanged.
    net_profit_usd: float
    # Running rolling hit rate (wins / decided * 100, to 1 decimal) through this pick.
    hit_rate_pct: float


class GetPickOfTheDayStatsResponse(TypedDict):
    object: Literal["pick_of_the_day_stats"]
    data: PickOfTheDayStats
    meta: ResponseMeta


class PickOfTheDayStats(TypedDict):
    categories: list[PickOfTheDayStatsCategoriesItem]
    days: list[PickOfTheDayStatsDaysItem]
    hit_rate: PickOfTheDayHitRate
    market_expectations: PickOfTheDayStatsMarketExpectations
    market_types: list[PickOfTheDayStatsCategoriesItem]
    months: list[PickOfTheDayStatsCategoriesItem]
    outcome_stats: PickOfTheDayStatsOutcomeStats
    price_bands: list[PickOfTheDayStatsCategoriesItem]
    records: PickOfTheDayStatsRecords
    sports: list[PickOfTheDayStatsCategoriesItem]
    streaks: PickOfTheDayStatsStreaks
    tiers: list[PickOfTheDayStatsCategoriesItem]
    total_sides: list[PickOfTheDayStatsCategoriesItem]
    voids: list[PickOfTheDayStatsVoidsItem]


class _PickOfTheDayStatsCategoriesItemRequired(TypedDict):
    clv_measured: int
    key: str
    label: str
    losses: int
    pending: int
    picks: int
    priced_decided: int
    settled: int
    small_sample: bool
    staked_usd: float
    void: int
    wins: int


class PickOfTheDayStatsCategoriesItem(_PickOfTheDayStatsCategoriesItemRequired, total=False):
    canonical_category: str
    clv_avg_display: str
    clv_avg_pct: float
    clv_avg_pp: float
    clv_avg_pp_display: str
    edge_display: str
    edge_pp: float
    net_profit_display: str
    net_profit_usd: float
    priced_in_display: str
    priced_in_pct: float
    roi_display: str
    roi_pct: float
    unit_score: float
    unit_score_display: str
    win_rate_display: str
    win_rate_pct: float


class _PickOfTheDayStatsDaysItemRequired(TypedDict):
    # Format: date.
    date: str
    losses: int
    pending: int
    picks: int
    void: int
    wins: int


class PickOfTheDayStatsDaysItem(_PickOfTheDayStatsDaysItemRequired, total=False):
    net_profit_display: str
    net_profit_usd: float
    sweep: Literal["win", "loss"] | str
    unit_score: float
    unit_score_display: str


class PickOfTheDayStatsMarketExpectations(TypedDict):
    # Format: date.
    as_of_date: str
    price_basis: str
    timezone: str
    windows: list[PickOfTheDayStatsMarketExpectationsWindowsItem]


class PickOfTheDayStatsMarketExpectationsWindowsItem(TypedDict):
    clv_avg_display: str | None
    clv_avg_pct: float | None
    clv_avg_pp: float | None
    clv_avg_pp_display: str | None
    clv_measured: int
    clv_missing: int
    expected_wins: float | None
    expected_wins_display: str | None
    # Format: date.
    from_date: str | None
    key: str
    label: str
    numeric_unavailable: bool
    priced_decided: int
    # Format: date.
    through_date: str
    units: float | None
    units_display: str | None
    units_z: float | None
    units_z_display: str | None
    unpriced_decided: int
    wins: int
    wins_z: float | None
    wins_z_display: str | None


class PickOfTheDayStatsOutcomeStats(TypedDict):
    concentration: PickOfTheDayStatsOutcomeStatsConcentration
    drawdown: PickOfTheDayStatsOutcomeStatsDrawdown
    profit_factor: PickOfTheDayStatsOutcomeStatsProfitFactor
    rolling: list[PickOfTheDayStatsOutcomeStatsRollingItem]


class PickOfTheDayStatsOutcomeStatsConcentration(TypedDict):
    positive_wins: int
    remaining_valued_decided: int
    removed_wins: int
    roi_without_top_wins_display: str | None
    roi_without_top_wins_pct: float | None
    target_wins: int
    top_wins_share_display: str | None
    top_wins_share_pct: float | None
    valued_decided: int


class PickOfTheDayStatsOutcomeStatsDrawdown(TypedDict):
    completed_days: int
    current_days_below_peak: int | None
    current_drawdown_display: str | None
    current_drawdown_units: float | None
    days_below_peak: int | None
    excluded_days: int
    # Format: date.
    from_date: str | None
    longest_days_below_peak: int | None
    longest_recovery_days: int | None
    max_drawdown_display: str | None
    max_drawdown_units: float | None
    # Format: date.
    peak_date: str | None
    peak_net_profit_usd: float | None
    # Format: date.
    through_date: str | None


class PickOfTheDayStatsOutcomeStatsProfitFactor(TypedDict):
    display: str | None
    gross_loss_usd: float | None
    gross_profit_usd: float | None
    state: Literal["empty", "measured", "no_losses", "numeric_unavailable"] | str
    value: float | None
    valued_decided: int


class PickOfTheDayStatsOutcomeStatsRollingItem(TypedDict):
    # Format: date.
    from_date: str | None
    losses: int
    roi_display: str | None
    roi_pct: float | None
    # Format: date.
    through_date: str | None
    units: float | None
    units_display: str | None
    valued_decided: int
    win_rate_display: str | None
    win_rate_pct: float | None
    window_size: int
    wins: int


class _PickOfTheDayStatsRecordsRequired(TypedDict):
    sweeps: PickOfTheDayStatsRecordsSweeps


class PickOfTheDayStatsRecords(_PickOfTheDayStatsRecordsRequired, total=False):
    best_day: PickOfTheDayStatsRecordsBestDay
    biggest_win: PickOfTheDayStatsRecordsBiggestWin
    longest_losing_day_streak: PickOfTheDayStatsRecordsLongestLosingDayStreak
    longest_winning_day_streak: PickOfTheDayStatsRecordsLongestLosingDayStreak
    winning_days: PickOfTheDayStatsRecordsWinningDays
    worst_day: PickOfTheDayStatsRecordsBestDay


class PickOfTheDayStatsRecordsBestDay(TypedDict):
    # Format: date.
    date: str
    date_display: str
    losses: int
    net_profit_display: str
    net_profit_usd: float
    picks: int
    wins: int


class PickOfTheDayStatsRecordsBiggestWin(TypedDict):
    category: str
    # Format: date.
    date: str
    date_display: str
    matchup: str
    net_profit_display: str
    net_profit_usd: float


class PickOfTheDayStatsRecordsLongestLosingDayStreak(TypedDict):
    days: int
    # Format: date.
    end_date: str
    net_profit_display: str
    net_profit_usd: float
    range_display: str
    # Format: date.
    start_date: str


class _PickOfTheDayStatsRecordsSweepsRequired(TypedDict):
    clean_sweeps: int
    min_decided: int
    wipeouts: int


class PickOfTheDayStatsRecordsSweeps(_PickOfTheDayStatsRecordsSweepsRequired, total=False):
    latest_clean_sweep: PickOfTheDayStatsRecordsSweepsLatestCleanSweep
    latest_wipeout: PickOfTheDayStatsRecordsSweepsLatestCleanSweep


class PickOfTheDayStatsRecordsSweepsLatestCleanSweep(TypedDict):
    # Format: date.
    date: str
    date_display: str
    losses: int
    wins: int


class PickOfTheDayStatsRecordsWinningDays(TypedDict):
    flat: int
    losing: int
    settled: int
    winning: int
    winning_pct: float
    winning_pct_display: str


class _PickOfTheDayStatsStreaksRequired(TypedDict):
    longest_loss: int
    longest_win: int


class PickOfTheDayStatsStreaks(_PickOfTheDayStatsStreaksRequired, total=False):
    current: int
    current_day: int
    current_day_display: str
    current_display: str


class _PickOfTheDayStatsVoidsItemRequired(TypedDict):
    # Format: date.
    pick_date: str
    pick_id: str
    pick_rank: int


class PickOfTheDayStatsVoidsItem(_PickOfTheDayStatsVoidsItemRequired, total=False):
    backed_price: float
    backed_side: str
    category: str
    matchup: str


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
    """An unresolved published pick. Carries only date, rank, hash, algorithm, seal instant and permalink.
    Kickoff and game identity are withheld; seal time remains public commitment provenance."""
    state: Literal["sealed"]
    # ET product day the pick belongs to (YYYY-MM-DD). Format: date.
    pick_date: str
    # Deprecated compatibility daily release slot; use pick_id for identity and publication_order for scheduling.
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
    # The pick's stable public page, `https://0xinsider.com/pick-of-the-day/picks/{pick_id}`. Format: uri.
    permalink: str
    # Stable pick row identity as decimal text. Never use a quality rank as identity.
    pick_id: str
    # Compatibility release slot. No quality claim; historic scheduling order is retained.
    publication_order: int
    # Viewer-independent free selection designation. New rows store it explicitly; historic null storage uses the
    # original free slot.
    is_free_selection: bool
    # Deprecated (#24157): always null. No replacement lineage was ever recorded in this field; the key stays so
    # existing V1 clients keep parsing. Identify a pick by pick_id.
    supersedes_pick_id: str | None
    # Explicit proof provenance: 1 retains historic eight-field canonical JSON; 2 binds stable pick_id and version
    # without pick_rank.
    commitment_version: Literal[1, 2] | int


class PickOfTheDayLedgerOpenedEntry(TypedDict):
    """A settled pick whose commitment is open: the nonce plus the exact payload the hash was taken over.
    Concatenate the payload bytes as received with the decoded nonce and sha256 them to reproduce
    commitment_hash."""
    state: Literal["opened"]
    # ET product day the pick belongs to (YYYY-MM-DD). Format: date.
    pick_date: str
    # Deprecated compatibility daily release slot; use pick_id for identity and publication_order for scheduling.
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
    # Why the site withdrew this pick from its track record, or null when the pick counts.
    # provider_game_cancelled: Polymarket marked the game Cancelled while the pick was pending.
    # published_after_kickoff: the pick was ...
    withdrawal_reason: Literal["provider_game_cancelled", "published_after_kickoff", None] | str | None
    # Frozen matchup, for a reader.
    matchup: str
    # Frozen canonical sport bucket (for example Basketball or MMA), not the exact public league identity; the
    # archive owns that.
    category: str
    # The pick's stable public page, `https://0xinsider.com/pick-of-the-day/picks/{pick_id}`. Format: uri.
    permalink: str
    # Stable pick row identity as decimal text. Never use a quality rank as identity.
    pick_id: str
    # Compatibility release slot. No quality claim; historic scheduling order is retained.
    publication_order: int
    # Viewer-independent free selection designation. New rows store it explicitly; historic null storage uses the
    # original free slot.
    is_free_selection: bool
    # Deprecated (#24157): always null. No replacement lineage was ever recorded in this field; the key stays so
    # existing V1 clients keep parsing. Identify a pick by pick_id.
    supersedes_pick_id: str | None
    # Explicit proof provenance: 1 retains historic eight-field canonical JSON; 2 binds stable pick_id and version
    # without pick_rank.
    commitment_version: Literal[1, 2] | int


class PickOfTheDayCommitmentPayloadV1(TypedDict):
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
    # Provider platform. Always polymarket.
    platform: Literal["polymarket"]


class PickOfTheDayCommitmentPayloadV2(TypedDict):
    """Version 2 rank-free canonical payload: sorted nine keys, unchanged string escaping, exact decimal
    text and whole-second UTC kickoff. pick_id is decimal text; version is JSON integer 2."""
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
    # Provider platform. Always polymarket.
    platform: Literal["polymarket"]
    # Stable pick row identity as decimal text. Never use a quality rank as identity.
    pick_id: str
    version: Literal[2]


# Select using the entry commitment_version, never implicit payload shape. All historic v1 hashes remain
# unchanged.
PickOfTheDayCommitmentPayload = Union[PickOfTheDayCommitmentPayloadV1, PickOfTheDayCommitmentPayloadV2]


class _PickOfTheDayLedgerUncommittedEntryRequired(TypedDict):
    state: Literal["uncommitted"]
    # ET product day the pick belongs to (YYYY-MM-DD). Format: date.
    pick_date: str
    # Deprecated compatibility daily release slot; use pick_id for identity and publication_order for scheduling.
    pick_rank: int
    # Always true: this pick has no commitment and never will.
    pre_commitment: Literal[True]
    # How the pick settled, or pending.
    outcome: Literal["pending", "win", "loss", "void"] | str
    # When outcome was LAST written to a settled value, or null when that instant is unknown. It moves with a
    # corrected market re-mapping an already-settled pick, while commitment_hash stays untouched -- which is how a
    # mirror ...
    resolved_at: str | None
    # The pick's market, side and price once it has settled; null while it is pending, and null for a settled pick
    # whose stored row lacks one of these columns. Not hashed: nothing was committed over these values, which is
    # ...
    payload: PickOfTheDayUncommittedPayload | None
    # The pick's stable public page, `https://0xinsider.com/pick-of-the-day/picks/{pick_id}`. Format: uri.
    permalink: str
    # Stable pick row identity as decimal text. Never use a quality rank as identity.
    pick_id: str
    # Compatibility release slot. No quality claim; historic scheduling order is retained.
    publication_order: int
    # Viewer-independent free selection designation. New rows store it explicitly; historic null storage uses the
    # original free slot.
    is_free_selection: bool
    # Deprecated (#24157): always null. No replacement lineage was ever recorded in this field; the key stays so
    # existing V1 clients keep parsing. Identify a pick by pick_id.
    supersedes_pick_id: str | None


class PickOfTheDayLedgerUncommittedEntry(_PickOfTheDayLedgerUncommittedEntryRequired, total=False):
    """A pick without a commitment, retained so the record cannot omit unprovable entries. Unresolved
    entries omit game identity; once resolved, matchup, category and payload become public. Existing
    opened canonical payload bytes and hashes are unchanged."""
    # Omitted while the pick is pending; once it settles, why the site withdrew it from its track record, or null
    # when the pick counts. provider_game_cancelled: Polymarket marked the game Cancelled while the pick was
    # pending. ...
    withdrawal_reason: Literal["provider_game_cancelled", "published_after_kickoff", None] | str | None
    # Frozen matchup, for a reader.
    matchup: str
    # Frozen canonical sport bucket (for example Basketball or MMA), not the exact public league identity; the
    # archive owns that.
    category: str


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
    # Provider platform. Always polymarket.
    platform: Literal["polymarket"]


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
    # api.polymarket.com/v2/leaderboard?time_period=week|month&sort_by=PNL). This is the ranking axis and the rows
    # are ...
    trending_pnl_usd: float
    window_markets_traded: int
    # Distinct in-window UTC trade days from our trades (0 if the winner is not in our DB).
    window_trade_days: int
    # The wallet's sports and esports realized P&L on each UTC day of the window, ascending, one point a day,
    # pnl_usd 0 on a day with none: the same in-scope realized day series the trader P&L endpoint serves. Empty
    # while ...
    daily_pnl_series: list[TrendingWalletDailyPnlSeriesItem]
    # `ready` when daily_pnl_series is served; an all-zero one is a wallet with no sports or esports P&L in the
    # window. `pending` when the wallet's sports and esports record does not carry its daily series yet, or the
    # wallet ...
    daily_pnl_series_status: Literal["ready", "pending"] | str


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
    # All-time trader grade; a separate axis from streak_tier. Led by realized profit on sports and esports
    # markets (the money actually banked, about 95 percent of the grade; since 2026-10-22, the sports and esports
    # share of ...
    grade: Literal["S", "A", "B", "C", "D", "F"] | str
    # Hot-streak tier (trailing-7d cross-sectional percentile). Omitted when there is no recent activity.
    streak_tier: Literal["hot", "rising", "neutral", "cooling", "cold"] | str
    # Additive (#29971): the wallet's sports and esports realized P&L in USD, the same figure as
    # pnl.in_scope.realized_pnl on GET /api/v1/trader/{address} and the 0xinsider profile's Sports P&L, as of the
    # board's last ...
    in_scope_realized_pnl: float
    # Deprecated since 2026-10-27 and never sent. It was Polymarket's net total P&L over every Polymarket market
    # of the wallet, and wallet figures cover sports and esports markets only (#29971). Read
    # in_scope_realized_pnl.
    all_time_pnl_usd: float
    # Deprecated since 2026-10-27 and never sent. It was the neg-risk conversion correction to the wallet-wide
    # all_time_pnl_usd (#29971). Its sports and esports part is inside in_scope_realized_pnl.
    pnl_correction: PnlCorrection
    all_time_score: float
    # Format: date-time.
    last_synced: str


class TrendingWalletDailyPnlSeriesItem(TypedDict):
    # Format: date.
    date: str
    pnl_usd: float


class ListLeaderboardLeaguesResponse(TypedDict):
    object: Literal["leaderboard_leagues"]
    data: LeaderboardLeagues
    meta: ResponseMeta


class LeaderboardLeagues(TypedDict):
    leagues: list[LeaderboardLeaguesLeaguesItem]
    min_ranked: int
    min_resolved: int
    # Format: date-time.
    refreshed_at: str


class LeaderboardLeaguesLeaguesItem(TypedDict):
    category: str
    name: str
    ranked_traders: int
    slug: str
    sport: str
    total_traders: int


class GetSportLeaderboardResponse(TypedDict):
    object: Literal["sport_leaderboard"]
    data: SportLeaderboard
    meta: ResponseMeta


class SportLeaderboard(TypedDict):
    # Format: date-time.
    as_of: str | None
    category: str | None
    edge_average: float | None
    league: SportLeaderboardLeague1 | None
    limit: int
    min_resolved: int
    rows: list[SportLeaderboardRowsItem]
    sort: Literal["edge", "pnl", "win_rate"] | str
    sport: str
    total_traders: int
    volume_scope: Literal["sports_and_esports"]


class SportLeaderboardLeague1(TypedDict):
    name: str
    ranked_traders: int
    slug: str


class SportLeaderboardRowsItem(TypedDict):
    address: str
    cost: float | None
    edge_hold: Literal["category_loss", "record_incomplete"] | str | None
    edge_skill: float | None
    grade: Literal["S", "A", "B", "C", "D", "F"] | str | None
    id: str
    # Format: date-time.
    last_category_trade_at: str | None
    losses: int
    n_resolved: int
    platform: Literal["polymarket"]
    pnl: float | None
    price_edge: SportLeaderboardRowsItemPriceEdge1 | None
    rank: int
    roi: float | None
    username: str | None
    volume: float | None
    win_rate: float | None
    win_rate_wilson_lb: float | None
    wins: int


class SportLeaderboardRowsItemPriceEdge1(TypedDict):
    avg_price: float
    edge: float
    edge_lower: float
    hit_rate: float
    markets: int
    status: Literal["ranked", "too_few_markets", "sample_mismatch"] | str


class _ListCategoryLeadersResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[CategoryLeader]
    has_more: bool
    meta: ResponseMeta


class ListCategoryLeadersResponse(_ListCategoryLeadersResponseRequired, total=False):
    next_cursor: str
    # Number of rows returned: up to three per category.
    total: int


class CategoryLeader(TypedDict):
    address: str
    # Format: date-time.
    as_of: str
    category: str
    edge_lower_bound: float | None
    grade: Literal["S", "A", "B", "C", "D", "F"] | str | None
    id: str
    independent_events: int
    n_resolved: int | None
    platform: Literal["polymarket"]
    pnl: float | None
    rank: int
    unresolved_events: int
    username: str | None
    win_rate: float | None


class _GetCategoryLeaderboardResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[CategoryLeader]
    has_more: bool
    meta: ResponseMeta


class GetCategoryLeaderboardResponse(_GetCategoryLeaderboardResponseRequired, total=False):
    next_cursor: str
    # Wallets in the category whose edge lower bound is above zero, Wallets in the full walk across every page:
    # those in the category, under this request's active_within and min_events, whose edge lower bound is above
    # zero. ...
    total: int


class _SearchMarketsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[MarketSearchResult]
    has_more: bool
    meta: ResponseMeta


class SearchMarketsResponse(_SearchMarketsResponseRequired, total=False):
    next_cursor: str
    # Total matching rows when the read model exposes a count; the key is absent when it does not.
    total: int


class _MarketSearchResultRequired(TypedDict):
    id: str
    condition_id: str
    title: str
    slug: str | None
    category: str | None
    # Provider platform. Always polymarket, or null when the row carries no stored value.
    platform: Literal["polymarket", None] | str | None
    # closed once Polymarket has closed trading or the market has resolved; active otherwise. The same rule labels
    # a market on markets/search, markets/explore and market/{condition_id}/snapshot.
    status: Literal["active", "closed"] | str


class MarketSearchResult(_MarketSearchResultRequired, total=False):
    event_slug: str


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
    # Provider platform. Always polymarket, or null when the row carries no stored value.
    platform: Literal["polymarket", None] | str | None
    category: str | None
    # Markets in the event cluster, ranked by volume with condition_id as the tie-breaker. The selected
    # representative is retained within the 12-market cap.
    markets: list[ExploreMarket]
    # The volume of the group's highest-volume market, which is markets[0]: the same figure as that market's
    # volume, Polymarket's cumulative taker volume in shares rather than cash. Null when unavailable.
    rep_volume: float | None
    # Canonical key since #16304; rep_whales is its deprecated spelling, emitted beside it with the same value
    # until its sunset on 2027-02-01 (#29352).
    rep_large_trades: int | None
    # Deprecated spelling of rep_large_trades, emitted beside it with the same value. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read rep_large_trades.
    rep_whales: int | None


class ExploreMarket(TypedDict):
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
    # Provider platform. Always polymarket, or null when the row carries no stored value.
    platform: Literal["polymarket", None] | str | None
    # closed once Polymarket has closed trading or the market has resolved; active otherwise. The same rule labels
    # a market on markets/search, markets/explore and market/{condition_id}/snapshot.
    status: Literal["active", "closed"] | str
    # Polymarket's traded-volume figure for the market, as last stored: cumulative taker volume in shares, each
    # counted at its $1 settlement value, not the cash that changed hands (100 shares bought at $0.40 add 100, not
    # 40). ...
    volume: float | None
    liquidity: float | None
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value until its sunset on 2027-02-01 (#29352).
    large_trade_count: int | None
    # Deprecated spelling of large_trade_count, emitted beside it with the same value. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read large_trade_count.
    whale_trade_count: int | None
    # Canonical key since #16304; whale_distinct_wallets is its deprecated spelling, emitted beside it with the
    # same value until its sunset on 2027-02-01 (#29352).
    large_trade_distinct_wallets: int | None
    # Deprecated spelling of large_trade_distinct_wallets, emitted beside it with the same value. Sunset
    # 2027-02-01 (#29352): removed from V1 on that date; read large_trade_distinct_wallets.
    whale_distinct_wallets: int | None
    # Canonical key since #16304; whale_total_usd is its deprecated spelling, emitted beside it with the same
    # value until its sunset on 2027-02-01 (#29352).
    large_trade_total_usd: float | None
    # Deprecated spelling of large_trade_total_usd, emitted beside it with the same value. Sunset 2027-02-01
    # (#29352): removed from V1 on that date; read large_trade_total_usd.
    whale_total_usd: float | None
    # Canonical key since #16304; whale_last_trade_at is its deprecated spelling, emitted beside it with the same
    # value until its sunset on 2027-02-01 (#29352). Format: date-time.
    large_trade_last_at: str | None
    # Deprecated spelling of large_trade_last_at, emitted beside it with the same value. Sunset 2027-02-01
    # (#29352): removed from V1 on that date; read large_trade_last_at. Format: date-time.
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
    # The outcome graded money leans toward RELATIVE TO THE PRICE: named only when the graded money's share of a
    # side diverges from that side's price-implied share by at least 10 points, with at least $500 on the leaning
    # side ...
    smart_label: str | None
    # When the oldest stored smart-money wallet behind this split (smart_score, smart_count and smart_label) last
    # finished syncing. Graded wallets sync on different schedules, so this is often hours or days ago. Some
    # holdings ...
    sharp_money_as_of: str | None
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
    score_components: ExploreMarketScoreComponents
    freshness: ExploreMarketFreshness


class ExploreMarketScoreComponents(TypedDict):
    volume_signal: float | None
    # Canonical key since #16304; whale_signal is its deprecated spelling, emitted beside it with the same value
    # until its sunset on 2027-02-01 (#29352).
    large_trade_signal: float | None
    # Deprecated spelling of large_trade_signal, emitted beside it with the same value. Sunset 2027-02-01
    # (#29352): removed from V1 on that date; read large_trade_signal.
    whale_signal: float | None
    liquidity_signal: float | None
    recency_signal: float | None
    # Canonical key since #16308; smart_money_signal is its deprecated spelling, emitted beside it with the same
    # value until its sunset on 2027-02-01 (#29352).
    sharp_money_signal: float | None
    # Deprecated spelling of sharp_money_signal; emitted beside it with the same value. Sunset 2027-02-01
    # (#29352): removed from V1 on that date; read sharp_money_signal.
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
    # Deprecated alias of sharp_money; byte-identical. Sunset 2027-02-01 (#29352): removed from V1 on that date;
    # read sharp_money.
    smart_money: SmartMoneyFlowMarketSmartMoney
    timeframe: str


class SmartMoneyFlowMarketMarket(TypedDict):
    id: str
    condition_id: str
    title: str | None
    slug: str | None
    category: str | None
    # Provider platform. Always polymarket, or null when the row carries no stored value.
    platform: Literal["polymarket", None] | str | None


class SmartMoneyFlowMarketSharpMoney(TypedDict):
    """Sharp-money flow aggregate for the market (canonical; smart_money is a deprecated byte-identical
    alias)."""
    net_flow_usd: float
    direction: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the net-flow direction outcome; null
    # when unavailable (e.g. unsynced markets).
    token_id: str | None
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value until its sunset on 2027-02-01 (#29352).
    large_trade_count: int
    # Deprecated spelling of large_trade_count, emitted beside it with the same value. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read large_trade_count.
    whale_trade_count: int
    buy_volume_usd: float
    sell_volume_usd: float


class SmartMoneyFlowMarketSmartMoney(TypedDict):
    """Deprecated alias of sharp_money; byte-identical. Sunset 2027-02-01 (#29352): removed from V1 on that
    date; read sharp_money."""
    net_flow_usd: float
    direction: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the net-flow direction outcome; null
    # when unavailable (e.g. unsynced markets).
    token_id: str | None
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value until its sunset on 2027-02-01 (#29352).
    large_trade_count: int
    # Deprecated spelling of large_trade_count, emitted beside it with the same value. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read large_trade_count.
    whale_trade_count: int
    buy_volume_usd: float
    sell_volume_usd: float


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
    # with the same value until its sunset on 2027-02-01 (#29352).
    large_trades: PlatformCapabilityStatus
    # Deprecated spelling of large_trades, emitted beside it with the same value. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read large_trades.
    whale_signal: PlatformCapabilityStatus
    suspicious_trades: PlatformCapabilityStatus
    # Deprecated spelling of suspicious_trades, emitted beside it with the same value. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read suspicious_trades.
    insider_radar: PlatformCapabilityStatus
    market_snapshot: PlatformCapabilityStatus


# Every capability the API serves reports supported. The field names a per-capability status so a client can
# branch on coverage; no other value is emitted.
PlatformCapabilityStatus = Literal["supported"]


class _GetMarketHoldersResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[MarketHolder]
    has_more: bool
    # Holders matching the request's `outcome` and `min_grade` filters across every page.
    total: int
    market: MarketHoldersMarket
    scan: MarketHoldersScan
    totals: MarketHoldersTotals
    meta: ResponseMeta


class GetMarketHoldersResponse(_GetMarketHoldersResponseRequired, total=False):
    # Absent on the last page.
    next_cursor: str


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
    grade: Literal["S", "A", "B", None] | str | None
    # Shares held on `side`, from the complete provider scan.
    shares: float
    # Polymarket's own currentValue for this leg, in USD. Null when the snapshot predates the value map.
    current_value_usd: float | None
    # The wallet's last recorded trade anywhere, null when unknown. Format: date-time.
    last_traded_at: str | None
    # Why `category_win_rate` is present or absent: `measured` (rate present), `not_enough_data` (under the floor
    # of 5 decided markets in the category), or `unavailable` (the market has no canonical category, or the read
    # ...
    category_win_rate_status: Literal["measured", "not_enough_data", "unavailable", "untracked"] | str


class MarketHolder(_MarketHolderRequired, total=False):
    # Shares on the other outcome when the wallet holds both. Absent when the wallet is one-sided.
    other_outcome_shares: float
    # This wallet's win rate in the market's canonical category (`market.category`): the share of its settled
    # markets in that category (it closed its position by selling out, or the market resolved) whose realized P&L
    # closed ...
    category_win_rate: float
    # The two counts `category_win_rate` is the ratio of, from the same row: `wins / decided` equals the rate.
    # Every settled Polymarket market the wallet traded (it closed its position by selling out, or the market
    # resolved) ...
    category_win_record: MarketHolderCategoryWinRecord
    # The wallet's average entry price in the market's canonical category, as a 0..1 fraction of $1 (0.98 is 98
    # cents). Its sample is the wallet's markets in that category that resolved to a winning side, of $20 or more
    # where ...
    category_avg_price: float
    # Where `category_win_rate` and `category_win_record` were measured: for an esports market the game (`LoL`,
    # `CS2`, `Dota 2`, `Valorant`, `Call of Duty`, `Honor of Kings`, `Mobile Legends: Bang Bang`, `Overwatch`,
    # `Rainbow ...
    category_win_rate_game: str
    category_evidence: HolderCategoryEvidence
    # Whole days since this wallet's first trade, rounded down (3.6 days reads 3), so it changes once a day, not
    # on every request. The five badge fields are present together, only for a wallet that draws at least one
    # badge.
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
    rate. Every settled Polymarket market the wallet traded (it closed its position by selling out, or
    the market resolved) in the market's canonical category, at any position size, rebuilt daily.
    Present only with `category_win_rate_status` = `measured`."""
    # Settled markets in the category that this wallet closed with a profit.
    wins: int
    # Settled markets in the category that this wallet closed with a profit or a loss. A market resolved at zero
    # realized P&L is in neither count.
    decided: int


class _HolderCategoryEvidenceRequired(TypedDict):
    status: Literal["live", "insufficient", "stale", "unknown", "degraded"] | str


class HolderCategoryEvidence(_HolderCategoryEvidenceRequired, total=False):
    """Current category evidence, independent of the global grade. Pick of the Day stamps only the served
    display roster; frozen entry snapshots remain unchanged."""
    canonical_category: str
    skill: CategorySkillV2


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
    # yes_usd split by grade: where the S, A and B money on YES sits.
    yes_grade_usd: MarketHoldersSideGradeUsd
    # no_usd split by grade: where the S, A and B money on NO sits.
    no_grade_usd: MarketHoldersSideGradeUsd


class MarketHoldersSideGrades(TypedDict):
    s: int
    a: int
    b: int


class MarketHoldersSideGradeUsd(TypedDict):
    """Polymarket currentValue in USD per grade on one side, over the same wallets as that side's usd
    total. Each value is rounded to the cent after summing, so s + a + b can differ from the side total
    by up to 2 cents."""
    # USD held by S-grade wallets netting this side.
    s: float
    # USD held by A-grade wallets netting this side.
    a: float
    # USD held by B-grade wallets netting this side.
    b: float


class GetMarketTopHoldersResponse(TypedDict):
    object: Literal["market_top_holders"]
    data: MarketTopHolders
    meta: ResponseMeta


class _MarketTopHoldersRequired(TypedDict):
    market: MarketHoldersMarket
    # The largest YES holders, by shares, up to `limit`.
    yes: list[MarketTopHolder]
    # The largest NO holders, by shares, up to `limit`.
    no: list[MarketTopHolder]
    totals: MarketTopHoldersTotals
    # `unavailable` when the wallet record read failed: `in_scope_realized_pnl`, `in_scope_volume` and
    # `strategy_type` are then null for every row because they were not read, not because they are unknown.
    profiles_status: Literal["available", "unavailable"] | str
    # `true` when this is the market's last sample, served after its 30 s window while a refresh runs;
    # `positions_as_of` is then at most 300 s old. Read again in a few seconds for the refreshed sample. Always
    # `false` on a ...
    source_stale: bool


class MarketTopHolders(_MarketTopHoldersRequired, total=False):
    # When the daily pass behind the rows' category win records began. Absent when the market has no category or
    # the read answered no row. Format: date-time.
    category_records_as_of: str
    # When this holder sample was built. Format: date-time.
    computed_at: str
    # When Polymarket's holder board behind this sample was fetched: up to 120 s before `computed_at` on an open
    # market. Absent on a resolved market, whose sample reads no live board, and when the fetch stamp could not be
    # ...
    positions_as_of: str


class _MarketTopHolderRequired(TypedDict):
    # 1-based position on this outcome, by shares.
    rank: int
    # `trd_`-prefixed trader id, accepted by `GET /api/v1/trader/{address}`.
    trader_id: str
    # Lowercased proxy wallet.
    address: str
    # The wallet's display name; null when it shows none.
    name: str | None
    # All-time trader grade, S to F. Null for a wallet 0xinsider has not graded: this route lists every holder
    # whatever its grade.
    grade: Literal["S", "A", "B", "C", "D", "F", None] | str | None
    # Shares held on this outcome.
    shares: float
    # Polymarket's current value of this position, in USD. Null when the provider served none.
    current_value_usd: float | None
    # Average price paid for the shares still held, as a 0..1 fraction of $1. Null when the provider served none.
    avg_entry_price: float | None
    # Polymarket's realized P&L of this position (sells and redemptions), in USD. Null when the provider served no
    # economics for the row.
    position_realized_pnl: float | None
    # Polymarket's mark-to-market P&L of the shares still held, in USD. On a resolved market the mark is the
    # settlement price.
    position_unrealized_pnl: float | None
    # `position_realized_pnl` plus `position_unrealized_pnl`, in USD.
    position_total_pnl: float | None
    # The wallet's realized P&L on sports and esports markets, in USD, the figure on its 0xinsider profile. Null
    # until 0xinsider has computed the record, never 0 in its place, and null for every row when `profiles_status`
    # is ...
    in_scope_realized_pnl: float | None
    # The wallet's volume traded on sports and esports markets, in USD. Null under the same rule as
    # `in_scope_realized_pnl`.
    in_scope_volume: float | None
    # The wallet's stored trading-style label (see Wallet trading styles); null when it has none.
    strategy_type: str | None
    # The wallet's last recorded trade anywhere, null when unknown. Format: date-time.
    last_traded_at: str | None


class MarketTopHolder(_MarketTopHolderRequired, total=False):
    # Shares on the other outcome when the wallet holds both; the wallet is then listed on both sides. Absent when
    # it is one-sided.
    other_outcome_shares: float
    # This wallet's win rate in the market's canonical category (`market.category`): the share of its settled
    # markets in that category (it closed its position by selling out, or the market resolved) whose realized P&L
    # closed ...
    category_win_rate: float
    # The two counts `category_win_rate` is the ratio of, from the same row: `wins / decided` equals the rate.
    # Every settled Polymarket market the wallet traded (it closed its position by selling out, or the market
    # resolved) ...
    category_win_record: MarketHolderCategoryWinRecord
    # The wallet's average entry price in the market's canonical category, as a 0..1 fraction of $1 (0.98 is 98
    # cents). Its sample is the wallet's markets in that category that resolved to a winning side, of $20 or more
    # where ...
    category_avg_price: float
    # Where `category_win_rate` and `category_win_record` were measured: for an esports market the game (`LoL`,
    # `CS2`, `Dota 2`, `Valorant`, `Call of Duty`, `Honor of Kings`, `Mobile Legends: Bang Bang`, `Overwatch`,
    # `Rainbow ...
    category_win_rate_game: str
    # Why `category_win_rate` is present or absent: `measured` (rate present), `not_enough_data` (the wallet is on
    # file and under the floor of 5 decided markets in the category), `untracked` (0xinsider has no record of the
    # ...
    category_win_rate_status: Literal["measured", "not_enough_data", "unavailable", "untracked"] | str
    # Whole days since this wallet's first trade, rounded down (3.6 days reads 3), so it changes once a day, not
    # on every request. The five badge fields are present together, only for a wallet that draws at least one
    # badge.
    wallet_age_days: float | None
    # True when the wallet's first trade was under 30 days ago.
    is_new_wallet: bool
    # Distinct markets the wallet has traded.
    markets_traded: int | None
    # True when the wallet is flagged as automated.
    is_bot: bool
    # The wallet's X handle without the @, when linked.
    x_username: str | None


class MarketTopHoldersTotals(TypedDict):
    # Holders in the YES sample, before `limit`. Equal to `sample_cap` means that many or more.
    yes_count: int
    # Holders in the NO sample, before `limit`.
    no_count: int
    # Shares summed over the YES sample.
    yes_shares: float
    # Shares summed over the NO sample.
    no_shares: float
    # The most holders the sample keeps per outcome (100).
    sample_cap: int


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
    # Deprecated alias of sharp_money; byte-identical. Sunset 2027-02-01 (#29352): removed from V1 on that date;
    # read sharp_money.
    smart_money: MarketFlowSmartMoney
    timeframe: str


class MarketFlowMarket(TypedDict):
    id: str
    condition_id: str
    title: str
    slug: str | None
    category: str | None
    # Provider platform. Always polymarket, or null when the row carries no stored value.
    platform: Literal["polymarket", None] | str | None


class MarketFlowSharpMoney(TypedDict):
    """Outcome-aware flow from all tracked whale trades in the window, without a grade filter. BUY YES and
    SELL NO add net exposure; BUY NO and SELL YES subtract it. Gross buy/sell volumes count both
    outcomes. Top positions are separately graded. Direction uses unrounded net: negative is NO,
    otherwise YES; the zero tie-break is not conviction. Canonical; smart_money is a deprecated byte-
    identical alias."""
    net_flow_usd: float
    direction: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the net-flow direction outcome; null
    # when unavailable (e.g. unsynced markets).
    token_id: str | None
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value until its sunset on 2027-02-01 (#29352).
    large_trade_count: int
    # Deprecated spelling of large_trade_count, emitted beside it with the same value. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read large_trade_count.
    whale_trade_count: int
    buy_volume_usd: float
    sell_volume_usd: float
    top_positions: list[MarketFlowSharpMoneyTopPositionsItem]
    # Age of the oldest stored position snapshot behind top_positions: the minimum wallet sync clock over the
    # positions this body publishes. The roster is a stored read rather than a live one, and graded wallets sit on
    # ...
    oldest_snapshot_as_of: str | None


class MarketFlowSharpMoneyTopPositionsItem(TypedDict):
    id: str
    address: str
    username: str | None
    grade: Literal["S", "A", "B", "C", "D", "F", None] | str | None
    side: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for this outcome; null when unavailable
    # (e.g. unsynced markets).
    token_id: str | None
    size_usd: float


class MarketFlowSmartMoney(TypedDict):
    """Deprecated alias of sharp_money; byte-identical. Sunset 2027-02-01 (#29352): removed from V1 on that
    date; read sharp_money."""
    net_flow_usd: float
    direction: Literal["YES", "NO"] | str
    # The Polymarket CLOB token id (ERC1155 asset id, decimal string) for the net-flow direction outcome; null
    # when unavailable (e.g. unsynced markets).
    token_id: str | None
    # Canonical key since #16304 (Polymarket's noun is large trade); whale_trade_count is its deprecated spelling,
    # emitted beside it with the same value until its sunset on 2027-02-01 (#29352).
    large_trade_count: int
    # Deprecated spelling of large_trade_count, emitted beside it with the same value. Sunset 2027-02-01 (#29352):
    # removed from V1 on that date; read large_trade_count.
    whale_trade_count: int
    buy_volume_usd: float
    sell_volume_usd: float
    top_positions: list[MarketFlowSharpMoneyTopPositionsItem]
    # Age of the oldest stored position snapshot behind top_positions: the minimum wallet sync clock over the
    # positions this body publishes. The roster is a stored read rather than a live one, and graded wallets sit on
    # ...
    oldest_snapshot_as_of: str | None


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
    # closed once Polymarket has closed trading or the market has resolved; active otherwise. The same rule labels
    # a market on markets/search, markets/explore and market/{condition_id}/snapshot.
    status: Literal["active", "closed"] | str
    description: str | None
    image: str | None
    # Polymarket series slug from the canonical identity row, null when unavailable. A sports series identifies a
    # league and must not be used as a per-matchup grouping key.
    series_slug: str | None
    # Always null. Deprecated (#24169): 0xinsider has never stored a value for this field. The key stays on the
    # wire until its sunset on 2027-02-01 (#29352), when it is removed; do not read it.
    market_type: str | None
    # Always null. Deprecated (#24169): 0xinsider stores no value for this field on a Polymarket market. The key
    # stays on the wire until its sunset on 2027-02-01 (#29352), when it is removed; do not read it. market.status
    # and ...
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
    # The outcome's display price, the probability Polymarket shows for it: the midpoint of the cached top of book
    # when the spread is at most 0.10, otherwise the token's last trade price. Omitted when neither is known, ...
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
    # Polymarket's traded-volume figure for the market, as last stored: cumulative taker volume in shares, each
    # counted at its $1 settlement value, not the cash that changed hands (100 shares bought at $0.40 add 100, not
    # 40). ...
    volume_usd: float | None
    liquidity_usd: float | None
    # Polymarket's taker volume over the 24 hours before volume_24h_as_of, in shares, each counted at its $1
    # settlement value, not the cash that changed hands (100 shares bought at $0.40 add 100, not 40). The name
    # ends in ...
    volume_24h_usd: float | None
    # When 0xinsider read volume_24h_usd from Polymarket; the figure covers the 24 hours before this time. Null
    # exactly when volume_24h_usd is null. Format: date-time.
    volume_24h_as_of: str | None
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
    live_score: MarketSnapshotSportsLiveScore
    reason: str


class MarketSnapshotSportsLiveScore(TypedDict, total=False):
    """Live-score period and elapsed may be omitted when unavailable (older responses use null). A score
    entry may omit full_name when it equals team; fall back to team. Distinct aliases and score
    admission markers are preserved. For live esports, scores[].map_score retains an available pair
    through an update omitting both sides only within the same live map, series format and series
    totals. Map changes and final state follow current provider updates; absent detail remains
    unavailable. Optional tennis_points supplies independently sourced current-game points and serving
    side; absence means ..."""
    tennis_points: TennisPoints


class _TennisPointsRequired(TypedDict):
    source: Literal["api_tennis"]
    # API-Tennis match ID. This is not a Polymarket market or event ID.
    match_key: int
    # API-Tennis player IDs in the same first/second order as live_score.scores. These are not Polymarket team
    # IDs.
    player_keys: list[int]
    # Current-game point values in first/second order. Read strings, including A for advantage and numeric
    # tiebreak points. Missing points are not zero.
    points: list[str]
    # Orders only the tennis_points group for the same match. Never compare this with live_score.source_revision.
    source_revision: int
    # When 0xinsider observed these API-Tennis facts. This is not a timestamp from the court. Format: date-time.
    observed_at: str
    # Stop displaying the point group at this instant, even if the enclosing score remains fresh. The group
    # expires 30 seconds after observed_at. Format: date-time.
    expires_at: str
    # Current set number. Display points only while this matches the enclosing scoreboard, unless set_games is
    # present.
    set_number: int
    # Current-set games in first/second order. Display points only while these match the enclosing scoreboard,
    # unless set_games is present.
    games: list[int]


class TennisPoints(_TennisPointsRequired, total=False):
    """Optional current-game tennis facts from API-Tennis, aligned with live_score.scores display order.
    These facts have their own revision and expiry; Polymarket remains the source of sets, match status,
    period, and the outer live-score revision. New observations require corroborated identity, current
    set/games, and live state. Where Polymarket publishes no score (tennis doubles, whose live_score
    reads one 0-0 set throughout), the group binds on both pairs' names, the tour, the date and API-
    Tennis's live flag, and carries set_games, the provider's set score for the match. Cached responses
    and ..."""
    # The serving player in live_score.scores display order. Omitted when API-Tennis does not identify the server.
    serving_side: Literal["first", "second"] | str
    # API-Tennis games in every listed set, first set first, each in first/second order. Present only when
    # Polymarket publishes no score for the match (tennis doubles): display these as the set score, and discard
    # the group ...
    set_games: list[list[int]]


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
    """Provider-first bucketed OHLC price candles for a market's outcome tokens, derived from our stored
    copy of the Polymarket CLOB prices-history series (covers open and resolved markets)."""
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


class GetMarketWalletsInOutResponse(TypedDict):
    object: Literal["market_wallets_in_out"]
    data: MarketWalletsInOut
    meta: ResponseMeta


class MarketWalletsInOut(TypedDict):
    """One market's net buyers and net sellers over a 24h or 7d window, as the market page's wallets in/out
    panel shows a Pro viewer."""
    # The market's raw provider condition id.
    condition_id: str
    # The window the nets are summed over: 24h or 7d.
    window: str
    # The window's inclusive start; null only when the bounds are unknown. Format: date-time.
    window_start: str | None
    # The window's inclusive end, the read's clock; null only when the bounds are unknown. Format: date-time.
    window_end: str | None
    # Totals over every wallet that traded the market in the window, not only the listed 50.
    summary: MarketWalletsInOutSummary
    # Wallets whose net is positive, largest first, at most 25.
    net_buyers: list[MarketWalletsInOutNetBuyersItem]
    # Wallets whose net is negative, most negative first, at most 25.
    net_sellers: list[MarketWalletsInOutNetBuyersItem]


class MarketWalletsInOutSummary(TypedDict):
    """Totals over every wallet that traded the market in the window, not only the listed 50."""
    # Wallets with a positive net in the window.
    wallets_in: int
    # Wallets with a negative net in the window.
    wallets_out: int
    # The sum of every wallet's net, in USD. A fully rotated wallet nets zero and is on neither side.
    net_usd: float


class MarketWalletsInOutNetBuyersItem(TypedDict):
    """One wallet's net in the window."""
    # Lowercase proxy wallet.
    address: str
    # The name the site shows: the 0xinsider username, else the shortened address.
    display_name: str
    # Today's grade; null for an ungraded or untracked wallet.
    grade: Literal["S", "A", "B", "C", "D", "F"] | str | None
    # Buys minus sells in the window, both outcomes, in USD: the matched notional, fees excluded.
    net_usd: float
    # Fills in the window.
    trades: int
    # The wallet's newest trade on any market, at or before window_end; null when unknown. Format: date-time.
    last_traded_at: str | None


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
    # When this read assembled the catalog; with status ended, cancelled or postponed, when it read the stored
    # records. Per-source vintage is on each game's freshness. Format: date-time.
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
    # Whether this read includes a market classified as paying on a draw, including soccer's independent 1X2 draw
    # leg. Read this instead of assuming a two-outcome moneyline.
    draw_offered: bool
    # The game's winner markets the sports board binds to its sides (the moneyline, or a soccer game's three 1X2
    # legs), ordered by condition_id. Spreads, totals, period lines and props are on GET ...
    markets: list[GameMarket]
    freshness: GameFreshness
    coverage: GameCoverage
    # The game's page on 0xinsider.
    url: str


class Game(_GameRequired, total=False):
    """One sports or esports game: both sides, its schedule, provider status, its winner markets (the
    moneyline, or the soccer 1X2 legs) with their available provider moneyline price states and
    liquidity, and the game's traded volume. The event's other markets are on GET
    /api/v1/games/{event_slug}/markets. Assembled from the same provider-first live and upcoming
    projections the site's boards use, with no request-time provider fan-out."""
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
    sharp_money: GameSharpMoney
    # The game's traded volume, the figure the sports board carries for it, with its source, basis, unit and
    # observation clock. A client can rank or filter games by volume.value. Omitted when the board carries no
    # volume for ...
    volume: GameVolume


class _GameStatusRequired(TypedDict):
    # scheduled: kickoff is ahead, or the provider still lists the game open and neither in play nor ended. With
    # no live-score frame a game stays scheduled past its kickoff until the provider says otherwise. live: the ...
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
    # The live-score feed's status string, verbatim. Omitted when no live-score frame carries one. This API never
    # puts a label of its own here, such as Scheduled for a listed game.
    provider_status: str
    # The provider's period label, for example Q3, End Q2 or T5. Omitted when the provider sent none.
    period: str
    # The game clock as the provider spells it, never reformatted. Omitted when the provider sent none.
    clock: str
    # Whether the game is in play. It is the provider's own in-play flag, except that three cases read false: a
    # game the provider reports suspended (period SUS), a game rescheduled to a later kickoff, and a tennis match
    # that ...
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
    platform: Literal["polymarket"]


class GameMarket(_GameMarketRequired, total=False):
    """One Polymarket market linked to this game."""
    # The provider's market slug. Omitted when the provider sent none.
    slug: str
    # The provider's own market type, for example moneyline or spread. Omitted when the provider sent none. Not an
    # enum: the provider owns this vocabulary and adds to it.
    sports_market_type: str
    # Which side of the game this market's YES leg pays. Soccer 1X2 legs are explicitly classified as home, draw
    # or away by the provider projection. draw is a real value, not a competitor. Omitted when the provider
    # projection ...
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
    # Polymarket's reported liquidity for this market. Omitted when the provider read carried none, and on a
    # finished game read from its stored record; never 0 in place of a missing figure.
    liquidity: GameMarketLiquidity


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


class _GameMarketLiquidityRequired(TypedDict):
    # The provider's figure at full precision.
    value: float
    # Always gamma: the Polymarket Gamma API.
    source: Literal["gamma"]


class GameMarketLiquidity(_GameMarketLiquidityRequired, total=False):
    """One market's liquidity as Polymarket reports it (Gamma liquidityNum), verbatim. Polymarket documents
    it only as reported market liquidity, with no unit. It describes the market's resting order book,
    not traded volume."""
    # When 0xinsider read the sports board body this figure came from, never a provider-authored timestamp.
    # Omitted when that read has no clock. Format: date-time.
    observed_at: str


class _GameFreshnessRequired(TypedDict):
    # What produced this game: live or upcoming, the board half that carried it, or stored, the stored record of a
    # finished game that has left the board (GET /api/v1/games/{event_slug}, and GET /api/v1/games with a finished
    # ...
    source: Literal["live", "upcoming", "stored"] | str
    # Whether that half returned a truthful source body for this read.
    source_status: Literal["ok", "unavailable"] | str
    # Whether that half had a source body at all. not_applicable means the sport has no configured source for that
    # half.
    source_availability: Literal["available", "unavailable", "not_applicable"] | str
    # Freshness of the cached source body, never inferred from the response clock or the row count. not_applicable
    # for a stored game, whose record is final.
    source_freshness: Literal["fresh", "stale", "unknown", "not_applicable"] | str
    # Whether a reader should be told these rows are behind. This applies the half's own servable-age bar (15 s
    # live, 120 s upcoming), which is not the same as source_freshness: a live board whose scores are seconds old
    # reads ...
    delayed: bool


class GameFreshness(_GameFreshnessRequired, total=False):
    """How current this game's facts are. Independent per source: the board half that produced the game,
    and the live-score frame that produced its scores."""
    # The source body's data vintage. Omitted when the read has no vintage anchor, which is not age zero. For a
    # stored game, the later of its last live-score write and its last leg settlement. Format: date-time.
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
    # available when a live-score frame supplied a score for this game. A game no live-score feed has reported
    # yet, as most scheduled games are, reads unavailable.
    scores: Literal["available", "unavailable"] | str
    # provider_ids when every side carries a provider id, labels when only the provider's names identify them,
    # unavailable when neither exists. Do not join on names when this reads labels.
    competitors: Literal["provider_ids", "labels", "unavailable"] | str
    # available when the provider supplied a kickoff.
    schedule: Literal["available", "unavailable"] | str


class GameSharpMoney(TypedDict):
    """Event-level sharp money for one game. Every aggregate field is null unless status is computed; null
    means unknown, never zero."""
    allocation: Literal["exact", "degraded"] | str | None
    # Format: date-time.
    computed_at: str | None
    event_slug: str
    holders_partial: bool | None
    lifecycle: Literal["live", "settled", "indeterminate"] | str | None
    # Format: date-time.
    money_as_of: str | None
    object: str
    outcomes: list[GameSharpMoneyOutcomesItem]
    status: Literal["computed", "not_computed", "unavailable"] | str
    total_usd: float | None
    trader_count: int | None
    unallocated_usd: float | None
    verdict: GameSharpMoneyVerdict11 | GameSharpMoneyVerdict12 | GameSharpMoneyVerdict13 | GameSharpMoneyVerdict14 | GameSharpMoneyVerdict15 | GameSharpMoneyVerdict16 | GameSharpMoneyVerdict17 | GameSharpMoneyVerdict18 | None


class GameSharpMoneyOutcomesItem(TypedDict):
    is_leader: bool
    label: str
    pct: int
    side: Literal["home", "draw", "away"] | str
    usd: float
    wallets: MarketHoldersSideGrades


class GameSharpMoneyVerdict11(TypedDict):
    kind: Literal["no_sharp_money"]


class GameSharpMoneyVerdict12(TypedDict):
    kind: Literal["all_on"]
    label: str


class GameSharpMoneyVerdict13(TypedDict):
    kind: Literal["split"]


class GameSharpMoneyVerdict14(TypedDict):
    kind: Literal["leans"]
    label: str
    pct: int


class GameSharpMoneyVerdict15(TypedDict):
    kind: Literal["unavailable"]


class GameSharpMoneyVerdict16(TypedDict):
    divergence_pts: int
    kind: Literal["leans_over_price"]
    label: str


class GameSharpMoneyVerdict17(TypedDict):
    kind: Literal["no_clear_lean"]


class GameSharpMoneyVerdict18(TypedDict):
    kind: Literal["withheld"]


class _GameVolumeRequired(TypedDict):
    # The volume at full precision, in unit.
    value: float
    # The Polymarket API the figure was read from: polymarket_data (the Data API's live volume) or gamma (the
    # Gamma API).
    source: Literal["polymarket_data", "gamma"] | str
    # How long after observed_at 0xinsider treats the figure as current: 60 or 300 by source and basis, or 3600
    # for an older figure kept because a later read of the same total was lower or missing (a cumulative volume
    # never ...
    fresh_for_seconds: int


class GameVolume(_GameVolumeRequired, total=False):
    """A game's traded volume as Polymarket reports it, read by the sports board with no request-time
    provider call. A one-side taker share count, the number Polymarket's own pages print behind a dollar
    sign, not the cash that changed hands."""
    # taker_shares: cumulative one-side taker volume in shares. One share pays $1 at settlement, so this is not
    # cash traded. Omitted only on a figure observed before units were recorded; never assume cash.
    unit: Literal["taker_shares"]
    # game_lines: the game volume Polymarket's game page states, summed over the game's own lines. event_total:
    # the whole event's volume, stated when no game volume was readable. The two can differ in either direction.
    # ...
    basis: Literal["game_lines", "event_total"] | str
    # When 0xinsider read the figure from the provider, never a provider-authored timestamp. Omitted when no read
    # time is held for it. Format: date-time.
    observed_at: str


class GamesCoverage(TypedDict):
    """What this deployment covers, published with every page so a client never has to guess whether an
    empty list means no games or no coverage."""
    # Canonical sport buckets served, sorted.
    sports: list[str]
    # League tags served, sorted. EuroLeague is euroleague, NCAA men's college basketball cbb and NCAA women's
    # college basketball cwbb, all under the Basketball sport bucket.
    leagues: list[str]
    # Scopes whose source half was unavailable for this read, as <sport>:<half>. Empty means every scope answered.
    sources_unavailable: list[str]


class GetGameResponse(TypedDict):
    object: Literal["game"]
    data: Game
    # When this read assembled the catalog. Per-source vintage is on freshness. Format: date-time.
    as_of: str
    meta: ResponseMeta


class _ListGameMarketsResponseRequired(TypedDict):
    data: list[ListGameMarketsResponseDataItem]
    event_slug: str
    families: list[ListGameMarketsResponseFamiliesItem]
    has_more: bool
    meta: ResponseMeta
    object: str


class ListGameMarketsResponse(_ListGameMarketsResponseRequired, total=False):
    next_cursor: str


class _ListGameMarketsResponseDataItemRequired(TypedDict):
    condition_id: str
    event_slug: str
    id: str
    outcomes: list[ListGameMarketsResponseDataItemOutcomesItem]
    status: str


class ListGameMarketsResponseDataItem(_ListGameMarketsResponseDataItemRequired, total=False):
    group_item_title: str
    line: float
    line_outcome_index: int
    negative_risk: bool
    platform: str
    slug: str
    sports_market_type: str
    title: str
    sharp_money: ListGameMarketsResponseDataItemSharpMoney


class _ListGameMarketsResponseDataItemOutcomesItemRequired(TypedDict):
    index: int


class ListGameMarketsResponseDataItemOutcomesItem(_ListGameMarketsResponseDataItemOutcomesItemRequired, total=False):
    label: str
    token_id: str


class ListGameMarketsResponseDataItemSharpMoney(TypedDict):
    # Format: date-time.
    money_as_of: str | None
    outcomes: list[ListGameMarketsResponseDataItemSharpMoneyOutcomesItem]
    status: Literal["computed", "not_computed", "unavailable"] | str
    trader_count: int | None


class ListGameMarketsResponseDataItemSharpMoneyOutcomesItem(TypedDict):
    index: int
    usd: float
    wallets: MarketHoldersSideGrades


class _ListGameMarketsResponseFamiliesItemRequired(TypedDict):
    active: int
    markets: int


class ListGameMarketsResponseFamiliesItem(_ListGameMarketsResponseFamiliesItemRequired, total=False):
    sports_market_type: str


class GetGameSharpMoneyResponse(TypedDict):
    object: Literal["game_sharp_money"]
    data: GameSharpMoney
    meta: ResponseMeta


class ListGameTradesResponse(TypedDict):
    object: Literal["list"]
    # Newest first.
    data: list[GameTrade]
    # Always false: the list is the game's newest limit fills, not a walk. Poll again for newer fills.
    has_more: bool
    # The game the rows were read for, lowercased.
    event_slug: str
    # true when the rows are the game's last complete read, served while its refresh runs. Read again in a few
    # seconds for the live rows.
    source_stale: bool
    meta: ResponseMeta


class GameTrade(TypedDict):
    """One fill in a game, as the game page's activity list shows it."""
    # Stable fill identity: {transaction_hash}:{token_id}:{wallet}:{shares}. Deduplicate on it across polls.
    id: str
    # When the fill happened, to the second. Format: date-time.
    traded_at: str
    # The provider's side of the fill.
    side: Literal["BUY", "SELL"] | str
    # The traded outcome's label; null when the provider named none.
    outcome: str | None
    # 0 for the first (Yes) outcome token, 1 for the second (No); null when the provider did not say.
    outcome_index: int | None
    # Fill price, 0 to 1.
    price: float
    # Shares filled.
    shares: float
    # USDC notional of the fill.
    size_usd: float
    # The signed handicap the fill's side carries on a spread line, for example -1.5 or 1.5; null off spreads.
    point: float | None
    trader: GameTradeTrader
    market: GameTradeMarket


class GameTradeTrader(TypedDict):
    # Lowercase proxy wallet.
    address: str
    # The name the site shows: the 0xinsider username, else the provider's name or pseudonym, else the shortened
    # address.
    display_name: str
    # The trader's grade today; null for an ungraded or untracked wallet.
    grade: Literal["S", "A", "B", "C", "D", "F", None] | str | None


class GameTradeMarket(TypedDict):
    # The market's v1 id, mkt_ plus the condition_id.
    id: str
    # The raw provider condition_id.
    condition_id: str
    # The market's question.
    title: str | None
    # The market's page slug.
    slug: str | None
    # The market's name within the game, for example Draw, O/U 2.5, First to Score: CD Guadalajara, Game 2: Any
    # Player Quadra Kill.
    line_label: str | None


class GetGameHoldersResponse(TypedDict):
    object: Literal["game_holders_batch"]
    data: list[BatchGameHoldersItem]
    meta: BatchResponseMeta


class _BatchGameHoldersItemRequired(TypedDict):
    # Zero-based request index. Duplicate inputs keep separate result rows.
    index: int
    input: str
    status: Literal["ok", "error"] | str


class BatchGameHoldersItem(_BatchGameHoldersItemRequired, total=False):
    data: GameHoldersItem
    error: ApiErrorBody


class GameHoldersItem(TypedDict):
    """One market of a game holders batch: GET /api/v1/market/{condition_id}/holders unfiltered and cut to
    the batch limit."""
    # The roster's top holders by current value, at most limit.
    data: list[MarketHolder]
    # More graded holders than limit: page them on GET /api/v1/market/{condition_id}/holders.
    has_more: bool
    # Graded holders in the roster, across every page.
    total: int
    market: MarketHoldersMarket
    scan: MarketHoldersScan
    totals: MarketHoldersTotals
    # When this roster was computed. A cached roster is at most 60 seconds old. Format: date-time.
    computed_at: str
    # true when the roster came from the 60-second roster cache.
    cached: bool


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


class EventReplayMeta(TypedDict):
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
    retry_schedule_reason: Literal["receiver_retry_after", "transient_failure", "permanent_or_auth_failure", "manual_redelivery", "configuration_changed", None] | str | None
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


class GetHealthResponseData(TypedDict):
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
    method: Literal["initialize", "notifications/initialized", "notifications/cancelled", "ping", "tools/list", "tools/call", "server/discover"]


class CreateMcpJsonRpcResponseBody(_CreateMcpJsonRpcResponseBodyRequired, total=False):
    # Request identifier, a string or a number, echoed exactly in one JSON-RPC response; a notification omits it
    # and receives an empty HTTP 202. A null id answers HTTP 400 with JSON-RPC error -32600.
    id: str | float
    # Method-specific MCP parameters.
    params: dict[str, Any]


class _CreateMcpJsonRpcResponseResponseRequired(TypedDict):
    jsonrpc: Literal["2.0"]
    id: str | float | None


class CreateMcpJsonRpcResponseResponse(_CreateMcpJsonRpcResponseResponseRequired, total=False):
    result: dict[str, Any]
    error: CreateMcpJsonRpcResponseResponseError


class _CreateMcpJsonRpcResponseResponseErrorRequired(TypedDict):
    code: int
    message: str


class CreateMcpJsonRpcResponseResponseError(_CreateMcpJsonRpcResponseResponseErrorRequired, total=False):
    # Optional JSON-serializable error data.
    data: dict[str, Any] | list[Any] | str | float | bool | None


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


class SnapshotCompleteness(TypedDict):
    # complete only on a final body (snapshot.status final). partial for a live range and for a closed range whose
    # body was read before final_after; reason says which. empty when the range has no whale activity.
    status: Literal["complete", "partial", "empty"] | str
    reason: str
    expected_days: int
    # Canonical key since #16304; covered_days_with_whale_activity is its deprecated spelling, emitted beside it
    # with the same value until its sunset on 2027-02-01 (#29352).
    covered_days_with_large_trade_activity: int
    # Deprecated spelling of covered_days_with_large_trade_activity, emitted beside it with the same value. Sunset
    # 2027-02-01 (#29352): removed from V1 on that date; read covered_days_with_large_trade_activity.
    covered_days_with_whale_activity: int


class ReportReconciliation(TypedDict):
    volume_kind: Literal["local_whale_activity_volume"]
    # Where the whale volume in this report is read from: the column name `whale_alerts.usdc_notional_num`,
    # followed in parentheses by the reconciliation note the server attaches to it. The server has always sent the
    # note ...
    whale_volume_source: str
    notes: str


class ReportPayload(TypedDict):
    # Canonical key since #16304; total_whale_trades is its deprecated spelling, emitted beside it with the same
    # value until its sunset on 2027-02-01 (#29352).
    total_large_trades: int | None
    total_whale_trades: int | None
    # Canonical key since #16304; total_whale_volume is its deprecated spelling, emitted beside it with the same
    # value until its sunset on 2027-02-01 (#29352).
    total_large_trade_volume: float | None
    total_whale_volume: float | None
    biggest_trade_size: float | None
    active_traders: int | None
    # Canonical key since #16304; top_whale_trades is its deprecated spelling, emitted beside it with the same
    # value until its sunset on 2027-02-01 (#29352).
    top_large_trades: list[ReportPayloadTopLargeTradesItem] | None
    top_whale_trades: list[ReportPayloadTopLargeTradesItem] | None
    categories: list[ReportPayloadCategoriesItem] | None
    # Counts of current grades for distinct Polymarket traders with at least one whale alert in the report's
    # source date range. The grade is the current projection at snapshot materialization time, not a historical
    # grade at ...
    grade_distribution: list[ReportPayloadGradeDistributionItem] | None
    # Which markets the report counts. sports_and_esports for a period that ends on or after 2026-10-21: totals,
    # categories, top trades and the grade cohort cover sports and esports markets only. all_markets for an
    # earlier ...
    market_scope: Literal["all_markets", "sports_and_esports"] | str


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
    # Always polymarket, or null when the row carries no stored value.
    platform: Literal["polymarket", None] | str | None
    # Trader display name, when known.
    name: str | None
    # Trader pseudonym, when no display name is known.
    pseudonym: str | None
    # Trader grade (S-F) at snapshot time.
    trader_grade: Literal["S", "A", "B", "C", "D", "F", None] | str | None


class ReportPayloadCategoriesItem(TypedDict):
    category: str | None
    large_trade_count: int | None
    whale_trade_count: int | None
    category_volume: float | None


class ReportPayloadGradeDistributionItem(TypedDict):
    grade: Literal["S", "A", "B", "C", "D", "F", None] | str | None
    count: int | None


class GetResolutionReportResponse(TypedDict):
    object: Literal["resolution_report"]
    data: ResolutionReport
    meta: ResponseMeta


class _ResolutionReportRequired(TypedDict):
    accuracy: float | None
    all_wallets_accuracy: float | None
    all_wallets_right: int | None
    all_wallets_wrong: int | None
    date: str | None
    generated_at: str | None
    grade_basis: Literal["at_resolution", "current"] | str | None
    market_scope: Literal["all_markets", "sports_and_esports"] | str
    markets_without_smart_positions: int | None
    no_consensus: int | None
    positions_grade_unknown: int | None
    positions_without_side: int | None
    smart_money_right: int | None
    smart_money_wrong: int | None
    source_updates_pending: bool
    time_basis_counts: ResolutionReportTimeBasisCounts1 | None
    total_resolved: int | None
    total_smart_pnl: float | None
    with_smart_positions: int | None


class ResolutionReport(_ResolutionReportRequired, total=False):
    markets: list[ResolutionReportMarketsItem]


class ResolutionReportMarketsItem(TypedDict):
    all_wallets_right: bool | None
    category: str | None
    condition_id: str | None
    confidence: float | None
    event_slug: str | None
    out_of_product_scope: bool
    outcome_no: str | None
    outcome_yes: str | None
    # Format: date-time.
    report_at: str
    smart_consensus: str | None
    smart_right: bool | None
    smart_trader_count: int | None
    time_basis: Literal["polymarket_gamma_closed_time", "observed_resolution"] | str
    title: str | None
    total_smart_pnl: float | None
    traders: list[ResolutionReportMarketsItemTradersItem]
    weighted_no: float | None
    weighted_yes: float | None
    winning_outcome: int | None


class ResolutionReportMarketsItemTradersItem(TypedDict):
    address: str | None
    correct: bool | None
    cost: float | None
    grade: Literal["S", "A", "B", "C", "D", "F"] | str | None
    # Format: date-time.
    last_traded_at: str | None
    pnl: float | None
    side: str | None
    username: str | None


class ResolutionReportTimeBasisCounts1(TypedDict):
    observed_resolution: int
    polymarket_gamma_closed_time: int


class GetTraderExportSnapshotResponse(TypedDict):
    object: Literal["trader_export_snapshot"]
    data: TraderExportSnapshot
    meta: ResponseMeta


class TraderExportSnapshot(TypedDict):
    address: str
    # The markets the export file's trades and markets sections hold: sports and esports markets only.
    # counts.exported_markets, counts.estimated_trade_rows, counts.estimated_size_mb,
    # reconciliation.exported_market_cost_basis ...
    product_scope: Literal["sports_esports_v1"]
    # Format: date-time.
    generated_at: str
    source_range: ExportSourceRange
    completeness: ExportCompleteness
    reconciliation: ExportVolumeReconciliation
    counts: ExportCounts
    large_export_policy: LargeExportPolicy


class ExportSourceRange(TypedDict):
    # The first UTC day in the export file's pnl section, the wallet's sports and esports realized P&L by day: the
    # file's export_metadata.pnl_date_from. Null when that section has no day, including while pnl_series_status
    # is ...
    first_pnl_date: str | None
    # The last UTC day in the export file's pnl section: the file's export_metadata.pnl_date_to. Null when that
    # section has no day. Format: date.
    last_pnl_date: str | None
    # Whether the export file's pnl section holds the wallet's sports and esports day series, the file's
    # export_metadata.pnl_series_status. pending means 0xinsider has not computed the series yet: the dates are
    # null and ...
    pnl_series_status: Literal["ready", "pending"] | str
    # The latest trade in the wallet's sports and esports markets. Null when it has none. Format: date-time.
    latest_trade_at: str | None
    # Same instant as latest_trade_at: the latest activity of the markets the export holds. Format: date-time.
    latest_market_activity_at: str | None


class ExportCompleteness(TypedDict):
    status: Literal["complete", "partial", "empty"] | str
    reason: str
    sync_coverage: float


class ExportVolumeReconciliation(TypedDict):
    # Deprecated (#30499): always null since 2026-10-29. It held Polymarket's volume across every market of the
    # wallet, which reconciles nothing against the sports and esports exported_activity_volume; the key stays so
    # ...
    provider_lifetime_volume: float | None
    # Volume in USD, buys and sells, in sports and esports markets, each fill's size times its price with fees
    # excluded, summed over the wallet's stored daily volume rows (from the fills 0xinsider stores for the
    # wallet): the ...
    exported_activity_volume: float | None
    # Cost basis in USD summed over the wallet's sports and esports markets, the markets section of the export.
    exported_market_cost_basis: float
    # Always null. provider_lifetime_volume covered every market and exported_activity_volume sports and esports
    # markets only, so their difference measured nothing; the field stays so existing clients keep parsing the
    # object.
    provider_activity_volume_gap: float | None
    # Always null, for the same reason as provider_activity_volume_gap.
    activity_volume_coverage: float | None


class ExportCounts(TypedDict):
    # The days in the export file's pnl section, the wallet's sports and esports realized P&L by UTC day: the
    # file's export_metadata.pnl_rows, at most its earliest 3650 days. 0 while source_range.pnl_series_status is
    # pending, ...
    pnl_days: int
    # The wallet's sports and esports markets: the rows of the export's markets section, before its 50,000-row
    # cap.
    exported_markets: int
    # Estimated trades in the wallet's sports and esports markets: the summed trade counts of those markets. The
    # file counts its own rows in generation.source_watermarks.trades.rows.
    estimated_trade_rows: int
    # Estimated file size from estimated_trade_rows and exported_markets.
    estimated_size_mb: float


class LargeExportPolicy(TypedDict):
    mode: Literal["v1_async_export"]
    current_internal_route: str
    # Programmatic API-key-gated export routes (submit/status/download/cancel) and supported formats (json,
    # ndjson, csv).
    v1_async: LargeExportPolicyV1Async
    direct_streaming: LargeExportPolicyDirectStreaming
    async_job: LargeExportPolicyAsyncJob
    rate_limit: LargeExportPolicyRateLimit


class LargeExportPolicyV1Async(TypedDict):
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


class LargeExportPolicyDirectStreaming(TypedDict):
    available_when: str
    backpressure: str
    chunk_size_rows: int


class LargeExportPolicyAsyncJob(TypedDict):
    available_when: str
    status_values: list[str]
    retention: str


class LargeExportPolicyRateLimit(TypedDict):
    daily_cap_per_user: int
    per_address_hourly_cap: int


class TraderExportJob(TypedDict):
    object: Literal["trader_export_job"]
    data: TraderExportJobData
    meta: ResponseMeta


class _TraderExportJobDataRequired(TypedDict):
    # Format: int64.
    job_id: int
    # queued: waiting for a worker. A running job reads queued again, with error saying why, when its worker
    # restarts for a deploy (the next worker claims it within seconds) or stops without handing it back (requeued
    # within a ...
    status: Literal["queued", "running", "ready", "failed", "reconcile_required", "expired", "cancel_requested", "cancelled"] | str
    format: Literal["json", "ndjson", "csv"] | str
    # Trade rows the file holds: trades in the wallet's sports and esports markets, counted in the file's own read
    # snapshot. Null until the worker has read the snapshot (queued, and early in running); a job accepted before
    # ...
    total_trades: int | None
    # Trade rows written so far; equals total_trades once the file is read. Format: int64.
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
    # Worker claims so far. A claim handed back when its worker restarts for a deploy is not counted, so attempt
    # steps back by one when the job reads queued again for that reason.
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


class _TraderExportGenerationRequired(TypedDict):
    # Opaque generation identity selected for the coherent read snapshot. Format: uuid.
    id: str
    # Format: date-time.
    selected_at: str
    consistency: Literal["repeatable_read"]
    source_watermarks: TraderExportSourceWatermarks


class TraderExportGeneration(_TraderExportGenerationRequired, total=False):
    # The markets the file's trades and markets sections hold: sports and esports markets only
    # (export_metadata.scope_note in a JSON or NDJSON file names the sections that still cover every market).
    # Absent on a file written ...
    product_scope: Literal["sports_esports_v1"]


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
    # sports_esports_rows: the file holds every stored trade in the wallet's sports and esports markets.
    # all_matching_rows on a file written before 2026-10-22, which holds every market's trades.
    coverage: str
    # Trade rows the file holds, counted in the same read snapshot as the rows. Format: int64.
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
    # The monthly request quota (#16111): where the account stands against the requests the current Pro or Max
    # plan includes per UTC calendar month. Reading it here spends nothing. null only when the month's count could
    # not ...
    monthly_quota: UsageDataMonthlyQuota | None


class UsageDataRateLimit(TypedDict):
    used: int
    # The per-minute window's limit for the caller's plan: 100 requests on Pro, 200 on Max. The same number
    # RateLimit-Limit reports on a counted request.
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
    """The monthly request quota (#16111): where the account stands against the requests the current Pro or
    Max plan includes per UTC calendar month. Reading it here spends nothing. null only when the month's
    count could not be read for this response."""
    # Admitted requests so far this UTC calendar month.
    used: int
    # Requests the account's plan includes per UTC calendar month: 500,000 for Pro, 2,000,000 for Max.
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
    # four times limit with pay as you go on (2,000,000 for Pro). null for an admin account, which no number
    # stops. ...
    ceiling: int | None
    # Why pay as you go is unavailable, or null. usage_price_reconciliation_required: the account's usage
    # subscription carries a historical price whose included requests differ from its plan's, so pay as you go
    # stays off ...
    unavailable_reason: Literal["usage_price_reconciliation_required", None] | str | None


class AccountIdentity(TypedDict):
    object: Literal["account"]
    data: AccountIdentityData
    meta: ResponseMeta


class AccountIdentityData(TypedDict):
    user_id: int
    credential_id: int
    # The kind of credential that made the request: api_key is a full-access developer key, oauth_grant an OAuth
    # access token, integration_key a named integration key with fixed scopes created on ...
    credential_kind: Literal["api_key", "oauth_grant", "integration_key"] | str
    # The credential is currently valid; revoked, expired or unknown credentials are rejected.
    credential_status: Literal["active"]
    entitlement: AccountIdentityDataEntitlement
    # The scopes an OAuth grant or integration key carries; null for full developer-key access.
    scopes: list[str] | None


class AccountIdentityDataEntitlement(TypedDict):
    paid_data_access: Literal["active", "lapsed"] | str
    # When paid data access is lapsed, the caller should renew the subscription; otherwise null.
    recovery_action: Literal["renew_subscription", None] | str | None


__SubmitWhaleDatasetBodyRequiredFields = TypedDict("__SubmitWhaleDatasetBodyRequiredFields", {
    # Format: date-time.
    "from": "str",
    # Format: date-time.
    "to": "str",
}, total=True)

class _SubmitWhaleDatasetBodyRequired(__SubmitWhaleDatasetBodyRequiredFields):
    pass


class SubmitWhaleDatasetBody(_SubmitWhaleDatasetBodyRequired, total=False):
    # Raw provider condition id or mkt_-prefixed id.
    condition_id: str
    # USD minimum, normalized to cents like replay.
    min_size: float


class WhaleDatasetJob(TypedDict):
    object: Literal["whale_dataset_job"]
    data: WhaleDatasetJobData
    meta: ResponseMeta


class _WhaleDatasetJobDataRequired(TypedDict):
    # Format: int64.
    job_id: int
    # queued: waiting for a worker. A running job reads queued again, with error saying why, when its worker
    # restarts for a deploy (the next worker claims it within seconds) or stops without handing it back (requeued
    # within a ...
    status: Literal["queued", "running", "ready", "failed", "reconcile_required", "expired", "cancel_requested", "cancelled"] | str
    format: Literal["ndjson"]
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
    # Snapshot selection clock, null until the artifact is written; not provider completeness. Format: date-time.
    data_as_of: str | None
    # When the owner asked to cancel the job; null otherwise. Set on every cancelled job, including one cancelled
    # while queued. While status is cancel_requested this is the instant the worker was asked to stop. Format: ...
    cancel_requested_at: str | None
    # When the job reached cancelled; null until then. Format: date-time.
    cancelled_at: str | None
    # Worker claims so far. A claim handed back when its worker restarts for a deploy is not counted, so attempt
    # steps back by one when the job reads queued again for that reason.
    attempt: int
    # The job fails when attempt reaches this.
    max_attempts: int
    filters: WhaleDatasetFilters


class WhaleDatasetJobData(_WhaleDatasetJobDataRequired, total=False):
    # Seconds to wait before polling again. Absent when terminal. 5 while queued, running or cancel_requested; 300
    # while reconcile_required, the cadence that state can change at.
    poll_after_s: int
    # Present only while status is ready: the stored object's identity, so a client can check the download it
    # receives.
    artifact: WhaleDatasetJobDataArtifact


class WhaleDatasetJobDataArtifact(TypedDict):
    """Present only while status is ready: the stored object's identity, so a client can check the download
    it receives."""
    # Stable identity for this completed export artifact; unchanged when a temporary download URL is renewed.
    artifact_id: str
    # The storage ETag of the object.
    etag: str | None
    # Bytes on the wire (gzip); file_size is the decompressed size. Format: int64.
    compressed_size_bytes: int | None
    content_type: Literal["application/x-ndjson"]
    content_encoding: Literal["gzip"]
    # Immutable source, window, replay handoff, count and hashes of both content and gzip bytes.
    manifest: WhaleDatasetArtifactManifest | None


class WhaleDatasetArtifactManifest(TypedDict):
    # Version of the artifact manifest contract.
    manifest_version: str
    format: Literal["ndjson"]
    schema_version: Literal["whale_dataset_v1"]
    coverage: Literal["best_effort_detected_whale_alerts"]
    generation: WhaleDatasetGeneration
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


class WhaleDatasetGeneration(TypedDict):
    dataset_schema_version: Literal["whale_dataset_v1"]
    # Format: uuid.
    id: str
    # Format: date-time.
    selected_at: str
    consistency: Literal["repeatable_read_commit_horizon"]
    filters: WhaleDatasetFilters
    # All snapshot rows have a writer xid strictly below this closed visibility horizon. Decimal string preserves
    # integer precision.
    commit_horizon_xid: str
    continuation: WhaleDatasetContinuation
    source: Literal["whale_alerts"]
    # Best-effort detected whale alerts only; not all provider fills. No trader or market enrichment.
    coverage: str
    # Format: date-time.
    expires_at: str
    extraction_elapsed_ms: int


_WhaleDatasetFiltersFields = TypedDict("_WhaleDatasetFiltersFields", {
    # Format: date-time.
    "from": "str",
    # Format: date-time.
    "to": "str",
    "condition_id": "str | None",
    "min_size_cents": "int | None",
}, total=True)

class WhaleDatasetFilters(_WhaleDatasetFiltersFields):
    """Normalized immutable request; [from, to), maximum 31 days; min_size rounded to cents like durable
    replay."""


class WhaleDatasetContinuation(TypedDict):
    path: Literal["/api/v1/events/feed/since"]
    # Opaque commit-safe replay cursor; replay the same condition_id and min_size.
    cursor: str
    # Writer floor included by the replay cursor. It can precede the snapshot horizon to include arrivals after
    # the finite window end.
    from_commit_xid: str
    condition_id: str | None
    # Normalized USD threshold; pass it to the replay query.
    min_size: str | None
    deduplication_identity: str
    time_window_applies_to_deltas: Literal[False]
    delivery: str


class GetPickOfTheDayLedgerEntryResponse(TypedDict):
    object: Literal["pick_of_the_day_ledger_entry"]
    data: PickOfTheDayLedgerEntry
    meta: ResponseMeta


class CreateWebhookVerificationAttemptRequest(TypedDict):
    # The original one-time token returned by webhook creation or a URL change. Sent only in the request body and
    # signed receiver challenge.
    verification_token: str


class CreateWebhookVerificationAttemptResponse(TypedDict):
    object: Literal["webhook_verification_attempt"]
    data: WebhookVerificationAttempt
    meta: ResponseMeta


class WebhookVerificationAttempt(TypedDict):
    # Format: uuid.
    id: str
    object: Literal["webhook_verification_attempt"]
    # Format: int64.
    webhook_id: int
    # queued/running are pending consent. verified means the same endpoint revision answered 2xx and activated
    # atomically. failed/cancelled/expired are terminal and do not restart on polling or replay.
    state: Literal["queued", "running", "verified", "failed", "cancelled", "expired"] | str
    # Sanitized last observation. Null before an observation; queued retries may retain their previous failure
    # outcome.
    outcome: Literal["verified", "target_rejected", "challenge_timeout", "transport_failed", "receiver_rejected", "token_expired", "endpoint_changed", "owner_revoked", "attempts_exhausted", "internal_error", None] | str | None
    attempt_count: int
    max_attempts: Literal[4]
    # Earlier of the verification-token deadline and 15 minutes after admission. Activation is forbidden at or
    # after this instant. Format: date-time.
    expires_at: str
    # Scheduled retry/admission time while queued; null while running or terminal. Format: date-time.
    next_attempt_at: str | None
    # Actual receiver HTTP status, when one arrived. No receiver response body or resolved address is returned.
    last_response_status: int | None
    # Format: date-time.
    started_at: str | None
    # Format: date-time.
    completed_at: str | None
    # Format: date-time.
    created_at: str
    # Format: date-time.
    updated_at: str
    # Relative authorized API path for this attempt. Uses the same bearer credential as admission.
    status_url: str


class _ComboFillsResponseRequired(TypedDict):
    object: Literal["list"]
    data: list[ComboFill]
    sort: Literal["recent", "largest", "payout"] | str
    window: Literal["24h", "7d", "all"] | str
    # Format: int64.
    limit: int
    coverage: ComboCoverage
    # A continuation is available based on page fullness. Its next page may be empty.
    has_more: bool
    meta: ResponseMeta


class ComboFillsResponse(_ComboFillsResponseRequired, total=False):
    # Exclusive block_number:log_index continuation for recent ordering.
    next_cursor: str
    # Continuation offset for largest or payout ordering. Format: int64.
    next_offset: int


class ComboFill(TypedDict):
    # Stable fill identity.
    id: str
    # Format: int64.
    block_number: int
    # Format: int64.
    log_index: int
    # Format: date-time.
    block_timestamp: str
    tx_hash: str
    # Taker wallet address.
    trader: str | None
    trader_name: str | None
    trader_grade: Literal["S", "A", "B", "C", "D", "F", None] | str | None
    # Recorded wallet-wide trade time. Format: date-time.
    last_traded_at: str | None
    action: Literal["buy", "sell"] | str
    # Combo identifier: 0x followed by 62 lowercase hex characters. This differs from a binary market condition
    # ID.
    condition_id: str
    # 0 is YES, 1 is NO. Format: int64.
    outcome_index: int
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    shares: str
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    collateral_usdc: str
    # Execution price for the traded outcome; null for a zero-share event.
    price: str | None
    # Execution price normalized to YES.
    price_yes: str | None
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    fee_usdc: str
    # Format: int64.
    leg_count: int | None
    # Result of the YES conjunction, independent of the wallet side or its P&L.
    status: Literal["pending", "won", "lost", "unknown"] | str
    status_reason: str | None
    # Format: int64.
    won_legs: int
    # Shares per dollar at execution; not a forecast or guaranteed return.
    payout_multiplier: str | None
    legs: list[ComboLeg]


class ComboLeg(TypedDict):
    # Format: int64.
    leg_index: int
    # Format: int64.
    outcome_index: int
    # Format: int64.
    module_id: int
    state: Literal["pending", "won", "lost", "void", "unknown"] | str
    market: ComboLegMarket | None


class _ComboLegMarketRequired(TypedDict):
    # Source of the leg facts.
    source: Literal["markets", "provider"] | str
    # Full binary CTF condition ID for this leg.
    condition_id: str
    title: str | None
    slug: str | None
    event_slug: str | None
    outcome_label: str | None
    image: str | None
    category: str | None
    # Provider outcome index; negative sentinels describe void or unresolved states. Format: int64.
    winning_outcome: int | None
    # Format: date-time.
    resolved_at: str | None
    # A closed market may still have no terminal outcome.
    market_closed: bool | None
    # Stored daily price for this leg outcome token; not a live quote.
    pick_price_daily: float | None
    # Observation time of the stored daily price. Format: date-time.
    pick_price_as_of: str | None
    # Whole days since the stored daily bucket. Format: int64.
    pick_price_age_days: int | None
    # Unmodified provider leg status when available.
    provider_leg_status: str | None


class ComboLegMarket(_ComboLegMarketRequired, total=False):
    # Provider-resolved URL including the referral tag. Format: uri.
    polymarket_url: str


class ComboCoverage(TypedDict):
    state: Literal["paused", "uninitialized", "stale", "backfilling", "live"] | str
    ingest_enabled: bool
    cursors: list[ComboCoverageCursor]
    # Format: int64.
    max_lag_blocks: int | None
    # Format: date-time.
    oldest_cursor_update: str | None
    # Format: int64.
    lifecycle_lag_blocks: int | None
    lifecycle_backfilling: bool
    # Time the coverage state was evaluated; not a market-price timestamp. Format: date-time.
    computed_at: str


class ComboCoverageCursor(TypedDict):
    # Indexed contract.
    contract: str
    # Format: int64.
    last_block: int
    # Format: int64.
    seed_block: int
    seed_origin: str
    # Format: int64.
    chain_finalized_block: int | None
    # Format: int64.
    lag_blocks: int | None
    # Format: date-time.
    updated_at: str


class CombosSummaryResponse(TypedDict):
    object: Literal["combos_summary"]
    data: CombosSummary
    meta: ResponseMeta


class CombosSummary(TypedDict):
    """Stored live combo count. Null means the first count is unavailable, never zero."""
    live: ComboLiveCount | None


class ComboLiveCount(TypedDict):
    # Traded combos whose YES conjunction remains pending. Format: int64.
    count: int
    # Time the count was computed; check its age before using it. Format: date-time.
    computed_at: str


class ComboResponse(TypedDict):
    object: Literal["combo"]
    data: ComboDetail
    meta: ResponseMeta


class ComboDetail(TypedDict):
    """One combo with its newest 100 fills and all-time lifecycle totals. Paid API callers receive full
    access."""
    access: Literal["full"]
    combo: Combo
    fills: list[ComboFill]
    lifecycle: ComboLifecycleStats | None
    coverage: ComboCoverage


class Combo(TypedDict):
    # Combo identifier: 0x followed by 62 lowercase hex characters. This differs from a binary market condition
    # ID.
    condition_id: str
    # Format: int64.
    leg_count: int | None
    # Format: date-time.
    prepared_at: str | None
    # Whether the preparation event has been indexed.
    legs_known: bool
    legs: list[ComboLeg]
    window: ComboWindowStats | None
    totals: ComboTotals | None
    # Result of the YES conjunction, independent of the wallet side or its P&L.
    status: Literal["pending", "won", "lost", "unknown"] | str
    # Reason the conjunction result cannot be verified, when unknown.
    status_reason: str | None


class ComboWindowStats(TypedDict):
    # Format: int64.
    fills: int
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    volume_usdc: str
    # Format: int64.
    distinct_traders: int
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    largest_fill_usdc: str


class ComboTotals(TypedDict):
    # Format: int64.
    fills: int
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    volume_usdc: str
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    largest_fill_usdc: str
    # Format: date-time.
    first_fill_at: str
    # Format: date-time.
    last_fill_at: str
    # Last taker execution normalized to YES; not a current quote.
    last_fill_price_yes: str | None
    # Format: int64.
    last_fill_outcome_index: int
    last_fill_action: Literal["buy", "sell"] | str


class ComboLifecycleStats(TypedDict):
    # Format: int64.
    splits: int
    # Format: int64.
    merges: int
    # Format: int64.
    redeems: int
    # Format: int64.
    compresses: int
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    split_usdc: str
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    merge_usdc: str
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    redeemed_shares: str
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    redeemed_usdc: str
    # Exact decimal string from the stored chain or SQL value; preserve precision until display.
    compressed_usdc: str
    # Format: date-time.
    last_event_at: str


class _EdgeHunterBoardResponseRequired(TypedDict):
    object: Literal["edge_hunter"]
    data: EdgeHunterBoard
    meta: ResponseMeta


class EdgeHunterBoardResponse(_EdgeHunterBoardResponseRequired, total=False):
    # Normalized axes requested with a selector or category; omitted on an unselected default read.
    selection: EdgeHunterSelection


class EdgeHunterBoard(TypedDict):
    """The full Max-only Edge Hunter board. Defaults cover all sports and esports with B grade floor,
    48-hour horizon and at most 30 rows; common selections, legacy category, min_grade and limit narrow
    that projection. No pagination or ETag. Rows add frozen market_context discovery metadata."""
    # When the ranked snapshot was computed. Date current quotes with their own ts values. Format: date-time.
    as_of: str
    horizon_hours: int
    # Requested holder-presence grade floor, S/A/B. A holder at that grade or better admits the row; other holders
    # remain visible.
    min_grade: Literal["S", "A", "B"] | str
    # live uses the current graded holder pile; db_only is a weaker stored-data fallback.
    ranking_source: Literal["live", "db_only"] | str
    # degraded means directional enrichment was unavailable.
    directional_source: Literal["live", "degraded"] | str
    cached_age_seconds: int | None
    viewer: Literal["max"]
    # Always null: Edge Hunter has no free signal slot.
    free_rank: int | None
    # Ranked rows after normalized selections and grade filtering, before the view-specific limit cap.
    total: int
    rows: list[EdgeHunterRow]


class EdgeHunterRow(TypedDict):
    """One full Max row from Edge Hunter. signal is populated on every row this endpoint returns. Identity
    and quotes preserve provider values; unknown values stay null."""
    rank: int
    state: Literal["full"]
    free: Literal[False]
    condition_id: str
    event_slug: str | None
    title: str | None
    category: Literal["Basketball", "Football", "Baseball", "Hockey", "MMA", "Boxing", "Soccer", "Cricket", "Golf", "Tennis", "Esports", "Racing", "Table Tennis", "Pickleball", None] | str | None
    raw_category: str | None
    # Format: date-time.
    game_start_time: str | None
    # Cumulative provider taker volume in shares, not cash in USD. Null when unavailable.
    volume: float | None
    participants: list[EdgeHunterParticipant]
    image: str | None
    outcomes: list[EdgeHunterOutcome]
    signal: EdgeHunterSignal | None
    # Required nullable frozen metadata context. Null only during the legacy-generation transition; selected reads
    # require sidecar readiness and fail closed with 503 instead.
    market_context: EdgeHunterMarketContext | None


class _EdgeHunterParticipantRequired(TypedDict):
    name: str


class EdgeHunterParticipant(_EdgeHunterParticipantRequired, total=False):
    # Format: int64.
    provider_id: int
    logo: str
    logo_mark_dark: bool
    color: str
    headshot: str
    # Format: int64.
    headshot_revision: int
    tour: str
    logo_mark_light: bool
    logo_mark_measured: bool


class EdgeHunterOutcome(TypedDict):
    """One provider outcome in fixed YES/NO order, including its frozen token identity and independently
    observed quote. Null current_price means no verified current quote is available."""
    index: Literal[0, 1] | int
    label: str | None
    # Format: int64.
    provider_id: int | None
    # Frozen provider CLOB token ID for this exact outcome in YES/NO order. Null when unavailable; not a
    # participant identity.
    token_id: str | None
    current_price: EdgeHunterPrice | None


class _EdgeHunterPriceRequired(TypedDict):
    # Provider probability as a decimal string. Keep its precision until display.
    price: str
    basis: Literal["midpoint", "last_trade"] | str
    # Source observation clock in epoch milliseconds, represented as a string.
    ts: str


class EdgeHunterPrice(_EdgeHunterPriceRequired, total=False):
    # Backend validation clock in epoch milliseconds. Omitted when no current-source validation is available.
    validated_at: str


class EdgeHunterSignal(TypedDict):
    """Backed-side analytics, token identity, frozen ranked_at and aggregate category evidence from the
    ranked snapshot, plus a separately dated current quote. Scores rank attention; they are not
    probabilities or order instructions."""
    piled_side: str | None
    piled_outcome_index: Literal[0, 1] | int
    # Fraction of graded money on the backed side, not a percentage from 0 to 100.
    sharp_pct: float | None
    backed_sharp_usd: float
    s_count: int
    a_count: int
    b_count: int
    graded_holders: int
    top_grade: Literal["S", "A", "B", None] | str | None
    smart_score: float | None
    net_side: str | None
    conviction_score: float
    one_way_holder_count: int | None
    hedged_holder_count: int | None
    one_way_graded_usd: float | None
    directional_confidence: float | None
    directional_rank_score: float
    current_price: EdgeHunterPrice | None
    # Frozen provider CLOB token ID for the backed outcome. Null when unavailable; matches
    # outcomes[piled_outcome_index].token_id when the shared provider context is available.
    token_id: str | None
    # UTC computation time copied from this ranked row's frozen signal_created_at. It dates the ranking, not the
    # separately observed quote, metadata writer, or wallet entry. Format: date-time.
    ranked_at: str
    # Existing aggregate category evidence copied from the same ranked snapshot. Read its status, coverage and own
    # clocks; it never changes admission or ordering and is not a predicted return.
    category_skill: EdgeHunterCategorySkill


class EdgeHunterCategorySkill(TypedDict):
    """Category evidence over the full uncapped piled-side S/A/B holder allocation. It never changes signal
    membership, ordering, routing, or sizing."""
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


class EdgeHunterMarketContext(TypedDict):
    """Metadata frozen with the read generation. Values are nullable when the provider/canonical source has
    no value; no title-based inference or current-clock fallback."""
    # Normalized machine/provider league identity. Known wire/tag aliases normalize; other provider identities
    # match exact lowercase keys.
    league: str | None
    # Exact provider series slug, usable in series_slugs selection.
    series_slug: str | None
    # Exact provider sports_market_type, usable in market_types selection.
    market_type: str | None
    # Exact local canonical metadata writer market_canonical.updated_at. This is not a provider observation clock;
    # null means unavailable. Format: date-time.
    metadata_updated_at: str | None


class EdgeHunterSelection(TypedDict, total=False):
    """Normalized requested selection axes. Only requested axes appear; omitted for unselected defaults.
    Arrays are nonempty, sorted and deduplicated. OR within an axis, AND across axes."""
    kind: Literal["sports", "esports"] | str
    # Resolved legacy canonical bucket or non_sport for an unmappable category.
    category: str
    # Canonical sport buckets, including Esports and Table Tennis, matched case-insensitively. Unknown names and
    # league aliases such as NFL are rejected in sports; use category for legacy bucket aliases or leagues for
    # exact ...
    sports: list[str]
    # Normalized machine/provider league identities, such as nfl, cfb, nba, epl, cs2, lol, dota2 or valorant.
    # Known wire/tag aliases normalize; other provider keys match exact lowercase identity. This is separate from
    # ...
    leagues: list[str]
    # Exact provider sports_market_type values. This is an open provider taxonomy, distinct from exact market IDs.
    # Read market_context.market_type; missing selected metadata excludes the row.
    market_types: list[str]
    # Exact market selections. Raw provider condition IDs and the existing mkt_-prefixed aliases normalize to raw
    # IDs. Unknown well-formed IDs return an empty result.
    condition_ids: list[str]
    # Exact provider event slugs. Use event_slug returned on the row; no title or slug-prefix guessing.
    event_slugs: list[str]
    # Exact provider series slugs. Read market_context.series_slug; a missing selected series excludes the row.
    series_slugs: list[str]


class _EdgeHunterSignalsResponseRequired(TypedDict):
    object: Literal["list"]
    view: Literal["signals"]
    data: list[EdgeHunterRankedSignal]
    has_more: bool
    meta: ResponseMeta


class EdgeHunterSignalsResponse(_EdgeHunterSignalsResponseRequired, total=False):
    """Full Edge Hunter signals list envelope. The view literal distinguishes advanced collections,
    including empty pages."""
    next_cursor: str
    total: int
    # Normalized axes requested with a selector or category; omitted on an unselected default read.
    selection: EdgeHunterSelection


class EdgeHunterRankedSignal(TypedDict):
    """One ranked pre-game sports market where graded sharp money is piled on one side, with required-
    status category evidence from partial forward-observed Polymarket fills."""
    # The side profitable wallets hold, as a provider-backed display label. Canonical spelling of piled_side
    # (#16310), same value: when provider group context is unavailable it may remain a bare Yes/No/Over/Under, so
    # do not ...
    side: str | None
    # UTC time at which the snapshot that ranked this row was computed. Canonical spelling of signal_created_at
    # (#16310), same value. Format: date-time.
    ranked_at: str
    # Recorded side backing score; higher values indicate stronger backing.
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
    category: Literal["Basketball", "Football", "Baseball", "Hockey", "MMA", "Boxing", "Soccer", "Cricket", "Golf", "Tennis", "Esports", "Racing", "Table Tennis", "Pickleball", None] | str | None
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
    top_grade: Literal["S", "A", "B", None] | str | None
    # Canonical sharp-money score (yes_usd - no_usd)/(yes_usd + no_usd) in [-1, 1] (piled-yes positive, piled-no
    # negative). Deprecated (#16310): `side_share` is the canonical spelling and carries the same value; this key
    # ...
    smart_score: float | None
    # Cumulative provider taker volume in shares, not cash or dollars.
    volume: float | None
    # Aggregate recent flow direction on the market; null when unavailable.
    net_side: Literal["BUY", "SELL", None] | str | None
    # Recorded conviction score; higher values indicate stronger conviction.
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
    # Recorded side ordering score; higher values sort first.
    directional_rank_score: float
    category_skill: EdgeHunterCategorySkill
    # 1-based rank within the (min_grade-filtered) ranked result.
    rank: int
    # Required nullable frozen metadata context. Null only during the legacy-generation transition; selected reads
    # require sidecar readiness and fail closed with 503 instead.
    market_context: EdgeHunterMarketContext | None


class _EdgeHunterObservationsResponseRequired(TypedDict):
    object: Literal["list"]
    view: Literal["observations"]
    data: list[EdgeHunterObservation]
    has_more: bool
    # Pass as cursor for the next page. Always sent; null on the last page.
    next_cursor: str | None
    # Completion time of the shared observation snapshot pinned by the cursor. Format: date-time.
    snapshot_as_of: str
    # True when an operational failure or unknown provider-board, holder, directional, reconciliation, or internal
    # completeness state made this snapshot partial. This is snapshot-wide and can retain degradation that the ...
    degraded: bool
    # Sorted, deduplicated causes from the canonical all-sports generation, unchanged by category, cohort or
    # selectors; with admission=most_held_48h, from that selection's generation. Empty exactly when degraded is
    # false. ...
    degradation_reasons: list[EdgeHunterObservationDegradationReason]
    coverage: EdgeHunterObservationCoverage
    funnel: EdgeHunterFunnelReport
    meta: ResponseMeta


class EdgeHunterObservationsResponse(_EdgeHunterObservationsResponseRequired, total=False):
    """Full Edge Hunter observations list envelope. Required degradation_reasons explains the source-
    generation verdict; required coverage distinguishes source input, intentional capacity exclusions,
    source emissions, incomplete holder scans, selection and the returned page. The view literal
    distinguishes advanced collections, including empty pages."""
    # Normalized axes requested with a selector or category; omitted on an unselected default read.
    selection: EdgeHunterSelection
    # Echoes the opt-in admission rule a request named; omitted on a default read. When present, data, funnel,
    # coverage, degraded and degradation_reasons describe that selection, not the default one.
    admission: Literal["most_held_48h"]
    # cohort=wider_holder only, for the default selection and for admission=most_held_48h: markets that had a
    # wider_holder card in an earlier snapshot of the same selection, have none in this one, and have not kicked
    # off. ...
    departures: list[EdgeHunterObservationDeparture]
    # The ranked_at of the view=signals snapshot whose listed markets this snapshot excluded from wider_holder as
    # primary_slate_candidate. The refresh that computed this snapshot read it as it started, so it can be one ...
    signals_as_of: str | None


class EdgeHunterObservation(TypedDict):
    """One explicitly observation-only holder-pile measurement. It is evidence for cohort evaluation, not
    an execution instruction, and is isolated from the funded Edge Hunter signals view."""
    # The side profitable wallets hold, as a provider-backed display label. Canonical spelling of piled_side
    # (#16310), same value: when provider group context is unavailable it may remain a bare Yes/No/Over/Under, so
    # do not ...
    side: str | None
    # Recorded side backing score; higher values indicate stronger backing.
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
    # Which evaluation place in its sport the row took this refresh. most_held: a wider_holder place for up to 8
    # markets per sport kicking off within 24 hours, most graded holders first, kept until kickoff while the
    # holder ...
    admitted_by: Literal["most_held", "soonest_kickoff", "most_held_48h"] | str
    # Always true. This row must not be routed to an order executor.
    observation_only: Literal[True]
    # Nullable provider-backed piled-outcome display label. When provider group context is unavailable, it may
    # remain a bare Yes/No/Over/Under; do not use it alone as participant identity. Deprecated (#16310): `side` is
    # the ...
    piled_side: str | None
    # Provider binary-column selector: 0 selects outcome_yes/token_id_yes; 1 selects outcome_no/token_id_no. It
    # does not identify home/away or a participant. Use piled_side together with title/event context for display.
    piled_outcome_index: Literal[0, 1] | int
    # Aggregate piled-side market midpoint recorded at observed_at. This is an observation price mark, not a
    # wallet entry cost.
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
    # Cumulative provider taker volume in shares, not cash or dollars.
    volume: float
    # Recorded conviction score; higher values indicate stronger conviction.
    conviction_score: float
    # Whether the provider holder page came from the shared cache or a live provider read.
    provider_read_source: Literal["cached", "live"] | str
    # True only when the provider page read for each outcome token listed every holder of that token. Observation
    # collection reads one 100-row page per token; a token with more holders stays incomplete. False means holder
    # ...
    holder_scan_complete: bool
    # Proven provider holder observation time. A warm cache hit uses only the original provider completion time
    # from its companion metadata, never cache-read time. A wider_holder or emerging_pile row whose holder read
    # did not ...
    holder_snapshot_at: str | None
    # Truthful state of the directional read, which classifies each graded holder by its fresh synced legs across
    # the game's markets and, when holder_scan_complete is true, by Polymarket's currentValue on both outcomes of
    # ...
    directional_status: Literal["available", "unknown_ungrouped", "unknown_stale", "unavailable"] | str
    one_way_holder_count: int | None
    hedged_holder_count: int | None
    one_way_graded_usd: float | None
    directional_confidence: float | None
    # Recorded side ordering score; higher values sort first.
    directional_rank_score: float
    # 1-based rank within this observation cohort and snapshot.
    rank: int
    # Required nullable frozen metadata context. Null only during the legacy-generation transition; selected reads
    # require sidecar readiness and fail closed with 503 instead.
    market_context: EdgeHunterMarketContext | None


class EdgeHunterObservationDegradationReason(TypedDict):
    """One observed cause of operational degradation in the canonical all-sports observation generation.
    Reasons are independent of the one-terminal-per-input funnel and remain unchanged through category,
    cohort and selector projection. Intentional capacity limits and an unconfigured upcoming source are
    not degradation reasons."""
    # Recorded producer cause. holder_scan_incomplete is retired and no longer emitted: the one-page holder read
    # is an intentional bound, disclosed by each row's holder_scan_complete and by
    # coverage.incomplete_holder_markets, ...
    reason: Literal["holder_scan_incomplete", "live_source_stale", "directional_unavailable", "funnel_unreconciled", "board_live_unavailable", "board_upcoming_unavailable", "provider_unavailable", "holder_deadline_unavailable", "holder_computation_unavailable", "missing_stored_market", "price_unavailable", "in_play_stale_observed", "in_play_directional_unavailable", "internal_unclassified", "board_source_unavailable", "board_deadline_unavailable"] | str
    # Canonical sport for the recorded cause; null only for generation-wide evidence without a sport attribution.
    sport: str | None


class EdgeHunterObservationCoverage(TypedDict):
    """Measured coverage of the frozen canonical observation generation and this requested page. For sports
    and esports reads, the first four counts remain global through category, cohort and all selectors;
    with admission=most_held_48h they count that selection's generation, where every wider_holder
    candidate it did not take is capacity_limited. They are neither a census of all provider markets nor
    a count of successfully evaluated holders. Selected and returned counts describe the requested
    projection. An unmappable legacy category synthesizes a zero-work empty generation with all six
    counts zero ..."""
    # Sum of canonical source-generation funnel input across all sports, before category, cohort or selector
    # projection.
    input_markets: int
    # Canonical source-generation input assigned capacity_limited. These markets were intentionally outside the
    # bounded holder-work admission and are not missing emitted rows. It includes the admitted pregame
    # wider_holder ...
    capacity_limited_markets: int
    # All wider_holder and in_play observations emitted in the canonical source generation, before cohort,
    # category or selector projection. Emerging pile is an overlapping projection and does not add source
    # emissions.
    emitted_observations: int
    # Canonical source-generation markets whose attempted holder scan did not establish complete coverage,
    # including incomplete scans that did not emit an observation. Collection reads one 100-row page per token, so
    # a market ...
    incomplete_holder_markets: int
    # Observations matching the requested cohort, category, selectors and applicable pinned projection cutoff
    # before pagination.
    selected_observations: int
    # Observation rows on this page; equals data.length.
    returned_observations: int


class EdgeHunterFunnelReport(TypedDict):
    """Per-sport accountable funnel for the full observation snapshot, returned on every page."""
    sports: list[EdgeHunterSportFunnelReport]


class EdgeHunterSportFunnelReport(TypedDict):
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
    # slug (nfl, cfb, nba, wnba, euroleague-basketball, ncaa-basketball, cwbb, nhl, mls, valorant, league-of-
    # legends, ...
    board_upcoming_unavailable_scopes: list[Literal["category", "nfl", "cfb", "nba", "wnba", "euroleague-basketball", "ncaa-basketball", "cwbb", "nhl", "mls", "valorant", "league-of-legends", "counter-strike-2", "dota-2", "registry", "union", "wave"] | str]
    # Stored-universe rows plus provider-board rows missing from storage.
    input: int
    # Sparse counts over the closed 25-value terminal vocabulary: outside_horizon, resolved, provider_closed,
    # provider_excluded, invalid_market, missing_token, missing_stored_market, not_provider_live, ...
    terminals: dict[str, int]
    # Sum of every sparse terminal count.
    terminal_total: int
    # True exactly when input equals terminal_total.
    reconciled: bool


class EdgeHunterObservationDeparture(TypedDict):
    """A market whose wider_holder card left this selection before kickoff, with why it left."""
    # Raw Polymarket condition id.
    condition_id: str
    event_slug: str | None
    # Canonical sport bucket the departed card carried.
    category: Literal["Basketball", "Football", "Baseball", "Hockey", "MMA", "Boxing", "Soccer", "Cricket", "Golf", "Tennis", "Esports", "Racing", "Table Tennis", "Pickleball"] | str
    # The departed card's admitted_by: most_held_48h on an admission=most_held_48h response.
    admitted_by: Literal["most_held", "soonest_kickoff", "most_held_48h"] | str
    # Kickoff the departed card carried, in UTC. The entry leaves the list once it passes. Format: date-time.
    game_start_time: str
    # The departed card's observed_at: when its last evaluation finished. Format: date-time.
    last_observed_at: str
    # snapshot_as_of of the first snapshot of this selection without the card. Format: date-time.
    departed_at: str
    # Why the market has no card: its terminal in this selection's funnel in the snapshot it left, and while that
    # terminal reports a read that did not finish (holder_deadline_unavailable, provider_unavailable, ...
    reason: EdgeHunterObservationTerminalReason


# Closed 25-value terminal-reason vocabulary for the accountable Edge Hunter observation funnel. capacity_limited
# is intentional bounded provider-work admission and does not itself set the snapshot degraded.
# board_source_unavailable is a completed board-source failure; board_deadline_unavailable ...
EdgeHunterObservationTerminalReason = Union[Literal["outside_horizon", "resolved", "provider_closed", "provider_excluded", "invalid_market", "missing_token", "missing_stored_market", "not_provider_live", "board_source_unavailable", "board_deadline_unavailable", "primary_slate_candidate", "zero_indexed_holder_research", "capacity_limited", "provider_unavailable", "holder_deadline_unavailable", "holder_computation_unavailable", "holder_scan_incomplete", "no_current_graded_holder", "split_holder_pile", "price_unavailable", "wider_holder_emitted", "in_play_emitted", "in_play_stale_observed", "in_play_directional_unavailable", "internal_unclassified"], str]
