class RuleBasedScheduler:
    def schedule(self, requests: list[dict]) -> list[dict]:
        scheduled = []
        for index, request in enumerate(sorted(requests, key=lambda entry: (-int(entry.get("priority", 0)), float(entry.get("estimated_energy_kwh", 0))))):
            scheduled.append({
                "vehicle_id": request.get("vehicle_id"),
                "scheduled_at": request.get("requested_at"),
                "score": 78.0 + index * 1.5,
                "confidence": 82.0,
                "algorithm": "rule_based",
            })
        return scheduled
