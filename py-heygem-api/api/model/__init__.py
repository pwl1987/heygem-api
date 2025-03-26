from fastapi import APIRouter
from .endpoints import model

router = APIRouter(tags=["模型服务"])
router.include_router(model.router, prefix="/model")
