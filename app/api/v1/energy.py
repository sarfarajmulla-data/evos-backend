from fastapi import APIRouter

from app.services.energy_service import EnergyService

router = APIRouter()
service = EnergyService()


@router.get("/energy/summary")
async def energy_summary() -> dict:
    return service.summarize()
