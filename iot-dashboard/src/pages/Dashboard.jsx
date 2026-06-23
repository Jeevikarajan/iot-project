import { useEffect, useState } from "react";
import { getStats, getHistory } from "../services/api";
import StatsCards from "../components/StatsCards";
import SensorChart from "../components/SensorChart";
import Navbar from "../components/Navbar";

const Dashboard = () => {
  const [stats, setStats] = useState({});
  const [history, setHistory] = useState([]);

  useEffect(() => {
  fetchData(); // initial load

  const interval = setInterval(() => {
    fetchData(); // repeat every 5 sec
  }, 5000);

  return () => clearInterval(interval); // cleanup
}, []);

  const fetchData = async () => {
    try {
      const statsRes = await getStats();
      setStats(statsRes.data.data);

      const historyRes = await getHistory();
      setHistory(historyRes.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <Navbar />

      <div className="container">
        <StatsCards stats={stats} />
        <SensorChart data={history} />
      </div>
    </div>
  );
};

export default Dashboard;