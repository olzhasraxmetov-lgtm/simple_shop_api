from fastapi import APIRouter, Depends, HTTPException, status
from app.services.category_service import CategoryService
from app.schemas.category import CategoryResponse, CategoryCreate, CategoryUpdate
from app.api.deps import get_category_service


router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/")
async def get_categories():
    return 'products'
