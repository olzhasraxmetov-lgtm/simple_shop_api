from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import categories


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

app.include_router(categories.router)

@app.get('/')
async def root():
    return {"message": "Hello World"}