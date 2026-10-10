# Security audit

## Controls present

- Secrets are represented only as environment variables.
- `.env` and database artifacts are ignored.
- CORS origins are configurable and credentials are disabled.
- Forecast horizons are bounded.
- Unknown fleet resources return 404 rather than success-shaped data.
- CI runs dependency consistency checks.

## Required before production

Add authentication, role enforcement, rate limiting, request-size limits,
structured audit logs, dependency scanning, PostgreSQL least-privilege roles,
secret rotation, and a provider-backed penetration test.

The current API is suitable for local/frontend contract development, not
untrusted public exposure. Supabase service-role credentials remain server
configuration only; no live Supabase project was configured or contacted.
