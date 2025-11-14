from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

from ..models.event import Sector
from ..models.source import SourceType


@dataclass
class NormalizedRecord:
    """Canonical event representation shared between public and classified feeds."""

    timestamp: datetime
    source_name: str
    source_type: SourceType
    source_origin: str
    country: str
    sector: Sector
    text: str
    language: str | None = None
    geo_lat: float | None = None
    geo_lon: float | None = None
    metadata: dict | None = None


class BaseConnector(ABC):
    """
    Base connector for ingesting OSINT (or future classified) feeds.

    Classified connectors (SIGINT, internal logs, SITREPs, etc.) can inherit from the
    same interface to guarantee uniform normalization and downstream handling.
    """

    name: str
    description: str
    source_type: SourceType

    def __init__(self, data_dir: Path | None = None) -> None:
        backend_root = Path(__file__).resolve().parents[2]
        self.data_dir = data_dir or backend_root / "sample_data"

    @abstractmethod
    def fetch(self) -> Iterable[NormalizedRecord]:
        """Yield normalized records ready for the NLP pipeline."""


__all__ = ["BaseConnector", "NormalizedRecord"]
