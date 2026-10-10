from datetime import datetime


def normalize_dataset(records: list[dict]) -> list[dict]:
    normalized = []
    for row in records:
        normalized_row = dict(row)
        for key in ("energy_kwh", "soc", "solar_kwh", "grid_kwh", "storage_kwh"):
            if key in normalized_row and normalized_row[key] is not None:
                normalized_row[key] = float(normalized_row[key])
        if "timestamp" in normalized_row and isinstance(normalized_row["timestamp"], str):
            normalized_row["timestamp"] = datetime.fromisoformat(normalized_row["timestamp"])
        normalized.append(normalized_row)
    return normalized
