import type { Campaign, CampaignDetail, EventItem } from './types';

const API_BASE = (import.meta.env.VITE_API_BASE as string) ?? 'http://localhost:8000';

const createUrl = (path: string, params?: Record<string, string | number | undefined>) => {
  const url = new URL(path, API_BASE);
  if (params) {
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined && value !== null) {
        url.searchParams.set(key, String(value));
      }
    });
  }
  return url;
};

async function request<T>(path: string, params?: Record<string, string | number | undefined>): Promise<T> {
  const res = await fetch(createUrl(path, params), {
    headers: {
      'Content-Type': 'application/json',
    },
  });
  if (!res.ok) {
    const message = await res.text();
    throw new Error(`API ${res.status}: ${message}`);
  }
  return (await res.json()) as T;
}

export const getCampaigns = (params?: Record<string, string | number | undefined>) =>
  request<Campaign[]>('/campaigns', params);

export const getCampaign = (id: string) => request<CampaignDetail>(`/campaigns/${id}`);

export const getEvents = (params?: Record<string, string | number | undefined>) =>
  request<EventItem[]>('/events', params);

export const getEvent = (id: string) => request<EventItem>(`/events/${id}`);
