import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import Linear_Regression as LR
import tkinter as tk
from tkinter import ttk, messagebox
import Linear_Regression as LR

dataset = pd.read_csv('study_vs_score_data_1.csv')
# print(dataset.head())
# print(dataset.tail())
# print(dataset.shape)

# print(dataset.isnull().sum())

X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values
# print(X)
# print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=2)

model = LR.Linear_Regression(learning_rate=0.006, no_of_iterations=1000)
model.fit(X_train,Y_train)

# print(model.w[0])
# print(model.b)

test_data_prediction = model.predict(X_test)
# print(X_test)
# print(test_data_prediction)  

# Prediction function
def predict_score():
    try:
        hours = float(entry.get())
        predicted_score = model.predict(np.array([[hours]]))[0]
        predicted_score = max(0, min(100, predicted_score)) 
        result_label.config(text=f"📘 Predicted Exam Score: {predicted_score:.2f} / 100")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")



# GUI setup
root = tk.Tk()
root.title("📚 Exam Score Predictor")
root.geometry("480x420")
root.configure(bg="#f0f8ff")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                font=("Segoe UI", 11),
                foreground="white",
                background="#007acc",
                padding=10)
style.map("TButton", background=[("active", "#005f99")])

# Title
title = tk.Label(root, text="🎓 Exam Score Predictor", font=("Segoe UI", 22, "bold"), fg="#003366", bg="#f0f8ff")
title.pack(pady=25)

# Input Label
label = tk.Label(root, text="Enter Hours of Study:", font=("Segoe UI", 13), bg="#f0f8ff", fg="#003366")
label.pack()

# Entry Field
entry = tk.Entry(root, font=("Segoe UI", 14), justify="center", relief="solid", bd=1, width=20)
entry.pack(pady=10)

# Predict Button
predict_btn = ttk.Button(root, text="🎯 Predict Score", command=predict_score)
predict_btn.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Segoe UI", 16, "bold"), fg="#006400", bg="#f0f8ff")
result_label.pack(pady=30)

# Footer
footer = tk.Label(root, text="Made by Neev", font=("Segoe UI", 10), bg="#f0f8ff", fg="#666")
footer.pack(side="bottom", pady=10)

# Run the GUI loop
root.mainloop()
