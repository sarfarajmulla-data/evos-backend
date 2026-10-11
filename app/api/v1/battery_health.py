from fastapi import APIRouter

from app.services.battery_health_service import BatteryHealthService

router = APIRouter()
service = BatteryHealthService()


@router.get("/battery-health/{vehicle_id}")
async def battery_health(vehicle_id: str) -> dict:
    return service.assess(vehicle_id=vehicle_id)
