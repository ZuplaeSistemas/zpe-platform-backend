from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.handlers.user_handler import UserHandler
from app.schemas.user_schema import UserCreate, UserOut

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    handler = UserHandler()
    return await handler.register_user(user_in=user_in, db=db)
