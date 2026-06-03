from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER : str
    POSTGRES_PASSWORD : str
    POSTGRES_SERVER : str
    POSTGRES_PORT : str 
    POSTGRES_DB : str

    # This dynamically builds the URL string needed for SQLAlchemy for database connection
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    # Tells pydantic to look for .env file
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
