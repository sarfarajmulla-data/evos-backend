class ForecastService:
    def predict_demand(self, historical_values: list[float], horizon_hours: int = 6) -> dict:
        if not historical_values:
            historical_values = [18.0, 20.5, 24.2, 19.8, 22.1]
        avg = sum(historical_values) / len(historical_values)
        forecast = avg * (1.0 + (horizon_hours / 24.0) * 0.08)
        return {"horizon_hours": horizon_hours, "forecast_kwh": round(forecast, 2), "baseline_mean_kwh": round(avg, 2)}
