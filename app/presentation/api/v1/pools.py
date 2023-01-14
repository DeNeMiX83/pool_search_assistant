from fastapi import APIRouter, Depends, status
from app.presentation.api.di import provide_get_recommended_pool

#core
from app.core.pool.usecase.get_recommended_pools import GetRecommendedPoolsUseCase
from app.core.shared.entities.value_objects.uuid import UUID


router = APIRouter()

@router.get(
    path="",
    status_code=status.HTTP_200_OK,
)
async def get_recommended_pool(
    pool_id: UUID,
    usecase: GetRecommendedPoolsUseCase = Depends(provide_get_recommended_pool),
):
    pools = await usecase.execute(pool_id)
    return pools