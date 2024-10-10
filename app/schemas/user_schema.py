from pydantic import BaseModel, ConfigDict, EmailStr, Field


# Schema para criar um novo usuário
class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=100)
    username: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str = Field(..., min_length=8)

    model_config = ConfigDict(from_attributes=True)


# Schema para exibir os dados do usuário (saída)
class UserOut(BaseModel):
    id: int
    full_name: str
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# Schema para representar o usuário no banco de dados (com hash da senha)
class UserInDB(UserOut):
    hashed_password: str
