from datetime import UTC, datetime


def time_utc() -> datetime:
    return datetime.now(UTC)
