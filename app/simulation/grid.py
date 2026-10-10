class GridModel:
    def estimate_grid_import(self, demand_kwh: float, renewable_kwh: float) -> float:
        return max(0.0, demand_kwh - renewable_kwh)
