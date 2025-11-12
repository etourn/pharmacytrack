// api/apiClient.js
import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://132.161.155.87:8000", // update if using real backend URL
  timeout: 5000,
});

export default apiClient;

export async function login(email, password) {
  const res = await api.post("/login", {
    username: email,
    password,
  });
  return res.data;
}

