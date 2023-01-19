from fastapi import APIRouter, Depends, status
from app.presentation.api.di import (
    provide_get_recommended_pool_stub
)
#core
from app.core.pool.usecases.get_recommended_pools import GetRecommendedPoolsUseCase
from app.core.shared.entities import value_objects as vo


router = APIRouter()

@router.get(
    path="",
    status_code=status.HTTP_200_OK,
)
async def get_recommended_pool(
    pool_id: int,
    usecase: GetRecommendedPoolsUseCase = Depends(provide_get_recommended_pool_stub),
):
    pools = await usecase.execute(pool_id)
    return pools