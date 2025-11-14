from __future__ import annotations

from datetime import datetime
from typing import Sequence

from sqlalchemy import Select, select
from sqlalchemy.orm import selectinload

from ..ingestion.base import NormalizedRecord
from ..models import Entity, EntityType, Event, Sector, Source, SourceType
from ..nlp.ner import ExtractedEntity
from ..utils.logging import get_logger

logger = get_logger("event_service")


class EventService:
    """Business logic around events, sources, and entities."""

    @staticmethod
    async def get_or_create_source(
        session,
        *,
        name: str,
        source_type: SourceType,
        description: str | None = None,
    ) -> Source:
        stmt = select(Source).where(Source.name == name)
        result = await session.execute(stmt)
        source = result.scalar_one_or_none()
        if source:
            return source
        source = Source(name=name, source_type=source_type, description=description)
        session.add(source)
        await session.flush()
        logger.info("created source", extra={"source_name": name, "source_type": source_type.value})
        return source

    @staticmethod
    async def ingest_record(
        session,
        *,
        record: NormalizedRecord,
        source: Source,
        relevance_score: float,
        is_security_relevant: bool,
        entities: list[ExtractedEntity],
    ) -> Event:
        context = dict(record.metadata or {})
        context.setdefault("source_origin", record.source_origin)

        event = Event(
            timestamp=record.timestamp,
            source_id=source.id,
            country=record.country,
            sector=record.sector if isinstance(record.sector, Sector) else Sector.UNKNOWN,
            geo_lat=record.geo_lat,
            geo_lon=record.geo_lon,
            language=record.language,
            text=record.text,
            context=context,
            relevance_score=relevance_score,
            is_security_relevant=is_security_relevant,
        )
        session.add(event)
        await session.flush()

        for item in entities:
            entity = Entity(
                event_id=event.id,
                entity_type=item.entity_type or EntityType.UNKNOWN,
                value=item.value,
                confidence=item.confidence,
            )
            session.add(entity)
        logger.info(
            "ingested event",
            extra={
                "event_id": event.id,
                "source": source.name,
                "sector": event.sector.value,
                "country": event.country,
                "relevance": round(relevance_score, 3),
            },
        )
        return event

    @staticmethod
    async def list_events(
        session,
        *,
        country: str | None = None,
        sector: Sector | None = None,
        time_from: datetime | None = None,
        time_to: datetime | None = None,
        min_relevance: float | None = None,
        limit: int = 50,
        offset: int = 0,
    ) -> Sequence[Event]:
        stmt: Select = (
            select(Event)
            .options(
                selectinload(Event.source),
                selectinload(Event.entities),
                selectinload(Event.campaigns),
            )
            .order_by(Event.timestamp.desc())
            .limit(limit)
            .offset(offset)
        )
        if country:
            stmt = stmt.where(Event.country == country)
        if sector:
            stmt = stmt.where(Event.sector == sector)
        if time_from:
            stmt = stmt.where(Event.timestamp >= time_from)
        if time_to:
            stmt = stmt.where(Event.timestamp <= time_to)
        if min_relevance is not None:
            stmt = stmt.where(Event.relevance_score >= min_relevance)

        result = await session.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def get_event(session, event_id: str) -> Event | None:
        stmt = (
            select(Event)
            .where(Event.id == event_id)
            .options(
                selectinload(Event.source),
                selectinload(Event.entities),
                selectinload(Event.campaigns),
            )
        )
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def list_entities(
        session,
        *,
        entity_type: EntityType | None = None,
        value: str | None = None,
        limit: int = 100,
    ) -> Sequence[Entity]:
        stmt: Select = select(Entity).order_by(Entity.id.desc()).limit(limit)
        if entity_type:
            stmt = stmt.where(Entity.entity_type == entity_type)
        if value:
            stmt = stmt.where(Entity.value.ilike(f"%{value}%"))
        result = await session.execute(stmt)
        return result.scalars().all()


__all__ = ["EventService"]
