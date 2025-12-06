from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.core.database import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, session: AsyncSession, model: Type[ModelType]):
        self.session = session
        self.model = model

    async def get_by_id(self, id: int) -> ModelType | None:
        result = await self.session.scalar(select(self.model).where(self.model.id == id))
        return result.first()

    async def get_all_paginated_items(self, skip: int = 0, limit: int = 100) -> list[ModelType]:
        result = await self.session.scalars(
            select(self.model).offset(skip).limit(limit)
        )
        return list(result.all())

    async def create(self, data: ModelType) -> ModelType:
        self.session.add(data)
        await self.session.commit()
        await self.session.refresh(data)
        return data

    async def update(self, obj: ModelType, data: dict) -> ModelType:
        for key, value in data.items():
            setattr(obj, key, value)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj