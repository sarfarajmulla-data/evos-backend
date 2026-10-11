from app.algorithms.evos_optimizer import EVOSOptimizer
from app.algorithms.fcfs import FCFS
from app.algorithms.rule_based import RuleBasedScheduler


def test_fcfs_schedule_orders_by_arrival():
    requests = [
        {"vehicle_id": "EV-02", "requested_at": "2024-06-01T02:00:00Z", "estimated_energy_kwh": 18.0, "priority": 2},
        {"vehicle_id": "EV-01", "requested_at": "2024-06-01T01:00:00Z", "estimated_energy_kwh": 22.5, "priority": 1},
    ]
    scheduled = FCFS().schedule(requests)
    assert scheduled[0]["vehicle_id"] == "EV-01"


def test_rule_based_scheduler_prefers_higher_priority():
    requests = [
        {"vehicle_id": "EV-01", "requested_at": "2024-06-01T01:00:00Z", "estimated_energy_kwh": 22.5, "priority": 1},
        {"vehicle_id": "EV-02", "requested_at": "2024-06-01T02:00:00Z", "estimated_energy_kwh": 18.0, "priority": 4},
    ]
    scheduled = RuleBasedScheduler().schedule(requests)
    assert scheduled[0]["vehicle_id"] == "EV-02"


def test_evos_optimizer_returns_ranked_output():
    requests = [{"vehicle_id": "EV-03", "requested_at": "2024-06-01T03:00:00Z", "estimated_energy_kwh": 30.0, "priority": 3}]
    scheduled = EVOSOptimizer().schedule(requests)
    assert len(scheduled) == 1
    assert scheduled[0]["algorithm"] == "evos_intelligent"
