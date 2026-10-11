from __future__ import annotations

from typing import Any

import httpx


class PVGISAdapter:
    base_url = "https://re.jrc.ec.europa.eu/api/v5_2/seriescalc"

    def __init__(self, timeout: float = 30.0, client: httpx.Client | None = None) -> None:
        self.timeout = timeout
        self.client = client

    def fetch_hourly(self, latitude: float, longitude: float, year: int) -> dict[str, Any]:
        if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
            raise ValueError("latitude or longitude is outside valid bounds")
        params: dict[str, str | int | float] = {
            "lat": latitude,
            "lon": longitude,
            "startyear": year,
            "endyear": year,
            "pvcalculation": 0,
            "outputformat": "json",
        }
        response = (self.client or httpx.Client(timeout=self.timeout)).get(self.base_url, params=params)
        response.raise_for_status()
        payload = response.json()
        hourly = payload.get("outputs", {}).get("hourly")
        if not isinstance(hourly, list):
            raise TypeError("PVGIS response is missing hourly output")
        return {
            "source": "PVGIS",
            "provenance": "IMPORTED_EXTERNAL",
            "latitude": latitude,
            "longitude": longitude,
            "observations": hourly,
        }
