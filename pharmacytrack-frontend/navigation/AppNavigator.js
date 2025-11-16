import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

// Screens
import LoginScreen from "./screens/LoginScreen";
import DashboardScreen from "./screens/DashboardScreen";
import SalesEntryScreen from "./screens/SalesEntryScreen";

const Stack = createNativeStackNavigator();

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ headerShown: false }}
        />
        <Stack.Screen name="Dashboard" component={DashboardScreen} />
        <Stack.Screen name="SalesEntry" component={SalesEntryScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
