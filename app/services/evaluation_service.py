class EvaluationService:
    def compare_algorithms(self, algorithms: dict) -> dict:
        scores = {name: sum(item.get("score", 0) for item in values) for name, values in algorithms.items()}
        if not scores:
            return {"leader": None, "scores": {}}
        return {
            "leader": max(scores, key=lambda name: scores[name]),
            "scores": scores,
        }
