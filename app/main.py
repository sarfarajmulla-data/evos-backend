from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exceptions import EVOSException
from app.db import Base, engine

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Electric vehicle fleet operations, scheduling, and sustainability analytics API.",
    docs_url="/docs" if settings.app_env != "production" else None,
    redoc_url="/redoc" if settings.app_env != "production" else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.exception_handler(EVOSException)
async def evos_exception_handler(_: Request, exc: EVOSException) -> JSONResponse:
    return JSONResponse(status_code=400, content={"error": exc.message, "code": exc.code})


@app.get("/")
async def root():
    return {
        "app": settings.app_name,
        "status": "ok",
        "api_prefix": settings.api_v1_prefix,
    }


@app.get("/health", tags=["operations"])
async def health():
    return {"status": "ok", "service": settings.app_name, "version": "0.1.0"}


@app.get("/ready", tags=["operations"])
async def ready():
    return {"status": "ready", "environment": settings.app_env}


app.include_router(api_router)
