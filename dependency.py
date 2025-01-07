from database import get_db_session
from repository import TaskRepository, TaskCacheRepository
from cache import get_redis_connection
from service import TaskService
from fastapi import Depends
from redis.asyncio import Redis


def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)


# def get_cache_repository() -> TaskCacheRepository:
#     redis_connection = get_redis_connection()
#     return TaskCacheRepository(redis_connection)
def get_cache_repository(
    redis_connection: Redis = Depends(get_redis_connection)
) -> TaskCacheRepository:
    return TaskCacheRepository(redis_connection)


def get_tasks_service(
        task_repository: TaskRepository = Depends(get_tasks_repository),
        task_cache: TaskCacheRepository = Depends(get_cache_repository)
) -> TaskService:
    return TaskService(
        task_repository=task_repository,
        task_cache=task_cache
    )