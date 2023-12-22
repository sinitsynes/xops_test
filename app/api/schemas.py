from datetime import datetime

from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: str | list[str] = "ok"


class AddLinksRequest(BaseModel):
    visited_at: int = datetime.now().timestamp()
    links: list[str]


class AddLinksResponse(StatusResponse):
    pass


class VisitedDomainsResponse(StatusResponse):
    domains: list[str]
