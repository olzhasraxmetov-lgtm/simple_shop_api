from typing import Optional, List
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.models.category import CategoryORM

class CategoryService:
    """Сервис для работы с категорями"""

    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def get_all(self) -> list[CategoryResponse]:
        categories = await self.category_repository.get_all_active()
        return [CategoryResponse.model_validate(category) for category in categories]