from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:

    def create(self, db: Session, user: UserCreate) -> User:
        db_user = User(
            full_name=user.full_name,
            nickname=user.nickname,
            email=user.email,
            hashed_password=user.password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_by_email(self, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()
