from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import categories
from app.api.v1 import products

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

app.include_router(categories.router)
app.include_router(products.router)

@app.get('/')
async def root():
    return {"message": "Hello World"}