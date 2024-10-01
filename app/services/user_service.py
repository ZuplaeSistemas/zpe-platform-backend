from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse
from app.core.security import get_password_hash
from fastapi import Depends, HTTPException, status


class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    def create_user(self, db: Session, user: UserCreate) -> UserResponse:
        # Verificar se as senhas coincidem
        if user.password != user.password_confirmation:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match"
            )

        # Verificar se o e-mail já está registrado
        existing_user = self.repository.get_by_email(db, user.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Gerar o hash da senha
        hashed_password = get_password_hash(user.password)
        user.password = hashed_password

        # Criar o usuário e retornar o UserResponse
        created_user = self.repository.create(db, user)

        # Usar model_validate para retornar o UserResponse
        return UserResponse.model_validate(created_user)
