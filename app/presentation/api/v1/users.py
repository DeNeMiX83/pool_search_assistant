from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.presentation.api.di import (
    provide_register_user_stub,
    provide_login_user_stub,
    provide_logout_user_stub,
)

from app.core.user.exceptions import AuthError

from app.core.user.usecases import (
    RegisterUserUseCase,
    LoginUserUseCase,
    LogoutUserUseCase,
)
from app.core.user import dto


router = APIRouter()


@router.post(
    path="/register",
    status_code=status.HTTP_200_OK,
)
async def register_user(
    user: dto.UserRegister,
    usecase: RegisterUserUseCase = Depends(provide_register_user_stub),
    response: Response = Response(),
):
    try:
        await usecase.execute(user)
    except AuthError as e:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"message": str(e)}
    return {"message": "User created successfully"}


@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
)
async def login_user(
    user: dto.UserLogin,
    usecase: LoginUserUseCase = Depends(provide_login_user_stub),
    response: Response = Response(),
):
    try:
        session_id = await usecase.execute(user)
    except AuthError as e:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"message": str(e)}
    return {"sesion_id": session_id}


@router.post(
    path="/logout",
    status_code=status.HTTP_200_OK,
)
async def logout_user(
    user: dto.UserLogout,
    usecase: LogoutUserUseCase = Depends(provide_logout_user_stub),
):
    try:
        await usecase.execute(user)
    except AuthError as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )
    return {"message": "User logged out successfully"}
