from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.repositories.abstract_user_repository import AbstractUserRepository

class SqlAlchemyUserRepository(AbstractUserRepository):
    # Конкретная реализация интерфейса репозитория для SQLAlchemy

    def __init__(self, session: AsyncSession):
        self.session = session
        # Принимаем асинхронную сессию SQLAlchemy в качестве зависимости

    async def get_by_id(self, user_id: int) -> User | None:
        # Получить пользователя по ID
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
        # scalar_one_or_none — вернёт None, если нет результата

    async def get_by_email(self, email: str) -> User | None:
        # Получить пользователя по email
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def add(self, user: User) -> None:
        # Добавление пользователя в сессию
        self.session.add(user)
