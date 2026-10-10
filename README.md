# EVOS Backend

[![CI](https://github.com/sarfarajmulla-data/evos-backend/actions/workflows/ci.yml/badge.svg)](https://github.com/sarfarajmulla-data/evos-backend/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

EVOS (Electric Vehicles Operations and Sustainability) is a backend for electric-vehicle fleet scheduling, battery health analysis, renewable coordination, and sustainability reporting.

## Verified status
This repository is currently a functional backend scaffold with local verification, not a completed production system for all live external datasets. The code is locally tested and exposes a working API, but live dataset integrations and Supabase connectivity remain blocked or unimplemented without credentials and a configured external project.

## Features
- FastAPI app with a versioned `/api/v1` API
- Health, readiness, and dataset-status endpoints
- FCFS, rule-based, and EVOS-style scheduling heuristics
- Energy summary, forecasting, confidence scoring, and evaluation services
- SQLite-backed local startup for development
- Docker and `.env.example` configuration
- Automated pytest suite for local validation

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python -m compileall .
pytest -q
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API routes
- `GET /`
- `GET /health`
- `GET /ready`
- `GET /docs`
- `GET /openapi.json`
- `GET /api/v1/health`
- `GET /api/v1/status`
- `GET /api/v1/datasets`
- `GET /api/v1/datasets/status`
- `GET /api/v1/fleet/vehicles`
- `GET /api/v1/fleet/vehicles/{vehicle_id}`
- `GET /api/v1/scheduler/demo`
- `POST /api/v1/scheduler/plan`
- `GET /api/v1/energy/summary`
- `GET /api/v1/battery-health/{vehicle_id}`
- `GET /api/v1/forecasting/demand`
- `POST /api/v1/confidence/score`
- `POST /api/v1/explainability/decision`
- `POST /api/v1/simulations/run`
- `POST /api/v1/evaluation/compare`

## Database and external integration notes
- Local development uses SQLite by default (`DATABASE_URL=sqlite:///./evos.db`).
- Supabase/PostgreSQL configuration is supported via environment variables but not live-verified without a real project.
- External datasets are represented as adapter/status modules and documented in `docs/DATASET_CONNECTIVITY_MATRIX.md`.
- No real credentials or secrets are committed to the repo.

## Documentation
- [System design](docs/system-design.md)
- [Architecture](docs/architecture.md)
- [API conventions](docs/api-conventions.md) and [OpenAPI](docs/openapi.yaml)
- [Data model](docs/data-model.md), [permissions](docs/permissions.md), and
  [testing](docs/testing.md)
- [Hosting](docs/hosting.md), [monitoring](docs/monitoring.md), and
  [runbooks](docs/runbooks/deploy.md)
- [Backend audit](docs/BACKEND_AUDIT.md)
- [Dataset connectivity matrix](docs/DATASET_CONNECTIVITY_MATRIX.md)
- [Internal dataset audit](docs/INTERNAL_DATASET_AUDIT.md)
- [API endpoint audit](docs/API_ENDPOINT_AUDIT.md)
- [Security audit](docs/SECURITY_AUDIT.md)
- [Test results](docs/TEST_RESULTS.md)
- `docs/FRONTEND_INTEGRATION.md`

## Limitations
This project is not yet a fully complete production backend against the original EVOS specification. It has passed local smoke and unit tests, but external integration, live data ingestion, Supabase persistence, and full scheduler validation remain blocked pending credentials and a configured provider environment.
