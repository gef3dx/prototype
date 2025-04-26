from fastapi import FastAPI
from app.routers import user_router
from app.core.container import Container
from app.database import AsyncSessionLocal

app = FastAPI()

container = Container()
# Инициализируем контейнер

container.session.override(AsyncSessionLocal)
# Заменяем "заглушку" session на реальную фабрику сессий

# Add container as state to the app to avoid attribute error
app.state.container = container
# Связываем контейнер с FastAPI-приложением

app.include_router(user_router.router)
# Подключаем маршруты
