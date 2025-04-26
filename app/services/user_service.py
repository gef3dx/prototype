from app.repositories.abstract_user_repository import AbstractUserRepository
from app.models.user import User
import hashlib

class UserService:
    # Сервис, который инкапсулирует бизнес-логику

    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo
        # Используем абстрактный репозиторий, а не конкретную реализацию

    async def get_user_by_email(self, email: str) -> User | None:
        # Возвращает пользователя по email
        return await self.repo.get_by_email(email)

    async def register_user(self, username: str, email: str, password: str) -> User:
        # Хэшируем пароль (не используем пока bcrypt, чтобы упростить)
        hashed = hashlib.sha256(password.encode()).hexdigest()
        user = User(username=username, email=email, hashed_password=hashed)
        await self.repo.add(user)
        return user
