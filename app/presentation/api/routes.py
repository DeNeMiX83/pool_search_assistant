from fastapi import APIRouter
from app.presentation.api.v1 import pools


router = APIRouter()
router.include_router(pools.router, prefix="/pools", tags=["pools"])
