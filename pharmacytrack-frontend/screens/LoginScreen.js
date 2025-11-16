import React, { useState } from "react";
import { View, TextInput, Button, Text } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { login } from "../api/apiClient";
import { useRouter } from "expo-router";

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    // call API
    const response = await fetch("http://127.0.0.1:8000/api/v1/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
      navigation.replace("Dashboard");   
    } else {
      alert("Login failed");
    }
  };

  return (
    <View>
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
}

