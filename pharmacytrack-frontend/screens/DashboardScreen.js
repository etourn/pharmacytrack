// screens/DashboardScreen.js
import React, { useEffect, useState } from "react";
import { View, Text, FlatList } from "react-native";
import apiClient from "../api/apiClient";

export default function DashboardScreen() {
  const [medicines, setMedicines] = useState([]);

  useEffect(() => {
    async function fetchMedicines() {
      try {
        const res = await apiClient.get("/medicines");
        setMedicines(res.data);
      } catch (err) {
        console.error("Error fetching medicines:", err);
      }
    }
    fetchMedicines();
  }, []);

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 24, fontWeight: "bold", marginBottom: 10 }}>
        Medicines List
      </Text>
      <FlatList
        data={medicines}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <Text style={{ paddingVertical: 6 }}>
            {item.name} — {item.brand}
          </Text>
        )}
      />
    </View>
  );
}
