import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000", // change when deployed
});

export const getStats = () => API.get("/stats");
export const getHistory = () => API.get("/sensor-history");