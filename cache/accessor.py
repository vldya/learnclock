from redis import asyncio as redis
from settings import REDIS_HOST, REDIS_PORT


async def get_redis_connection() -> redis.Redis:
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)




