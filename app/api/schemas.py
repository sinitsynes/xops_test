from datetime import datetime

from pydantic import BaseModel, NonNegativeInt


class StatusResponse(BaseModel):
    status: str | list[str] = "ok"


class AddLinksRequest(BaseModel):
    visited_at: int = datetime.now().timestamp()
    links: list[str]


class AddLinksResponse(StatusResponse):
    pass


class VisitedDomainsResponse(StatusResponse):
    domains: list[str]


class VisitedDomainsRequest(BaseModel):
    start_date: NonNegativeInt | None = None
    end_date: NonNegativeInt | None = None