from passlib.context import CryptContext

# Definir o contexto de criptografia para usar o argon2
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Gera o hash da senha usando argon2"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha em texto puro corresponde ao hash gerado com argon2"""
    return pwd_context.verify(plain_password, hashed_password)
