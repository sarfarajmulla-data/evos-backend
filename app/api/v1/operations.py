from fastapi import APIRouter

from app.schemas.operations import ScenarioRequest, SustainabilityRequest
from app.services.operations_service import OperationsService

router = APIRouter()
service = OperationsService()


@router.get("/scenario")
async def get_scenario() -> dict:
    return service.get_scenario()


@router.put("/scenario")
async def update_scenario(payload: ScenarioRequest) -> dict:
    return service.set_scenario(payload.model_dump())


@router.get("/chargers")
async def list_chargers() -> list[dict]:
    return service.chargers()


@router.post("/sustainability/metrics")
async def sustainability_metrics(payload: SustainabilityRequest) -> dict:
    return service.sustainability(**payload.model_dump())
