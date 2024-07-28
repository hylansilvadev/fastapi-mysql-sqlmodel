from fastapi import APIRouter

from .user_route import router as user_router
from .security_route import router as security_router

router = APIRouter(prefix="/api/v1")

router.include_router(user_router)
router.include_router(security_router)