from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from ..models.entity import EntityType


class EntityRead(BaseModel):
    id: int
    entity_type: EntityType
    value: str
    confidence: float

    model_config = ConfigDict(from_attributes=True)
