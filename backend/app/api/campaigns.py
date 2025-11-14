from __future__ import annotations

from datetime import datetime
from collections import Counter

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_session
from ..models.event import Sector
from ..schemas import CampaignDetail, CampaignRead, EventSummary
from ..services.campaign_service import CampaignService

router = APIRouter(prefix="/campaigns", tags=["campaigns"])


@router.get("", response_model=list[CampaignRead])
async def list_campaigns(
    sector: Sector | None = Query(default=None),
    country: str | None = Query(default=None, min_length=2, max_length=3),
    min_risk: float | None = Query(default=None, ge=0, le=100),
    time_from: datetime | None = Query(default=None, alias="from"),
    time_to: datetime | None = Query(default=None, alias="to"),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    session: AsyncSession = Depends(get_session),
) -> list[CampaignRead]:
    campaigns = await CampaignService.list_campaigns(
        session,
        sector=sector,
        country=country,
        min_risk=min_risk,
        time_from=time_from,
        time_to=time_to,
        limit=limit,
        offset=offset,
    )
    response: list[CampaignRead] = []
    for campaign in campaigns:
        response.append(
            CampaignRead.model_validate(campaign).model_copy(
                update={"event_count": len(campaign.events)}
            )
        )
    return response


@router.get("/{campaign_id}", response_model=CampaignDetail)
async def get_campaign(campaign_id: str, session: AsyncSession = Depends(get_session)) -> CampaignDetail:
    campaign = await CampaignService.get_campaign(session, campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    sorted_events = sorted(campaign.events, key=lambda evt: evt.timestamp)
    entity_counter = Counter()
    for event in campaign.events:
        for entity in event.entities:
            entity_counter[entity.entity_type.value] += 1

    detail = CampaignDetail.model_validate(campaign).model_copy(
        update={
            "event_count": len(campaign.events),
            "events": [EventSummary.model_validate(event) for event in sorted_events],
            "entity_counts": dict(entity_counter),
        }
    )
    return detail
