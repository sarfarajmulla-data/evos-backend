from fastapi import APIRouter

from app.services.dataset_service import DatasetService

router = APIRouter()
service = DatasetService()


@router.get("/datasets")
async def list_datasets() -> list[dict]:
    return service.list_datasets()


@router.get("/datasets/status")
async def dataset_status_endpoint() -> list[dict]:
    return service.status()


@router.get("/datasets/import-history")
async def import_history() -> list[dict]:
    return service.history()


@router.post("/datasets/import")
async def import_dataset(name: str, source: str | None = None) -> dict:
    return service.import_dataset(name=name, source=source)
