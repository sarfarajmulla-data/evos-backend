from fastapi import APIRouter

from app.schemas.common import SchedulingRequest
from app.services.scheduler_service import SchedulerService

router = APIRouter()
service = SchedulerService()


@router.get("/scheduler/demo")
async def demo_schedule() -> dict:
    return service.build_demo_plan()


@router.post("/scheduler/plan")
async def plan_schedule(requests: list[SchedulingRequest]) -> dict:
    payload = [item.model_dump() for item in requests]
    return service.plan(payload)
