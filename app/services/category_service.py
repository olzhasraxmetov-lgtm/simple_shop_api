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

    async def create_category(self, category: CategoryCreate) -> CategoryResponse:
        category = CategoryORM(**category.model_dump())
        created_category = await self.category_repository.create(category)
        return CategoryResponse.model_validate(created_category)

    async def get_category_by_id(self, category_id: int) -> CategoryResponse:
        category = await self.category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Category not found')
        return CategoryResponse.model_validate(category)

    async def update_category(self, category_id: int, category_data: CategoryUpdate) -> CategoryResponse:
        category_db = await self.category_repository.get_by_id(category_id)
        if not category_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
        update_data = category_data.model_dump(exclude_unset=True)

        updated_category = await self.category_repository.update(category_db, update_data)

        return CategoryResponse.model_validate(updated_category)