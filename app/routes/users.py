from fastapi import APIRouter, Depends

from app.dependency import get_user_service
from app.schema import UserLoginSchema, UserCreateSchema
from app.service import UserService

router = APIRouter(prefix='/user', tags=['user'])


@router.post('', response_model=UserLoginSchema)
async def create_user(
        body: UserCreateSchema,
        user_service: UserService = Depends(get_user_service)
):
    return await user_service.create_user(body.username, body.password)