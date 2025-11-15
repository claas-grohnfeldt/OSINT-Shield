## 0. Top-Level Domains (for orientation)

From a user / organisation perspective, the platform’s use cases cluster into:

1. **Influence & information operations**  
2. **Civil unrest, protests, and public order**  
3. **Extremism, hate, and radicalisation**  
4. **Terrorism and targeted violence planning**  
5. **Critical infrastructure & sectoral risk**  
6. **Cyber threat intelligence and digital operations**  
7. **Conflict & defence situational awareness**  
8. **Policy, diplomacy, and strategic analysis**  
9. **Analyst productivity, knowledge management, and training**
---

## 1. Influence & Information Operations

### 1.1 Propaganda & Disinformation Campaigns

- **Campaign detection and clustering**
  - Detect coordinated narratives across platforms and languages.  
  - Group posts, channels, accounts and media into campaigns.

- **Source, root, and infrastructure analysis**
  - Attribute campaigns to likely sponsoring entities (state, proxies, NGOs, commercial actors).  
  - Identify core “hub” accounts, channels, media outlets.

- **Audience and reach analysis**
  - Measure spread, amplification paths, echo chambers.  
  - Identify vulnerable demographics / regions.

- **Impact and risk estimation**
  - Assess impact on public opinion, CI risk, protest risk, election security.  
  - Scenario modelling (“if this narrative continues, which risks increase?”).

### 1.2 AI-Generated & Synthetic Content

- **Deepfake / synthetic media detection**
  - Images, videos, audio and text (LLM-generated narratives, comment floods).

- **Linking synthetic content to campaigns**
  - Map detected synthetic content back to campaigns and sponsoring entities.

- **Country/actor-of-interest filters**
  - Configurable watchlists (e.g. specific states or groups).  
  - Alerts when synthetic campaigns originate from, or target, specific regions or institutions.

- **Defence & communication support**
  - Provide evidence and timelines for public communication, fact-checking, and debunking.

---

## 2. Civil Unrest, Protests, and Public Order

### 2.1 Protest & Demonstration Lifecycle

- **Early detection of planned protests**
  - Detect calls for protests/demos across platforms and languages.  
  - Distinguish legitimate protest vs. malicious, violent or foreign-influenced attempts.

- **Prediction & forecasting**
  - Estimate time, location, expected attendance.  
  - Track risk of escalation (violence, clashes; CI proximity).

- **Real-time monitoring**
  - Live OSINT for on-going events (images, videos, streams, Telegram, hashtags).  
  - Detection of live disinformation or fake imagery surrounding the protest.

- **Mapping & representation**
  - Geospatial maps of protest routes, hotspots, and incidents.  
  - Overlays with CI locations, police deployments (where known), sensitive areas.

- **Post-event analysis**
  - Identify key organisers/promoters.  
  - Link protests to propaganda / foreign influence campaigns.  
  - Lessons learned for future risk assessment.

### 2.2 Protection of Democratic Processes

- **Election-related information ops**
  - Monitor narratives aiming to delegitimise elections.  
  - Detect coordinated voter suppression, false information about voting.

- **Targeting of institutions**
  - Campaigns specifically targeting courts, parliament, public broadcasters, etc.

- **Legal & public communication support**
  - Provide evidentiary timelines and campaign mappings for official reports.

---

## 3. Extremism, Hate Speech, and Radicalisation

### 3.1 Hate Speech Detection & Analysis

- **Detection of hate content**
  - Multi-lingual hate speech and incitement to violence detection.

- **Correlation with actors and channels**
  - Map hate content to specific groups, channels, individuals.

- **Trend and geographic analysis**
  - Regional spikes in hate speech targeting specific groups (ethnic, religious, political).  
  - Link spikes to offline events or propaganda narratives.

### 3.2 Extremist Networks & Radicalisation Pathways

- **Extremist group monitoring**
  - Track extremist organisations, symbols, slogans, recruitment channels.

- **Radicalisation funnel analysis**
  - Identify how users move from “soft” content to harder extremist material.

- **Cross-platform migration**
  - Detect when banned groups reappear under new identities or on new platforms.

---

## 4. Terrorism and Targeted Violence Planning

### 4.1 Early Warning from OSINT

- **Leak and chatter detection**
  - Identify posts or documents leaking details of planned attacks (time, location, method).  
  - Watch for suspicious reconnaissance (photos of CI, police stations, government buildings).

- **Threats to specific persons or institutions**
  - Threat intelligence for VIPs, politicians, journalists, judges, etc.

