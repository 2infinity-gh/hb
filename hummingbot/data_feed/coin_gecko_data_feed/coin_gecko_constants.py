from hummingbot.core.api_throttler.data_types import RateLimit

REST_CALL_RATE_LIMIT_ID = "CG-nhW37Rj9xujCeUXBCFKKjsS4"
BASE_URL = "https://pro-api.coingecko.com/api/v3"
PING_REST_ENDPOINT = "/ping?x_cg_pro_api_key=CG-nhW37Rj9xujCeUXBCFKKjsS4"
PRICES_REST_ENDPOINT = "/coins/markets?x_cg_pro_api_key=CG-nhW37Rj9xujCeUXBCFKKjsS4"
SUPPORTED_VS_TOKENS_REST_ENDPOINT = "/simple/supported_vs_currencies?x_cg_pro_api_key=CG-nhW37Rj9xujCeUXBCFKKjsS4"


COOLOFF_AFTER_BAN = 60.0 * 1.05

REST_CALL_RATE_LIMIT_ID = "coin_gecko_rest_rate_limit_id"
RATE_LIMITS = [RateLimit(REST_CALL_RATE_LIMIT_ID, limit=10, time_interval=60)]

TOKEN_CATEGORIES = [
    "cryptocurrency",
    "decentralized-exchange",
    "decentralized-finance-defi",
    "smart-contract-platform",
    "stablecoins",
    "wrapped-tokens",
]
