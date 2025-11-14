import { Routes, Route } from 'react-router-dom';
import Dashboard from './routes/Dashboard';
import CampaignDetail from './routes/CampaignDetail';
import EventDetail from './routes/EventDetail';
import Sidebar from './components/layout/Sidebar';
import Topbar from './components/layout/Topbar';

function App() {
  return (
    <div className="flex h-screen bg-night text-white">
      <Sidebar />
      <div className="flex flex-1 flex-col overflow-hidden">
        <Topbar />
        <main className="flex-1 overflow-y-auto bg-slate p-4 sm:p-6">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/campaigns/:id" element={<CampaignDetail />} />
            <Route path="/events/:id" element={<EventDetail />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
