import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib
from pathlib import Path

# Load trained model
model = joblib.load(Path(__file__).with_name("model.pkl"))

# Main window
root = tk.Tk()
root.title("Ames House Price Prediction")
root.geometry("650x680")
root.resizable(False, False)
root.configure(bg="#F1F5F9")

# Colors
NAVY = "#142D4E"
BLUE = "#2563EB"
WHITE = "#FFFFFF"
BG = "#F1F5F9"
TEXT = "#26364A"
GREY = "#64748B"

# Header
header = tk.Frame(root, bg=NAVY, height=125)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="🏠  Ames House Price Predictor",
    font=("Segoe UI", 22, "bold"),
    bg=NAVY,
    fg=WHITE
).pack(pady=(22, 5))

tk.Label(
    header,
    text="Estimate your property's market value",
    font=("Segoe UI", 10),
    bg=NAVY,
    fg="#CBD5E1"
).pack()

# Main card
card = tk.Frame(
    root,
    bg=WHITE,
    padx=35,
    pady=22,
    highlightbackground="#E2E8F0",
    highlightthickness=1
)
card.pack(padx=45, pady=25, fill="both")

tk.Label(
    card,
    text="Property Details",
    font=("Segoe UI", 17, "bold"),
    bg=WHITE,
    fg=NAVY
).pack(anchor="w")

tk.Label(
    card,
    text="Enter the following information about your house.",
    font=("Segoe UI", 9),
    bg=WHITE,
    fg=GREY
).pack(anchor="w", pady=(3, 18))

# Input fields
fields = [
    ("Plot Area (sq. ft.)", "LotArea", "entry"),
    ("House Quality (1-10)", "OverallQual", "quality"),
    ("Year of Construction", "YearBuilt", "year"),
    ("Living Area (sq. ft.)", "GrLivArea", "entry"),
    ("Garage Capacity (Cars)", "GarageCars", "garage")
]

entries = {}

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Custom.TEntry",
    fieldbackground="#F8FAFC",
    padding=9,
    font=("Segoe UI", 10)
)

style.configure(
    "Custom.TCombobox",
    fieldbackground="#F8FAFC",
    padding=7,
    font=("Segoe UI", 10)
)

for label_text, feature, field_type in fields:

    row = tk.Frame(card, bg=WHITE)
    row.pack(fill="x", pady=7)

    tk.Label(
        row,
        text=label_text,
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT,
        width=25,
        anchor="w"
    ).pack(side="left")

    if field_type == "quality":
        widget = ttk.Combobox(
            row,
            values=list(range(1, 11)),
            state="readonly",
            style="Custom.TCombobox",
            width=22
        )
        widget.set("7")

    elif field_type == "garage":
        widget = ttk.Combobox(
            row,
            values=[0, 1, 2, 3, 4],
            state="readonly",
            style="Custom.TCombobox",
            width=22
        )
        widget.set("2")

    else:
        widget = ttk.Entry(
            row,
            style="Custom.TEntry",
            width=25
        )

        if feature == "LotArea":
            widget.insert(0, "8450")
        elif feature == "YearBuilt":
            widget.insert(0, "2000")
        elif feature == "GrLivArea":
            widget.insert(0, "1500")

    widget.pack(side="right")
    entries[feature] = widget


# Prediction function

def predict_price():
    try:
        features = {
            "LotArea": float(entries["LotArea"].get()),
            "OverallQual": int(entries["OverallQual"].get()),
            "YearBuilt": int(entries["YearBuilt"].get()),
            "GrLivArea": float(entries["GrLivArea"].get()),
            "GarageCars": int(entries["GarageCars"].get())
        }

        df = pd.DataFrame([features])
        prediction = model.predict(df)[0]

        price_text = f"${prediction:,.2f}"

        print("Prediction calculated:", price_text)

        # Update GUI label
        result_label.config(
            text=price_text,
            fg="green",
            font=("Segoe UI", 22, "bold")
        )

        # Force GUI refresh
        result_label.pack()
        root.update()

        # Temporary confirmation popup
        messagebox.showinfo(
            "Prediction Successful",
            f"Predicted House Price: {price_text}"
        )

    except Exception as e:
        messagebox.showerror("Prediction Error", str(e))



# Predict button
predict_button = tk.Button(
    card,
    text="Predict House Price  →",
    command=predict_price,
    font=("Segoe UI", 11, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground="#1D4ED8",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=12
)
predict_button.pack(pady=(25, 15))

# Result section
result_frame = tk.Frame(
    card,
    bg="#F0FDF4",
    padx=15,
    pady=12
)
result_frame.pack(fill="x")

tk.Label(
    result_frame,
    text="ESTIMATED HOUSE PRICE",
    font=("Segoe UI", 9, "bold"),
    bg="#F0FDF4",
    fg=GREY
).pack()

result_var = tk.StringVar()
result_var.set("Your prediction will appear here")

result_label = tk.Label(
    result_frame,
    textvariable=result_var,
    font=("Segoe UI", 17, "bold"),
    bg="#F0FDF4",
    fg="#26364A"
)
result_label.pack(pady=5)

# Footer
tk.Label(
    root,
    text="Powered by Machine Learning | XGBoost Regressor",
    font=("Segoe UI", 9),
    bg=BG,
    fg=GREY
).pack(pady=5)

root.mainloop()
