from __future__ import annotations

from datetime import date
from typing import Any

import httpx


class NASAPowerAdapter:
    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"

    def __init__(self, timeout: float = 30.0, client: httpx.Client | None = None) -> None:
        self.timeout = timeout
        self.client = client

    def fetch_daily(self, latitude: float, longitude: float, start: date, end: date) -> dict[str, Any]:
        if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
            raise ValueError("latitude or longitude is outside valid bounds")
        params: dict[str, str | int | float] = {
            "parameters": "ALLSKY_SFC_SW_DWN",
            "community": "RE",
            "longitude": longitude,
            "latitude": latitude,
            "start": start.strftime("%Y%m%d"),
            "end": end.strftime("%Y%m%d"),
            "format": "JSON",
        }
        response = (self.client or httpx.Client(timeout=self.timeout)).get(self.base_url, params=params)
        response.raise_for_status()
        payload = response.json()
        parameter = payload.get("properties", {}).get("parameter", {}).get("ALLSKY_SFC_SW_DWN")
        if not isinstance(parameter, dict):
            raise TypeError("NASA POWER response is missing solar parameter data")
        units = payload.get("parameters", {}).get("ALLSKY_SFC_SW_DWN", {}).get("units")
        return {
            "source": "NASA_POWER",
            "provenance": "IMPORTED_EXTERNAL",
            "latitude": latitude,
            "longitude": longitude,
            "units": units,
            "observations": [{"date": key, "solar_kwh_m2": value} for key, value in parameter.items() if value != -999],
        }
