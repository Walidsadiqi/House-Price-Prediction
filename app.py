import streamlit as st
import numpy as np
import joblib
import os

# Load pipeline
pipeline_path = "house_price_pipeline.pkl"
if not os.path.exists(pipeline_path):
    st.error("❌ Missing pipeline file!")
    st.stop()

pipeline = joblib.load(pipeline_path)

# Features order
features_order = ["floors", "waterfront", "lat", "bedrooms", "sqft_basement",
                  "view", "bathrooms", "sqft_living15", "sqft_above", "grade", "sqft_living"]

# Custom CSS for the app's style (using gradient background, shadow effects, and hover effects)
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #4CA1AF, #C4E0E5);
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 12px;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45A049;
    }
    .stNumberInput>div>label {
        font-size: 18px;
        color: #333;
    }
    .stTitle {
        color: #2C3E50;
        font-size: 36px;
        font-weight: bold;
    }
    .stSelectbox>div>label {
        font-size: 18px;
        color: #333;
    }
    .stAlert {
        background-color: #E74C3C;
        color: white;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🏡 House Price Prediction App")

# Inputs in a form layout
with st.form(key='prediction_form'):
    col1, col2 = st.columns(2)

    with col1:
        floors = st.number_input("Floors", 1.0, 5.0, 1.0)
        lat = st.number_input("Latitude", 47.0, 48.0, 47.5)
        bedrooms = st.number_input("Bedrooms", 1, 10, 3)
        sqft_basement = st.number_input("Basement sqft", 0, 3000, 0)
        view = st.number_input("View (0-4)", 0, 4, 0)
        bathrooms = st.number_input("Bathrooms", 1.0, 10.0, 2.0)

    with col2:
        waterfront = st.selectbox("Waterfront", [0, 1])
        sqft_living15 = st.number_input("Living15 sqft", 500, 10000, 2000)
        sqft_above = st.number_input("Above sqft", 500, 8000, 1500)
        grade = st.number_input("Grade (1-13)", 1, 13, 7)
        sqft_living = st.number_input("Living sqft", 500, 10000, 2000)

    # Submit button for form
    submit_button = st.form_submit_button(label="Predict Price")

# Prepare input data
input_data = np.array([[floors, waterfront, lat, bedrooms, sqft_basement, view,
                        bathrooms, sqft_living15, sqft_above, grade, sqft_living]])

# Prediction logic
if submit_button:
    price = pipeline.predict(input_data)[0]
    st.success(f"🎉 Estimated House Price: ${price:,.2f}")

# Add footer for polish
st.markdown("""
    <footer style="text-align: center; padding: 10px 0; font-size: 14px; color: #555;">
        Made with ❤️ by Walid Sadiqi | House Prediction App
    </footer>
""", unsafe_allow_html=True)