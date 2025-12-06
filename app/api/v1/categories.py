from fastapi import APIRouter, Depends, HTTPException, status
from app.services.category_service import CategoryService
from app.schemas.category import CategoryResponse, CategoryCreate, CategoryUpdate
from app.api.deps import get_category_service


router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/", response_model=list[CategoryResponse])
async def get_categories(service: CategoryService = Depends(get_category_service)):
    return await service.get_all()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
async def create_category(category: CategoryCreate, service: CategoryService = Depends(get_category_service)):
    return await service.create_category(category)

@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category_by_id(category_id: int, service: CategoryService = Depends(get_category_service)):
    return await service.get_category_by_id(category_id)

@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(
  category_id: int, category: CategoryUpdate,
  service: CategoryService = Depends(get_category_service),
):
    return await service.update_category(category_id, category)

@router.delete("/{category_id}", response_model=CategoryResponse)
async def delete_category(
        category_id: int,
        service: CategoryService = Depends(get_category_service),
):
    return await service.delete_category(category_id)

