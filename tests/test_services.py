from app.services.battery_health_service import BatteryHealthService
from app.services.confidence_service import ConfidenceService
from app.services.energy_service import EnergyService
from app.services.forecast_service import ForecastService
from app.services.scheduler_service import SchedulerService


def test_energy_summary():
    summary = EnergyService().summarize(100.0, 50.0, 20.0)
    assert summary["total_kwh"] == 170.0
    assert summary["renewable_share"] == 0.7058823529411765


def test_battery_health_assessment():
    summary = BatteryHealthService().assess("EV-01", soc=74.0, degradation_factor=0.09)
    assert summary["vehicle_id"] == "EV-01"
    assert summary["health_percent"] > 80


def test_forecast_service():
    result = ForecastService().predict_demand([10.0, 15.0, 20.0], horizon_hours=12)
    assert result["horizon_hours"] == 12
    assert result["forecast_kwh"] > 0


def test_confidence_score():
    result = ConfidenceService().score(renewable_share=0.8, urgency=3, tariff=0.12, soc=82)
    assert 0 <= result["score_percent"] <= 100


def test_scheduler_service_outputs_algorithms():
    result = SchedulerService().build_demo_plan()
    assert set(result["algorithms"].keys()) == {"fcfs", "rule_based", "evos_intelligent"}
