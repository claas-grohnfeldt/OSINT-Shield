import { useEffect, useMemo, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getEvent } from '../lib/api';
import type { EventItem } from '../lib/types';

const EventDetail = () => {
  const { id } = useParams();
  const [event, setEvent] = useState<EventItem | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) return;
    let cancelled = false;
    getEvent(id)
      .then((data) => {
        if (!cancelled) {
          setEvent(data);
          setError(null);
        }
      })
      .catch((err) => !cancelled && setError((err as Error).message));
    return () => {
      cancelled = true;
    };
  }, [id]);

  const escapeRegex = (value: string) => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

  const highlightText = useMemo(() => {
    if (!event?.entities?.length || !event.text) return event?.text ?? '';
    let highlighted = event.text;
    event.entities.forEach((entity) => {
      const regex = new RegExp(`(${escapeRegex(entity.value)})`, 'gi');
      highlighted = highlighted.replace(regex, '<mark class="bg-neon-cyan/40 text-white">$1</mark>');
    });
    return highlighted;
  }, [event]);

  if (!id) return <div>Missing event id.</div>;
  if (error) return <div className="text-red-300">{error}</div>;
  if (!event) return <div className="text-white/70">Loading event…</div>;

  return (
    <article className="space-y-4">
      <div className="rounded-xl border border-white/10 bg-white/5 p-5">
        <div className="text-xs text-white/60">{new Date(event.timestamp).toLocaleString()}</div>
        <h2 className="text-2xl font-semibold">{event.sector.toUpperCase()} – {event.country}</h2>
        <p className="text-white/70">Source: {event.source.name}</p>
        <div className="mt-3 flex flex-wrap gap-2 text-xs text-white/60">
          <span className="rounded bg-white/10 px-2 py-1">Relevance {(event.relevance_score * 100).toFixed(0)}%</span>
          <span className="rounded bg-white/10 px-2 py-1">Security flag: {event.is_security_relevant ? 'Yes' : 'No'}</span>
        </div>
      </div>
      <div className="rounded-xl border border-white/10 bg-[#0b172c] p-5 text-sm leading-relaxed" dangerouslySetInnerHTML={{ __html: highlightText }} />
      <section className="rounded-xl border border-white/10 bg-white/5 p-5">
        <h3 className="text-lg font-semibold">Entities</h3>
        <div className="mt-3 flex flex-wrap gap-2 text-xs">
          {event.entities?.map((entity) => (
            <span
              key={entity.id}
              className="rounded-full border border-white/10 bg-white/10 px-3 py-1 capitalize"
            >
              {entity.entity_type}: {entity.value}
            </span>
          ))}
          {!event.entities?.length && <span className="text-white/60">No entities extracted.</span>}
        </div>
      </section>
      <section className="rounded-xl border border-white/10 bg-white/5 p-5 text-sm">
        <h3 className="text-lg font-semibold">Linked campaigns</h3>
        <div className="mt-2 flex flex-wrap gap-3">
          {event.campaigns.map((campaign) => (
            <Link
              key={campaign.id}
              to={`/campaigns/${campaign.id}`}
              className="rounded border border-neon-cyan/40 px-3 py-2 text-neon-cyan"
            >
              {campaign.label}
            </Link>
          ))}
          {!event.campaigns.length && <span className="text-white/60">Not clustered yet.</span>}
        </div>
      </section>
    </article>
  );
};

export default EventDetail;
