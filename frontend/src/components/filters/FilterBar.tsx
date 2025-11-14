interface FilterBarProps {
  sector?: string;
  country?: string;
  minRisk: number;
  onChange: (next: { sector?: string; country?: string; minRisk: number }) => void;
}

const sectors = ['energy', 'logistics', 'defence', 'telecom', 'space', 'other'];
const countries = ['PL', 'DE', 'RO', 'LT', 'EE'];

const FilterBar = ({ sector, country, minRisk, onChange }: FilterBarProps) => (
  <div className="flex flex-col gap-3 rounded-lg border border-white/10 bg-white/5 p-4 text-sm">
    <div className="flex flex-wrap gap-4">
      <label className="flex flex-col gap-1">
        <span className="text-white/60">Sector</span>
        <select
          value={sector ?? ''}
          onChange={(e) => onChange({ sector: e.target.value || undefined, country, minRisk })}
          className="rounded bg-[#0b162b] px-3 py-2"
        >
          <option value="">All</option>
          {sectors.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>
      <label className="flex flex-col gap-1">
        <span className="text-white/60">Country</span>
        <select
          value={country ?? ''}
          onChange={(e) => onChange({ sector, country: e.target.value || undefined, minRisk })}
          className="rounded bg-[#0b162b] px-3 py-2"
        >
          <option value="">All</option>
          {countries.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>
    </div>
    <label className="flex flex-col gap-1">
      <span className="text-white/60">Minimum risk: {minRisk}</span>
      <input
        type="range"
        min={0}
        max={100}
        step={5}
        value={minRisk}
        onChange={(e) => onChange({ sector, country, minRisk: Number(e.target.value) })}
      />
    </label>
  </div>
);

export default FilterBar;
