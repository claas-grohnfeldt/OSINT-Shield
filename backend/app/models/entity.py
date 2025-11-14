from __future__ import annotations

from enum import Enum

from sqlalchemy import Enum as SAEnum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base


class EntityType(str, Enum):
    PERSON = "person"
    ORG = "org"
    THREAT_ACTOR = "threat_actor"
    IP = "ip"
    DOMAIN = "domain"
    CVE = "cve"
    COUNTRY = "country"
    CITY = "city"
    FACILITY = "facility"
    HASH = "hash"
    TOOL = "tool"
    UNKNOWN = "unknown"


class Entity(Base):
    __tablename__ = "entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"), nullable=False, index=True)
    entity_type: Mapped[EntityType] = mapped_column(SAEnum(EntityType), nullable=False, default=EntityType.UNKNOWN)
    value: Mapped[str] = mapped_column(String(255), nullable=False)
    confidence: Mapped[float] = mapped_column(Float, default=0.5)

    event = relationship("Event", back_populates="entities")


__all__ = ["Entity", "EntityType"]
