import type { EventItem } from '../../lib/types';
import EventCard from './EventCard';

interface Props {
  events: EventItem[];
}

const EventList = ({ events }: Props) => (
  <div className="space-y-3">
    {events.map((event) => (
      <EventCard key={event.id} event={event} />
    ))}
    {!events.length && (
      <div className="rounded border border-dashed border-white/20 p-6 text-center text-white/60">
        No events available.
      </div>
    )}
  </div>
);

export default EventList;
