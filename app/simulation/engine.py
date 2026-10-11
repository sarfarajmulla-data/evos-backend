class SimulationEngine:
    def run(self, demand_kwh: float, renewable_kwh: float, fleet_size: int = 12) -> dict:
        return {
            "demand_kwh": demand_kwh,
            "renewable_kwh": renewable_kwh,
            "fleet_size": fleet_size,
            "renewable_share": round((renewable_kwh / (demand_kwh + renewable_kwh)) * 100.0, 2) if demand_kwh + renewable_kwh else 0.0,
        }
