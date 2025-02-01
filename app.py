import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

# Set up the Streamlit app
st.set_page_config(page_title="Vehicle Cybersecurity Demo", layout="wide")
st.title("🚗 Vehicle Cybersecurity Simulation Dashboard")

# Load car image
car_image = Image.open("car_image.png")
st.image(car_image, caption="Vehicle Simulation", use_column_width=True)

# Simulate CAN Bus Data
def generate_can_data(num_entries):
    data = []
    for _ in range(num_entries):
        entry = {
            "Timestamp": pd.Timestamp.now(),
            "ID": np.random.randint(100, 110),
            "Speed": np.random.randint(0, 150),
            "RPM": np.random.randint(500, 7000),
            "Status": "Normal"
        }
        # Introduce anomalies
        if np.random.rand() > 0.9:
            entry["Speed"] = np.random.choice([0, 200])  # Anomalous speed
            entry["Status"] = "Anomalous"
        data.append(entry)
        time.sleep(0.1)  # Simulate real-time data generation
    return pd.DataFrame(data)

# Display CAN Bus Data
st.subheader("📊 Real-Time CAN Bus Data")
num_entries = st.slider("Number of Data Entries", min_value=10, max_value=100, value=20)
can_data = generate_can_data(num_entries)
st.dataframe(can_data)

# Anomaly Detection
st.subheader("🔍 Anomaly Detection")
anomalies = can_data[can_data["Status"] == "Anomalous"]
if not anomalies.empty:
    st.warning(f"Detected {len(anomalies)} anomalies in the CAN bus data.")
    st.dataframe(anomalies)
else:
    st.success("No anomalies detected.")

# VSOC Notification Simulation
st.subheader("📡 VSOC Notification")
if st.button("Forward Anomalies to VSOC"):
    if not anomalies.empty:
        st.info("Anomalies forwarded to VSOC for further analysis.")
        # Simulate VSOC analysis
        with st.spinner("Analyzing anomalies at VSOC..."):
            time.sleep(2)
        st.success("VSOC analysis complete. Threat identified as 'Malware Injection'.")
    else:
        st.info("No anomalies to forward.")

# OTA Update Simulation
st.subheader("🚀 OTA Update Deployment")
if st.button("Deploy OTA Security Patch"):
    st.info("Deploying OTA Update...")
    time.sleep(2)  # Simulate deployment time
    st.success("OTA Security Patch deployed successfully!")

# IDPS Ruleset Update Simulation
st.subheader("🛡️ IDPS Ruleset Update")
if st.button("Update IDPS Ruleset"):
    st.info("Updating IDPS ruleset to address new threats...")
    time.sleep(2)  # Simulate update time
    st.success("IDPS ruleset updated successfully!")

# Quantum Technology Integration Simulation
st.subheader("🔒 Quantum Technology Integration")
if st.button("Integrate Quantum Security"):
    st.info("Integrating quantum technology for enhanced security...")
    time.sleep(2)  # Simulate integration time
    st.success("Quantum security measures implemented successfully!")
