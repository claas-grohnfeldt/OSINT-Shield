from __future__ import annotations

from collections import Counter
from datetime import datetime

from sqlalchemy import Select, delete, select
from sqlalchemy.orm import selectinload

from ..models import Campaign, Event, Sector, event_campaign_association
from ..nlp.clustering import cluster_events
from ..nlp.scoring import compute_campaign_risk
from ..utils.logging import get_logger

logger = get_logger("campaign_service")


class CampaignService:
    """Create and query campaign groupings produced by the clustering layer."""

    @staticmethod
    async def rebuild_campaigns(session) -> list[Campaign]:
        events_stmt = select(Event).options(selectinload(Event.source), selectinload(Event.entities))
        events = (await session.execute(events_stmt)).scalars().all()
        await session.execute(delete(event_campaign_association))
        await session.execute(delete(Campaign))
        if not events:
            logger.info("no events available for campaign building")
            return []

        clusters = cluster_events(events)
        campaigns: list[Campaign] = []
        for idx, cluster_events_list in enumerate(clusters.values(), start=1):
            countries = sorted({event.country for event in cluster_events_list})
            top_sector = Counter(event.sector for event in cluster_events_list).most_common(1)[0][0]
            risk = compute_campaign_risk(cluster_events_list)
            campaign = Campaign(
                label=f"Cluster {idx}",
                description=f"{len(cluster_events_list)} linked events across {', '.join(countries)}",
                sector=top_sector if isinstance(top_sector, Sector) else Sector.UNKNOWN,
                risk_score=risk,
                countries=countries,
                time_start=min(event.timestamp for event in cluster_events_list),
                time_end=max(event.timestamp for event in cluster_events_list),
            )
            campaign.events.extend(cluster_events_list)
            session.add(campaign)
            campaigns.append(campaign)
            logger.info("campaign created", extra={"campaign": campaign.label, "risk": risk})
        await session.flush()
        return campaigns

    @staticmethod
    async def list_campaigns(
        session,
        *,
        sector: Sector | None = None,
        country: str | None = None,
        min_risk: float | None = None,
        time_from: datetime | None = None,
        time_to: datetime | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> list[Campaign]:
        stmt: Select = (
            select(Campaign)
            .options(selectinload(Campaign.events))
            .order_by(Campaign.risk_score.desc())
            .limit(limit)
            .offset(offset)
        )
        if sector:
            stmt = stmt.where(Campaign.sector == sector)
        if min_risk is not None:
            stmt = stmt.where(Campaign.risk_score >= min_risk)
        if time_from:
            stmt = stmt.where(Campaign.time_end >= time_from)
        if time_to:
            stmt = stmt.where(Campaign.time_start <= time_to)
        result = await session.execute(stmt)
        campaigns = result.scalars().all()
        if country:
            campaigns = [
                campaign
                for campaign in campaigns
                if campaign.countries and country in campaign.countries
            ]
        return campaigns

    @staticmethod
    async def get_campaign(session, campaign_id: str) -> Campaign | None:
        stmt = (
            select(Campaign)
            .where(Campaign.id == campaign_id)
            .options(
                selectinload(Campaign.events).selectinload(Event.entities),
                selectinload(Campaign.events).selectinload(Event.source),
            )
        )
        result = await session.execute(stmt)
        return result.scalar_one_or_none()
