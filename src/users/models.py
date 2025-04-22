from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.BaseModels.BaseModel import BaseModel


class Users(BaseModel):
    """
    Модель пользователей
    """
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(String(32), unique=True)