# Exploratory Data Analysis (EDA) Project

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create Sample Dataset
data = {
    'Hours_Studied': [2, 3, 4, 5, 6, 7, 8, 9],
    'Attendance': [60, 65, 70, 75, 80, 85, 90, 95],
    'Previous_Score': [50, 55, 60, 65, 70, 75, 80, 85],
    'Final_Score': [55, 60, 65, 70, 75, 80, 85, 90]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Dataset:")
print(df)

# Basic Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Correlation Matrix
print("\nCorrelation Matrix:")
print(df.corr())

# Visualization 1 - Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(x='Hours_Studied', y='Final_Score', data=df)
plt.title("Hours Studied vs Final Score")
plt.show()

# Visualization 2 - Histogram
plt.figure(figsize=(6,4))
sns.histplot(df['Final_Score'], bins=5, kde=True)
plt.title("Distribution of Final Scores")
plt.show()

# Visualization 3 - Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Insights
print("\nInsights:")
print("1. Final scores increase with study hours.")
print("2. Attendance positively affects performance.")
print("3. Strong positive correlation exists between all variables.")
