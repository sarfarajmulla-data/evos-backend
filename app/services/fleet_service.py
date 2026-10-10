from app.repositories.fleet_repository import list_demo_vehicles


class FleetService:
    def list_vehicles(self) -> list[dict]:
        return list_demo_vehicles()

    def get_vehicle(self, vehicle_id: str) -> dict | None:
        for item in list_demo_vehicles():
            if item["vehicle_id"] == vehicle_id:
                return item
        return None
