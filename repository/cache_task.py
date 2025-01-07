import json
from typing import Optional, Any

from redis import Redis

from shema.task import TaskSchema


class TaskCacheRepository:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def get_tasks(self) -> Optional[list[TaskSchema]]:
        tasks_json = await self.redis.lrange('tasks', 0, -1)
        if tasks_json:
            return [TaskSchema.model_validate(json.loads(task)) for task in tasks_json]
        return None

    async def set_tasks(self, tasks: list[TaskSchema]) -> None:
        tasks_json = [task.json() for task in tasks]
        await self.redis.rpush('tasks', *tasks_json)
        await self.redis.expire('tasks', 60)

