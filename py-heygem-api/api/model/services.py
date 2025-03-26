from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.models import Model
from ..schemas import ModelCreate, ModelUpdate

async def get_models(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Model)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()

async def get_model(db: AsyncSession, model_id: int):
    result = await db.execute(
        select(Model)
        .where(Model.id == model_id)
    )
    return result.scalars().first()

async def create_model(db: AsyncSession, model: ModelCreate):
    db_model = Model(
        name=model.name,
        video_path=model.video_path,
        audio_path=model.audio_path,
        voice_id=model.voice_id
    )
    db.add(db_model)
    await db.commit()
    await db.refresh(db_model)
    return db_model

async def update_model(db: AsyncSession, model_id: int, model: ModelUpdate):
    result = await db.execute(
        select(Model)
        .where(Model.id == model_id)
    )
    db_model = result.scalars().first()
    if db_model is None:
        return None
    
    for var, value in vars(model).items():
        if value is not None:
            setattr(db_model, var, value)
    
    await db.commit()
    await db.refresh(db_model)
    return db_model

async def delete_model(db: AsyncSession, model_id: int):
    result = await db.execute(
        select(Model)
        .where(Model.id == model_id)
    )
    db_model = result.scalars().first()
    if db_model is None:
        return False
    
    await db.delete(db_model)
    await db.commit()
    return True