### 4.2 Attack Lifecycle Support

- **Pre-attack indicators**
  - Illegal procurement chatter, “how-to” discussions, past test-runs.

- **During incident**
  - Rapid OSINT fusion for situational awareness.

- **Post-incident attribution support**
  - Link public claims, extremist propaganda, and digital traces to responsible actors.

---

## 5. Critical Infrastructure (CI) & Sectoral Risk

### 5.1 CI Threat Monitoring

- **CI-specific threat mentions**
  - Detect threats directed at specific facilities or companies.  
  - Identify sabotage discussions targeting energy, telecom, transport, health, finance, etc.

- **Proximity of protests / unrest to CI**
  - Geospatial correlation between demonstrations, unrest and nearby CI sites.

- **Cyber-physical cross-correlation**
  - Link cyber campaigns (ransomware, phishing) with physical threats or protests around the same CI operator.

### 5.2 CI Risk Assessment & Reporting

- **CI risk dashboards**
  - Per-sector and per-region risk scores (dynamic).

- **Scenario exploration**
  - “What happens if this CI site is impacted?” – support risk, resilience, and planning teams.

- **Dependencies & cascading effects**
  - Link CI sites to dependent networks (transport hubs, data centres supporting other services, etc.).

---

## 6. Cyber Threat Intelligence & Digital Operations

### 6.1 IOC & Campaign Discovery

- **Extraction of IOCs from OSINT**
  - CVEs, malware names, IPs, domains, URLs, file hashes, tools.

- **Campaign clustering**
  - Grouping of incidents, reports and chatter into coherent cyber campaigns.

### 6.2 Actor & Infrastructure Tracking

- **APT and cybercrime group monitoring**
  - Attribution support by linking artefacts across incidents and sources.

- **Attack surface & brand monitoring**
  - Monitoring mentions of a specific organisation, brand, or domain in OSINT and darknet.

### 6.3 Darknet and Breach Intelligence

- **Leak and credential monitoring**
  - Detection of breaches, leaked credentials, databases.

- **Sale of access**
  - Detection of offers to sell access to CI, large companies or government networks.

---

## 7. Conflict & Defence Situational Awareness

### 7.1 Frontline Mapping & Territorial Control

- **Frontline inference from OSINT + satellite**
  - Combine social media, news, drone footage, and satellite to map frontline changes.

- **Time-series of frontline evolution**
  - Track shifts over time, correlate with major operations, sanctions, political moves.

### 7.2 Military Activity and Capability Monitoring

- **Troop and equipment movement proxies**
  - OSINT indicators: convoy videos, satellite imagery of staging areas, logistics.

- **Weapon systems and new technology**
  - Detection of new weapon deployments, drones, EW systems, etc.

### 7.3 Civilian Harm & Infrastructure Damage

- **Damage assessment**
  - Estimation of damage to cities, CI, humanitarian infrastructure.

- **Humanitarian impact**
  - Population displacement, refugee flows (OSINT side), restrictions and blockades.

---

## 8. Policy, Diplomacy, and Strategic Analysis

### 8.1 Foreign Influence & Interference

- **Influence operations targeting political decisions**
  - Campaigns directed at specific laws, international agreements, or diplomatic initiatives.

- **Narrative alignment across countries**
  - Compare narratives pushed in multiple countries by the same actor.

### 8.2 Sanctions, Evasion & Economic Security

- **OSINT on sanctions evasion patterns**
  - Alternative trade routes, shell companies, parallel financial systems.

- **Impact assessment of sanctions and policies**
  - How information operations evolve in response to policy decisions.

---

## 9. Analyst Productivity, Knowledge Management, and Training

### 9.1 Search, Exploration, and Sense-making

- **Unified search and discovery**
  - Cross-source, cross-language search with entity awareness.

- **Graph exploration**
  - Help analysts quickly see relationships between actors, campaigns, events, IOCs, CI.

- **Geospatial exploration**
  - Map-driven exploration of incidents, protests, CI risks, conflict zones.

### 9.2 Case Management and Collaboration

- **Investigation workspaces**
  - Bundle events, entities, evidence into cases with timelines.

- **Collaboration & handover**
  - Support multi-agency collaboration while respecting data access policies.

### 9.3 Training, Simulation & Evaluation

- **Training datasets and red-team simulations**
  - Generate realistic scenarios for analyst training.

- **Model evaluation from analyst perspective**
  - Use real cases to test model performance and improve trust.
