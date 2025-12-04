from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class CategoryBase(BaseModel):
    """
    Базовая модель категорий
    """
    name: str = Field(min_length=6, max_length=20, description='Название категории')
    description: str = Field(min_length=1, max_length=100, description='Описание категории')

class CategoryCreate(CategoryBase):
    """
    Модель для создания категории
    """
    pass

class CategoryUpdate(CategoryBase):
    """
    Модель для обновления категории
    """
    name: str | None = Field(None, min_length=6, max_length=20)
    description: str | None = Field(None, min_length=1, max_length=100)

class CategoryResponse(CategoryBase):
    """
    Модель для ответа
    """
    id: int
    created_at: datetime
    is_active: bool
    model_config = ConfigDict(from_attributes=True)