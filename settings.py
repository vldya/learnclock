from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlite_db_name: str = 'learn_clock.sqlite'


# Redis
REDIS_HOST: str = 'localhost'
REDIS_PORT: int = 6379