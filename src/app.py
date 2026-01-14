import tkinter as tk
from tkinter import ttk
import pandas as pd

class AppInterface:
    def __init__(self, model):
            self.model = model

    def run(self):
        self.window = tk.Tk()
        self.window.title("Heart Disease Prediction App")
        self.window.geometry("500x800")
        self.window.configure(bg="#f4f9ff")  

        style = ttk.Style()
        style.theme_use("clam")

        # Labels
        style.configure("TLabel",
                        background="#f4f9ff",
                        foreground="#003366",
                        font=("Segoe UI", 11))

    
        style.configure("TEntry",
                        fieldbackground="#ffffff", 
                        foreground="#003366",
                        insertcolor="#003366",
                        padding=6,
                        bordercolor="#a7c7e7",
                        lightcolor="#a7c7e7",
                        darkcolor="#a7c7e7")

        # Buttons
        style.configure("TButton",
                        background="#2d89ef",
                        foreground="#ffffff",
                        font=("Segoe UI", 13, "bold"),
                        padding=10,
                        borderwidth=0)
        
        style.configure("Input.TFrame", background="#f4f9ff")

        style.map("TButton",
                background=[("active", "#1b5fbd")])

        # ----- Title -----
        title = ttk.Label(self.window,
                        text="Heart Disease Prediction",
                        font=("Segoe UI", 22, "bold"),
                        foreground="#1b5fbd",
                        background="#f4f9ff")  # matchar fönstrets bakgrund
        title.pack(pady=25)

        # Feature names
        self.feature_names = [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak",
            "slope", "ca", "thal"
        ]

        self.entries = {}

        # ----- Input fields -----
        for feature in self.feature_names:
            frame = ttk.Frame(self.window, style="Input.TFrame")
            frame.pack(pady=7)

            label = ttk.Label(frame, text=feature.capitalize() + ":")
            label.pack(side="left", padx=8)

            entry = ttk.Entry(frame, width=16)
            entry.pack(side="left", padx=8)
            self.entries[feature] = entry

        # ----- Predict button -----
        predict_button = ttk.Button(self.window,
                                    text="Run Medical Analysis",
                                    command=self.predict)
        predict_button.pack(pady=30)

        # ----- Result label -----
        self.result_label = ttk.Label(self.window,
                                    text="",
                                    font=("Segoe UI", 15, "bold"),
                                    foreground="#003366",
                                    background="#f4f9ff")
        self.result_label.pack(pady=20)

        self.window.mainloop()



    def predict(self):
        try:
    
            user_input = []
            for feature in self.feature_names:
                value = float(self.entries[feature].get())
                user_input.append(value)
            df = pd.DataFrame([user_input], columns=self.feature_names)
            prediction = self.model.predict(df)
            if prediction == 1:
                self.result_label.config(text="⚠️ Risk of heart disease", foreground="red")
            else:
                self.result_label.config(text="✔️ No risk detected", foreground="green")

        except Exception as e:
            self.result_label.config(text=f"Error: {e}", foreground="orange")
