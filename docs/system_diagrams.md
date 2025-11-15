
## 1. Components & Responsibilities (high level)

### External Data Sources
-	Social/media & messaging: Telegram, X, FB, IG, TikTok, VK, forums, darknet, etc.
-	News & press: multi-lingual media, official press releases.
-	CTI: vendor reports, public CTI feeds, MITRE, URLHaus, VirusTotal, etc.
-	Geo/satellite/aerial: Sentinel/Copernicus, EUMETSAT, NASA, drones.
-	Infrastructure & registries: OSM, CI datasets, WHOIS/DNS, domain registries, public protest registries.

### Ingestion & Streaming
-	Connectors & scrapers (per source).
-	API clients, RSS readers, file collectors (PDF/CSV, satellite products).
-	Validation, de-duplication, basic normalisation.
-	Streaming bus (e.g. Kafka) for real-time feeds.

### Raw & Processed Data Storage
-	Data lake / object store for raw + intermediate artefacts.
-	Document store (e.g. MongoDB) for enriched documents.
-	Relational DB (PostgreSQL) for core entities and configuration.
-	Search index (Elastic/OpenSearch) for full-text search.
-	Graph DB for entities/relations.
-	Geospatial store (PostGIS) for map-heavy queries.
-	Labelled dataset store for ML training data.

### Processing & Enrichment
-	ETL pipelines (batch + streaming).
-	NLP services (classification, NER, event extraction).
-	CV services (image/video analysis).
-	Geo-enrichment (reverse geocoding, OSM overlays, CI proximity).
-	STIX/TAXII normalisation & CTI entity extraction.

### Labelling & ML Lifecycle
-	Pre-labelling / weak supervision service.
-	Annotation UI & backend.
-	Training pipelines, feature store, model registry.
-	Online & batch inference services.
-	MLOps monitoring (drift, performance).

### Threat Analytics & Correlation
-	Knowledge graph builder.
-	Correlation & fusion engine (merge entities/events).
-	Rules engine (deterministic logic).
-	Statistical & ML-based anomaly detection.
-	Risk scoring & prioritisation.

### Frontend & Integrations
-	Analyst UI (dashboards, graphs, timelines, maps).
-	Case management & investigation workbench.
-	Admin/config UI (sources, rules, risk models).
-	APIs & webhooks for SIEM/TIP/SOC tools (STIX/TAXII, REST, etc.).

### Security & Governance (cross-cutting)
-	Identity & access management.
-	Auditing & logging.
-	Data lineage & provenance tracking.
-	Privacy, legal & policy enforcement.

⸻

## 2. Modular Breakdown (services/modules)

You can think of these as microservices / domains:
1.	Source Connectors
    - social-media-connector-*, news-collector, cti-feed-ingestor, satellite-fetcher, dns-whois-collector, etc.
2.	Ingestion & Streaming
    -	ingestion-gateway (auth, rate limiting, validation)
    -	stream-router (routes events to topics)
    -	Kafka (or similar) topics per source/type.
3.	ETL & Enrichment
    -	etl-orchestrator
    -	text-normalizer (language detection, cleaning)
    -	nlp-enricher (classification, NER, event extraction)
    -	cv-enricher (image/video models)
    -	geo-enricher
    -	stix-normalizer (emits STIX objects/relationships)
4.	Storage Services
    -	raw-store-service
    -	document-store-service
    -	search-index-service
    -	graph-store-service
    -	geo-store-service
    -	timeseries-store-service (optional for metrics/logs)
5.	Labelling / Annotation
    -	prelabelling-service (rules, weak supervision, model-aided)
    -	annotation-backend
    -	annotation-ui
    -	gold-dataset-service
6.	ML Platform
    -	feature-store
    -	training-orchestrator
    -	model-registry
    -	online-inference-service
    -	batch-inference-service
    -	ml-monitoring-service
7.	Threat Analytics & Correlation
    -	knowledge-graph-builder
    -	correlation-engine
    -	rules-engine
    -	anomaly-engine
    -	risk-scoring-service
    -	alerting-service
