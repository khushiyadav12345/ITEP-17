from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db_config import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    email:Mapped[str] = mapped_column(String(100), unique=True,nullable=False,index=True)
    password: Mapped[str] = mapped_column( String(100),nullable=False)

    posts:Mapped[list["Post"]] = relationship("Post",
                                              cascade="all,delete-orphan",
                                              back_populates="user")