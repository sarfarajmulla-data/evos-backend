from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class FleetVehicle(Base):
    __tablename__ = "fleet_vehicles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    vehicle_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    battery_capacity_kwh: Mapped[float] = mapped_column(Float, nullable=False)
    state_of_charge: Mapped[float] = mapped_column(Float, default=0.5)
    location: Mapped[str] = mapped_column(String, default="campus_a")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class VehicleTelemetry(Base):
    __tablename__ = "vehicle_telemetry"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    vehicle_id: Mapped[str] = mapped_column(String, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    temperature_c: Mapped[float] = mapped_column(Float, default=20.0)
    power_kw: Mapped[float] = mapped_column(Float, default=0.0)


class ChargingSession(Base):
    __tablename__ = "charging_sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    vehicle_id: Mapped[str] = mapped_column(String, nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    end_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    energy_kwh: Mapped[float] = mapped_column(Float, default=0.0)
    charger_id: Mapped[str] = mapped_column(String, default="charger-01")
