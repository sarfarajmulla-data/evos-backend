from datetime import datetime

from pydantic import BaseModel, Field


class DatasetImportRequest(BaseModel):
    name: str = Field(..., description="Dataset name to load")
    source: str | None = Field(default=None, description="Public data source")


class DatasetSummary(BaseModel):
    name: str
    source: str
    rows: int
    columns: list[str]


class FleetVehicleOut(BaseModel):
    vehicle_id: str
    name: str
    battery_capacity_kwh: float
    state_of_charge: float
    location: str


class SchedulingRequest(BaseModel):
    vehicle_id: str
    requested_at: datetime
    estimated_energy_kwh: float = Field(..., gt=0, le=1000)
    priority: int = Field(default=1, ge=0, le=10)
    duration_hours: float = Field(default=1.0, gt=0, le=24)
    departure_at: datetime | None = None
    state_of_charge: float = Field(default=50.0, ge=0, le=100)
    charger_type: str = "ac"


class SchedulingResult(BaseModel):
    vehicle_id: str
    scheduled_at: datetime
    algorithm: str
    score: float
    confidence: float


class EnergySummary(BaseModel):
    solar_kwh: float
    grid_kwh: float
    storage_kwh: float
    total_kwh: float
    renewable_share: float


class BatteryHealthResponse(BaseModel):
    vehicle_id: str
    health_percent: float
    degradation_percent: float
    recommended_action: str


class SimulationInput(BaseModel):
    scenario_name: str = "campus_day"
    horizon_hours: int = Field(default=24, ge=1, le=168)
    demand_kwh: float = Field(default=250.0, ge=0)
    renewable_kwh: float = Field(default=180.0, ge=0)
    fleet_size: int = Field(default=20, ge=0, le=1000)
    timestep_minutes: int = Field(default=60, ge=5, le=60)
    grid_import_limit_kw: float = Field(default=80.0, ge=0)
    battery_capacity_kwh: float = Field(default=100.0, ge=0)
    battery_reserve_percent: float = Field(default=20.0, ge=0, le=100)
    charger_count: int = Field(default=6, ge=0, le=1000)
    charger_power_kw: float = Field(default=7.4, ge=0)


class ExplainabilityInput(BaseModel):
    vehicle_id: str
    current_soc: float
    tariff: float
    renewable_available: float
    urgency: int = 1
