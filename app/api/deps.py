from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_db
from app.repositories.category_repository import CategoryRepository
from app.services.category_service import CategoryService


def get_category_service(db: AsyncSession = Depends(get_db)) -> CategoryService:
    """Dependency для получения CategoryService"""
    repository = CategoryRepository(db)
    return CategoryService(repository)
