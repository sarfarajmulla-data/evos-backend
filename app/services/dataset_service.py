from app.data.ingestion.dataset_loader import load_demo_dataset
from app.data.transformations.normalize import normalize_dataset
from app.data.validation.validators import validate_dataset_records
from app.data.ingestion.framework import IngestionFramework
from app.services.dataset_registry import dataset_status


class DatasetService:
    def __init__(self) -> None:
        self.ingestion = IngestionFramework()

    def list_datasets(self) -> list[dict]:
        return [
            {"name": "fleet_summary", "source": "mock/public/fleet_summary", "rows": 3, "columns": ["vehicle_id", "battery_kwh", "state_of_charge"]},
            {"name": "energy_mix", "source": "mock/public/energy_mix", "rows": 3, "columns": ["timestamp", "solar_kwh", "grid_kwh", "storage_kwh"]},
        ] + [
            {
                "name": item["name"],
                "source": item["official_url"] or item["access_method"],
                "rows": item["records_retrieved"],
                "columns": [],
                "status": item["last_import_status"],
                "provenance": item["provenance"],
            }
            for item in dataset_status()
        ]

    def import_dataset(self, name: str, source: str | None = None) -> dict:
        payload = load_demo_dataset(name)
        records = payload.get("rows", [])
        validated = validate_dataset_records(records)
        normalized = normalize_dataset(validated)
        result = self.ingestion.import_records(
            source=source or "mock/public",
            records=normalized,
            required_columns={"vehicle_id", "battery_kwh", "state_of_charge"}
            if name == "fleet_summary"
            else None,
        )
        return {
            "name": name,
            "source": source or "mock",
            "rows": len(normalized),
            "columns": list(normalized[0].keys()) if normalized else [],
            "import_id": result.import_id,
            "status": result.status,
            "duplicates_skipped": result.duplicates_skipped,
            "records_persisted": result.records_persisted,
            "provenance": result.provenance,
        }

    def status(self) -> list[dict]:
        return dataset_status()

    def history(self) -> list[dict]:
        return self.ingestion.history()
