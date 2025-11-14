import { CircleMarker, Popup } from 'react-leaflet';
import type { Campaign } from '../../lib/types';

const coords: Record<string, [number, number]> = {
  PL: [52.237, 21.017],
  DE: [52.52, 13.405],
  RO: [44.426, 26.102],
  LT: [54.687, 25.279],
  EE: [59.437, 24.753],
  LV: [56.949, 24.105],
  FR: [48.8566, 2.3522],
  IT: [41.9028, 12.4964],
  ES: [40.4168, -3.7038],
};

interface Props {
  campaigns: Campaign[];
  onSelect?: (id: string) => void;
}

const CampaignMarkers = ({ campaigns, onSelect }: Props) => {
  const computeCenter = (countries?: string[] | null): [number, number] => {
    const points = (countries ?? [])
      .map((country) => coords[country])
      .filter((value): value is [number, number] => Boolean(value));
    if (!points.length) {
      return [52, 10];
    }
    const [lat, lon] = points.reduce(
      (acc, current) => [acc[0] + current[0], acc[1] + current[1]],
      [0, 0]
    );
    return [lat / points.length, lon / points.length];
  };

  return (
    <>
      {campaigns.map((campaign) => {
        const center = computeCenter(campaign.countries);
        const radius = Math.max(8, Math.min(20, campaign.risk_score / 5));
        const color = campaign.risk_score > 70 ? '#f472b6' : campaign.risk_score > 40 ? '#3cf6ff' : '#14b8a6';
        return (
          <CircleMarker
            key={campaign.id}
            center={center}
            pathOptions={{ color, fillColor: color, fillOpacity: 0.5 }}
            radius={radius}
            eventHandlers={{
              click: () => onSelect?.(campaign.id),
            }}
          >
            <Popup>
              <div className="text-sm">
                <div className="font-semibold">{campaign.label}</div>
                <div>Risk score: {campaign.risk_score}</div>
                <div>Sector: {campaign.sector}</div>
              </div>
            </Popup>
          </CircleMarker>
        );
      })}
    </>
  );
};

export default CampaignMarkers;
