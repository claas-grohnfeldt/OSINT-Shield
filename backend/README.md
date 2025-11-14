# OSINT Shield – Backend

FastAPI + SQLAlchemy service that ingests OSINT-style feeds, enriches them with NLP, and exposes campaign + event APIs.

## Tech stack

- Python 3.12+, FastAPI, SQLAlchemy 2.x, Pydantic v2
- SQLite (dev) managed through async SQLAlchemy
- Lightweight NLP: TF-IDF classifier, spaCy + regex NER, TF-IDF clustering
- uv for dependency and environment management

## Getting started

```bash
cd backend
uv sync
uv run python -m app.ingestion.sample_loader  # load sample OSINT data
uv run uvicorn app.main:app --reload --port 8000
```

Visit `http://localhost:8000/docs` for interactive API docs.

To install tooling such as pytest/mypy run `uv sync --group dev`.

## Data model

- **Source** – describes where an event originated (social, news, technical, future classified feeds).
- **Event** – normalized payload with timestamp, country, sector, language, free text, relevance score.
- **Entity** – named entities / indicators extracted from the event.
- **Campaign** – grouped events with shared features + computed risk score.

## NLP pipeline

1. `RelevanceClassifier` – TF-IDF + Logistic Regression binary classifier.
2. `ThreatNER` – spaCy entity ruler + regex for IPs/domains/CVEs/actors.
3. `cluster_events` – TF-IDF vectors -> Agglomerative clustering.
4. `compute_campaign_risk` – heuristic scoring using event counts, sector weight, and geographic diversity.

## Tests

```bash
uv sync --group dev
uv run pytest
```

Tests spin up an isolated SQLite DB, run the ingestion loader, and hit the FastAPI endpoints.
