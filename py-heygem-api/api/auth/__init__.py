from fastapi import APIRouter
from .endpoints import auth, users

router = APIRouter(tags=["认证服务"])
router.include_router(auth.router, prefix="/auth")
router.include_router(users.router, prefix="/users")
