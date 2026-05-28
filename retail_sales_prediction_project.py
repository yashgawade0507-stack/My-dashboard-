# Real-World Data Project (Retail Domain)
# Retail Sales Prediction and Data Analysis Using Python

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Create Sample Dataset
data = {
    'Advertising_Spend': [10, 12, 13, 15, 16, 18, 20, 22, 25, 30],
    'Sales': [100, 120, 130, 150, 165, 180, 200, 220, 250, 300]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Data Visualization
plt.figure(figsize=(6,4))
sns.scatterplot(x='Advertising_Spend', y='Sales', data=df)

plt.title("Advertising Spend vs Sales")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.show()

# Prepare Data for Machine Learning
X = df[['Advertising_Spend']]
y = df['Sales']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict Sales
predictions = model.predict(X_test)

print("\nPredicted Sales:")
print(predictions)

# Evaluate Model
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print("\nMean Absolute Error:", mae)
print("Mean Squared Error:", mse)

# Final Visualization
plt.figure(figsize=(6,4))

plt.scatter(X_test, y_test, label='Actual Sales')
plt.plot(X_test, predictions, label='Predicted Line')

plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.title("Sales Prediction")

plt.legend()
plt.show()

# Conclusion
print("\nProject Completed Successfully!")
