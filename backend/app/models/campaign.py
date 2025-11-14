from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Enum as SAEnum, Float, String, Text
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base
from .event import Sector, event_campaign_association


def _uuid() -> str:
    return str(uuid4())


class Campaign(Base):
    __tablename__ = "campaigns"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    label: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    sector: Mapped[Sector] = mapped_column(SAEnum(Sector), nullable=False, default=Sector.UNKNOWN)
    risk_score: Mapped[int] = mapped_column(Float, default=0.0)
    countries: Mapped[list[str] | None] = mapped_column(JSON)
    time_start: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    time_end: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    events = relationship(
        "Event",
        secondary=event_campaign_association,
        back_populates="campaigns",
    )


__all__ = ["Campaign"]
