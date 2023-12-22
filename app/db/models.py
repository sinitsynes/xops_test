from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column


class BaseModel(MappedAsDataclass, DeclarativeBase):
    pass


class VisitedLink(BaseModel):
    __tablename__ = "visited_link"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    link: Mapped[str]
    domain: Mapped[str]
    visited_at: Mapped[int] = mapped_column(BigInteger)
