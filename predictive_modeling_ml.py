# Predictive Modeling Using Machine Learning
# Example Project using Random Forest Classifier

# Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Create Sample Dataset
# -----------------------------
# Example: Student study hours and exam result prediction

data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Attendance': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Result': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -----------------------------
# Step 2: Define Features & Target
# -----------------------------
X = df[['Study_Hours', 'Attendance']]
y = df['Result']

# -----------------------------
# Step 3: Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# Step 4: Train Model
# -----------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# Step 5: Predict Output
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Step 6: Check Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# -----------------------------
# Step 7: Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# -----------------------------
# Step 8: Classification Report
# -----------------------------
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# Step 9: Visualize Confusion Matrix
# -----------------------------
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# -----------------------------
# Step 10: Predict New Data
# -----------------------------
new_data = [[6, 80]]

prediction = model.predict(new_data)

if prediction[0] == 1:
    print("\nPredicted Result: PASS")
else:
    print("\nPredicted Result: FAIL")
