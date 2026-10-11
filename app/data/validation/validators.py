from app.core.exceptions import DatasetValidationError


def validate_dataset_records(records: list[dict]) -> list[dict]:
    if not isinstance(records, list):
        raise DatasetValidationError("Dataset payload must be a list of record objects.")
    if not records:
        raise DatasetValidationError("Dataset contains no records.")
    for record in records:
        if not isinstance(record, dict):
            raise DatasetValidationError("Each dataset record must be a JSON object.")
    return records
