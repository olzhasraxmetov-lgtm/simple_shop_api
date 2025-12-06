from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
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

    async def get_by_id(self, category_id: int):
        stmt  = select(CategoryORM).where(CategoryORM.id == category_id,
                                          CategoryORM.is_active == True)
        result = await self.session.scalars(stmt)
        return result.first()

    async def get_by_id_any(self, category_id: int):
        stmt = select(CategoryORM).where(CategoryORM.id == category_id)
        result = await self.session.scalars(stmt)
        return result.first()

    async def soft_delete(self, category_id: int):
        await self.session.execute(
            update(CategoryORM).where(CategoryORM.id == category_id).values(is_active=False)
        )
        await self.session.commit()
        return await self.get_by_id_any(category_id)
