class FleetSimulationModel:
    def load_fleet(self, fleet_size: int) -> dict:
        return {"fleet_size": fleet_size, "vehicles": [f"EV-{idx:02d}" for idx in range(1, fleet_size + 1)]}
