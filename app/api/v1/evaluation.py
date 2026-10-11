from fastapi import APIRouter

from app.services.evaluation_service import EvaluationService

router = APIRouter()
service = EvaluationService()


@router.post("/evaluation/compare")
async def compare_algorithms() -> dict:
    payload = {
        "fcfs": [{"score": 72.0}, {"score": 69.0}],
        "rule_based": [{"score": 83.5}, {"score": 79.1}],
        "evos_intelligent": [{"score": 92.8}, {"score": 91.4}],
    }
    return service.compare_algorithms(payload)
