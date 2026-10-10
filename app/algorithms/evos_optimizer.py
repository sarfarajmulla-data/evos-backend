class EVOSOptimizer:
    def schedule(self, requests: list[dict]) -> list[dict]:
        scheduled = []
        for index, request in enumerate(sorted(requests, key=lambda entry: (-(int(entry.get("priority", 0)) * 2 + float(entry.get("estimated_energy_kwh", 0)) / 10), ))):
            combined_score = 80.0 + (request.get("priority", 0) * 2.5) - (index * 1.8)
            scheduled.append({
                "vehicle_id": request.get("vehicle_id"),
                "scheduled_at": request.get("requested_at"),
                "score": round(combined_score, 2),
                "confidence": 90.0,
                "algorithm": "evos_intelligent",
            })
        return scheduled
