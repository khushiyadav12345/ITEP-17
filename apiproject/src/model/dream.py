from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db_config import Base

class Dream(Base):
    __tablename__ = "dream"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    mood: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(1000))
