class BatteryHealthService:
    def assess(self, vehicle_id: str, soc: float = 70.0, degradation_factor: float = 0.12) -> dict:
        health_percent = max(0.0, min(100.0, 100.0 - degradation_factor * 100.0))
        recommended_action = "monitor" if health_percent > 80 else "schedule maintenance"
        return {
            "vehicle_id": vehicle_id,
            "health_percent": round(health_percent, 2),
            "degradation_percent": round(degradation_factor * 100.0, 2),
            "recommended_action": recommended_action,
        }
