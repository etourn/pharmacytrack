import api from "./apiClient";
import * as SecureStore from "expo-secure-store";

export async function login(email, password) {
  try {
    const response = await api.post("/login", { email, password });
    const { access_token } = response.data;

    await SecureStore.setItemAsync("token", access_token);

    api.defaults.headers.common["Authorization"] = `Bearer ${access_token}`;
    return true;
  } catch (error) {
    console.error("Login failed:", error.response?.data || error.message);
    return false;
  }
}

export async function getToken() {
  return await SecureStore.getItemAsync("token");
}
