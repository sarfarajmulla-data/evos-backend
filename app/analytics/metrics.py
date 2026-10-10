class AnalyticsMetrics:
    def compute_daily_sustainability(self, renewable_kwh: float, total_kwh: float) -> float:
        return round((renewable_kwh / total_kwh) * 100.0, 2) if total_kwh else 0.0
