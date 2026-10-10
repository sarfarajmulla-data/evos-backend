class FCFS:
    def schedule(self, requests: list[dict]) -> list[dict]:
        scheduled = []
        for index, request in enumerate(sorted(requests, key=lambda entry: entry.get("requested_at", ""))):
            scheduled.append({
                "vehicle_id": request.get("vehicle_id"),
                "scheduled_at": request.get("requested_at"),
                "score": 65.0 - index * 2.5,
                "confidence": 72.0,
                "algorithm": "fcfs",
            })
        return scheduled
