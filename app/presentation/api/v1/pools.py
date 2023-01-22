from fastapi import APIRouter, Query, Depends, status, HTTPException
from app.presentation.api.di import (
    provide_get_recommended_pool_stub,
    provide_like_pool_stub,
    provide_unlike_pool_stub,
    get_user_data_by_session_id_stub,
)

# core
from app.core.pool.usecases import (
    GetRecommendedPoolsUseCase, LikePoolUseCase, UnlikePoolUseCase
)
from app.core.pool import dto

router = APIRouter()


@router.get(
    path="",
    status_code=status.HTTP_200_OK,
)
async def get_recommended_pool(
    pool_id: int,
    usecase: GetRecommendedPoolsUseCase = Depends(
        provide_get_recommended_pool_stub
    ),
):
    pools = await usecase.execute(pool_id)
    return pools


@router.post(
    path="/like",
    status_code=status.HTTP_200_OK,
)
async def like_pool(
    pool_id: int = Query(...),
    user_data: dict = Depends(get_user_data_by_session_id_stub),
    usecase: LikePoolUseCase = Depends(provide_like_pool_stub),
):
    pool_like = dto.PoolLike(
        pool_id=pool_id,
        user_id=user_data["user_id"],
    )
    try:
        await usecase.execute(pool_like)
    except ValueError as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return {"message": "success"}


@router.post(
    path="/unlike",
    status_code=status.HTTP_200_OK,
)
async def unlike_pool(
    pool_id: int = Query(...),
    user_data: dict = Depends(get_user_data_by_session_id_stub),
    usecase: UnlikePoolUseCase = Depends(provide_unlike_pool_stub),
):
    pool_like = dto.PoolLike(
        pool_id=pool_id,
        user_id=user_data["user_id"],
    )
    try:
        await usecase.execute(pool_like)
    except ValueError as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return {"message": "success"}
