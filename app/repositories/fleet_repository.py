from typing import Any


def list_demo_vehicles() -> list[dict[str, Any]]:
    return [
        {"vehicle_id": "EV-01", "name": "Campus Van 01", "battery_capacity_kwh": 88.0, "state_of_charge": 78.0, "location": "north-bay"},
        {"vehicle_id": "EV-02", "name": "Campus Van 02", "battery_capacity_kwh": 95.0, "state_of_charge": 63.0, "location": "hub"},
        {"vehicle_id": "EV-03", "name": "Campus Van 03", "battery_capacity_kwh": 72.0, "state_of_charge": 71.0, "location": "south-bay"},
    ]
