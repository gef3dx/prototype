from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# Импорты из SQLAlchemy для работы в async-режиме

from sqlalchemy.orm import declarative_base
# Создание базы моделей (ORM)

from app.core.config import settings
# Подключаем конфигурацию из .env

engine = create_async_engine(settings.DATABASE_URL, echo=True)
# Создаём асинхронный движок (echo=True для логирования SQL-запросов)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
# Создаём фабрику сессий (по аналогии с sessionmaker, но async)

Base = declarative_base()
# Это базовый класс, от которого будут наследоваться все ORM-модели

async def get_session():
    # Dependency для FastAPI — асинхронная сессия
    async with AsyncSessionLocal() as session:
        yield session
        # yield вместо return — FastAPI будет использовать эту функцию как Depends
