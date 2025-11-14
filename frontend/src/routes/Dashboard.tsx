import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getCampaigns, getEvents } from '../lib/api';
import type { Campaign, EventItem } from '../lib/types';
import EuMap from '../components/map/EuMap';
import CampaignList from '../components/campaigns/CampaignList';
import EventList from '../components/events/EventList';
import FilterBar from '../components/filters/FilterBar';

interface Filters {
  sector?: string;
  country?: string;
  minRisk: number;
}

const Dashboard = () => {
  const [campaigns, setCampaigns] = useState<Campaign[]>([]);
  const [events, setEvents] = useState<EventItem[]>([]);
  const [filters, setFilters] = useState<Filters>({ minRisk: 40 });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    let cancelled = false;
    const fetchData = async () => {
      setLoading(true);
      try {
        const [campaignData, eventData] = await Promise.all([
          getCampaigns({
            sector: filters.sector,
            country: filters.country,
            min_risk: filters.minRisk,
          }),
          getEvents({
            sector: filters.sector,
            country: filters.country,
            limit: 5,
          }),
        ]);
        if (!cancelled) {
          setCampaigns(campaignData);
          setEvents(eventData);
          setError(null);
        }
      } catch (err) {
        if (!cancelled) {
          setError((err as Error).message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    };
    fetchData();
    return () => {
      cancelled = true;
    };
  }, [filters]);

  return (
    <div className="space-y-4">
      <FilterBar sector={filters.sector} country={filters.country} minRisk={filters.minRisk} onChange={setFilters} />
      {error && <div className="rounded border border-red-400/40 bg-red-500/20 p-3 text-sm text-red-200">{error}</div>}
      <div className="grid gap-4 lg:grid-cols-5">
        <div className="lg:col-span-3">
          <EuMap campaigns={campaigns} onSelect={(id) => navigate(`/campaigns/${id}`)} height={430} />
        </div>
        <div className="lg:col-span-2 space-y-3">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">Active Campaigns</h2>
            {loading && <span className="text-xs text-white/60">Loading…</span>}
          </div>
          <CampaignList campaigns={campaigns} />
        </div>
      </div>
      <section>
        <div className="mb-2 flex items-center justify-between">
          <h2 className="text-lg font-semibold">Recent Events</h2>
          <button
            type="button"
            onClick={() => setFilters((current) => ({ ...current, minRisk: 0 }))}
            className="text-xs text-neon-cyan hover:underline"
          >
            Reset filters
          </button>
        </div>
        <EventList events={events} />
      </section>
    </div>
  );
};

export default Dashboard;
