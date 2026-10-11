from fastapi import APIRouter

from app.schemas.common import ExplainabilityInput

router = APIRouter()


@router.post("/explainability/decision")
async def explain_decision(payload: ExplainabilityInput) -> dict:
    reason = "renewables are high and the vehicle is sufficiently charged, so the schedule is favoured for the next available slot."
    return {"vehicle_id": payload.vehicle_id, "reason": reason, "confidence": 88.0}
