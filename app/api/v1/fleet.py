from fastapi import APIRouter, HTTPException

from app.services.fleet_service import FleetService

router = APIRouter()
service = FleetService()


@router.get("/fleet/vehicles")
async def get_fleet_vehicles() -> list[dict]:
    return service.list_vehicles()


@router.get("/fleet/vehicles/{vehicle_id}")
async def get_vehicle(vehicle_id: str) -> dict:
    vehicle = service.get_vehicle(vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail={"code": "vehicle_not_found", "vehicle_id": vehicle_id})
    return vehicle
