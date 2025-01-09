from database import get_db_session
from repository import TaskRepository, TaskCacheRepository, UserRepository
from cache import get_redis_connection
from service import TaskService, UserService
from fastapi import Depends
from sqlalchemy.orm import Session
from redis.asyncio import Redis

from service.auth import AuthService


def get_tasks_repository(db_session: Session = Depends(get_db_session)) -> TaskRepository:
    return TaskRepository(db_session)


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


def get_user_repository(db_session: Session = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repository=user_repository)


def get_auth_service(user_repository: UserRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repository=user_repository)
