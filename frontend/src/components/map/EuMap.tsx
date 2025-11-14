import { MapContainer, TileLayer } from 'react-leaflet';
import type { Campaign } from '../../lib/types';
import CampaignMarkers from './CampaignMarkers';

interface Props {
  campaigns: Campaign[];
  onSelect?: (id: string) => void;
  height?: number;
}

const EuMap = ({ campaigns, onSelect, height = 420 }: Props) => (
  <div className="overflow-hidden rounded-xl border border-white/10 bg-[#0a1224]">
    <MapContainer
      center={[52, 10]}
      zoom={4}
      scrollWheelZoom={false}
      style={{ height }}
      className="z-0"
    >
      <TileLayer
        attribution='&copy; <a href="https://carto.com/">Carto</a>'
        url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png"
      />
      <CampaignMarkers campaigns={campaigns} onSelect={onSelect} />
    </MapContainer>
  </div>
);

export default EuMap;
