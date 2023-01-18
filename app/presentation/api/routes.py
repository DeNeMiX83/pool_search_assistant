from fastapi import APIRouter
from app.presentation.api.v1 import pools
from app.presentation.api.v1 import users


router = APIRouter()
router.include_router(pools.router, prefix="/pools", tags=["pools"])
router.include_router(users.router, prefix="/users", tags=["users"])
