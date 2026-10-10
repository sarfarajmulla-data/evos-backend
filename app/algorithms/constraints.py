def feasible_schedule(request: dict, battery_capacity_kwh: float) -> bool:
    energy_needed = float(request.get("estimated_energy_kwh", 0.0))
    return energy_needed <= battery_capacity_kwh * 0.9
