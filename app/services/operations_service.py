from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

DEFAULT_SCENARIO = {
    "scenario_id": "illustrative-campus",
    "name": "Illustrative campus",
    "provenance": "ILLUSTRATIVE_DEMO",
    "assumptions": {
        "shuttle_buses": 6,
        "utility_vehicles": 10,
        "service_vans": 4,
        "dc_chargers": 2,
        "dc_charger_power_kw": 30.0,
        "ac_chargers": 4,
        "ac_charger_power_kw": 7.4,
        "solar_capacity_kwp": 100.0,
        "stationary_battery_capacity_kwh": 100.0,
        "stationary_battery_power_kw": 50.0,
        "stationary_battery_reserve_percent": 20.0,
        "grid_import_limit_kw": 80.0,
    },
}


class OperationsService:
    def __init__(self) -> None:
        self.scenario: dict[str, Any] = DEFAULT_SCENARIO

    def get_scenario(self) -> dict:
        return self.scenario

    def set_scenario(self, scenario: dict) -> dict:
        self.scenario = {
            "scenario_id": scenario.get("scenario_id", "custom"),
            "name": scenario.get("name", "Custom scenario"),
            "provenance": "ILLUSTRATIVE_DEMO",
            "assumptions": scenario["assumptions"],
        }
        return self.scenario

    def chargers(self) -> list[dict]:
        assumptions: dict[str, Any] = self.scenario["assumptions"]
        chargers = []
        for index in range(int(assumptions["dc_chargers"])):
            chargers.append({"charger_id": f"dc-{index + 1}", "type": "dc", "power_kw": assumptions["dc_charger_power_kw"], "available": True})
        for index in range(int(assumptions["ac_chargers"])):
            chargers.append({"charger_id": f"ac-{index + 1}", "type": "ac", "power_kw": assumptions["ac_charger_power_kw"], "available": True})
        return chargers

    def maintenance_alerts(self) -> list[dict]:
        return [
            {
                "alert_id": "battery-balance-ev-02",
                "vehicle_id": "EV-02",
                "severity": "medium",
                "kind": "RULE_BASED_ALERT",
                "message": "Battery balancing recommended",
                "provenance": "CALCULATED",
                "created_at": datetime.now(UTC).isoformat(),
            }
        ]

    def sustainability(self, solar_kwh: float | None, grid_kwh: float | None, delivered_kwh: float | None, carbon_g_per_kwh: float | None = None, tariff_per_kwh: float | None = None) -> dict:
        missing = [name for name, value in {"solar_kwh": solar_kwh, "grid_kwh": grid_kwh, "delivered_kwh": delivered_kwh}.items() if value is None]
        if missing:
            return {"status": "INSUFFICIENT_EVIDENCE", "missing_inputs": missing, "provenance": "CALCULATED"}
        assert solar_kwh is not None
        assert grid_kwh is not None
        assert delivered_kwh is not None
        total = solar_kwh + grid_kwh
        return {
            "status": "CALCULATED",
            "provenance": "CALCULATED",
            "solar_kwh": solar_kwh,
            "grid_kwh": grid_kwh,
            "energy_delivered_kwh": delivered_kwh,
            "renewable_share": solar_kwh / total if total else 0.0,
            "electricity_cost": grid_kwh * tariff_per_kwh if tariff_per_kwh is not None else None,
            "operational_emissions_gco2e": grid_kwh * carbon_g_per_kwh if carbon_g_per_kwh is not None else None,
            "missing_inputs": [],
        }
