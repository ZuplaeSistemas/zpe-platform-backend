from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexão do banco de dados assíncrono
SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://zuplae:platform2024@localhost:5432/zpe_platform_db"
)

# Criar o engine assíncrono para conectar ao banco de dados
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Criar a fábrica de sessões assíncronas
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

# Base para a criação das models
Base = declarative_base()


# Dependência para usar em toda a aplicação
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
