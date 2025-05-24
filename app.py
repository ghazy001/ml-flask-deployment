from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load the model and preprocessing tools
def load_model():
    model = joblib.load('models/knn_model.joblib')
    scaler = joblib.load('models/scaler.joblib')
    label_encoders = joblib.load('models/label_encoders.joblib')
    numeric_cols = joblib.load('models/numeric_cols.joblib')
    target_encoder = joblib.load('models/target_encoder.joblib')
    feature_names = joblib.load('models/feature_names.joblib')
    return model, scaler, label_encoders, numeric_cols, target_encoder, feature_names

@app.route('/')
def home():
    # Hardcoded options based on your dataset
    gender_options = ['M', 'F']
    subject_options = ['Math', 'English', 'Science', 'Arabic', 'CS', 'Quran', 'Spanish', 'French', 'History', 'Geography', 'Biology', 'Chemistry', 'Geology']
    income_options = ['Low', 'Medium', 'High']
    nationality_options = ['KW', 'Jordan', 'Palestine', 'Iraq', 'Lebanon', 'Egypt', 'USA', 'Venezuela', 'Iran', 'Saudi Arabia', 'Syria', 'Morocco', 'Tunisia']
    lms_options = ['Yes', 'No']

    return render_template('index.html', 
                           gender_options=gender_options,
                           subject_options=subject_options,
                           income_options=income_options,
                           nationality_options=nationality_options,
                           lms_options=lms_options)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load models and encoders
        model, scaler, label_encoders, numeric_cols, target_encoder, feature_names = load_model()

        # Collect input from the form
        age = float(request.form['age'])
        gender = request.form['gender']
        subject = request.form['subject']
        income = request.form['income']
        nationality = request.form['nationality']
        study_hours = float(request.form['study_hours'])
        lms = request.form['lms']

        # Construct input DataFrame
        input_data = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Subject': [subject],
            'Family_Income_Level': [income],
            'NationalITy': [nationality],
            'Study_Hours_per_Week': [study_hours],
            'LMS': [lms]
        })

        # Encode categorical variables
        for col, encoder in label_encoders.items():
            if col in input_data.columns:
                try:
                    input_data[col] = encoder.transform(input_data[col].astype(str))
                except Exception:
                    most_common = encoder.transform([encoder.classes_[0]])[0]
                    print(f"Unseen value in {col}, using default.")
                    input_data[col] = most_common

        # ✅ Scale all numeric columns at once
        input_data[numeric_cols] = scaler.transform(input_data[numeric_cols])

        # ✅ Reorder columns to match training order
        missing = set(feature_names) - set(input_data.columns)
        if missing:
            raise ValueError(f"Missing input features: {missing}")

        input_data = input_data[feature_names]

        # Make prediction
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        # Decode prediction
        prediction_label = target_encoder.inverse_transform([prediction])[0]
        class_labels = target_encoder.classes_
        class_probs = {label: float(prob) for label, prob in zip(class_labels, probabilities)}

        return render_template('result.html', 
                               prediction=prediction_label,
                               probability=round(max(probabilities) * 100, 2),
                               class_probs=class_probs)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    if not os.path.exists('models/knn_model.joblib'):
        print("Model not found. Please run the training script first.")
    app.run(debug=True)
