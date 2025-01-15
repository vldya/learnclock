from redis import asyncio as redis
from app.settings import Settings


async def get_redis_connection() -> redis.Redis:
    settings = Settings()
    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        decode_responses=True
    )