8.	APIs & Frontend
    -	query-api (for UI and external integrations)
    -	alert-api / webhook-dispatcher
    -	analyst-ui (dashboards, graph, map)
    -	admin-ui
9.	Security & Governance
    -	auth-service
    -	policy-engine (data access, retention rules)
    -	audit-log-service
    -	config-service (central config & feature flags)

⸻

## 3. Diagrams


#### 3.1 High-level Overall Layered System Design (Layers only)

```mermaid
graph TD
  L1["Layer 1 - External data sources"]
  L2["Layer 2 - Ingestion and streaming"]
  L3["Layer 3 - Processing and enrichment"]
  L4["Layer 4 - Storage and knowledge"]
  L5["Layer 5 - ML and threat analytics"]
  L6["Layer 6 - Frontend and integrations"]

  L1 --> L2 --> L3 --> L4 --> L5 --> L6
```

#### 3.2 Compact Vertical Overall Design (few components per layer)
```mermaid
graph TD
  %% Layer 1
  subgraph L1["Layer 1 - External data sources"]
    direction TB
    SM["Social and messaging platforms"]
    News["News and press"]
    CTI["CTI and threat feeds"]
    Geo["Satellite and geo data"]
  end

  %% Layer 2
  subgraph L2["Layer 2 - Ingestion and streaming"]
    direction TB
    Conn["Source connectors"]
    GW["Ingestion gateway"]
    Bus["Streaming bus"]
  end

  %% Layer 3
  subgraph L3["Layer 3 - Processing and enrichment"]
    direction TB
    ETL["ETL orchestrator"]
    NLP["NLP enrichment"]
    CV["CV enrichment"]
    GeoEnrich["Geo enrichment"]
    STIXNorm["STIX normaliser"]
  end

  %% Layer 4
  subgraph L4["Layer 4 - Storage and knowledge"]
    direction TB
    Raw["Raw data lake"]
    Docs["Document store"]
    Search["Search index"]
    Graph["Knowledge graph database"]
    GeoDB["Geospatial database"]
  end

  %% Layer 5
  subgraph L5["Layer 5 - ML and threat analytics"]
    direction TB
    Feat["Feature store"]
    Train["Training orchestrator"]
    Registry["Model registry"]
    Corr["Correlation engine"]
    Anom["Anomaly detection"]
    Risk["Risk scoring and alerts"]
  end

  %% Layer 6
  subgraph L6["Layer 6 - Frontend and integrations"]
    direction TB
    UI["Analyst UI"]
    Admin["Admin and config UI"]
    API["Query and integration API"]
    SIEM["External SIEM and TIP"]
  end

  %% Vertical layer connections
  L1 --> L2
  L2 --> L3
  L3 --> L4
  L4 --> L5
  L5 --> L6
```

#### 3.3 Layers

##### 3.3.1 Layer 1 – External Data Sources

```mermaid
graph TD
  subgraph L1["Layer 1 - External data sources"]
    direction TB
    SM["Social and messaging platforms"]
    News["News and press"]
    CTI["CTI and threat feeds"]
    Geo["Satellite and geo providers"]
    Infra["Infrastructure and registry data"]
    Darknet["Darknet markets and forums"]
  end

  SM --> Out["To ingestion and streaming layer"]
  News --> Out
  CTI --> Out
  Geo --> Out
  Infra --> Out
  Darknet --> Out
```
#### 3.3.2 Layer 2 – Ingestion and Streaming

```mermaid
graph TD
  InL1["From external data sources"] --> Conn

  subgraph L2["Layer 2 - Ingestion and streaming"]
    direction TB
    Conn["Source connectors and scrapers"]
    GW["Ingestion gateway (validation and auth)"]
    Val{"Valid and accepted?"}
    Err["Error and rejection log"]
    Bus["Streaming bus (for example Kafka topics)"]
  end

  Conn --> GW
  GW --> Val
  Val -- "No" --> Err
  Val -- "Yes" --> Bus

  Bus --> OutL3["To processing and enrichment layer"]
```

