# System design

## Requirements

EVOS accepts fleet charging requests, ranks them with deterministic
algorithms, and exposes energy, battery, forecast, simulation, and
explainability results as JSON. It must be repeatable, observable, timezone
aware, and safe to run without external credentials.

## Users and scope

Primary users are fleet operators, energy analysts, and frontend clients.
The current scope is a modular API and local simulation engine. Authentication,
multi-tenant billing, autonomous charger control, and production ETL are
out of scope until their provider and operational contracts are approved.
