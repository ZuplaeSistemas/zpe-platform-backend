from sqlalchemy import MetaData
from sqlalchemy.orm import as_declarative, declared_attr

metadata = MetaData()


@as_declarative()
class Base:
    id: any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
