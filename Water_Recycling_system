# ============================================
# SOLAR-POWERED WATER RECYCLING SYSTEM (v1.1)
# Author: Jessica Ferreira
# Description: Fixed integration between Prediction and Recycling
# ============================================

import requests
import pandas as pd
import csv
import time
import random
import joblib  # Added to save the model for Project #2
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split # For validation
from sklearn.metrics import r2_score # For the accuracy score

# ---------- SECTION 2: SYSTEM CONFIGURATION ----------
import os
from dotenv import load_dotenv

# This command "wakes up" the connection to your .env tab
load_dotenv() 

# --- LINKING TO .ENV ---
# We use os.getenv("KEY", default_value)
# float() and int() are used because .env values are always read as text
LATITUDE = float(os.getenv("LATITUDE", 47.3769))
LONGITUDE = float(os.getenv("LONGITUDE", 8.5417))
API_URL = os.getenv("API_URL", "https://api.open-meteo.com/v1/forecast")

WATER_TANK_CAPACITY = int(os.getenv("WATER_TANK_CAPACITY", 5000))
BATTERY_CAPACITY = int(os.getenv("BATTERY_CAPACITY", 10000))

# These can remain hardcoded as internal system logic
MIN_WATER_LEVEL = 500
PUMP_POWER_WATTS = 1500
BATTERY_LEVEL = 3000 

MODES = {
    "FULL": {"power_needed": 1500, "water_processed": 200},
    "ECO": {"power_needed": 500, "water_processed": 60},
    "MAINTENANCE": {"power_needed": 100, "water_processed": 10},
    "OFF": {"power_needed": 0, "water_processed": 0}
}

# ---------- SECTION 3: SOLAR PREDICTION MODEL ----------
def train_solar_model(historical_data):
   
    X = historical_data[['hour', 'day_of_year', 'temperature_2m', 'cloud_cover']]
    y = historical_data['shortwave_radiation']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = r2_score (y_test, predictions)
    print(f"AI Model Accuracy (R2 Score): {accuracy:.4f}")

    joblib.dump(model, 'solar_model.pkl')
    print("💾 JesFer Brain Saved: 'solar_model.pkl' is ready for the Water Module.")
    return model

# ---------- SECTION 4: WATER RECYCLING SYSTEM ----------
class WaterRecyclingSystem:
    def __init__(self, tank_capacity, min_level):
        self.tank_capacity = tank_capacity
        self.current_water = tank_capacity * 0.6  # Start at 60%
        self.min_level = min_level
        self.total_water_recycled = 0
        self.operation_log = []

    def recycle_water(self, solar_power_available, hours_of_sunlight):
        global BATTERY_LEVEL
        total_energy = BATTERY_LEVEL + (solar_power_available * hours_of_sunlight)
        
        # Decision Logic
        if self.current_water < self.min_level:
            operation = MODES["MAINTENANCE"] # Emergency
        elif solar_power_available > 500:
            operation = MODES["FULL"]
        elif solar_power_available > 200:
            operation = MODES["ECO"]
        else:
            return 0, 0

        energy_needed = operation["power_needed"] * hours_of_sunlight
        
        if energy_needed <= total_energy:
            water_processed = operation["water_processed"]
            # Apply safety max(0, ...) and min(capacity, ...)
            self.current_water = min(self.tank_capacity, self.current_water + water_processed)
            self.total_water_recycled += water_processed
            BATTERY_LEVEL -= min(BATTERY_LEVEL, energy_needed)
            return water_processed, energy_needed
        return 0, 0

    def use_water(self, liters):
        # Prevent negative water
        self.current_water = max(0, self.current_water - liters)

# ---------- SECTION 5: MAIN SIMULATION ----------
def run_solar_water_system():
    global BATTERY_LEVEL
    # Create the system instance
    ws = WaterRecyclingSystem(WATER_TANK_CAPACITY, MIN_WATER_LEVEL)
    
    # 1. Training Phase
    print("\n🧠 Training Solar AI...")
    # (Assuming training data fetch happens here as per your original code)
    # For this fix, we assume historical_df is ready:
    # solar_model = train_solar_model(historical_df)
    with open('system_history.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Solar_W', 'Water_L', 'Battery_Wh', 'Status'])
    print ("\n"+ "="*60)
    print("SIMULATION STARTING - 48 HOUR CYCLE")
    print("="*60)

    start_time=datetime.now()

    # 2. Simulation Loop
    for hour_offset in range(48):
        print(hour_offset)
        current_time= start_time+timedelta(hours=hour_offset)
        current_hour = current_time.hour
        solar_input = random.uniform (400,600)
        if 6 <= current_hour<=18:
            predicted_solar = random.uniform(200,800)
        else:
            predicted_solar = 0
            # Logic for solar prediction, consumption, and recycling
        water_used = random.uniform(10,40)
        if (7<= current_hour<=9) or (19<= current_hour<=21):
            water_used = random.uniform (20,50)
        else:
            water_used = random.uniform(2,8)

        ws.use_water(water_used) # Example usage
        water_recycled, energy_usef=ws.recycle_water(predicted_solar,1)

        with open('system_history.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    current_time.strftime('%Y-%m-%d %H:%M'),
                    f"{predicted_solar:.2f}",
                    f"{ws.current_water:.2f}",
                    f"{BATTERY_LEVEL:.2f}",
                    "Active" if water_recycled > 0 else "Consuming"
                ])
            
    print(f"✅ Simulation Complete. Total Recycled: {ws.total_water_recycled}L")
    return ws # Return the system so Interactive mode can use it

# ---------- SECTION 6: UPDATED INTERACTIVE MODE ----------
def interactive_control(ws): # ws is the active WaterRecyclingSystem
    global BATTERY_LEVEL
    print("\n🎮 INTERACTIVE MODE LINKED TO LIVE SYSTEM")
    
    while True:
        user_input = input("\n(status, use [L], recycle, exit) > ").lower().split()
        if not user_input: continue
        cmd = user_input[0]
        
        if cmd == 'status':
            print(f"💧 Water: {ws.current_water:.0f}L | 🔋 Battery: {BATTERY_LEVEL:.0f}Wh")
        elif cmd == 'use':
            amt = float(user_input[1]) if len(user_input) > 1 else 10
            ws.use_water(amt)
            print(f"🚰 Used {amt}L")
        elif cmd == 'recycle':
            # Manual trigger uses existing class logic
            w, e = ws.recycle_water(800, 1)
            print(f"♻️ Processed {w}L using {e}Wh")
        elif cmd == 'exit':
            break

# ---------- SECTION 7: MAIN MENU ----------
if __name__ == "__main__":
    # Create one master system to share between Simulation and Interactive modes
    master_system = WaterRecyclingSystem(WATER_TANK_CAPACITY, MIN_WATER_LEVEL)
    
    while True:
        print("\n🌍 JESFER INTEGRATED SYSTEM")
        print("1. Run Simulation\n2. Interactive Control\n3. Exit")
        choice = input("Select: ")
        
        if choice == '1':
            run_solar_water_system()
        elif choice == '2':
            interactive_control(master_system)
        elif choice == '3':
            break