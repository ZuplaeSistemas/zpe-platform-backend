import bcrypt

from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserOut


class UserService:
    def hash_password(self, password: str) -> str:
        # Gera um salt e aplica o hash na senha
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        # Verifica se a senha fornecida corresponde ao hash armazenado
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )

    async def create_user(
        self, user_in: UserCreate, user_repo: UserRepository
    ) -> UserOut:
        # Verifica se o e-mail ou nome de usuário já existem
        if await user_repo.get_user_by_email(user_in.email):
            raise ValueError("Email already registered")
        if await user_repo.get_user_by_username(user_in.username):
            raise ValueError("Username already taken")

        # Hash da senha e criação do usuário
        hashed_password = self.hash_password(user_in.password)
        user = await user_repo.create_user(
            user_in=user_in, hashed_password=hashed_password
        )

        # Retornar o usuário criado
        return UserOut(**user.__dict__)
