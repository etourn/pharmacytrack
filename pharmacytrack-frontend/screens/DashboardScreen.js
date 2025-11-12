import React, { useEffect, useState } from "react";
import { View, Text, FlatList } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import api from "api/apiClient";

export default function DashboardScreen() {
  const [medicines, setMedicines] = useState([]);

  useEffect(() => {
    const fetchMedicines = async () => {
      const token = await AsyncStorage.getItem("token");
      const res = await api.get("/medicines", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setMedicines(res.data);
    };
    fetchMedicines();
  }, []);

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 18, fontWeight: "bold" }}>Medicines</Text>
      <FlatList
        data={medicines}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <Text>{item.name} ({item.brand})</Text>
        )}
      />
    </View>
  );
}
