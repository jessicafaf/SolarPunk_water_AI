import joblib

# 1. LOAD THE 'BRAIN'
# JesFer needs to remember what he learned in the first script
try:
    model = joblib.load('solar_model.pkl')
    print("💧 JesFer's Water Module: Solar Model Loaded.")
except:
    print("❌ Error: No solar model found. Run solar_predictor.py first!")
    exit()

# 2. THE RECYCLING LOGIC
def run_recycling_check(temp, clouds):
    # Ask the brain for the solar intensity
    solar_prediction = model.predict([[temp, clouds]])[0]
    
    print(f"\n--- 🛰️ JesFer Water Analysis ---")
    print(f"Solar Forecast: {solar_prediction:.2f} W/m²")
    
    # SYSTEM DECISIONS
    if solar_prediction > 500:
        status = "FULL POWER"
        action = "Activating UV Filtration and Greywater Pumps. Energy is abundant!"
    elif solar_prediction > 200:
        status = "ECONOMY MODE"
        action = "Running basic filtration. Conserving energy for nighttime."
    else:
        status = "STANDBY"
        action = "Pumps off. Waiting for sun. Minimal filtration active."
    
    return status, action

# 3. TEST THE SYSTEM
# Let's simulate a real-world check
current_temp = 24
current_clouds = 15

mode, suggestion = run_recycling_check(current_temp, current_clouds)

print(f"System Mode: {mode}")
print(f"JesFer Action: {suggestion}")
print("--------------------------------")