#### 3.3.3 Layer 3 – Processing and Enrichment
```mermaid
graph TD
  InL2["From streaming bus"] --> ETL

  subgraph L3["Layer 3 - Processing and enrichment"]
    direction TB
    ETL["ETL orchestrator"]
    Pre["Pre processing (dedupe and parsing)"]
    TextNorm["Text normaliser"]
    MediaExt["Media extractor (images and video)"]
    GeoMeta["Geo metadata extractor"]
    NLP["NLP enrichment (classification and NER)"]
    CV["CV enrichment (scene, objects and OCR)"]
    GeoEnrich["Geo enrichment and CI proximity"]
    STIXNorm["STIX normaliser (CTI objects and relations)"]
  end

  ETL --> Pre
  Pre --> TextNorm
  Pre --> MediaExt
  Pre --> GeoMeta

  TextNorm --> NLP
  MediaExt --> CV
  GeoMeta --> GeoEnrich

  NLP --> STIXNorm
  CV --> STIXNorm
  GeoEnrich --> STIXNorm

  ETL --> OutRaw["To raw data lake in storage layer"]
  NLP --> OutDocs["To document store in storage layer"]
  CV --> OutDocs
  GeoEnrich --> OutDocs
  STIXNorm --> OutGraph["To knowledge graph and search in storage layer"]
```

#### 3.3.4 Layer 4 – Storage and Knowledge

```mermaid
graph TD
  InProc["From processing and enrichment layer"] --> Raw
  InProc --> Docs
  InProc --> Graph
  InProc --> Search
  InProc --> GeoDB

  subgraph L4["Layer 4 - Storage and knowledge"]
    direction TB
    Raw["Raw data lake"]
    Docs["Document store"]
    Search["Search index"]
    Graph["Knowledge graph database"]
    GeoDB["Geospatial database"]
    Labels["Labelled dataset store"]
  end

  Docs --> Labels

  Raw --> OutML["To ML and training layer"]
  Docs --> OutML
  Labels --> OutML

  Graph --> OutQ["To query and analytics"]
  Search --> OutQ
  GeoDB --> OutQ
```

#### 3.3.5 Layer 5 – ML and Threat Analytics

```mermaid
graph TD
  InStore["From storage and knowledge layer"] --> Feat

  subgraph L5a["ML lifecycle"]
    direction TB
    Feat["Feature store"]
    Train["Training orchestrator"]
    Registry["Model registry"]
    OnlineInf["Online inference service"]
    BatchInf["Batch inference jobs"]
  end

  Feat --> Train
  Train --> Registry
  Registry --> OnlineInf
  Registry --> BatchInf

  subgraph L5b["Threat analytics"]
    direction TB
    KGBuilder["Knowledge graph builder"]
    Corr["Correlation and fusion engine"]
    Rules["Rules engine"]
    Anom["Anomaly detection engine"]
    Risk["Risk scoring"]
    Alert["Alerting service"]
  end

  InStore --> KGBuilder
  OnlineInf --> KGBuilder
  BatchInf --> KGBuilder

  KGBuilder --> Corr
  Corr --> Rules
  Corr --> Anom
  Rules --> Risk
  Anom --> Risk
  Risk --> Alert

  Alert --> OutL6["To frontend and external systems"]
```

#### 3.3.6 Layer 6 – Frontend and Integrations
```mermaid
graph TD
  InAlert["From alerting service"] --> UI
  InQuery["From query and analytics APIs"] --> UI

  subgraph L6["Layer 6 - Frontend and integrations"]
    direction TB
    UI["Analyst UI (dashboards, map and graph)"]
    Cases["Case and investigation workspace"]
    Admin["Admin and configuration UI"]
    QueryAPI["Query and search API"]
    AlertAPI["Alert and webhook API"]
    SIEM["External SIEM and TIP"]
  end

  UI --> Cases
  Admin --> QueryAPI

  InAlert --> AlertAPI
  AlertAPI --> SIEM

  UI --> OutFB["Analyst feedback to labelling and ML layer"]
```
⸻

### 3.4 End-to-End Alerting Sequence (Sequence Diagram)

