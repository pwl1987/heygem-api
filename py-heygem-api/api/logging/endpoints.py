from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from typing import List
from pathlib import Path
from ..auth.services import get_current_user
from ..schemas import UserInDB
import os

router = APIRouter()
security = HTTPBearer()

@router.get("/logs", response_model=List[str])
async def get_log_files(
    current_user: UserInDB = Depends(get_current_user)
):
    """获取所有日志文件列表"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="只有管理员可以查看日志"
        )
    
    log_dir = Path("logs")
    if not log_dir.exists():
        return []
    
    return [f.name for f in log_dir.iterdir() if f.is_file()]

@router.get("/logs/{filename}")
async def get_log_content(
    filename: str,
    lines: int = 100,
    current_user: UserInDB = Depends(get_current_user)
):
    """获取日志文件内容"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="只有管理员可以查看日志"
        )
    
    log_path = Path("logs") / filename
    if not log_path.exists() or not log_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="日志文件不存在"
        )
    
    try:
        with open(log_path, "r") as f:
            content = f.readlines()[-lines:]
        return {"content": "".join(content)}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"读取日志失败: {str(e)}"
        )
