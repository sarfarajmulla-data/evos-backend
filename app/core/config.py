from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    app_name: str = "EVOS Backend"
    api_v1_prefix: str = "/api/v1"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = False
    log_level: str = "INFO"
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 60
    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"
    database_url: str = "sqlite:///./evos.db"
    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_service_role_key: str = ""
    dataset_timeout_seconds: int = 30
    acn_username: str = ""
    acn_password: str = ""
    elaadnl_api_key: str = ""
    pecan_street_api_key: str = ""
    nasa_power_api_key: str = ""
    default_simulation_horizon_hours: int = 24
    default_grid_import_limit_kw: float = 80.0
    default_battery_capacity_kwh: float = 100.0
    default_battery_reserve_percent: float = 20.0

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
