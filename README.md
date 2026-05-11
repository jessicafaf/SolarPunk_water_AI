# Solarpunk Water AI: Autonomous Resource Management

### 🌿 The Vision
This project is an AI-driven simulation of a Solarpunk ecosystem. It optimizes graywater recycling and household resource management by predicting solar radiation. It bridges the gap between environmental sustainability and advanced machine learning, demonstrating how "smart homes" can operate autonomously under variable weather conditions.

### 🧠 Technical Core
Originally built using a Random Forest architecture, the system is being upgraded to a **Deep Learning RNN (LSTM)** to better handle the temporal dependencies of weather patterns.

* **Predictive Modeling:** Uses historical weather data (Shortwave Radiation, Temperature, Cloud Cover) to forecast energy availability.
* **Automation Logic:** A 48-hour simulation loop that adjusts water recycling priority based on predicted solar gains.
* **Containerization:** Fully Dockerized to ensure environment parity and ease of remote deployment.

### 🛠️ Tech Stack
* **Language:** Python 3.x
* **AI Frameworks:** TensorFlow/Keras (RNN/LSTM), Scikit-Learn (Initial RF Model)
* **Data Handling:** Pandas, NumPy, MinMaxScaler
* **Visualization:** Matplotlib, Seaborn
* **DevOps:** Docker, Git

### 📂 Project Structure
- `water_recycler.py`: Core logic for the autonomous recycling system.
- `solar_predict.py`: The "Brain" - contains the Machine Learning model training and inference.
- `visualize_results.py`: Generates performance dashboards and solar forecast plots.
- `Dockerfile`: Configuration for containerized execution.
- `requirements.txt`: Python dependencies.

### 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/jessicafaf/SolarPunk_water_AI.git](https://github.com/jessicafaf/SolarPunk_water_AI.git)