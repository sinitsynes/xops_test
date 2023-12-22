from typing import Annotated
from fastapi import APIRouter, Depends, Query
from pydantic import NonNegativeInt

from app.db.connection import get_session
from app.api.schemas import (
    AddLinksRequest,
    AddLinksResponse,
    VisitedDomainsResponse,
    VisitedDomainsRequest,
)
from app.api.manager import WatcherManager

watcher = APIRouter()


@watcher.post("/visited_links", response_model=AddLinksResponse)
async def add_links(request: AddLinksRequest, session=Depends(get_session)):
    manager = WatcherManager(session)
    return await manager.save_links(request)


@watcher.get("/visited_domains", response_model=VisitedDomainsResponse)
async def visited_domains(
    from_parameter: Annotated[NonNegativeInt | None, Query(alias="from")] = None,
    to_parameter: Annotated[NonNegativeInt | None, Query(alias="to")] = None,
    session=Depends(get_session),
):
    manager = WatcherManager(session)
    request = VisitedDomainsRequest(start_date=from_parameter, end_date=to_parameter)
    return await manager.get_visited_domains(request)
