import { useNavigate } from 'react-router-dom';
import type { Campaign } from '../../lib/types';

interface Props {
  campaign: Campaign;
}

const CampaignCard = ({ campaign }: Props) => {
  const navigate = useNavigate();
  const badgeColor = campaign.risk_score > 70 ? 'bg-neon-magenta/30 text-neon-magenta' : 'bg-neon-cyan/20 text-neon-cyan';

  return (
    <button
      type="button"
      onClick={() => navigate(`/campaigns/${campaign.id}`)}
      className="w-full rounded-xl border border-white/10 bg-white/5 p-4 text-left transition hover:border-neon-cyan/60"
    >
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-semibold">{campaign.label}</h3>
        <span className={`rounded-full px-3 py-1 text-xs ${badgeColor}`}>Risk {campaign.risk_score}</span>
      </div>
      <p className="mt-1 text-sm text-white/70">{campaign.description ?? 'Ongoing hybrid activity cluster'}</p>
      <div className="mt-3 flex flex-wrap gap-3 text-xs text-white/60">
        <span className="rounded bg-white/10 px-2 py-1">Sector: {campaign.sector}</span>
        <span className="rounded bg-white/10 px-2 py-1">
          Countries: {(campaign.countries ?? ['EU']).join(', ')}
        </span>
        <span className="rounded bg-white/10 px-2 py-1">Events: {campaign.event_count}</span>
      </div>
    </button>
  );
};

export default CampaignCard;
