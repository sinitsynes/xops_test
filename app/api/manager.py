from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas import (
    AddLinksRequest,
    AddLinksResponse,
    VisitedDomainsRequest,
    VisitedDomainsResponse,
)
from app.db.models import VisitedLink
from app.db.operations import DatabaseOperations
from urllib.parse import urlsplit


class WatcherManager:
    def __init__(self, session: AsyncSession):
        self.db = DatabaseOperations(session)

    @staticmethod
    def make_link(link: str, visited_at: int) -> VisitedLink:
        domain = urlsplit(link).netloc
        return VisitedLink(link=link, visited_at=visited_at, domain=domain)

    async def save_links(self, request: AddLinksRequest) -> AddLinksResponse:
        links = [self.make_link(link, request.visited_at) for link in request.links]
        await self.db.write_to_db(links)
        return AddLinksResponse()

    async def get_visited_domains(
        self, request: VisitedDomainsRequest
    ) -> VisitedDomainsResponse:
        domains = await self.db.get_visited_domains(
            request.start_date, request.end_date
        )
        return VisitedDomainsResponse(domains=domains)
