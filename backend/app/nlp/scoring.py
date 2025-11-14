from __future__ import annotations

from collections import Counter

from ..models.event import Event, Sector


CRITICAL_SECTORS = {Sector.ENERGY, Sector.DEFENCE, Sector.SPACE, Sector.TELECOM}


def compute_campaign_risk(events: list[Event]) -> float:
    if not events:
        return 0.0

    total_events = len(events)
    avg_relevance = sum(event.relevance_score for event in events) / total_events
    unique_countries = len({event.country for event in events})
    unique_sources = len({event.source_id for event in events})
    sector_counts = Counter(event.sector for event in events)
    critical_bonus = 10 if any(sector in CRITICAL_SECTORS for sector in sector_counts) else 0

    base = total_events * 12
    diversity = unique_countries * 6 + unique_sources * 4
    score = min(100.0, base + diversity + avg_relevance * 40 + critical_bonus)
    return round(score, 1)


__all__ = ["compute_campaign_risk"]
