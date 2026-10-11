from __future__ import annotations

import csv
import hashlib
import json
import uuid
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from io import TextIOBase
from typing import Any

from app.core.provenance import Provenance


@dataclass
class ImportRecord:
    import_id: str
    source: str
    status: str
    started_at: str
    ended_at: str | None = None
    records_retrieved: int = 0
    records_accepted: int = 0
    records_rejected: int = 0
    duplicates_skipped: int = 0
    records_persisted: int = 0
    failure_category: str | None = None
    error_summary: str | None = None
    provenance: str = Provenance.IMPORTED_EXTERNAL
    records: list[dict[str, Any]] = field(default_factory=list)


class IngestionFramework:
    """Small, retry-safe ingestion core used by file and fixture adapters."""

    def __init__(self) -> None:
        self._history: list[ImportRecord] = []
        self._fingerprints: set[str] = set()

    def import_records(
        self,
        source: str,
        records: Iterable[dict[str, Any]],
        required_columns: set[str] | None = None,
        provenance: Provenance = Provenance.IMPORTED_EXTERNAL,
    ) -> ImportRecord:
        started = datetime.now(UTC).isoformat()
        result = ImportRecord(
            import_id=str(uuid.uuid4()),
            source=source,
            status="RUNNING",
            started_at=started,
            provenance=provenance,
        )
        try:
            for record in records:
                result.records_retrieved += 1
                if not isinstance(record, dict) or (
                    required_columns and not required_columns.issubset(record)
                ):
                    result.records_rejected += 1
                    continue
                fingerprint = self._fingerprint(source, record)
                if fingerprint in self._fingerprints:
                    result.duplicates_skipped += 1
                    continue
                self._fingerprints.add(fingerprint)
                result.records.append(dict(record))
                result.records_accepted += 1
            result.records_persisted = result.records_accepted
            result.status = "SUCCEEDED"
        except Exception as exc:  # noqa: BLE001 - record all ingestion failures
            result.status = "FAILED"
            result.failure_category = "VALIDATION_OR_PERSISTENCE"
            result.error_summary = str(exc)
        result.ended_at = datetime.now(UTC).isoformat()
        self._history.append(result)
        return result

    def import_file(
        self,
        source: str,
        handle: TextIOBase,
        file_type: str,
        required_columns: set[str] | None = None,
    ) -> ImportRecord:
        try:
            if file_type == "csv":
                records = list(csv.DictReader(handle))
            elif file_type == "json":
                payload = json.load(handle)
                records = payload if isinstance(payload, list) else payload.get("records", [])
            else:
                raise ValueError("file_type must be csv or json")
            return self.import_records(source, records, required_columns, Provenance.IMPORTED_EXTERNAL)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            result = ImportRecord(
                import_id=str(uuid.uuid4()),
                source=source,
                status="FAILED",
                started_at=datetime.now(UTC).isoformat(),
                ended_at=datetime.now(UTC).isoformat(),
                failure_category="RETRIEVAL_OR_PARSE",
                error_summary=str(exc),
            )
            self._history.append(result)
            return result

    def history(self) -> list[dict[str, Any]]:
        return [self._as_dict(item) for item in reversed(self._history)]

    @staticmethod
    def _fingerprint(source: str, record: dict[str, Any]) -> str:
        payload = json.dumps(record, sort_keys=True, default=str)
        return hashlib.sha256(f"{source}:{payload}".encode()).hexdigest()

    @staticmethod
    def _as_dict(record: ImportRecord) -> dict[str, Any]:
        return {
            key: value for key, value in record.__dict__.items() if key != "records"
        }
