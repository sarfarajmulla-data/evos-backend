from fastapi import APIRouter

from app.services.operations_service import OperationsService

router = APIRouter()
service = OperationsService()


@router.get("/maintenance/alerts")
async def maintenance_alerts() -> list[dict]:
    return service.maintenance_alerts()
