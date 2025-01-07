from dataclasses import dataclass

from repository import TaskRepository, TaskCacheRepository
from shema.task import TaskSchema


@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCacheRepository

    async def get_tasks(self):
        if tasks := await self.task_cache.get_tasks():
            return tasks
        else:
            tasks = self.task_repository.get_tasks()
            tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
            await self.task_cache.set_tasks(tasks_schema)
            return tasks_schema