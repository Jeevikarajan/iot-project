const StatsCards = ({ stats }) => {
  return (
    <div className="card-container">
      <div className="card">
        <h3> Avg Temperature</h3>
        <p>{stats.average_temperature?.toFixed(2)} °C</p>
      </div>

      <div className="card">
        <h3>Avg Humidity</h3>
        <p>{stats.average_humidity?.toFixed(2)} %</p>
      </div>

      <div className="card">
        <h3>Total Records</h3>
        <p>{stats.total_records}</p>
      </div>
    </div>
  );
};

export default StatsCards;