from datetime import datetime, timezone


def time_utc() -> datetime:
    return datetime.now(timezone.utc)
