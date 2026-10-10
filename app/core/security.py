"""Security helpers and API-key validation hooks for the EVOS backend."""


def validate_api_key(api_key: str | None) -> bool:
    return bool(api_key)
