from fastapi import APIRouter, status, Depends
from typing import Annotated

from dependency import get_tasks_repository, get_tasks_service
from service import TaskService
from schema.task import TaskSchema
from repository import TaskRepository

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/all', response_model=list[TaskSchema])
async def get_task(
        task_service: TaskService = Depends(get_tasks_service),
):
    return await task_service.get_tasks()


@router.post('/', response_model=TaskSchema)
async def create_task(
        task: TaskSchema,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_repository.create_task(task)
    return task


@router.patch(
    '/{task_id}',
    response_model=TaskSchema
)
async def update_task(
        task_id: int,
        name: str,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    return task_repository.update_task_name(task_id, name)


@router.delete(
    '/{task_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task(
        task_id: int,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_repository.delete_tasks(task_id)
    return
