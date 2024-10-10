from typing import Dict

from fastapi import FastAPI

from app.api.v1.endpoints import user_api

app = FastAPI()

# Registrar o router da versão 1 da API
app.include_router(user_api.router, prefix="/api/v1/users", tags=["users"])


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Welcome to the ZPE Platform Backend"}
