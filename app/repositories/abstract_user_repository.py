# app/repositories/abstract_user_repository.py
from abc import ABC, abstractmethod
from app.models.user import User

class AbstractUserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: int) -> User | None: pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None: pass

    @abstractmethod
    async def add(self, user: User) -> None: pass
