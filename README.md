# 🎓 Exam Score Predictor

This project is a simple machine learning app that predicts a student's exam score based on the number of hours they study, using a **custom linear regression model** implemented from scratch in Python. The application comes with a graphical user interface (GUI) built using **Tkinter**.

---

## 💡 Features

- 📈 Trained using a custom `Linear_Regression` class (no scikit-learn model).
- 📊 Predicts exam scores based on hours studied.
- ⚠️ Warns users against over-studying (more than 12 hours).
- 🖼️ Interactive and user-friendly GUI.
- ✅ Clean and readable code structure.

---

## 📁 Dataset

The dataset used is `study_vs_score_data_1.csv`, which contains two columns:
- `Hours` – Number of hours studied.
- `Scores` – Corresponding exam scores.

Make sure this CSV file is located in the same directory as the main script.

---

## 🧠 Model

The linear regression model is implemented from scratch:

- Uses gradient descent for optimization.
- Manually calculates weight and bias updates.
- Limits prediction output to range between 0 and 100.

---

## 🖥️ GUI (Tkinter)

The interface allows the user to:

- Enter the number of study hours.
- Click a button to see the predicted score.
- View alerts if input is invalid or exceeds 12 hours (health warning).

---

## 📦 Dependencies

- Python 3.x
- NumPy
- Pandas
- Tkinter (comes pre-installed with Python)
---

🛠 File Structure
.
├── Linear_Regression.py       # Custom linear regression model
├── app.py                     # Main script with GUI
├── study_vs_score_data_1.csv  # Dataset
└── README.md                  # Project documentation
