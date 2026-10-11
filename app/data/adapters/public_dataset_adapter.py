from dataclasses import dataclass, field
from typing import Any


@dataclass
class PublicDatasetAdapter:
    name: str
    source: str
    columns: list[str] = field(default_factory=list)

    def load_demo(self) -> list[dict[str, Any]]:
        base = [
            {"timestamp": "2024-06-01T00:00:00Z", "vehicle_id": "EV-01", "energy_kwh": 12.4, "soc": 78.0},
            {"timestamp": "2024-06-01T01:00:00Z", "vehicle_id": "EV-02", "energy_kwh": 18.7, "soc": 63.0},
            {"timestamp": "2024-06-01T02:00:00Z", "vehicle_id": "EV-03", "energy_kwh": 15.2, "soc": 70.0},
        ]
        return base
