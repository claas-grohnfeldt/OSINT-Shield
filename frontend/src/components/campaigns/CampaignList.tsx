import type { Campaign } from '../../lib/types';
import CampaignCard from './CampaignCard';

interface Props {
  campaigns: Campaign[];
}

const CampaignList = ({ campaigns }: Props) => (
  <div className="space-y-3" id="campaigns">
    {campaigns.map((campaign) => (
      <CampaignCard key={campaign.id} campaign={campaign} />
    ))}
    {!campaigns.length && (
      <div className="rounded border border-dashed border-white/20 p-6 text-center text-white/60">
        No campaigns match the current filters.
      </div>
    )}
  </div>
);

export default CampaignList;
