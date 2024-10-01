# app/api/v1/endpoints/user.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.db.session import get_db


router = APIRouter()


@router.post("/signup", response_model=UserResponse)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db),
    service: UserService = Depends()
) -> UserResponse:
    """
    Endpoint para registrar um novo usuário.
    """
    created_user = service.create_user(db, user)
    return created_user
