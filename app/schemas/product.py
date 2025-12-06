from pydantic import BaseModel, Field, ConfigDict, condecimal
from datetime import datetime
from decimal import Decimal


class ProductBase(BaseModel):
    """
    Базовая модель товара
    """
    title: str = Field(min_length=6, max_length=20, description='Название товара')
    description: str = Field(min_length=1, max_length=100, description='Описание товара')
    price: condecimal(max_digits=10, decimal_places=2, ge=0)
    quantity: int = Field(ge=0, description='Количество товара')

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    title: str | None = Field(None,min_length=6, max_length=20)
    description: str | None = Field(None,min_length=1, max_length=100)
    price: condecimal(max_digits=10, decimal_places=2, ge=0) | None = None
    quantity: int | None = Field(None,ge=0)

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)