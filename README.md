# 🚗 DriveSure: Detect, Predict, Prevent

DriveSure is a smart road safety companion. Harnessing real-time machine learning and robust video analysis, DriveSure alerts you to hazards like fog, potholes, and tire wear—before your journey is at risk. Everything comes together in a single, interactive Streamlit dashboard.

---

## 📚 Table of Contents

1. [Key Features](#key-features)
2. [Architecture Overview](#architecture-overview)
3. [Project Structure](#project-structure)
4. [Installation & Setup](#installation--setup)
5. [Usage Guide](#usage-guide)
6. [Tech Stack](#tech-stack)
7. [Team](#team)
8. [Feedback](#feedback)

---

## 🚀 Key Features

- **Real-time Hazard Detection:** Instantly detects fog and potholes from live video.
- **Tire Health Predictor:** Estimates tire degradation and notifies for maintenance.
- **Interactive Dashboard:** All data in one beautiful Streamlit app.
- **WebRTC-Ready:** Integrates your webcam for edge AI predictions.
- **Plug and Play:** Fast setup for instant road safety insights.

---

## 🏗️ Architecture Overview

flowchart TD
A1[dashboard.py]
A2[Models (fog, pothole, tire)]
A3[WebRTC Video Input]
A4[Streamlit UI]
A1 --> A2
A1 --> A3
A1 --> A4

---

## 📂 Project Structure
DriveSure/
│
├── models/ # Pre-trained ML models and scalers
│ ├── fog_detection_model.pkl
│ ├── fog_scaler.pkl
│ ├── pothole_model.h5
│ ├── scaler-2.pkl
│ └── tire_degradation_nn_model.h5
│
├── .DS_Store # System file (macOS)
├── .gitignore # Git ignore rules
├── .python-version # Python environment version
├── README.md # Project documentation
├── car_animation.json # Dashboard UI animation asset
├── dashboard.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── tire_predictions.csv # Reference tire wear data

---

## ⚙️ Installation & Setup

1. **Clone the repo**  
    ```
    git clone https://github.com/LaxmiVarshithaCH/DriveSure.git
    cd DriveSure
    ```
2. **Create a Python virtual environment**  
    ```
    python3 -m venv venv
    source venv/bin/activate       # Linux/macOS
    venv\Scripts\activate         # Windows
    ```
3. **Install dependencies**  
    ```
    pip install -r requirements.txt
    ```
4. **Add models and data files**  
   Place these files in `models/` directory (if not already present):
   - fog_detection_model.pkl
   - fog_scaler.pkl
   - pothole_model.h5
   - scaler-2.pkl
   - tire_degradation_nn_model.h5

   Also, ensure the root directory includes:
   - car_animation.json
   - tire_predictions.csv

---

## 🚦 Usage Guide

Start the dashboard:

streamlit run dashboard.py

- Dashboard launches in your browser.
- View real-time predictions (fog, pothole, tire).
- Toggle webcam integration for live hazard alerts.
- Explore analytics and visualizations interactively.

---

## 🧰 Tech Stack

- **Python 3.6+**
- **Streamlit** (dashboard UI)
- **TensorFlow / scikit-learn** (ML models)
- **OpenCV** (video analysis)
- **streamlit-webrtc** (webcam integration)
- **numpy, pandas** (data handling)

---

## 👥 Team

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LaxmiVarshithaCH">
        <img src="https://avatars.githubusercontent.com/LaxmiVarshithaCH" width="90px;" alt=""/>
        <br /><sub><b>Laxmi Varshitha Chennupalli</b></sub>
      </a>
      <br />
    </td>
    <!-- Add team members as needed -->
  </tr>
</table>

---

## 📬 Feedback

Have ideas, bug reports, or feature requests?  
- Open an issue or pull request.
- Let's make road safety smarter together! 🚦

---

**DriveSure: Smarter roads. Safer journeys. Every mile.**
