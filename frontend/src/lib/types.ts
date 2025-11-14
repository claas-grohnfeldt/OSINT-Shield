export type Sector =
  | 'energy'
  | 'logistics'
  | 'defence'
  | 'telecom'
  | 'space'
  | 'other'
  | 'unknown';

export interface Source {
  id: number;
  name: string;
  source_type: string;
  description?: string | null;
}

export interface Entity {
  id: number;
  entity_type: string;
  value: string;
  confidence: number;
}

export interface CampaignSnippet {
  id: string;
  label: string;
  risk_score: number;
  sector: Sector;
}

export interface EventSummary {
  id: string;
  timestamp: string;
  country: string;
  sector: Sector;
  relevance_score: number;
}

export interface EventItem {
  id: string;
  timestamp: string;
  country: string;
  sector: Sector;
  geo_lat?: number | null;
  geo_lon?: number | null;
  language?: string | null;
  text: string;
  metadata?: Record<string, unknown> | null;
  relevance_score: number;
  is_security_relevant: boolean;
  source: Source;
  campaigns: CampaignSnippet[];
  entities?: Entity[];
}

export interface Campaign {
  id: string;
  label: string;
  description?: string | null;
  sector: Sector;
  risk_score: number;
  countries?: string[] | null;
  time_start?: string | null;
  time_end?: string | null;
  event_count: number;
}

export interface CampaignDetail extends Campaign {
  events: EventSummary[];
  entity_counts: Record<string, number>;
}
