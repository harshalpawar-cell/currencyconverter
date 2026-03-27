import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# --- Dataset (sample) ---
data = {
    "maths":    [92, 85, 78, 88, 67, 73, 81, 90, 60, 76, 84, 69, 95, 55, 72, 80, 66, 87, 91, 74],
    "physics":  [90, 82, 75, 85, 65, 70, 79, 88, 58, 74, 80, 66, 94, 52, 70, 78, 64, 85, 89, 72],
    "cs":       [95, 88, 80, 90, 70, 75, 85, 92, 65, 78, 86, 72, 97, 60, 76, 84, 68, 89, 93, 79],
    "english":  [85, 80, 70, 78, 60, 68, 75, 82, 55, 72, 77, 65, 88, 50, 69, 74, 62, 79, 83, 71],
    "cgpa":     [9.3, 8.7, 7.8, 8.8, 6.8, 7.2, 8.1, 9.0, 6.2, 7.6, 8.4, 7.0, 9.6, 5.8, 7.3, 8.2, 6.7, 8.9, 9.2, 7.5]
}

df = pd.DataFrame(data)

# Features & Target
X = df[["maths", "physics", "cs", "english"]]
y = df["cgpa"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# --- User Input ---
m = float(input("Maths marks: "))
p = float(input("Physics marks: "))
c = float(input("CS marks: "))
e = float(input("English marks: "))

# Prediction
cgpa_pred = model.predict([[m, p, c, e]])

print("Predicted CGPA:", round(cgpa_pred[0], 2))