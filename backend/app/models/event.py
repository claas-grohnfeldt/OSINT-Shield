from __future__ import annotations

from datetime import datetime
from enum import Enum
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, Enum as SAEnum, Float, ForeignKey, String, Table, Text
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base
from .source import Source


def _uuid() -> str:
    return str(uuid4())


class Sector(str, Enum):
    ENERGY = "energy"
    LOGISTICS = "logistics"
    DEFENCE = "defence"
    TELECOM = "telecom"
    SPACE = "space"
    OTHER = "other"
    UNKNOWN = "unknown"


event_campaign_association = Table(
    "event_campaigns",
    Base.metadata,
    Column("event_id", String(36), ForeignKey("events.id", ondelete="CASCADE"), primary_key=True),
    Column("campaign_id", String(36), ForeignKey("campaigns.id", ondelete="CASCADE"), primary_key=True),
)


class Event(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id", ondelete="RESTRICT"), nullable=False)
    country: Mapped[str] = mapped_column(String(4), nullable=False)
    sector: Mapped[Sector] = mapped_column(SAEnum(Sector), nullable=False, default=Sector.UNKNOWN)
    geo_lat: Mapped[float | None] = mapped_column(Float)
    geo_lon: Mapped[float | None] = mapped_column(Float)
    language: Mapped[str | None] = mapped_column(String(8))
    text: Mapped[str] = mapped_column(Text, nullable=False)
    context: Mapped[dict | None] = mapped_column("metadata", JSON)
    relevance_score: Mapped[float] = mapped_column(Float, default=0.0)
    is_security_relevant: Mapped[bool] = mapped_column(Boolean, default=False)

    source = relationship(Source, back_populates="events")
    entities = relationship(
        "Entity",
        back_populates="event",
        cascade="all, delete-orphan",
    )
    campaigns = relationship(
        "Campaign",
        secondary=event_campaign_association,
        back_populates="events",
    )


__all__ = ["Event", "Sector", "event_campaign_association"]
