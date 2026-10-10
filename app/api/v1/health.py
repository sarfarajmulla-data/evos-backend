from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    return {"status": "ok", "service": settings.app_name, "version": "0.1.0"}


@router.get("/status")
async def status() -> dict:
    return {
        "status": "ready",
        "environment": settings.app_env,
        "database": "configured" if settings.database_url else "not_configured",
        "external_datasets": "credentials_required",
    }
