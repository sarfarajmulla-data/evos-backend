from fastapi import APIRouter

from app.api.v1.battery_health import router as battery_health_router
from app.api.v1.confidence import router as confidence_router
from app.api.v1.datasets import router as datasets_router
from app.api.v1.energy import router as energy_router
from app.api.v1.evaluation import router as evaluation_router
from app.api.v1.explainability import router as explainability_router
from app.api.v1.fleet import router as fleet_router
from app.api.v1.forecasting import router as forecasting_router
from app.api.v1.health import router as health_router
from app.api.v1.maintenance import router as maintenance_router
from app.api.v1.operations import router as operations_router
from app.api.v1.scheduler import router as scheduler_router
from app.api.v1.simulations import router as simulations_router
from app.core.config import settings

api_router = APIRouter(prefix=settings.api_v1_prefix)
api_router.include_router(health_router)
api_router.include_router(datasets_router)
api_router.include_router(fleet_router)
api_router.include_router(scheduler_router)
api_router.include_router(energy_router)
api_router.include_router(battery_health_router)
api_router.include_router(forecasting_router)
api_router.include_router(maintenance_router)
api_router.include_router(operations_router)
api_router.include_router(confidence_router)
api_router.include_router(explainability_router)
api_router.include_router(simulations_router)
api_router.include_router(evaluation_router)
