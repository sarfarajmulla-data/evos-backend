# Data model

The current model layer represents vehicles, energy readings, charging
requests, and forecast records. A production migration should add tenant,
audit, ingestion-run, and idempotency keys before accepting multi-tenant
writes.

Core relationships:

```text
fleet_vehicle 1 --- * charging_request
fleet_vehicle 1 --- * battery_reading
energy_reading * --- 1 forecast_window
dataset_import 1 --- * normalized_record
```

All timestamps should be stored in UTC and all energy values should carry
explicit kWh or kW units.
