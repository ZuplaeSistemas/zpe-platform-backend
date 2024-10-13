import bcrypt

from app.models.user import User
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

    async def create_user(self, user_in: UserCreate) -> UserOut:
        user_repo = UserRepository()

        # Verifica se o e-mail ou nome de usuário já existem
        if await user_repo.get_user_by_email(user_in.email):
            raise ValueError("Email already registered")
        if await user_repo.get_user_by_username(user_in.username):
            raise ValueError("Username already taken")

        # Hash da senha e criação do usuário
        hashed_password = self.hash_password(user_in.password)
        user = User(
            full_name=user_in.full_name,
            username=user_in.username,
            email=user_in.email,
            hashed_password=hashed_password,
        )
        user = await user_repo.add(user)

        # Acessando os dados explicitamente para evitar erros de `MissingGreenlet`
        user_out = UserOut(
            id=user.id,
            full_name=user.full_name,
            username=user.username,
            email=user.email,
        )
        return user_out
