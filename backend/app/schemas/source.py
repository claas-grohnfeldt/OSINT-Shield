from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from ..models.source import SourceType


class SourceRead(BaseModel):
    id: int
    name: str
    source_type: SourceType
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)
