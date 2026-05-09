# Student Exam Score Predictor

A Flask web application that predicts student exam scores based on various factors using machine learning.

## Features

- Predict exam scores based on student data
- Web interface for easy input
- Machine learning model trained on student performance data

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `python app.py`

## Deployment on Render

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set the following:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
4. Deploy!

## Technologies Used

- Flask
- scikit-learn
- pandas
- joblib