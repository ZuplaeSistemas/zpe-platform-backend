from fastapi import Header, HTTPException

from app.config import FIXED_TOKEN


async def verify_fixed_token(x_token: str = Header(...)):
    if x_token != FIXED_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
