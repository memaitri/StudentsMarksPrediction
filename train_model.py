# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df5 = pd.read_csv("student_performance_large_dataset.csv")

# Select useful features
x4 = df5[[
    "Age", "Gender", "Study_Hours_per_Week", "Preferred_Learning_Style",
    "Online_Courses_Completed", "Participation_in_Discussions", "Assignment_Completion_Rate (%)",
    "Attendance_Rate (%)", "Use_of_Educational_Tech", "Self_Reported_Stress_Level",
    "Time_Spent_on_Social_Media (hours/week)", "Sleep_Hours_per_Night"
]]

y4 = df5[["Exam_Score (%)"]]

# Drop Student_ID if present
if 'Student_ID' in x4.columns:
    x4 = x4.drop(columns=['Student_ID'])

# Convert categorical variables to numeric using one-hot encoding
x4_encoded = pd.get_dummies(x4, drop_first=True)

# Fit Linear Regression model
reg3 = LinearRegression()
reg3.fit(x4_encoded, y4)

# Save model and column names
joblib.dump(reg3, "linear_model.pkl")
joblib.dump(x4_encoded.columns.tolist(), "model_columns.pkl")

print("Model and column names saved successfully!")
