from typing import List

from fastapi import APIRouter, Depends

from app.dependencies import verify_fixed_token
from app.handlers.user_handler import UserHandler
from app.schemas.user_schema import UserCreate, UserOut

router = APIRouter()


@router.post(
    "/register", response_model=UserOut, dependencies=[Depends(verify_fixed_token)]
)
async def register_user(user_in: UserCreate):
    handler = UserHandler()
    return await handler.register_user(user_in=user_in)


@router.get(
    "/users", response_model=List[UserOut], dependencies=[Depends(verify_fixed_token)]
)
async def get_users():
    handler = UserHandler()
    return await handler.list_users()
