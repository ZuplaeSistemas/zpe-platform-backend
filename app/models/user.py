from sqlalchemy import Column, String
from app.db.base_class import Base


class User(Base):
    full_name = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
