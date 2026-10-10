from typing import ClassVar


class ConfidenceService:
    """Transparent evidence score; this is not a calibrated probability."""

    weights: ClassVar[dict[str, float]] = {
        "data_quality": 0.30,
        "model_reliability": 0.25,
        "constraint_verification": 0.30,
        "decision_stability": 0.15,
    }

    def score(
        self,
        renewable_share: float,
        urgency: int = 1,
        tariff: float = 0.18,
        soc: float = 70.0,
        data_quality: float | None = None,
        model_reliability: float = 0.75,
        constraint_verification: float = 1.0,
        decision_stability: float = 0.75,
        feasible: bool = True,
    ) -> dict:
        factors = {
            "data_quality": max(0.0, min(1.0, renewable_share if data_quality is None else data_quality)),
            "model_reliability": max(0.0, min(1.0, model_reliability)),
            "constraint_verification": max(0.0, min(1.0, constraint_verification)),
            "decision_stability": max(0.0, min(1.0, decision_stability)),
            "renewable_share": max(0.0, min(1.0, renewable_share)),
            "urgency": max(0.0, min(1.0, urgency / 5)),
            "tariff": max(0.0, min(1.0, 1.0 - tariff)),
            "soc": max(0.0, min(1.0, soc / 100.0)),
        }
        weighted = sum(self.weights[name] * factors[name] for name in self.weights)
        if not feasible:
            weighted = 0.0
        return {
            "score_percent": round(weighted * 100.0, 2),
            "calibrated_probability": False,
            "evidence_status": "SUFFICIENT" if feasible else "INFEASIBLE",
            "weights": self.weights,
            "factors": factors,
        }
