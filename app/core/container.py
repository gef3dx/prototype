from dependency_injector import containers, providers
# Импортируем базовые элементы для создания DI-контейнера

from sqlalchemy.ext.asyncio import AsyncSession
# Тип для асинхронной SQLAlchemy-сессии

from app.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
# Импорт реализаций репозитория пользователей

from app.services.user_service import UserService
# Импорт бизнес-логики работы с пользователями

class Container(containers.DeclarativeContainer):
    # Контейнер — это декларативный класс, где мы описываем зависимости
    
    wiring_config = containers.WiringConfiguration(modules=["app.routers.user_router"])
    # Указываем модули, в которых мы будем использовать автоподключение зависимостей с помощью @inject

    session = providers.Dependency(instance_of=AsyncSession)
    # Это абстрактный провайдер, мы позже его override'им в main.py (вставим AsyncSessionLocal)

    user_repository = providers.Factory(
        SqlAlchemyUserRepository,
        session=session,
    )
    # Создание экземпляра SqlAlchemyUserRepository с передачей session как зависимости

    user_service = providers.Factory(
        UserService,
        repo=user_repository,
    )
    # Создание экземпляра UserService, которому автоматически передаётся user_repository
