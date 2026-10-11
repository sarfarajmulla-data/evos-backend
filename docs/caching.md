# Caching

The current service is deterministic and does not require a cache for local
operation. If production traffic requires caching, use Redis for short-lived
forecast and dataset metadata responses with explicit TTLs. Never cache
credentials, authorization decisions, or mutable scheduling commands.
