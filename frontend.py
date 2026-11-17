import streamlit as st
import requests

st.set_page_config(
    page_title="House Price Prediction",
    layout="centered"
)

st.title("🏠 Ames House Price Prediction")

st.write(
    "Enter the house details below to estimate its selling price."
)

# Five simplified input fields

lot_area = st.number_input(
    "Plot Area (sq. ft.)",
    min_value=0.0,
    value=8450.0
)

overall_qual = st.slider(
    "House Quality (1-10)",
    min_value=1,
    max_value=10,
    value=7
)

year_built = st.number_input(
    "Year of Construction",
    min_value=1800,
    max_value=2026,
    value=2000
)

gr_liv_area = st.number_input(
    "Living Area (sq. ft.)",
    min_value=0.0,
    value=1500.0
)

garage_cars = st.selectbox(
    "Garage Capacity (Cars)",
    options=[0, 1, 2, 3, 4]
)

# Prediction button

if st.button("Predict House Price"):

    data = {
        "LotArea": lot_area,
        "OverallQual": overall_qual,
        "YearBuilt": year_built,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()

            st.success(
                f"Predicted House Price: "
                f"${result['prediction']:,.2f}"
            )
        else:
            st.error(f"Prediction failed: {response.text}")

    except requests.RequestException as e:
        st.error(f"Could not connect to backend: {e}")

