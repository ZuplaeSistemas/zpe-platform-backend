from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ZPE Platform"
    database_url: str = "postgresql://zpe:platforma%401508@localhost:5432/zpe_platform_db"

    class Config:
        env_file = ".env"


settings = Settings()
