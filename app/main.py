from fastapi import FastAPI
from app.api.v1.endpoints import user
from app.db.base import Base
from app.db.session import engine

app = FastAPI()

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["users"])
