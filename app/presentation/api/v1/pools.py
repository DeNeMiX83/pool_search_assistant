from fastapi import APIRouter, Query, Depends, status, HTTPException
from app.presentation.api.di import (
    provide_get_recommended_pool_stub,
    provide_like_pool_stub,
    provide_unlike_pool_stub,
    get_like_pools_by_user_id_stub,
    get_user_data_by_session_id_stub,
)

# core
from app.core.pool.usecases import (
    GetRecommendedPoolsUseCase, LikePoolUseCase, UnlikePoolUseCase
)
from app.core.pool import dto

router = APIRouter()


@router.get(
    path="/recommended",
    status_code=status.HTTP_200_OK,
)
async def get_recommended_pool(
    like_pool_entities: dict = Depends(get_like_pools_by_user_id_stub),
    usecase: GetRecommendedPoolsUseCase = Depends(
        provide_get_recommended_pool_stub
    ),
):
    if not like_pool_entities:
        return HTTPException(status_code=404, detail="No liked pools")

    like_pools = [pool.pool_id for pool in like_pool_entities]
    like_pools_dto = dto.LikePools(pool_ids=like_pools)
    pools = await usecase.execute(like_pools_dto)
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
