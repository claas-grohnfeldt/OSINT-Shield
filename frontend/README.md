# OSINT Shield – Frontend

React + TypeScript + Vite dashboard for visualising OSINT Shield campaigns, events, and risk on an EU map.

## Stack

- React 18 + React Router
- TypeScript + Vite
- Tailwind CSS (dark cyber-defence palette)
- React-Leaflet for mapping

## Development

```bash
cd frontend
npm install
npm run dev
```

- Dev server defaults to `http://localhost:5173`
- API base URL defaults to `http://localhost:8000`. Override via `VITE_API_BASE` env var.

## Build

```bash
npm run build
npm run preview
```

## Screens

- **Dashboard** – EU map with campaign markers, filter bar, campaign cards, and recent events.
- **Campaign Detail** – risk summary, timeline of events, entity counts, and mini-map.
- **Event Detail** – metadata, highlighted narrative, entity chips, and links back to campaigns.
