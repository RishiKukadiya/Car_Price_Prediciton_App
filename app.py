import streamlit as st
import pandas as pd
import joblib

# === Page Setup ===
st.set_page_config(page_title="🚘 Car Price Predictor", layout="wide")

# === Load Artifacts ===
model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("columns.pkl")

# === Encodings ===
car_make_encoding = {
    "BMW": 48000, "Audi": 45000, "Hyundai": 20000,
    "Ford": 30000, "Kia": 22000, "Tata": 18000,
    "Mercedes": 52000, "Toyota": 27000,
    "Mahindra": 21000, "Honda": 26000
}

fuel_types = [
    "regular unleaded", "premium unleaded (recommended)",
    "premium unleaded (required)", "diesel",
    "electric", "flex-fuel", "other"
]

# === Beautiful Title and Description ===
st.markdown("""
    <div style='text-align: center; padding: 10px 0 5px 0;'>
        <h1 style='font-size: 48px; color: #004466;'>🚘 Car Price Prediction App</h1>
        <p style='font-size: 20px; color: #333333; margin-top: -10px;'>
            Enter car details from the sidebar to estimate its market price using machine learning.
        </p>
    </div>
    <hr style="border: 1px solid #ddd;">
""", unsafe_allow_html=True)

# === Sidebar Inputs ===
st.sidebar.header("📋 Enter Car Details")

car_brand = st.sidebar.selectbox("🚗 Car Brand", list(car_make_encoding.keys()))
make_encoded = car_make_encoding[car_brand]

year = st.sidebar.slider("📅 Manufacture Year", 1990, 2025, 2015)
fuel_selected = st.sidebar.selectbox("⛽ Engine Fuel Type", fuel_types)
engine_cylinders = st.sidebar.selectbox("🔧 Engine Cylinders", [3, 4, 5, 6, 8, 10, 12])
transmission = st.sidebar.selectbox("⚙️ Transmission Type", ["automatic", "manual", "direct drive", "unknown"])
driven_wheels = st.sidebar.selectbox("🚙 Driven Wheels", ["front wheel drive", "rear wheel drive", "four wheel drive"])

# === Center-Aligned Predict Button ===
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎯 Predict Car Price", use_container_width=True):
        # === Prepare Input ===
        input_data = {
            'Year': year,
            'Engine Cylinders': engine_cylinders,
            'Make_encoded': make_encoded,

            'Engine Fuel Type_regular unleaded': int(fuel_selected == "regular unleaded"),
            'Engine Fuel Type_premium unleaded (recommended)': int(fuel_selected == "premium unleaded (recommended)"),
            'Engine Fuel Type_premium unleaded (required)': int(fuel_selected == "premium unleaded (required)"),
            'Engine Fuel Type_diesel': int(fuel_selected == "diesel"),
            'Engine Fuel Type_electric': int(fuel_selected == "electric"),
            'Engine Fuel Type_flex-fuel': int("flex-fuel" in fuel_selected),
            'Engine Fuel Type_other': int(fuel_selected == "other"),

            'Transmission Type_automatic': int(transmission == "automatic"),
            'Transmission Type_manual': int(transmission == "manual"),
            'Transmission Type_direct drive': int(transmission == "direct drive"),
            'Transmission Type_unknown': int(transmission == "unknown"),

            'Driven_Wheels_front wheel drive': int(driven_wheels == "front wheel drive"),
            'Driven_Wheels_rear wheel drive': int(driven_wheels == "rear wheel drive"),
            'Driven_Wheels_four wheel drive': int(driven_wheels == "four wheel drive"),
        }

        input_df = pd.DataFrame([input_data])
        for col in feature_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[feature_columns]

        # === Scale + Predict ===
        input_scaled = scaler.transform(input_df)
        predicted_price = model.predict(input_scaled)[0]
        usd_to_inr = 83.2  # 💡 Use current rate or fetch from API if needed
        predicted_price_inr = predicted_price * usd_to_inr
        # === Result Box ===
        st.markdown(
            f"""
            <div style='margin-top: 40px; background-color: #e6f7ff; padding: 25px;
                        border-radius: 12px; border: 1px solid #cce6ff; text-align: center;'>
                <h2 style='color: #007acc;'>💰 Estimated Car Price (MSRP)</h2>
                <h1 style='color: #004466; font-size: 42px;'>{predicted_price_inr:,.2f} ... INR</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.balloons()
