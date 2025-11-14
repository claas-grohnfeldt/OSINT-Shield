from __future__ import annotations

import asyncio

from ..db import AsyncSessionLocal, init_db
from ..nlp.classifier import RelevanceClassifier
from ..nlp.ner import ThreatNER
from ..services.campaign_service import CampaignService
from ..services.event_service import EventService
from ..utils.logging import get_logger
from .public_cyber_reports_connector import PublicCyberReportsConnector
from .public_news_connector import PublicNewsConnector
from .public_social_connector import PublicSocialConnector

logger = get_logger("sample_loader")


async def load_sample_data() -> None:
    await init_db()
    classifier = RelevanceClassifier()
    ner = ThreatNER()
    connectors = [
        PublicSocialConnector(),
        PublicNewsConnector(),
        PublicCyberReportsConnector(),
    ]

    async with AsyncSessionLocal() as session:
        total_events = 0
        for connector in connectors:
            source = await EventService.get_or_create_source(
                session,
                name=connector.name,
                source_type=connector.source_type,
                description=connector.description,
            )
            for record in connector.fetch():
                relevance = classifier.get_relevance(record.text)
                entities = ner.extract(record.text)
                await EventService.ingest_record(
                    session,
                    record=record,
                    source=source,
                    relevance_score=relevance.score,
                    is_security_relevant=relevance.is_relevant,
                    entities=entities,
                )
                total_events += 1
        await CampaignService.rebuild_campaigns(session)
        await session.commit()
        logger.info("sample data loaded", extra={"total_events": total_events})


def main() -> None:
    asyncio.run(load_sample_data())


if __name__ == "__main__":
    main()
