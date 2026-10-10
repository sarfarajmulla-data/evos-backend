# Threat model

Assets include fleet identifiers, charging schedules, energy telemetry,
provider credentials, and database contents. Threats include leaked secrets,
unauthorized schedule manipulation, malicious dataset payloads, denial of
service through oversized requests, and dependency vulnerabilities.

Controls include environment-only secrets, input validation, bounded forecast
horizons, restricted CORS, least-privilege database credentials, dependency
updates, CI tests, and private vulnerability reporting. Authentication,
rate limiting, tenant isolation, and production audit logging remain mandatory
before internet exposure.
