from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
# import @inject и Provide для подключения контейнера зависимостей

from app.core.container import Container
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
@inject  # Подключает зависимости из контейнера
async def register_user(
    user_data: UserCreate,
    session: AsyncSession = Depends(get_session),
    service: UserService = Depends(Provide[Container.user_service]),
):
    existing = await service.get_user_by_email(user_data.email)
    if existing:
        raise HTTPException(400, "Email already registered")

    new_user = await service.register_user(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
    )

    await session.commit()
    await session.refresh(new_user)
    # Обновляем объект из базы после коммита (чтобы получить ID, дату и т.п.)

    return new_user
