from pydantic import BaseModel, Field, EmailStr


class UsersSchema(BaseModel):
    """
    Схема для модели Users
    """
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr