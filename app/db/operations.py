from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select, distinct

from app.db.models import VisitedLink


class DatabaseOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def write_to_db(self, items: list[VisitedLink]):
        self.session.add_all(items)
        await self.session.commit()

    @staticmethod
    def _make_time_limits(start_date: int = None, end_date: int = None) -> list:
        where_clause = list()
        if start_date:
            where_clause.append(VisitedLink.visited_at >= start_date)
        if end_date:
            where_clause.append(VisitedLink.visited_at <= end_date)
        return where_clause

    async def get_visited_domains(self, start_date: int = None, end_date: int = None):
        where_clause = self._make_time_limits(start_date, end_date)
        query = select(distinct(VisitedLink.domain)).where(*where_clause)
        return (await self.session.execute(query)).scalars().all()
