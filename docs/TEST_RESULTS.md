# Test results

The local suite is the source of truth for this revision:

```text
pytest -q
19 passed
```

The suite covers health routes, scheduling algorithms, core services,
ingestion idempotency, simulation constraints, and mocked adapter parsing. CI
also runs `python -m compileall app` and `pip check`. External connectivity,
container deployment, and production data quality are not claimed by these
tests.

Additional acceptance checks:

```text
python -m compileall -q app migrations        PASS
ruff check app tests migrations                PASS
mypy app --explicit-package-bases --ignore-missing-imports  PASS
alembic upgrade head (isolated SQLite)         PASS
FastAPI smoke routes                           PASS
Docker image build                             NOT TESTED: Docker unavailable
```

Public no-credential requests retrieved valid response shapes from NASA POWER
and PVGIS for latitude 12.9716 and longitude 77.5946. Those responses were
parsed by the adapter tests; no provider data was persisted to the project
database.
