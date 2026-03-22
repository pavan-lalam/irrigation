import streamlit as st
import time
from mqtt_client import latest_data, run_mqtt
from model import model

st.set_page_config(page_title="Smart Irrigation", layout="wide")

st.title("🌱 Smart Irrigation Dashboard")

# Start MQTT thread only once
if "mqtt_started" not in st.session_state:
    run_mqtt()
    st.session_state["mqtt_started"] = True

placeholder = st.empty()

while True:

    with placeholder.container():

        if latest_data:

            st.subheader("📊 Live Sensor Data")

            col1, col2, col3 = st.columns(3)

            col1.metric("Moisture A", latest_data["mA"])
            col2.metric("Moisture B", latest_data["mB"])
            col3.metric("Moisture C", latest_data["mC"])

            st.write("🌡 Temperature:", latest_data["temp"])
            st.write("💧 Humidity:", latest_data["hum"])

            st.write("🚿 Pump:", "ON" if latest_data["pump"] else "OFF")

            st.write("Valve A:", latest_data["vA"])
            st.write("Valve B:", latest_data["vB"])
            st.write("Valve C:", latest_data["vC"])

            # ML Prediction
            X = [[latest_data["mA"], latest_data["temp"], latest_data["hum"]]]
            pred = model.predict(X)

            st.subheader("🌾 Yield Prediction")
            st.success(f"{pred[0]:.2f} %")

            # Crop Suggestion
            if latest_data["mA"] > 70:
                crop = "Rice 🌾"
            elif latest_data["mA"] > 50:
                crop = "Wheat 🌿"
            else:
                crop = "Millets 🌱"

            st.subheader("🌱 Suggested Crop")
            st.info(crop)

        else:
            st.warning("Waiting for MQTT data...")

    time.sleep(2)
