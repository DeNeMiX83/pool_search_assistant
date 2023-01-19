from fastapi import APIRouter, Depends, status
from app.presentation.api.di import (
    provide_register_user_stub,
    provide_login_user_stub,
)

from app.core.user.usecases import *
from app.core.user import dto


router = APIRouter()

@router.post(
    path="/register",
    status_code=status.HTTP_200_OK,
)
async def register_user(
    user: dto.User,
    usecase: RegisterUserUseCase = Depends(provide_register_user_stub),
):
    await usecase.execute(user)
    return {"message": "User created successfully"}


@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
)
async def login_user(
    user: dto.UserLogin,
    usecase: LoginUserUseCase = Depends(provide_login_user_stub),
):
    session_id = await usecase.execute(user)
    return {"sesion_id": session_id}