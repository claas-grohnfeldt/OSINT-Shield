# Data Pipeline

1. **Ingestion** – Each connector loads raw JSON/CSV, adds provenance (source type, origin, timestamps) and yields `NormalizedRecord` objects.
2. **Normalization** – Records align to common fields (country, sector, geo, language, free text) so analytics is source-agnostic.
3. **Classification** – `RelevanceClassifier` scores the text using TF-IDF + Logistic Regression and flags security-relevant events.
4. **NER & Indicator extraction** – `ThreatNER` maps actors, organisations, CVEs, IPs, domains, and facilities using spaCy + regex rules.
5. **Persistence** – SQLAlchemy stores Sources, Events, Entities, and metadata in SQLite. Entities preserve confidence for later fusion.
6. **Clustering** – TF-IDF vectors feed Agglomerative clustering to create campaigns grouping related events.
7. **Risk scoring** – `compute_campaign_risk` combines event counts, relevance, country spread, and sector criticality (energy/defence emphasis) to rank campaigns 0–100.
8. **API exposure** – FastAPI serves REST endpoints with filtering by sector, country, time, and risk.
9. **Analyst UX** – React dashboard pulls campaign + event data, renders Leaflet map markers, and exposes detail panes for investigations.
