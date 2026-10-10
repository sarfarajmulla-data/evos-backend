from datetime import date

import httpx

from app.data.adapters.nasa_power import NASAPowerAdapter
from app.data.adapters.pvgis import PVGISAdapter


def test_nasa_power_adapter_normalizes_response():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "properties": {"parameter": {"ALLSKY_SFC_SW_DWN": {"20240101": 4.5}}},
                "parameters": {"ALLSKY_SFC_SW_DWN": {"units": "kW-hr/m^2/day"}},
            },
            request=request,
        )

    result = NASAPowerAdapter(client=httpx.Client(transport=httpx.MockTransport(handler))).fetch_daily(
        12.9, 77.5, date(2024, 1, 1), date(2024, 1, 1)
    )
    assert result["observations"] == [{"date": "20240101", "solar_kwh_m2": 4.5}]


def test_pvgis_adapter_validates_hourly_output():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"outputs": {"hourly": [{"time": "20200101:0030", "G(i)": 0}]}}, request=request)

    result = PVGISAdapter(client=httpx.Client(transport=httpx.MockTransport(handler))).fetch_hourly(12.9, 77.5, 2020)
    assert result["observations"][0]["time"] == "20200101:0030"
