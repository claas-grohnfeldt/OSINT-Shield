from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_session
from ..models.event import Sector
from ..schemas import EventDetail, EventRead
from ..services.event_service import EventService

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=list[EventRead])
async def list_events(
    country: str | None = Query(default=None, min_length=2, max_length=3, description="ISO country code"),
    sector: Sector | None = Query(default=None),
    time_from: datetime | None = Query(default=None, alias="from"),
    time_to: datetime | None = Query(default=None, alias="to"),
    min_relevance: float | None = Query(default=None, ge=0, le=1),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    session: AsyncSession = Depends(get_session),
) -> list[EventRead]:
    events = await EventService.list_events(
        session,
        country=country,
        sector=sector,
        time_from=time_from,
        time_to=time_to,
        min_relevance=min_relevance,
        limit=limit,
        offset=offset,
    )
    return [EventRead.model_validate(event) for event in events]


@router.get("/{event_id}", response_model=EventDetail)
async def get_event(event_id: str, session: AsyncSession = Depends(get_session)) -> EventDetail:
    event = await EventService.get_event(session, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return EventDetail.model_validate(event)
