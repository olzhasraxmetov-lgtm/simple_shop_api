from fastapi import APIRouter, Depends, HTTPException, status
from app.services.category_service import CategoryService
from app.schemas.category import CategoryResponse
from app.api.deps import get_category_service


router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/", response_model=list[CategoryResponse])
async def get_categories(service: CategoryService = Depends(get_category_service)):
    return await service.get_all()