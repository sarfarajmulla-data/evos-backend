import os

print("APP_ENV=", os.getenv("APP_ENV", "development"))
print("DATABASE_URL=", os.getenv("DATABASE_URL", "sqlite:///./evos.db"))