```mermaid
sequenceDiagram
  participant Src as OSINT source
  participant Conn as Source connector
  participant Bus as Streaming bus
  participant ETL as ETL and enrichment
  participant ML as Online inference
  participant Threat as Threat analytics engine
  participant Store as Storage layer
  participant UI as Analyst UI
  participant SIEM as External SIEM or TIP

  Src->>Conn: New message, article or image
  Conn->>Bus: Normalised event
  Bus->>ETL: Process event

  ETL->>ML: Request predictions
  ML-->>ETL: Predicted labels and entities

  ETL->>Store: Save raw and enriched data
  ETL->>Threat: Send enriched event

  Threat->>Store: Update graph and indexes
  Threat->>Threat: Correlate and score risk
  Threat-->>Store: Persist alert

  Threat-->>UI: New alert for analyst
  Threat-->>SIEM: Send alert or IOC bundle

  UI->>Store: Analyst notes and feedback
  Store-->>ML: Export feedback as training data
```

### 3.5 Overall Layered System Design

```mermaid
graph TD
  %% Layer 1 - External Data Sources
  subgraph L1["Layer 1 - External data sources"]
    SM["Social and messaging platforms"]
    News["News and press releases"]
    CTI["CTI feeds and vendor reports"]
    GeoSat["Satellite, aerial and geo data"]
    Infra["OSM, CI datasets, DNS and registries"]
    Darknet["Darknet and forums"]
  end

  %% Layer 2 - Ingestion and streaming
  subgraph L2["Layer 2 - Ingestion and streaming"]
    Conn["Source connectors and scrapers"]
    IngestGW["Ingestion gateway (validation and auth)"]
    StreamBus["Streaming bus (for example Kafka)"]
  end

  %% Layer 3 - Processing and enrichment
  subgraph L3["Layer 3 - Processing and enrichment"]
    ETL["ETL orchestrator"]
    TextNorm["Text normaliser"]
    NLP["NLP enrichment (classification, NER, events)"]
    CV["CV enrichment (images and video)"]
    GeoEnrich["Geo enrichment and CI proximity"]
    STIXNorm["STIX normaliser"]
  end

  %% Layer 4 - Storage and knowledge
  subgraph L4["Layer 4 - Storage and knowledge"]
    RawStore["Raw data lake"]
    DocStore["Document store"]
    SearchIdx["Search index"]
    GraphDB["Knowledge graph database"]
    GeoDB["Geospatial database"]
    LabelStore["Labelled dataset store"]
  end

  %% Layer 5 - ML and threat analytics
  subgraph L5["Layer 5 - ML and threat analytics"]
    FeatStore["Feature store"]
    TrainOrch["Training orchestrator"]
    ModelReg["Model registry"]
    OnlineInf["Online inference service"]
    BatchInf["Batch inference jobs"]
    KGBuilder["Knowledge graph builder"]
    Corr["Correlation and fusion engine"]
    Rules["Rules engine"]
    Anom["Anomaly detection engine"]
    Risk["Risk scoring"]
    Alert["Alerting service"]
  end

  %% Layer 6 - Frontend and integrations
  subgraph L6["Layer 6 - Frontend and integrations"]
    AnalystUI["Analyst UI (dashboards, graph, map)"]
    AdminUI["Admin and config UI"]
    QueryAPI["Query and search API"]
    AlertAPI["Alert and webhook API"]
    SIEMTIP["External SIEM, TIP and SOC tools"]
  end

  %% Cross cutting
  subgraph Sec["Cross cutting - Security and governance"]
    Auth["Authentication and authorisation"]
    Policy["Policy and compliance"]
    Audit["Audit logging"]
    Config["Config service"]
  end

  %% Connections
  SM --> Conn
  News --> Conn
  CTI --> Conn
  GeoSat --> Conn
  Infra --> Conn
  Darknet --> Conn

  Conn --> IngestGW --> StreamBus

  StreamBus --> ETL
  ETL --> TextNorm --> NLP
  ETL --> CV
  ETL --> GeoEnrich

  NLP --> STIXNorm
  CV --> STIXNorm
  GeoEnrich --> STIXNorm

  ETL --> RawStore
  NLP --> DocStore
  CV --> DocStore
  GeoEnrich --> DocStore
  STIXNorm --> GraphDB
  STIXNorm --> SearchIdx

  %% Labelling and ML
  DocStore --> LabelStore
  LabelStore --> FeatStore
  FeatStore --> TrainOrch --> ModelReg
  ModelReg --> OnlineInf
  ModelReg --> BatchInf

  OnlineInf --> NLP
  OnlineInf --> Anom
  BatchInf --> Anom

  %% Threat analytics
  DocStore --> KGBuilder
  GraphDB --> KGBuilder
  KGBuilder --> Corr
  Corr --> Rules
  Corr --> Anom
  Rules --> Risk
  Anom --> Risk
  Risk --> Alert
  Alert --> SearchIdx

  %% Frontend
  SearchIdx --> QueryAPI
  GraphDB --> QueryAPI
  GeoDB --> QueryAPI
  QueryAPI --> AnalystUI
  QueryAPI --> AdminUI
  Alert --> AlertAPI --> SIEMTIP

  %% Security and governance influence
  Auth -.-> IngestGW
  Auth -.-> QueryAPI
  Auth -.-> AnalystUI
  Policy -.-> ETL
  Policy -.-> LabelStore
  Policy -.-> RawStore
  Audit -.-> Alert
  Audit -.-> AnalystUI
  Config -.-> Conn
  Config -.-> Rules
  Config -.-> TrainOrch
```

