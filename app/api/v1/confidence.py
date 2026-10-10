from fastapi import APIRouter

from app.services.confidence_service import ConfidenceService

router = APIRouter()
service = ConfidenceService()


@router.post("/confidence/score")
async def calculate_confidence(renewable_share: float = 0.72, urgency: int = 2, tariff: float = 0.17, soc: float = 76.0) -> dict:
    return service.score(renewable_share=renewable_share, urgency=urgency, tariff=tariff, soc=soc)
