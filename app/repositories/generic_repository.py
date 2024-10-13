from typing import Generic, Type, TypeVar

from sqlalchemy.future import select

from app.db.session_factory import SessionFactory

T = TypeVar("T")


class GenericRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self._model = model

    async def get_all(self) -> list[T]:
        async for session in SessionFactory.get_session():
            async with session:
                result = await session.execute(select(self._model))
                return result.scalars().all()

    async def get_by_id(self, id: int) -> T | None:
        async for session in SessionFactory.get_session():
            async with session:
                return await session.get(self._model, id)

    async def add(self, entity: T) -> T:
        async for session in SessionFactory.get_session():
            async with session.begin():
                session.add(entity)
            await session.commit()
            await session.refresh(entity)
            return entity
