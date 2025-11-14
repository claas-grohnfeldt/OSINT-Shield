from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..models.event import Sector
from .campaign import CampaignSnippet
from .entity import EntityRead
from .source import SourceRead


class EventRead(BaseModel):
    id: str
    timestamp: datetime
    country: str
    sector: Sector
    geo_lat: float | None = None
    geo_lon: float | None = None
    language: str | None = None
    text: str
    context: dict | None = Field(default=None, serialization_alias="metadata")
    relevance_score: float
    is_security_relevant: bool
    source: SourceRead
    campaigns: list[CampaignSnippet] = []

    model_config = ConfigDict(from_attributes=True)


class EventDetail(EventRead):
    entities: list[EntityRead] = []

    model_config = ConfigDict(from_attributes=True)
