"""Create initial EVOS operational tables."""

from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "fleet_vehicles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("vehicle_id", sa.String(), nullable=False, unique=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("battery_capacity_kwh", sa.Float(), nullable=False),
        sa.Column("state_of_charge", sa.Float(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_fleet_vehicles_id", "fleet_vehicles", ["id"])
    op.create_table(
        "vehicle_telemetry",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("vehicle_id", sa.String(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("temperature_c", sa.Float(), nullable=False),
        sa.Column("power_kw", sa.Float(), nullable=False),
    )
    op.create_index("ix_vehicle_telemetry_id", "vehicle_telemetry", ["id"])
    op.create_table(
        "charging_sessions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("vehicle_id", sa.String(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("end_time", sa.DateTime(), nullable=False),
        sa.Column("energy_kwh", sa.Float(), nullable=False),
        sa.Column("charger_id", sa.String(), nullable=False),
    )
    op.create_index("ix_charging_sessions_id", "charging_sessions", ["id"])
    op.create_table(
        "energy_readings",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("source", sa.String(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("energy_kwh", sa.Float(), nullable=False),
        sa.Column("price_per_kwh", sa.Float(), nullable=False),
    )
    op.create_index("ix_energy_readings_id", "energy_readings", ["id"])
    op.create_table(
        "forecast_records",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("target", sa.String(), nullable=False),
        sa.Column("horizon_hours", sa.Integer(), nullable=False),
        sa.Column("forecast_kwh", sa.Float(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_forecast_records_id", "forecast_records", ["id"])


def downgrade() -> None:
    op.drop_table("forecast_records")
    op.drop_table("energy_readings")
    op.drop_table("charging_sessions")
    op.drop_table("vehicle_telemetry")
    op.drop_table("fleet_vehicles")
