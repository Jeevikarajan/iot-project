import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend,
} from "recharts";

const SensorChart = ({ data }) => {
  const formatted = data.map((item, index) => ({
    name: index + 1,
    temperature: item.temperature,
    humidity: item.humidity,
  }));

  return (
    <div className="chart">
      <h3>📈 Sensor Data Over Time</h3>

      <LineChart width={700} height={300} data={formatted}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />

        <Line type="monotone" dataKey="temperature" stroke="#ff7300" />
        <Line type="monotone" dataKey="humidity" stroke="#387908" />
      </LineChart>
    </div>
  );
};

export default SensorChart;