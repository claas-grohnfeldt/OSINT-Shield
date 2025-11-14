from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from ..models.event import Sector


class CampaignSnippet(BaseModel):
    id: str
    label: str
    risk_score: float
    sector: Sector

    model_config = ConfigDict(from_attributes=True)


class EventSummary(BaseModel):
    id: str
    timestamp: datetime
    country: str
    sector: Sector
    relevance_score: float

    model_config = ConfigDict(from_attributes=True)


class CampaignRead(BaseModel):
    id: str
    label: str
    description: str | None = None
    sector: Sector
    risk_score: float
    countries: list[str] | None = None
    time_start: datetime | None = None
    time_end: datetime | None = None
    event_count: int = 0

    model_config = ConfigDict(from_attributes=True)


class CampaignDetail(CampaignRead):
    events: list[EventSummary] = []
    entity_counts: dict[str, int] = {}

    model_config = ConfigDict(from_attributes=True)
