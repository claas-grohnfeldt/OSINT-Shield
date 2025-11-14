# Architecture Overview

OSINT Shield links lightweight ingestion, NLP enrichment, and analyst tooling to provide early warning for hybrid threats targeting EU critical infrastructure.

```
Connectors → Normalization → NLP (classifier + NER) → SQLite → FastAPI → REST → React Dashboard
```

## Backend

- **Connectors** implement `BaseConnector` to fetch JSON/CSV data. Classified feeds can plug into the same interface without touching downstream logic.
- **Ingestion orchestration** (`sample_loader`) normalizes records, runs relevance scoring + NER, stores events/entities, then clusters them into campaigns.
- **NLP** uses a TF-IDF + Logistic Regression classifier for binary relevance plus a spaCy-based, regex-augmented NER tuned for cyber indicators.
- **Persistence** relies on SQLAlchemy models backed by SQLite (dev). The schema captures Sources, Events, Entities, and Campaigns (event clusters with risk scores).
- **APIs** expose `/health`, `/events`, `/campaigns`, and `/entities` endpoints for UI and automation.

## Frontend

- React + TypeScript + Vite + Tailwind compose the analyst dashboard.
- React Router drives navigation between Dashboard, Campaign detail, and Event inspector views.
- React-Leaflet renders EU maps with risk-proportional campaign markers.

## Extensibility

- Adding classified connectors only requires a new subclass + configuration—no core changes.
- NLP modules expose clear classes (`RelevanceClassifier`, `ThreatNER`, `cluster_events`, `compute_campaign_risk`) so they can be replaced with stronger models later.
- Database migrations can be introduced via Alembic if the schema grows beyond the prototype.
