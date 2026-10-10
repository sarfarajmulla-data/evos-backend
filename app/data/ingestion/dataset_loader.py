from app.data.adapters.public_dataset_adapter import PublicDatasetAdapter


def load_demo_dataset(name: str) -> dict:
    dataset_map = {
        "fleet_summary": PublicDatasetAdapter("fleet_summary", "mock/public/fleet_summary", ["vehicle_id", "battery_kwh", "state_of_charge"]).load_demo(),
        "energy_mix": PublicDatasetAdapter("energy_mix", "mock/public/energy_mix", ["timestamp", "solar_kwh", "grid_kwh", "storage_kwh"]).load_demo(),
    }
    return {"name": name, "rows": dataset_map.get(name, [])}
