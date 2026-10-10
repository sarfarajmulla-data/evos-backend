from typing import Any

from app.core.config import settings

DATASET_REGISTRY: dict[str, dict[str, Any]] = {
    "acn_data": {
        "official_url": "https://ev.caltech.edu/dataset.html",
        "purpose": "EV charging sessions and charging behaviour validation",
        "adapter": "app.data.adapters.public_dataset_adapter.PublicDatasetAdapter",
        "access_method": "Official download/API subject to provider access",
        "required_env": ["ACN_USERNAME", "ACN_PASSWORD"],
    },
    "elaadnl": {
        "official_url": "https://www.elaad.nl/",
        "purpose": "Supplementary EV charging behaviour",
        "adapter": "app.data.adapters.public_dataset_adapter.PublicDatasetAdapter",
        "access_method": "Provider download/API where available",
        "required_env": ["ELAADNL_API_KEY"],
    },
    "pecan_street": {
        "official_url": "https://dataport.pecanstreet.org/",
        "purpose": "Energy, EV, solar, and storage research data",
        "adapter": "app.data.adapters.public_dataset_adapter.PublicDatasetAdapter",
        "access_method": "Licensed Dataport access",
        "required_env": ["PECAN_STREET_API_KEY"],
    },
    "nasa_battery_aging": {
        "official_url": "https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/",
        "purpose": "Battery ageing and degradation calibration",
        "adapter": "app.data.adapters.public_dataset_adapter.PublicDatasetAdapter",
        "access_method": "Published file download",
        "required_env": [],
    },
    "nasa_power": {
        "official_url": "https://power.larc.nasa.gov/docs/",
        "purpose": "Solar-resource and meteorological inputs",
        "adapter": "app.data.adapters.nasa_power.NASAPowerAdapter",
        "access_method": "NASA POWER API",
        "required_env": ["NASA_POWER_API_KEY"],
    },
    "pvgis": {
        "official_url": "https://joint-research-centre.ec.europa.eu/pvgis-online-tool_en",
        "purpose": "PV performance estimates",
        "adapter": "app.data.adapters.pvgis.PVGISAdapter",
        "access_method": "PVGIS API",
        "required_env": [],
    },
    "tariffs": {
        "official_url": None,
        "purpose": "Regional historical electricity tariffs",
        "adapter": "CSV import interface",
        "access_method": "Documented user-supplied CSV",
        "required_env": [],
    },
    "carbon_intensity": {
        "official_url": None,
        "purpose": "Region-specific grid carbon intensity",
        "adapter": "CSV import interface",
        "access_method": "Documented user-supplied CSV",
        "required_env": [],
    },
}


def dataset_status() -> list[dict]:
    configured = {
        "acn_data": bool(settings.acn_username and settings.acn_password),
        "elaadnl": bool(settings.elaadnl_api_key),
        "pecan_street": bool(settings.pecan_street_api_key),
        "nasa_battery_aging": True,
        "nasa_power": bool(settings.nasa_power_api_key),
        "pvgis": True,
        "tariffs": False,
        "carbon_intensity": False,
    }
    return [
        {
            "name": name,
            **metadata,
            "configured": configured[name],
            "live_access_verified": False,
            "end_to_end_import_verified": False,
            "last_connection_attempt": None,
            "last_successful_connection": None,
            "last_successful_import": None,
            "last_import_status": "NOT_TESTED",
            "records_retrieved": 0,
            "records_accepted": 0,
            "records_rejected": 0,
            "records_persisted": 0,
            "last_error_category": "BLOCKED_CREDENTIALS" if not configured[name] else None,
            "provenance": "IMPORTED_EXTERNAL",
        }
        for name, metadata in DATASET_REGISTRY.items()
    ]
