from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class EnergyReading(Base):
    __tablename__ = "energy_readings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    source: Mapped[str] = mapped_column(String, default="grid")
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    energy_kwh: Mapped[float] = mapped_column(Float, default=0.0)
    price_per_kwh: Mapped[float] = mapped_column(Float, default=0.0)


class ForecastRecord(Base):
    __tablename__ = "forecast_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    target: Mapped[str] = mapped_column(String, default="demand")
    horizon_hours: Mapped[int] = mapped_column(Integer, default=24)
    forecast_kwh: Mapped[float] = mapped_column(Float, default=0.0)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
