from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_session
from ..models.entity import EntityType
from ..schemas import EntityRead
from ..services.event_service import EventService

router = APIRouter(prefix="/entities", tags=["entities"])


@router.get("", response_model=list[EntityRead])
async def list_entities(
    entity_type: EntityType | None = Query(default=None, alias="type"),
    value: str | None = Query(default=None),
    limit: int = Query(default=100, ge=1, le=500),
    session: AsyncSession = Depends(get_session),
) -> list[EntityRead]:
    entities = await EventService.list_entities(
        session,
        entity_type=entity_type,
        value=value,
        limit=limit,
    )
    return [EntityRead.model_validate(entity) for entity in entities]
