from pydantic import BaseModel, Field


class ScenarioRequest(BaseModel):
    scenario_id: str = "custom"
    name: str = "Custom scenario"
    assumptions: dict[str, float | int] = Field(default_factory=dict)


class SustainabilityRequest(BaseModel):
    solar_kwh: float | None = Field(default=None, ge=0)
    grid_kwh: float | None = Field(default=None, ge=0)
    delivered_kwh: float | None = Field(default=None, ge=0)
    carbon_g_per_kwh: float | None = Field(default=None, ge=0)
    tariff_per_kwh: float | None = Field(default=None, ge=0)
