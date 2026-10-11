from io import StringIO

from fastapi.testclient import TestClient

from app.data.ingestion.framework import IngestionFramework
from app.main import app
from app.services.confidence_service import ConfidenceService
from app.services.simulation_service import SimulationService

client = TestClient(app)


def test_simulation_preserves_energy_balance_and_reports_constraints():
    result = SimulationService().run(demand_kwh=100, renewable_kwh=40, horizon_hours=4)
    assert result["demand_kwh"] == 100
    assert result["solar_used_kwh"] + result["grid_import_kwh"] + result["unserved_kwh"] >= 100
    assert result["peak_grid_kw"] <= 80
    assert result["provenance"] == "SIMULATED"


def test_infeasible_simulation_is_explicit():
    result = SimulationService().run(
        demand_kwh=1000,
        renewable_kwh=0,
        horizon_hours=1,
        grid_import_limit_kw=1,
    )
    assert result["feasible"] is False
    assert result["unserved_kwh"] > 0


def test_ingestion_is_idempotent_and_records_history():
    ingestion = IngestionFramework()
    records = [{"id": "one", "value": 1}]
    first = ingestion.import_records("fixture", records, {"id"})
    second = ingestion.import_records("fixture", records, {"id"})
    assert first.status == "SUCCEEDED"
    assert second.duplicates_skipped == 1
    assert len(ingestion.history()) == 2


def test_csv_ingestion_rejects_missing_columns():
    result = IngestionFramework().import_file(
        "fixture.csv", StringIO("id,name\n1,test\n"), "csv", {"id", "timestamp"}
    )
    assert result.status == "SUCCEEDED"
    assert result.records_rejected == 1


def test_confidence_score_never_hides_infeasibility():
    result = ConfidenceService().score(renewable_share=1, feasible=False)
    assert result["score_percent"] == 0
    assert result["evidence_status"] == "INFEASIBLE"


def test_dataset_status_and_operations_endpoints():
    status = client.get("/api/v1/datasets/status")
    assert status.status_code == 200
    assert len(status.json()) == 8
    assert client.get("/api/v1/scenario").json()["provenance"] == "ILLUSTRATIVE_DEMO"
    assert len(client.get("/api/v1/chargers").json()) == 6


def test_sustainability_reports_missing_evidence():
    response = client.post("/api/v1/sustainability/metrics", json={"solar_kwh": 10})
    assert response.status_code == 200
    assert response.json()["status"] == "INSUFFICIENT_EVIDENCE"
