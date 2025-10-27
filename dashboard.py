import streamlit as st
import numpy as np
import random
import joblib
import pickle
from tensorflow.keras.models import load_model
import pandas as pd
from datetime import datetime
import os
import requests
import streamlit_lottie
from streamlit_lottie import st_lottie
import json
import time
import cv2
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
from datetime import datetime
import pandas as pd
import random
import os
from PIL import Image
import queue

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_car_url = "https://lottie.host/f2d6f8c6-0002-474d-9eea-13327b39bb86/cikYKzehBa.json"
lottie_car = load_lottie_file("car_animation.json")


with st.container():
    st.markdown(
        """
        <div style='text-align: center;'>
            <div style='max-width: 100%;'>
        """,
        unsafe_allow_html=True
    )

    st_lottie(lottie_car, speed=1, height=250, width=1200, key="car", quality="high")

    st.markdown(
        """
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


@st.cache_resource
def load_tire_model():
    return load_model('tire_degradation_nn_model.h5', compile=False)
tire_model=load_tire_model()
fog_model = joblib.load('fog_detection_model.pkl')
scaler = joblib.load('scaler-2.pkl')
scalerfog = joblib.load('fog_scaler.pkl')
pothole_model = load_model('pothole_model.h5', compile=False)

motorsport_map = {
    "F1": 0, "WEC": 1, "DTM": 2, "Sedan": 3, "Motor Car": 4, "SUV": 5
}
compound_map = {
    "C1": 0, "C2": 1, "C3": 2, "C4": 3, "C5": 4
}
driving_style_map = {
    "Aggressive": 0,
    "Normal": 1
}


st.set_page_config(layout="wide")
st.title("Vehicle Condition Dashboard")

tab1, tab2, tab3 = st.tabs(["Tire Health", "Fog Detection", "Pothole Detection"])

with tab1:
    st.subheader("Tire Health Prediction")

    col1, col2, col3 = st.columns(3)
    with col1:
        motorsport = st.selectbox("Select Motorsport Type", list(motorsport_map.keys()))
    with col2:
        compound = st.selectbox("Select Tire Compound", list(compound_map.keys()))
    with col3:
        driving_style = st.selectbox("Driving Style", list(driving_style_map.keys()))

    if st.button("Predict Tire Wear"):
        sample_input = {
            'Motorsport_Type': motorsport_map[motorsport],
            'lap_time': round(random.uniform(75.0, 120.0), 2),
            'Throttle': round(random.uniform(0.1, 1.0), 2),
            'Brake': round(random.uniform(0, 1), 2),
            'Steering_Position': round(random.uniform(-1, 1), 2),
            'Speed': round(random.uniform(30.0, 200.0), 2),
            'Surface_Roughness': round(random.uniform(0.01, 0.5), 2),
            'Ambient_Temperature': round(random.uniform(10.0, 40.0), 2),
            'Humidity': round(random.uniform(30.0, 90.0), 2),
            'Wind_Speed': round(random.uniform(0, 20), 2),
            'Lateral_G_Force': round(random.uniform(0.8, 1.5), 2),
            'Longitudinal_G_Force': round(random.uniform(0.6, 1.2), 2),
            'Tire_Compound': compound_map[compound],
            'Tire_Friction_Coefficient': round(random.uniform(0.2, 1.0), 2),
            'Tire_Tread_Depth': round(random.uniform(5.0, 10.0), 2),
            'Tire_wear': round(random.uniform(0.1, 0.9), 2),
            'Cumulative_Tire_Wear': round(random.uniform(0.1, 0.95), 2),
            'Driving_Style': driving_style_map[driving_style],
            'force_on_tire': round(random.uniform(1000, 8000), 2),
            'front_surface_temp': round(random.uniform(70.0, 120.0), 2),
            'rear_surface_temp': round(random.uniform(60.0, 110.0), 2),
            'front_inner_temp': round(random.uniform(65.0, 115.0), 2),
            'rear_inner_temp': round(random.uniform(60.0, 100.0), 2),
        }

        X = np.array([list(sample_input.values())])
        X_scaled = scaler.transform(X)
        prediction = tire_model.predict(X_scaled)[0][0]
        tire_wear = round(prediction, 2)
        record = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Tire Wear %": round(tire_wear, 2),
            "Driving Style": driving_style, 
            "Speed (km/h)": sample_input["Speed"],
            "Ambient Temp": sample_input["Ambient_Temperature"],
            "Tire Pressure": sample_input["Tire_Friction_Coefficient"],  
            "Brake Temp": sample_input["Brake"],
        }


        log_file = "tire_predictions.csv"

        if os.path.exists(log_file):
            pd.DataFrame([record]).to_csv(log_file, mode='a', header=False, index=False)
        else:
            pd.DataFrame([record]).to_csv(log_file, mode='w', header=True, index=False)

        st.markdown(f"### 🧮 Predicted Tire Wear: {tire_wear:.2f}%")

        

        if tire_wear > 85:
            st.error("Tire Change Recommended!")
        elif tire_wear > 55:
            st.warning("Moderate Wear — Plan for Maintenance.")
        else:
            st.success("Tire Condition is Good.")

        st.markdown("### 🔧 Smart Suggestion:")
        if driving_style == "Aggressive":
            st.write("Try reducing aggressive driving to reduce tire wear.")
        if compound in ["C4", "C5"]:
            st.write("Consider switching to harder compound for better durability.")
        if sample_input["Tire_Tread_Depth"] < 6:
            st.write("Tread depth is reducing, check alignment and pressure regularly.")

        with st.expander("View Model Input Features Used"):
            st.json(sample_input)

        st.markdown("## Tire Health Prediction History")
        if os.path.exists(log_file):
            df = pd.read_csv(log_file)
            st.dataframe(df.tail(10))  
        else:
            st.info("No prediction history found yet.")

with tab2:
    st.subheader("Fog Risk Prediction")

    recirculation_point = st.radio("Recirculation Mode", [0, 1], index=1, format_func=lambda x: "On" if x == 1 else "Off")

    

    if st.button("Predict Fog Risk"):
        inside_temp = round(random.uniform(20.0, 35.0), 2)
        outside_temp = round(random.uniform(5.0, 30.0), 2)
        rel_humidity = round(random.uniform(40.0, 100.0), 2)
        dew_point = round(random.uniform(5.0, 25.0), 2)

        fog_features = np.array([[inside_temp, outside_temp, rel_humidity, dew_point, recirculation_point]])
        fog_scaled = scalerfog.transform(fog_features)
        fog_risk = fog_model.predict(fog_scaled)[0]

        st.subheader("Fog Risk Result")
        st.write("**Fog Risk Level**")
        st.code(f"{fog_risk}", language="markdown")

        if fog_risk == 1:
            st.error("Fog Detected!")

            st.markdown("###Fog Detected. Activating defog system:")
            st.markdown("""
            - **AC ON** (cool mode)  
            - **Fan LOW**  
            - **Recirculation OFF** (fresh air)  
            - Monitoring humidity...
            """)
        
            current_rh = 90
            log_output = ""

            log_output += "Fog Detected!\n"
            log_output += "Fog Detected. Activating defog system:\n"
            log_output += " - AC ON (cool mode)\n"
            log_output += " - Fan LOW\n"
            log_output += " - Recirculation OFF (fresh air)\n"
            log_output += " - Monitoring humidity...\n\n"

            for i in range(10):
                time.sleep(0.5)
                log_output += f"⏱ Time: {i}s → RH: {current_rh}%\n"
                current_rh -= 3

            log_output += "\nRH dropped to 60% → Defog system OFF."

            st.code(log_output)


        else:
            st.success("Low Fog Risk. No defogging needed.")

        with st.expander("Sensor Data Used"):
            st.json({
            "Inside Temp (°C)": inside_temp,
            "Outside Temp (°C)": outside_temp,
            "Relative Humidity (%)": rel_humidity,
            "Dew Point (°C)": dew_point,
            "Recirculation Mode": "On" if recirculation_point == 1 else "Off"
        })

with tab3:
    st.subheader("Pothole Detection (Live)")

    option = st.radio("Choose Input Method:", ["Upload Image", "Live Camera"])

    if option == "Upload Image":
        uploaded_file = st.file_uploader("Upload Road Image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            image_resized = image.resize((100, 100))
            img_array = np.array(image_resized).astype("float32") / 255.0
            img_input = img_array.reshape(1, 100, 100, 3)

            st.image(image, caption="📷 Uploaded Image", use_column_width=True)

            preds = pothole_model.predict(img_input, verbose=0)[0]
            predicted_class = np.argmax(preds)
            confidence = preds[predicted_class]

            st.markdown("### Prediction Result")
            if predicted_class == 1:
                st.error(f"Pothole Detected! (Confidence: {confidence:.2f})")
            else:
                st.success(f"Plain Road Detected. (Confidence: {confidence:.2f})")

            with st.expander("Class Probabilities"):
                st.write({
                    "Plain Road": round(preds[0] * 100, 2),
                    "Pothole": round(preds[1] * 100, 2)
                })

    elif option == "Live Camera":

        from datetime import datetime

        class PotholeDetector(VideoProcessorBase):
            def __init__(self):
                self.result_text = ""
                self.pothole_count = 0
                self.detection_log = []  

            def recv(self, frame):
                img = frame.to_ndarray(format="bgr24")
                img_resized = cv2.resize(img, (100, 100))
                img_normalized = img_resized.astype("float32") / 255.0
                img_input = img_normalized.reshape(1, 100, 100, 3)

                preds = pothole_model.predict(img_input, verbose=0)[0]
                predicted_class = np.argmax(preds)
                confidence = preds[predicted_class]

                if predicted_class == 1:
                    self.result_text = f"Pothole Detected! (Confidence: {confidence:.2f})"
                    color = (0, 0, 255)
                    self.pothole_count += 1
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    self.detection_log.append(f"{timestamp} - Pothole detected")
                else:
                    self.result_text = f"Plain Road Detected. (Confidence: {confidence:.2f})"
                    color = (0, 255, 0)

                cv2.putText(img, self.result_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                return av.VideoFrame.from_ndarray(img, format="bgr24")

        webrtc_ctx = webrtc_streamer(
            key="pothole-detection",
            video_processor_factory=PotholeDetector,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )

        if webrtc_ctx.video_processor:
            st.markdown("### Live Prediction")
            st.info(webrtc_ctx.video_processor.result_text)

            if webrtc_ctx.video_processor.pothole_count > 5:
                st.error("The road is in bad condition! More than 5 potholes detected.")

            with st.expander("Detection Log"):
                logs = webrtc_ctx.video_processor.detection_log
                if not logs:
                    st.write("No potholes detected yet.")
                else:
                    for log in logs[-20:]:
                        st.write(log)