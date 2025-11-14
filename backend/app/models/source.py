from __future__ import annotations

from enum import Enum

from sqlalchemy import Enum as SAEnum
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base


class SourceType(str, Enum):
    PUBLIC_OSINT_SOCIAL = "public_osint_social"
    PUBLIC_OSINT_NEWS = "public_osint_news"
    PUBLIC_OSINT_TECH = "public_osint_tech"
    FUTURE_CLASSIFIED_SIGINT = "future_classified_sigint"
    FUTURE_INTERNAL_LOGS = "future_internal_logs"


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    source_type: Mapped[SourceType] = mapped_column(SAEnum(SourceType), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))

    events = relationship("Event", back_populates="source", cascade="all, delete-orphan")


__all__ = ["Source", "SourceType"]
