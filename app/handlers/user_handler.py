from fastapi import HTTPException

from app.schemas.user_schema import UserCreate, UserOut
from app.services.user_service import UserService


class UserHandler:
    def __init__(self):
        self.user_service = UserService()

    async def register_user(self, user_in: UserCreate) -> UserOut:

        # Verificar se as senhas correspondem
        if user_in.password != user_in.confirm_password:
            raise HTTPException(status_code=400, detail="Passwords do not match")

        # Criar o usuário e obter o objeto criado
        try:
            user = await self.user_service.create_user(user_in=user_in)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

        return user

    async def list_users(self) -> list[UserOut]:
        users = await self.user_service.list_users()
        return users
