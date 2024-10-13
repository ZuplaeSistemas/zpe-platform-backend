from sqlalchemy.future import select

from app.db.session_factory import SessionFactory
from app.models.user import User
from app.repositories.generic_repository import GenericRepository


class UserRepository(GenericRepository[User]):
    def __init__(self):
        super().__init__(User)

    async def get_user_by_email(self, email: str) -> User:
        async for session in SessionFactory.get_session():
            result = await session.execute(select(User).filter(User.email == email))
            return result.scalars().first()

    async def get_user_by_username(self, username: str) -> User:
        async for session in SessionFactory.get_session():
            result = await session.execute(
                select(User).filter(User.username == username)
            )
            return result.scalars().first()
