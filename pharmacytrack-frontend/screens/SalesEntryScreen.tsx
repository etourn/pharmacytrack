import React, { useEffect, useState } from "react";
import { View, Text, TextInput, Button, Alert, StyleSheet } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { Picker } from "@react-native-picker/picker";

const API_URL = "http://127.0.0.1:8000";

export default function SalesEntryScreen() {
  const [token, setToken] = useState<string | null>(null);

  const [medicines, setMedicines] = useState<any[]>([]);
  const [selectedMedicine, setSelectedMedicine] = useState<number | null>(null);

  const [batches, setBatches] = useState<any[]>([]);
  const [selectedBatch, setSelectedBatch] = useState<number | null>(null);

  const [quantity, setQuantity] = useState("");

  // Load token
  useEffect(() => {
    AsyncStorage.getItem("token").then(setToken);
  }, []);

  // Load medicine list
  useEffect(() => {
    if (!token) return;

    fetch(`${API_URL}/api/v1/medicines`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then(setMedicines)
      .catch(() => Alert.alert("Error", "Cannot load medicines."));
  }, [token]);

  // Load batches when a medicine is selected
  useEffect(() => {
    if (!selectedMedicine || !token) return;

    fetch(`${API_URL}/batches/by_medicine/${selectedMedicine}`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then(setBatches)
      .catch(() => Alert.alert("Error", "Cannot load batches."));
  }, [selectedMedicine]);

  const submitSale = async () => {
    if (!selectedBatch || !quantity) {
      Alert.alert("Missing info", "Please select batch and enter quantity.");
      return;
    }

    const response = await fetch(`${API_URL}/sales/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        batch_id: selectedBatch,
        quantity: Number(quantity),
      }),
    });

    if (response.ok) {
      Alert.alert("Success", "Sale recorded!");
      setQuantity("");
    } else {
      const error = await response.json();
      Alert.alert("Error", error.detail || "Failed to create sale.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Create Sale</Text>

      {/* Medicine Picker */}
      <Text style={styles.label}>Medicine</Text>
      <Picker
        selectedValue={selectedMedicine}
        onValueChange={(value) => setSelectedMedicine(value)}
      >
        <Picker.Item label="Select medicine…" value={null} />
        {medicines.map((m) => (
          <Picker.Item key={m.id} label={m.name} value={m.id} />
        ))}
      </Picker>

      {/* Batch Picker */}
      <Text style={styles.label}>Batch</Text>
      <Picker
        selectedValue={selectedBatch}
        onValueChange={(value) => setSelectedBatch(value)}
      >
        <Picker.Item label="Select batch…" value={null} />
        {batches.map((b) => (
          <Picker.Item
            key={b.id}
            label={`Batch ${b.batch_number} — ${b.quantity_available} left`}
            value={b.id}
          />
        ))}
      </Picker>

      {/* Quantity */}
      <Text style={styles.label}>Quantity</Text>
      <TextInput
        style={styles.input}
        keyboardType="numeric"
        value={quantity}
        onChangeText={setQuantity}
        placeholder="Enter quantity"
      />

      <Button title="Submit Sale" onPress={submitSale} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#fff",
  },
  title: {
    fontSize: 22,
    fontWeight: "600",
    marginBottom: 20,
  },
  label: {
    marginTop: 10,
    marginBottom: 5,
    fontWeight: "500",
  },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    padding: 10,
    borderRadius: 6,
    marginBottom: 20,
  },
});
