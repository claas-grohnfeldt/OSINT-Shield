from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Iterable

from ..models.event import Sector
from ..models.source import SourceType
from .base import BaseConnector, NormalizedRecord


class PublicNewsConnector(BaseConnector):
    """Mock connector representing EU-focused news wires."""

    file_name = "news_articles.json"

    def __init__(self, data_dir: Path | None = None) -> None:
        super().__init__(data_dir)
        self.name = "Continental Newswire"
        self.description = "Sample articles from pan-EU outlets"
        self.source_type = SourceType.PUBLIC_OSINT_NEWS

    def fetch(self) -> Iterable[NormalizedRecord]:
        path = self.data_dir / self.file_name
        payload = json.loads(path.read_text())
        for row in payload:
            yield NormalizedRecord(
                timestamp=_parse_ts(row["timestamp"]),
                source_name=self.name,
                source_type=self.source_type,
                source_origin=row.get("outlet", "unknown"),
                country=row.get("country", "EU"),
                sector=_sector(row.get("sector")),
                text=row.get("headline", "") + "\n" + row.get("summary", ""),
                language=row.get("language", "en"),
                geo_lat=row.get("geo", {}).get("lat"),
                geo_lon=row.get("geo", {}).get("lon"),
                metadata={"raw_id": row.get("id"), "url": row.get("url")},
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


__all__ = ["PublicNewsConnector"]
