import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getCampaign } from '../lib/api';
import type { CampaignDetail as CampaignDetailType } from '../lib/types';
import EuMap from '../components/map/EuMap';

const CampaignDetail = () => {
  const { id } = useParams();
  const [campaign, setCampaign] = useState<CampaignDetailType | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) return;
    let cancelled = false;
    const fetchData = async () => {
      try {
        const data = await getCampaign(id);
        if (!cancelled) {
          setCampaign(data);
          setError(null);
        }
      } catch (err) {
        if (!cancelled) {
          setError((err as Error).message);
        }
      }
    };
    fetchData();
    return () => {
      cancelled = true;
    };
  }, [id]);

  if (!id) return <div>Missing campaign id.</div>;
  if (error) return <div className="text-red-300">{error}</div>;
  if (!campaign) return <div className="text-white/70">Loading campaign…</div>;

  return (
    <div className="space-y-4">
      <div className="rounded-xl border border-white/10 bg-white/5 p-5">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <h2 className="text-2xl font-semibold">{campaign.label}</h2>
            <p className="text-white/70">{campaign.description}</p>
          </div>
          <div className="text-right">
            <div className="text-sm uppercase text-white/60">Risk</div>
            <div className="text-3xl font-bold text-neon-magenta">{campaign.risk_score}</div>
          </div>
        </div>
        <div className="mt-4 flex flex-wrap gap-3 text-xs text-white/60">
          <span className="rounded bg-white/10 px-2 py-1">Sector: {campaign.sector}</span>
          <span className="rounded bg-white/10 px-2 py-1">
            Countries: {(campaign.countries ?? ['EU']).join(', ')}
          </span>
          <span className="rounded bg-white/10 px-2 py-1">Events: {campaign.event_count}</span>
          <span className="rounded bg-white/10 px-2 py-1">
            Window: {campaign.time_start?.slice(0, 10)} → {campaign.time_end?.slice(0, 10)}
          </span>
        </div>
      </div>
      <EuMap campaigns={[campaign]} height={360} />
      <section className="grid gap-4 lg:grid-cols-3">
        <div className="rounded-xl border border-white/10 bg-white/5 p-4 lg:col-span-2">
          <h3 className="text-lg font-semibold mb-3">Timeline</h3>
          <ol className="space-y-3">
            {campaign.events.map((event) => (
              <li key={event.id} className="rounded border border-white/10 bg-[#0b172c] p-3 text-sm">
                <div className="flex items-center justify-between text-xs text-white/60">
                  <span>{new Date(event.timestamp).toLocaleString()}</span>
                  <span className="rounded bg-white/10 px-2 py-1">{event.sector}</span>
                </div>
                <div className="mt-2 flex items-center justify-between">
                  <span className="font-medium">Country: {event.country}</span>
                  <Link to={`/events/${event.id}`} className="text-neon-cyan text-xs hover:underline">
                    View event
                  </Link>
                </div>
                <div className="text-xs text-white/60">Relevance: {(event.relevance_score * 100).toFixed(0)}%</div>
              </li>
            ))}
          </ol>
        </div>
        <div className="rounded-xl border border-white/10 bg-white/5 p-4">
          <h3 className="text-lg font-semibold mb-3">Top entities</h3>
          <ul className="space-y-2 text-sm">
            {Object.entries(campaign.entity_counts).map(([entityType, count]) => (
              <li key={entityType} className="flex items-center justify-between">
                <span className="capitalize">{entityType.replace('_', ' ')}</span>
                <span className="text-neon-cyan">{count}</span>
              </li>
            ))}
            {!Object.keys(campaign.entity_counts).length && (
              <li className="text-white/60">No entities captured.</li>
            )}
          </ul>
        </div>
      </section>
    </div>
  );
};

export default CampaignDetail;
