# Ames_House_Price_Prediction
Ames House Price Prediction

This is a complete end-to-end Machine Learning project to predict house prices in Ames, Iowa.
The project includes:

✔ Model training (train_model.py)
✔ Saved model (model.pkl)
✔ FastAPI backend (main.py)
✔ Streamlit frontend (frontend.py)
✔ Tkinter GUI (ames_gui.py)

🚀 Project Overview

The Ames Housing dataset contains 80+ features describing residential homes.
This project builds a regression model that predicts the Sale Price based on input features.

📂 Project Structure
Ames_House_Price_Prediction/
│
├── train_model.py        # Script to train ML model and save model.pkl
├── model.pkl             # Trained model file
├── main.py               # FastAPI backend for predictions
├── frontend.py           # Streamlit web app for user input
├── ames_gui.py           # Tkinter desktop GUI (optional)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

🔧 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/sonam-kumawat/Ames_House_Price_Prediction.git
cd Ames_House_Price_Prediction

2️⃣ Install dependencies
pip install -r requirements.txt

🧠 Train the Model

Run the training script:

python train_model.py


This will generate model.pkl, which is used by your backend and UI.

⚙️ Run the FastAPI Backend
uvicorn main:app --reload


Backend opens at:

http://127.0.0.1:8000


Interactive API docs:

http://127.0.0.1:8000/docs

🖥 Run the Streamlit Frontend
streamlit run frontend.py


Enter house details → get predicted price instantly.

🪟 Run the Tkinter GUI (Optional)
python ames_gui.py



Metric	Score
RMSE	____
R²	____
