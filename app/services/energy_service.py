class EnergyService:
    def summarize(self, solar_kwh: float = 150.0, grid_kwh: float = 85.0, storage_kwh: float = 40.0) -> dict:
        total = solar_kwh + grid_kwh + storage_kwh
        renewable_share = (solar_kwh + storage_kwh) / total if total else 0.0
        return {
            "solar_kwh": solar_kwh,
            "grid_kwh": grid_kwh,
            "storage_kwh": storage_kwh,
            "total_kwh": total,
            "renewable_share": renewable_share,
        }
