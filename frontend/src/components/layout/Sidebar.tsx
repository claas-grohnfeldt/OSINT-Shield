import { NavLink } from 'react-router-dom';

const navItems = [
  { label: 'Dashboard', to: '/' },
  { label: 'Campaigns', to: '/#campaigns' },
  { label: 'Events', to: '/#events' },
  { label: 'Docs', to: 'https://github.com/example/osint-shield/tree/main/docs', external: true },
];

const Sidebar = () => (
  <aside className="w-64 bg-[#081125] p-6 hidden md:flex flex-col gap-4 border-r border-white/10">
    <div>
      <div className="text-sm uppercase tracking-[0.35em] text-neon-cyan">OSINT</div>
      <div className="text-2xl font-semibold">Shield</div>
    </div>
    <nav className="flex-1 space-y-3 text-sm">
      {navItems.map((item) =>
        item.external ? (
          <a
            key={item.label}
            href={item.to}
            target="_blank"
            rel="noreferrer"
            className="block rounded bg-white/5 px-3 py-2 hover:bg-white/10"
          >
            {item.label}
          </a>
        ) : (
          <NavLink
            key={item.label}
            to={item.to}
            className={({ isActive }) =>
              `block rounded px-3 py-2 ${isActive ? 'bg-neon-teal/20 text-neon-cyan' : 'hover:bg-white/10'}`
            }
          >
            {item.label}
          </NavLink>
        )
      )}
    </nav>
    <div className="text-xs text-white/60">European Situational Awareness Prototype</div>
  </aside>
);

export default Sidebar;
