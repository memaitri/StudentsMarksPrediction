# Student Performance Predictor

A Flask web application that predicts student exam scores based on various academic and personal factors using machine learning.

## Features

- Predict exam scores based on comprehensive student data
- User-friendly web interface for input
- Machine learning model trained on extensive student performance dataset
- Real-time predictions with detailed results

## Input Features

The model considers the following factors:
- Age
- Gender
- Study Hours per Week
- Preferred Learning Style
- Online Courses Completed
- Participation in Discussions
- Assignment Completion Rate
- Attendance Rate
- Use of Educational Technology
- Self-Reported Stress Level
- Time Spent on Social Media
- Sleep Hours per Night

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

- **Flask** - Web framework
- **scikit-learn** - Machine learning
- **pandas** - Data manipulation
- **joblib** - Model serialization

## Model Performance

The linear regression model provides accurate predictions based on historical student performance data.