from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.category import CategoryORM
from app.repositories.base import BaseRepository

class CategoryRepository(BaseRepository[CategoryORM]):
    """Репозиторий для работы с категориями"""

    def __init__(self, session: AsyncSession):
        super().__init__(session, CategoryORM)

    async def get_all_active(self) -> list[CategoryORM]:
        stmt = select(CategoryORM).where(CategoryORM.is_active == True)

        stmt = stmt.order_by(CategoryORM.name)
        result = await self.session.scalars(stmt)
        return list(result.all())
