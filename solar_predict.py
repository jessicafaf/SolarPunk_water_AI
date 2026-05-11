# IMPORT LIBRARIES 
import requests
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# 1. GETTING THE DATA
lat = 47.3769
lon = 8.5417

print("📡 JesFer is syncing with solar archives...")
# We keep the base URL simple and let 'params' do the heavy lifting
url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": lat,
    "longitude": lon,
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "hourly": "temperature_2m,cloud_cover,shortwave_radiation",
    "timezone": "auto"
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    print("✅ Connection Successful! JesFer is processing...") 
except Exception as e:
    print(f"❌ Connection Failed. Error: {e}")
    exit()

# 2. Cleaning and preparing the DataFrame
df = pd.DataFrame(data['hourly'])
df = df.dropna()

# --- NEW: SAVE HISTORICAL DATA ---
# This creates the 'data' folder if it doesn't exist and saves the CSV
if not os.path.exists('data'):
    os.makedirs('data')
df.to_csv('data/historical.csv', index=False)
print("💾 Historical data saved to data/historical.csv")

# 3. Training the 'Solar Brain'
X = df[['temperature_2m', 'cloud_cover']]
y = df['shortwave_radiation']

model = RandomForestRegressor(n_estimators=50)
model.fit(X, y)

# --- NEW: SAVE THE MODEL ---
joblib.dump(model, 'solar_model.pkl')
print("🧠 JesFer is ready: Solar patterns analyzed and model saved.")

# 4. Prediction Test
test_temp = 28
test_clouds = 0 

prediction = model.predict([[test_temp, test_clouds]])
intensity = prediction[0]

print(f"\n--- JESFER LIVE TEST ---")
print(f"If it is {test_temp}°C with {test_clouds}% clouds...")
print(f"JESFER predicts: {intensity:.2f} W/m² of solar energy.")

if intensity > 400:
    print("Action: High Yield! Powering up recycling systems and charging batteries.")
else: 
    print("Action: Low Yield, conserving water and starting EcoMode.")
print("------------------------")