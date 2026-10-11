# Frontend Integration Guide

Start the backend with `uvicorn app.main:app --reload` and use
`http://localhost:8000` as the local API base URL. The bundled Vite frontend
uses `http://localhost:8443` by default. OpenAPI is available at
`/openapi.json` and interactive docs at `/docs` outside production.

## Health and datasets

- `GET /health` and `GET /ready` are process probes.
- `GET /api/v1/datasets/status` returns all eight registered external sources
  and truthful configuration/verification fields.
- `GET /api/v1/datasets/import-history` returns local import records.
- `POST /api/v1/datasets/import?name=fleet_summary` imports the bundled demo
  fixture. This is labelled demo/fixture data, not measured campus data.

## Operations

- `GET /api/v1/scenario` returns the editable illustrative campus assumptions.
- `PUT /api/v1/scenario` updates a scenario for the running process.
- `GET /api/v1/chargers` returns charger compatibility and power metadata.
- `POST /api/v1/simulations/run` executes a bounded energy-balance simulation.
- `POST /api/v1/scheduler/plan` runs FCFS, rule-based, and EVOS heuristics on
  the same request list.
- `GET /api/v1/energy/summary` and
  `POST /api/v1/sustainability/metrics` expose supported energy metrics.
- `GET /api/v1/battery-health/{vehicle_id}` provides a documented
  rule-based assessment; it is not a measured battery diagnosis.
- `POST /api/v1/confidence/score` returns provisional weighted evidence
  components and explicitly marks infeasible decisions.
- `POST /api/v1/explainability/decision` returns the decision explanation.
- `POST /api/v1/evaluation/compare` compares supplied algorithm results.

## Conventions and security

Timestamps are ISO-8601, energy is kWh, power is kW, and percentages are
0-100 unless a field is named `share`. Validation errors are returned by
FastAPI; domain errors use `error` and `code`. The current local scaffold
does not enforce user authentication. Do not expose write endpoints
publicly until the deployment adds authentication, role authorization, and
rate limiting. Configure frontend origins with `CORS_ORIGINS`; never put
service-role or database credentials in the frontend.
