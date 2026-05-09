from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load model and column names
model = joblib.load("linear_model.pkl")
model_columns = joblib.load("model_columns.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    input_data = {
        'Age': int(request.form['Age']),
        'Gender': request.form['Gender'],
        'Study_Hours_per_Week': float(request.form['Study_Hours_per_Week']),
        'Preferred_Learning_Style': request.form['Preferred_Learning_Style'],
        'Online_Courses_Completed': int(request.form['Online_Courses_Completed']),
        'Participation_in_Discussions': float(request.form['Participation_in_Discussions']),
        'Assignment_Completion_Rate (%)': float(request.form['Assignment_Completion_Rate']),
        'Attendance_Rate (%)': float(request.form['Attendance_Rate']),
        'Use_of_Educational_Tech': request.form['Use_of_Educational_Tech'],
        'Self_Reported_Stress_Level': float(request.form['Self_Reported_Stress_Level']),
        'Time_Spent_on_Social_Media (hours/week)': float(request.form['Time_Spent_on_Social_Media']),
        'Sleep_Hours_per_Night': float(request.form['Sleep_Hours_per_Night'])
    }

    input_df = pd.DataFrame([input_data])

    # One-hot encode and align with training columns
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_encoded)[0][0]
    prediction = round(prediction, 2)

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
