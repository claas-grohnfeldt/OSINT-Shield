import { Link } from 'react-router-dom';
import type { EventItem } from '../../lib/types';

interface Props {
  event: EventItem;
}

const EventCard = ({ event }: Props) => (
  <div className="rounded-xl border border-white/10 bg-white/5 p-4 text-sm" id="events">
    <div className="flex flex-wrap items-center justify-between gap-2 text-xs text-white/60">
      <span>{new Date(event.timestamp).toLocaleString()}</span>
      <span className="rounded bg-white/10 px-2 py-1">{event.sector}</span>
      <span className="rounded bg-white/10 px-2 py-1">{event.country}</span>
    </div>
    <p className="mt-2 text-white/80 overflow-hidden text-ellipsis">{event.text}</p>
    <div className="mt-3 flex items-center justify-between text-xs text-white/60">
      <span>Source: {event.source.name}</span>
      <Link to={`/events/${event.id}`} className="text-neon-cyan hover:underline">
        Inspect
      </Link>
    </div>
  </div>
);

export default EventCard;
