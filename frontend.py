import streamlit as st
import requests

st.set_page_config(page_title="Ames House Price Prediction", layout="centered")

st.title("🏠 Ames House Price Prediction")
st.write("Enter the house details below to get the predicted sale price.")

# Input fields for 10 features
LotArea = st.number_input("Lot Area (sq ft)", min_value=0, value=8450)
OverallQual = st.number_input("Overall Quality (1–10)", min_value=1, max_value=10, value=7)
OverallCond = st.number_input("Overall Condition (1–10)", min_value=1, max_value=10, value=5)
YearBuilt = st.number_input("Year Built", min_value=1800, value=2003)
YearRemodAdd = st.number_input("Year Remodeled", min_value=1800, value=2003)
MasVnrArea = st.number_input("Masonry Veneer Area", min_value=0, value=196)
BsmtFinSF1 = st.number_input("Basement Finished Area", min_value=0, value=706)
TotalBsmtSF = st.number_input("Total Basement Area", min_value=0, value=856)
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", min_value=0, value=1710)
GarageCars = st.number_input("Garage Capacity (Cars)", min_value=0, value=2)

# API URL (FastAPI backend running locally)
API_URL = "http://127.0.0.1:8000/predict"

if st.button("Predict Price 🔮"):
    # Prepare data
    data = {
        "LotArea": LotArea,
        "OverallQual": OverallQual,
        "OverallCond": OverallCond,
        "YearBuilt": YearBuilt,
        "YearRemodAdd": YearRemodAdd,
        "MasVnrArea": MasVnrArea,
        "BsmtFinSF1": BsmtFinSF1,
        "TotalBsmtSF": TotalBsmtSF,
        "GrLivArea": GrLivArea,
        "GarageCars": GarageCars
    }

    # Call API
    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"🏡 **Predicted House Price:** ${result['prediction']:.2f}")
    else:
        st.error("❌ Error: Could not connect to backend API. Make sure FastAPI is running.")
