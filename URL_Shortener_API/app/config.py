from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_name: str
    database_port: str
    database_host: str
    database_user: str
    database_password: str

    class Config:
        env_file = ".env"

settings = Settings()