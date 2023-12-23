from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import HttpUrl
from app.api.schemas import (
    AddLinksRequest,
    AddLinksResponse,
    VisitedDomainsResponse,
)
from app.db.models import VisitedLink
from app.db.operations import DatabaseOperations



class WatcherManager:
    def __init__(self, session: AsyncSession):
        self.db = DatabaseOperations(session)

    @staticmethod
    def make_link(link: HttpUrl, visited_at: int) -> VisitedLink:
        return VisitedLink(link=link.unicode_string(), visited_at=visited_at, domain=link.host)

    async def save_links(self, request: AddLinksRequest) -> AddLinksResponse:
        links = [self.make_link(link, request.visited_at) for link in request.links]
        await self.db.write_to_db(links)
        return AddLinksResponse()

    async def get_visited_domains(self, start_date: int, end_date: int) -> VisitedDomainsResponse:
        domains = await self.db.get_visited_domains(start_date, end_date)
        return VisitedDomainsResponse(domains=domains)
