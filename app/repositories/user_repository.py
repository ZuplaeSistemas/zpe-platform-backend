from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select  # Usar select para consultas assíncronas

from app.models.user import User
from app.schemas.user_schema import UserCreate


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_in: UserCreate, hashed_password: str) -> User:
        db_user = User(
            full_name=user_in.full_name,
            username=user_in.username,
            email=user_in.email,
            hashed_password=hashed_password,
        )
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def get_user_by_email(self, email: str) -> User:
        result = await self.db.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    async def get_user_by_username(self, username: str) -> User:
        result = await self.db.execute(select(User).filter(User.username == username))
        return result.scalars().first()