### 3.6 Selected focus viewa 

#### 3.6.1 Data Ingestion & Processing Flow (Flowchart)

```mermaid
graph TD
  A["External source event (Telegram message or news article)"] --> B["Source connector"]
  B --> C["Ingestion gateway (schema, size and auth check)"]
  C --> D{"Valid and accepted?"}
  D -- "No" --> E["Reject and log error"]
  D -- "Yes" --> F["Streaming topic"]

  F --> G["Pre processor (dedupe, parsing, language detection)"]
  G --> H{"Security relevant?"}
  H -- "No" --> I["Store as low priority or archive"]
  H -- "Yes" --> J["ETL orchestrator"]

  J --> K["Text normaliser"]
  J --> L["Media extractor (images and video frames)"]
  J --> M["Geo metadata extractor"]

  K --> N["NLP enrichment (classification, NER and events)"]
  L --> O["CV enrichment (scene, objects and OCR)"]
  M --> P["Geo enrichment (reverse geocode and CI proximity)"]

  N --> Q["STIX normaliser"]
  O --> Q
  P --> Q

  %% Storage
  J --> R["Raw data lake"]
  N --> S["Document store"]
  O --> S
  P --> S
  Q --> T["Knowledge graph database"]
  Q --> U["Search index"]
```

⸻

### 3.6.2 Labelling & ML Lifecycle (Flowchart)

```mermaid
graph TD
  A["New enriched document, image or event"] --> B["Pre labelling service (rules, weak supervision, old models)"]
  B --> C["Annotation queue"]

  C --> D["Annotation UI and backend"]
  D --> E{"Annotator action"}

  E -- "Confirm or correct labels" --> F["Labelled sample"]
  E -- "Skip or flag issue" --> G["Review bucket"]

  F --> H["Labelled dataset store"]
  G --> H

  H --> I["Feature store builder"]
  I --> J["Feature store"]

  J --> K["Training orchestrator"]
  K --> L["Model training jobs"]
  L --> M["Validation and metrics report"]

  M --> N{"Meets performance and policy?"}
  N -- "No" --> O["Iterate on labels, features or models"]
  N -- "Yes" --> P["Register model in model registry"]

  P --> Q["Deploy to online inference service"]
  P --> R["Deploy to batch inference jobs"]

  Q --> S["Real time pipelines (NLP, CV, anomaly)"]
  R --> T["Periodic re scoring and backfilling"]

  S --> U["Analyst feedback and corrections"]
  U --> H
```

⸻
