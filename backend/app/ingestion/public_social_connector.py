from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Iterable

from ..models.event import Sector
from ..models.source import SourceType
from .base import BaseConnector, NormalizedRecord


class PublicSocialConnector(BaseConnector):
    """Mock connector that ingests social media chatter from a JSON file."""

    file_name = "social_posts.json"

    def __init__(self, data_dir: Path | None = None) -> None:
        super().__init__(data_dir)
        self.name = "Open Social Pulse"
        self.description = "Sample EU-focused social posts"
        self.source_type = SourceType.PUBLIC_OSINT_SOCIAL

    def fetch(self) -> Iterable[NormalizedRecord]:  # noqa: D401 - documented in base
        path = self.data_dir / self.file_name
        payload = json.loads(path.read_text())
        for row in payload:
            yield NormalizedRecord(
                timestamp=_parse_ts(row["timestamp"]),
                source_name=self.name,
                source_type=self.source_type,
                source_origin=row.get("platform", "unknown"),
                country=row.get("country", "EU"),
                sector=_sector(row.get("sector")),
                text=row.get("text", ""),
                language=row.get("language"),
                geo_lat=row.get("geo", {}).get("lat"),
                geo_lon=row.get("geo", {}).get("lon"),
                metadata={"raw_id": row.get("id"), "engagement": row.get("engagement")},
            )


def _parse_ts(value: str) -> datetime:
    if value.endswith("Z"):
        value = value.replace("Z", "+00:00")
    return datetime.fromisoformat(value)


def _sector(value: str | None) -> Sector:
    if not value:
        return Sector.UNKNOWN
    try:
        return Sector(value)
    except ValueError:
        return Sector.UNKNOWN


__all__ = ["PublicSocialConnector"]
