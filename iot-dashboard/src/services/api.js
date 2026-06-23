import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL
});

export const getStats = () => API.get("/stats");
export const getHistory = () => API.get("/sensor-history");