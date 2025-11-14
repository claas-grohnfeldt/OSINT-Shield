# OSINT Shield – Early Warning for Hybrid Threats Against EU Critical Infrastructure

OSINT Shield is a prototype that ingests open-source intelligence, enriches it with lightweight NLP, and surfaces clustered hybrid-threat campaigns on a web dashboard.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/414924a4-b5cb-4a05-8128-4b4a15bcff6e" />

## Why

European operators need early indicators of hybrid operations that mix cyber, disinfo, and physical disruption. OSINT Shield fuses public-style data, scores relevance, extracts entities, groups related events, and ranks the most urgent campaigns.

## Architecture Snapshot

```
Sample JSON feeds
   │
   ├─ connectors (social / news / cyber reports)
   │
   ├─ normalization → RelevanceClassifier → ThreatNER
   │
   ├─ SQLite (Sources, Events, Entities)
   │
   ├─ clustering + risk scoring → Campaigns
   │
   └─ FastAPI REST → React + Leaflet dashboard
```

## Features

- Pluggable ingestion connectors (public today, classified-ready tomorrow)
- Binary relevance classifier + rule-aided NER for threat entities
- Campaign clustering with heuristic risk scoring
- FastAPI REST with filters for country, sector, timeframe, and risk
- React/Tailwind dashboard with EU map, campaign list, and event inspector
- Sample data + docs for onboarding analysts and engineers

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Pydantic, SQLite, uv, scikit-learn, spaCy
- **Frontend**: React 18, TypeScript, Vite, TailwindCSS, React-Leaflet
- **Tooling**: pytest, GitHub Actions CI, .editorconfig

## Quickstart

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)
- Node.js 18+ (npm bundled)

### Backend

```bash
cd backend
uv sync                               # install runtime deps
uv run python -m app.ingestion.sample_loader  # load synthetic OSINT data
uv run uvicorn app.main:app --reload --port 8000
```

Explore the API at `http://localhost:8000/docs`.

For local testing (pytest) install the tooling group as well:

```bash
uv sync --group dev
uv run pytest
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` and start investigating campaigns.

For production builds run:

```bash
npm run build
npm run preview
```

## Analyst Walk-through

1. Load sample data via `sample_loader`.
2. Visit the dashboard: map markers show campaign centroid + risk (size/color).
3. Use the filter bar (sector, country, risk slider) to focus.
4. Click a campaign to inspect the timeline, entity counts, and affected countries.
5. Drill into an event for full text, highlighted entities, and source context.

## Extending with Classified Feeds

- Implement a new `BaseConnector` subclass for the classified source.
- Emit the same normalized fields; downstream NLP and clustering work unchanged.
- Use `docs/future_extensions_classified_feeds.md` for schema + governance tips.

## Repository Structure

- `backend/` – FastAPI app, ingestion, NLP, tests
- `frontend/` – React dashboard
- `docs/` – architecture, pipeline, source taxonomy, UX, classified roadmap
- `.github/workflows/ci.yaml` – runs backend tests + frontend build on push

## Validation Status

The following commands were executed on macOS (Node 25 / Python 3.12) to verify the repo end-to-end:

```bash
cd backend && uv sync && uv run python -m app.ingestion.sample_loader && uv run pytest
cd frontend && npm install && npm run build
```

No warnings or errors were observed.

## License

MIT – see [LICENSE](LICENSE).
