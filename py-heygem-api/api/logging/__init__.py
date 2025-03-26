from fastapi import APIRouter
from .endpoints import logs, metrics

router = APIRouter(tags=["日志监控"])
router.include_router(logs.router, prefix="/logs")
router.include_router(metrics.router, prefix="/metrics")
