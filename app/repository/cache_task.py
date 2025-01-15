import json
from typing import Optional

from redis import asyncio as Redis

from app.schema import TaskSchema


class TaskCacheRepository:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def get_tasks(self) -> Optional[list[TaskSchema]]:
        async with self.redis as redis:
            tasks_json = await redis.lrange('tasks', 0, -1)
            if tasks_json:
                return [TaskSchema.model_validate(json.loads(task)) for task in tasks_json]
        return None

    async def set_tasks(self, tasks: list[TaskSchema]) -> None:
        tasks_json = [task.json() for task in tasks]
        async with self.redis as redis:
            await redis.rpush('tasks', *tasks_json)
            await redis.expire('tasks', 60)

