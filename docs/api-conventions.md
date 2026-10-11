# API conventions

- Base path: `/api/v1`.
- JSON field names use `snake_case`.
- Timestamps are ISO-8601 with timezone information.
- Energy is kWh; power is kW; percentages are 0-100 unless named `share`.
- Successful collection endpoints return arrays; command endpoints return a
  result object with algorithm or scenario metadata.
- Invalid input returns FastAPI's validation response. Domain failures use
  `{ "error": "...", "code": "..." }`.
- Unknown resources return HTTP 404. Health endpoints are unauthenticated;
  protected write endpoints must acquire authentication before production use.
