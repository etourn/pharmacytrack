import React, { useEffect, useState } from "react";
import { View, Text, StyleSheet, TouchableOpacity, ScrollView } from "react-native";
import axios from "axios";

export default function DashboardScreen({ navigation }) {
  const [summary, setSummary] = useState(null);
  const [lowStock, setLowStock] = useState([]);

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const token = ""; // TODO: read from storage
      const res = await axios.get("http://127.0.0.1:8000/dashboard/summary", {
        headers: { Authorization: `Bearer ${token}` }
      });
      setSummary(res.data);

      const low = await axios.get("http://127.0.0.1:8000/batches/low_stock");
      setLowStock(low.data);

    } catch (err) {
      console.log("Dashboard error:", err);
    }
  };

  if (!summary) return <Text>Loading...</Text>;

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.heading}>Dashboard</Text>

      <View style={styles.card}>
        <Text>Total Medicines: {summary.total_medicines}</Text>
        <Text>Low Stock Items: {summary.low_stock_count}</Text>
        <Text>Expiring Soon: {summary.expiring_soon_count}</Text>
      </View>

      <Text style={styles.subheading}>Low Stock Alerts</Text>
      {lowStock.map((b) => (
        <View key={b.id} style={styles.card}>
          <Text>Batch: {b.batch_number}</Text>
          <Text>Qty: {b.quantity_available}</Text>
        </View>
      ))}

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("SalesEntry")}
      >
        <Text style={styles.buttonText}>Go to Sales Entry</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20 },
  heading: { fontSize: 24, fontWeight: "bold" },
  subheading: { fontSize: 18, marginTop: 20 },
  card: {
    padding: 12,
    marginVertical: 8,
    borderWidth: 1,
    borderRadius: 8
  },
  button: {
    backgroundColor: "#4CAF50",
    padding: 14,
    borderRadius: 8,
    marginTop: 24,
  },
  buttonText: { color: "white", textAlign: "center" }
});
