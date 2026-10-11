# Dataset connectivity matrix

| Source | Official documentation | Adapter/status | Access/env | Live | E2E import |
|---|---|---|---|---|---|
| ACN-Data | https://ev.caltech.edu/dataset.html | Registry + fixture adapter | `ACN_USERNAME`, `ACN_PASSWORD` | BLOCKED_CREDENTIALS | NOT_TESTED |
| ElaadNL | https://www.elaad.nl/ | Registry + fixture adapter | `ELAADNL_API_KEY` | BLOCKED_CREDENTIALS | NOT_TESTED |
| Pecan Street Dataport | https://dataport.pecanstreet.org/ | Registry + fixture adapter | `PECAN_STREET_API_KEY` and approval | BLOCKED_ACCESS_APPROVAL | NOT_TESTED |
| NASA battery aging | NASA PCoE repository | Registry + file-import interface | Published download | NOT_TESTED | NOT_TESTED |
| NASA POWER | https://power.larc.nasa.gov/docs/ | `app.data.adapters.nasa_power.NASAPowerAdapter` | `NASA_POWER_API_KEY` if required | VERIFIED_LIVE (public request) | PASS_FIXTURE_ONLY |
| PVGIS | https://joint-research-centre.ec.europa.eu/pvgis-online-tool_en | `app.data.adapters.pvgis.PVGISAdapter` | Public API | VERIFIED_LIVE (public request) | PASS_FIXTURE_ONLY |
| Historical tariffs | Provider is region-dependent | CSV import interface | User-supplied CSV | BLOCKED_ACCESS_APPROVAL | PASS_FIXTURE_ONLY |
| Grid carbon intensity | Provider is region-dependent | CSV import interface | User-supplied regional CSV | BLOCKED_ACCESS_APPROVAL | PASS_FIXTURE_ONLY |

The registry exposes configured credentials, connection/import timestamps, row
counters, provenance, and verification flags without performing large network
downloads during health checks. No external source is labelled connected
without a real connection and import test.

External source licenses, rate limits, schemas, and credentials must be
confirmed before enabling ingestion.
