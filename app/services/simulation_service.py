from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SimulationResult:
    demand_kwh: float
    solar_used_kwh: float
    grid_import_kwh: float
    storage_discharge_kwh: float
    storage_charge_kwh: float
    unserved_kwh: float
    peak_grid_kw: float
    final_storage_kwh: float


class SimulationService:
    """Deterministic campus energy balance with explicit hard constraints."""

    def run(
        self,
        scenario_name: str = "campus_day",
        horizon_hours: int = 24,
        demand_kwh: float = 250.0,
        renewable_kwh: float = 180.0,
        fleet_size: int = 20,
        timestep_minutes: int = 60,
        grid_import_limit_kw: float = 80.0,
        battery_capacity_kwh: float = 100.0,
        battery_reserve_percent: float = 20.0,
        charger_count: int = 6,
        charger_power_kw: float = 7.4,
    ) -> dict:
        if horizon_hours <= 0 or timestep_minutes <= 0:
            raise ValueError("horizon_hours and timestep_minutes must be positive")
        if battery_reserve_percent > 100:
            raise ValueError("battery_reserve_percent cannot exceed 100")

        steps = max(1, horizon_hours * 60 // timestep_minutes)
        step_hours = timestep_minutes / 60
        demand_step = demand_kwh / steps
        solar_step = max(0.0, renewable_kwh) / steps
        max_charging_power = max(0.0, charger_count * charger_power_kw)
        storage = battery_capacity_kwh * battery_reserve_percent / 100
        reserve = storage
        result = SimulationResult(demand_kwh, 0, 0, 0, 0, 0, 0, storage)

        for _ in range(steps):
            direct_solar = min(demand_step, solar_step)
            remaining = demand_step - direct_solar
            surplus = solar_step - direct_solar
            charge_room = max(0.0, battery_capacity_kwh - storage)
            storage_charge = min(charge_room, surplus)
            storage += storage_charge
            remaining_power_limited = max_charging_power * step_hours
            storage_discharge = min(max(0.0, storage - reserve), remaining, remaining_power_limited)
            storage -= storage_discharge
            remaining -= storage_discharge
            grid_power = min(remaining / step_hours if step_hours else 0.0, grid_import_limit_kw)
            grid_energy = grid_power * step_hours
            unserved = max(0.0, remaining - grid_energy)

            result.solar_used_kwh += direct_solar
            result.storage_charge_kwh += storage_charge
            result.storage_discharge_kwh += storage_discharge
            result.grid_import_kwh += grid_energy
            result.unserved_kwh += unserved
            result.peak_grid_kw = max(result.peak_grid_kw, grid_power)

        result.final_storage_kwh = storage
        served = result.demand_kwh - result.unserved_kwh
        renewable_share = result.solar_used_kwh / served if served else 0.0
        charger_capacity = max_charging_power * horizon_hours
        readiness = 100.0 if result.unserved_kwh == 0 else max(
            0.0, 100.0 * served / result.demand_kwh
        ) if result.demand_kwh else 100.0
        return {
            "scenario_name": scenario_name,
            "provenance": "SIMULATED",
            "horizon_hours": horizon_hours,
            "timestep_minutes": timestep_minutes,
            "fleet_size": fleet_size,
            "demand_kwh": round(result.demand_kwh, 4),
            "solar_available_kwh": round(renewable_kwh, 4),
            "solar_used_kwh": round(result.solar_used_kwh, 4),
            "grid_import_kwh": round(result.grid_import_kwh, 4),
            "storage_charge_kwh": round(result.storage_charge_kwh, 4),
            "storage_discharge_kwh": round(result.storage_discharge_kwh, 4),
            "final_storage_kwh": round(result.final_storage_kwh, 4),
            "unserved_kwh": round(result.unserved_kwh, 4),
            "peak_grid_kw": round(result.peak_grid_kw, 4),
            "renewable_share": round(renewable_share * 100, 2),
            "vehicle_readiness_percent": round(readiness, 2),
            "charger_capacity_kwh": round(charger_capacity, 4),
            "feasible": result.unserved_kwh == 0,
            "constraints": {
                "grid_import_limit_kw": grid_import_limit_kw,
                "battery_capacity_kwh": battery_capacity_kwh,
                "battery_reserve_kwh": reserve,
                "charger_count": charger_count,
                "charger_power_kw": charger_power_kw,
            },
        }
