from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Welcome to the ZPE Platform Backend"}
