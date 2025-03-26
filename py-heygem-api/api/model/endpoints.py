from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..schemas import ModelCreate, ModelOut, ModelUpdate
from ..services import (
    get_models,
    get_model,
    create_model,
    update_model,
    delete_model
)
from database import get_db
from config import settings

router = APIRouter(prefix=settings.API_PREFIX)

@router.get("/models", response_model=List[ModelOut])
async def list_models(
    skip: int = 0, 
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    return await get_models(db, skip=skip, limit=limit)

@router.get("/models/{model_id}", response_model=ModelOut)
async def read_model(
    model_id: int,
    db: AsyncSession = Depends(get_db)
):
    model = await get_model(db, model_id=model_id)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return model

@router.post("/models", response_model=ModelOut)
async def add_model(
    model: ModelCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_model(db, model=model)

@router.put("/models/{model_id}", response_model=ModelOut)
async def modify_model(
    model_id: int,
    model: ModelUpdate,
    db: AsyncSession = Depends(get_db)
):
    db_model = await get_model(db, model_id=model_id)
    if db_model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return await update_model(db, model_id=model_id, model=model)

@router.delete("/models/{model_id}")
async def remove_model(
    model_id: int,
    db: AsyncSession = Depends(get_db)
):
    db_model = await get_model(db, model_id=model_id)
    if db_model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    await delete_model(db, model_id=model_id)
    return {"message": "Model deleted successfully"}
