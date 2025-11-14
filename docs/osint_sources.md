# OSINT Source Categories Considered

| Category | Examples | Prototype Status |
| --- | --- | --- |
| Social / grassroots chatter | Telegram, X/Twitter, federated social feeds, activist channels | Simulated via `PublicSocialConnector` JSON |
| News & policy reporting | ENISA, EU Observer, national press releases | Simulated via `PublicNewsConnector` |
| Technical threat reporting | CERT advisories, vendor reports, malware blogs | Simulated via `PublicCyberReportsConnector` |
| Government / EU agencies | Europol, NATO STRATCOM, EEAS briefings | Placeholder – ready for future connectors |
| Classified / SIGINT feeds | Satellite, HUMINT, defensive sensors | Placeholder – described in `future_extensions_classified_feeds.md` |

For this prototype we keep data local, deterministic, and privacy-safe. Each entry emulates the structure and metadata that real feeds would provide so the rest of the platform can evolve without redesigning ingestion.
