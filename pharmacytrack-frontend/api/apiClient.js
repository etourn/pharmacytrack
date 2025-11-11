// api/apiClient.js
import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:8000/api/v1", // update if using real backend URL
  timeout: 5000,
});

export default apiClient;
