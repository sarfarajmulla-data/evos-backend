from fastapi import APIRouter

from app.schemas.common import SimulationInput
from app.services.simulation_service import SimulationService

router = APIRouter()
service = SimulationService()


@router.post("/simulations/run")
async def run_simulation(payload: SimulationInput) -> dict:
    return service.run(
        scenario_name=payload.scenario_name,
        horizon_hours=payload.horizon_hours,
        demand_kwh=payload.demand_kwh,
        renewable_kwh=payload.renewable_kwh,
        fleet_size=payload.fleet_size,
        timestep_minutes=payload.timestep_minutes,
        grid_import_limit_kw=payload.grid_import_limit_kw,
        battery_capacity_kwh=payload.battery_capacity_kwh,
        battery_reserve_percent=payload.battery_reserve_percent,
        charger_count=payload.charger_count,
        charger_power_kw=payload.charger_power_kw,
    )
