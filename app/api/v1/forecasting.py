from fastapi import APIRouter, Query

from app.services.forecast_service import ForecastService

router = APIRouter()
service = ForecastService()


@router.get("/forecasting/demand")
async def predict_demand(horizon_hours: int = Query(default=6, ge=1, le=168)) -> dict:
    return service.predict_demand([18.0, 21.2, 24.1, 19.9, 22.7], horizon_hours=horizon_hours)
