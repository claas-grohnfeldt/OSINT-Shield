# Contributing to OSINT Shield

Thanks for helping improve OSINT Shield – an open prototype for early warning against hybrid threats.

## Development setup

1. Install prerequisites:
   - Python 3.12+
   - [uv](https://github.com/astral-sh/uv)
   - Node.js 18+ and npm
2. Backend:
   ```bash
   cd backend
   uv sync
   uv run python -m app.ingestion.sample_loader
   uv run uvicorn app.main:app --reload --port 8000
   ```
3. Frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Coding standards

- Python: follow PEP 8, use type hints, and keep modules lint-friendly.
- Frontend: TypeScript + React hooks, favour functional components.
- Configuration: update docs when adding new connectors, models, or UI routes.

## Tests

- Backend: `uv run pytest`
- Frontend: `npm run build` ensures type-checking and bundle integrity.

Please open an issue before large changes so we can align on approach. All contributions are welcome!
