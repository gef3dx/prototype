from fastapi import APIRouter

from src.users import crud
from src.users.schemas import CreateUser

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
