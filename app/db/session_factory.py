from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db


class SessionFactory:
    @staticmethod
    async def get_session() -> AsyncGenerator[AsyncSession, None]:
        async for session in get_db():
            yield session
