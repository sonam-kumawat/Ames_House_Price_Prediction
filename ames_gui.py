import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Dictionary for tooltips (feature descriptions)
tooltips = {
    'LotArea': 'Lot size in square feet',
    'OverallQual': 'Overall material and finish quality (1-10)',
    'OverallCond': 'Overall condition rating (1-10)',
    'YearBuilt': 'Original construction year',
    'YearRemodAdd': 'Remodel year',
    'MasVnrArea': 'Masonry veneer area in sq ft',
    'BsmtFinSF1': 'Basement finished area in sq ft',
    'TotalBsmtSF': 'Total basement area in sq ft',
    'GrLivArea': 'Above grade (ground) living area in sq ft',
    'GarageCars': 'Size of garage in car capacity'
}

# Function to display tooltip
def show_tooltip(text):
    tooltip_label.config(text=text)

# Function to predict house price
def predict_price():
    try:
        features = {
            'LotArea': float(lotarea_entry.get()),
            'OverallQual': int(overallqual_entry.get()),
            'OverallCond': int(overallcond_entry.get()),
            'YearBuilt': int(yearbuilt_entry.get()),
            'YearRemodAdd': int(yearremod_entry.get()),
            'MasVnrArea': float(masvnr_entry.get()),
            'BsmtFinSF1': float(bsmtfin_entry.get()),
            'TotalBsmtSF': float(totalbsmt_entry.get()),
            'GrLivArea': float(grliv_entry.get()),
            'GarageCars': int(garage_entry.get())
        }
        df = pd.DataFrame([features])
        prediction = model.predict(df)[0]
        messagebox.showinfo("Prediction", f"Predicted House Price: ${prediction:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for all fields.")

# Create main window
root = tk.Tk()
root.title("🏠 Ames House Price Predictor")
root.geometry("450x500")
root.resizable(False, False)

# Title label
tk.Label(root, text="Ames Housing Price Predictor", font=("Helvetica", 16, "bold"), fg="blue").pack(pady=10)

# Frame for input fields
frame = tk.Frame(root)
frame.pack(pady=10)

# Create labels and entries
entries = []
for i, (feature, desc) in enumerate(tooltips.items()):
    tk.Label(frame, text=feature+":").grid(row=i, column=0, sticky='w', padx=10, pady=5)
    entry = tk.Entry(frame)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry.bind("<Enter>", lambda e, text=desc: show_tooltip(text))
    entry.bind("<Leave>", lambda e: show_tooltip(""))
    entries.append(entry)

(lotarea_entry, overallqual_entry, overallcond_entry, yearbuilt_entry, yearremod_entry,
 masvnr_entry, bsmtfin_entry, totalbsmt_entry, grliv_entry, garage_entry) = entries

# Tooltip label
tooltip_label = tk.Label(root, text="", fg="green", wraplength=400, justify="left")
tooltip_label.pack(pady=5)

# Predict button
tk.Button(root, text="Predict Price", command=predict_price, bg="lightblue", font=("Helvetica", 12, "bold")).pack(pady=15)

# Run GUI loop
root.mainloop()
