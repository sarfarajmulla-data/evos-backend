from datetime import datetime, timedelta

from app.algorithms.evos_optimizer import EVOSOptimizer
from app.algorithms.fcfs import FCFS
from app.algorithms.rule_based import RuleBasedScheduler


class SchedulerService:
    def plan(self, requests: list[dict]) -> dict:
        fcfs = FCFS().schedule(requests)
        rule = RuleBasedScheduler().schedule(requests)
        evos = EVOSOptimizer().schedule(requests)
        return {
            "algorithms": {
                "fcfs": fcfs,
                "rule_based": rule,
                "evos_intelligent": evos,
            },
            "recommended": evos[0] if evos else None,
        }

    def build_demo_plan(self) -> dict:
        now = datetime.utcnow()
        demo_requests = [
            {"vehicle_id": "EV-01", "requested_at": now, "estimated_energy_kwh": 22.5, "priority": 2, "duration_hours": 1.5},
            {"vehicle_id": "EV-02", "requested_at": now + timedelta(hours=1), "estimated_energy_kwh": 18.0, "priority": 4, "duration_hours": 2.0},
            {"vehicle_id": "EV-03", "requested_at": now + timedelta(hours=2), "estimated_energy_kwh": 29.0, "priority": 1, "duration_hours": 1.0},
        ]
        return self.plan(demo_requests)
