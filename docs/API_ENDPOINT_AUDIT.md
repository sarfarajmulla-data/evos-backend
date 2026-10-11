# API endpoint audit

| Surface | Status | Evidence |
|---|---|---|
| Root and docs | Implemented | FastAPI app |
| Health/readiness | Implemented | `/health`, `/ready`, `/api/v1/health` |
| Fleet | Implemented locally | In-memory repository |
| Scheduling | Implemented locally | Three deterministic algorithms |
| Energy/forecasting | Implemented locally | Service tests |
| Simulation/evaluation | Implemented locally | Service routes |
| Dataset import | Demo-only | No live provider |
| Authentication/RBAC | Not implemented | Production blocker |
| Dataset status/history | Implemented locally | `/datasets/status`, `/datasets/import-history` |
| Scenario/changers | Implemented locally | `/scenario`, `/chargers` |
| Sustainability | Implemented locally | `/sustainability/metrics` |
