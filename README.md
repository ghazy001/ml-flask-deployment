Internet Access Prediction Web Application
Overview
This is a Flask-based web application that predicts whether a student has internet access at home based on features such as age, gender, subject, family income level, nationality, study hours per week, and LMS (Learning Management System) usage. The prediction is made using a pre-trained K-Nearest Neighbors (KNN) model, with data preprocessing handled by StandardScaler and LabelEncoder from scikit-learn. The application provides a user-friendly interface built with Bootstrap and Chart.js for visualization of prediction results.
Features

Input Form: Users can input student details (age, gender, subject, etc.) via a web form.
Prediction Output: Displays whether the student has internet access ("Yes" or "No") along with the confidence probability.
Visualization: Shows a bar chart of class probabilities (Yes/No) using Chart.js.
Error Handling: Gracefully handles invalid inputs or missing model files with a dedicated error page.
Responsive Design: Built with Bootstrap for a mobile-friendly user interface.

Project Structure
├── models/
│   ├── knn_model.joblib        # Pre-trained KNN model
│   ├── scaler.joblib           # StandardScaler for numeric features
│   ├── label_encoders.joblib   # LabelEncoders for categorical features
│   ├── numeric_cols.joblib     # List of numeric columns
│   ├── target_encoder.joblib   # LabelEncoder for target variable
│   ├── feature_names.joblib    # List of feature names used in training
├── templates/
│   ├── index.html              # Home page with input form
│   ├── result.html             # Prediction result page
│   ├── error.html              # Error page for failed predictions
├── app.py                      # Main Flask application
├── requirements.txt            # Project dependencies
└── README.md                   # This file

Requirements
The project dependencies are listed in requirements.txt. The required Python packages are:

pandas>=2.0.0
numpy>=1.26.0
scikit-learn>=1.5.0
seaborn>=0.13.0
matplotlib>=3.8.0
joblib>=1.4.0
flask>=3.0.0

Installation

Clone the repository:
git clone <repository-url>
cd <repository-directory>


Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Ensure model files exist:

The application requires pre-trained model files in the models/ directory.
If the model files are missing, run the training script (not included in this repository) to generate:
knn_model.joblib
scaler.joblib
label_encoders.joblib
numeric_cols.joblib
target_encoder.joblib
feature_names.joblib





Usage

Run the application:
python app.py

The Flask server will start in debug mode, accessible at http://127.0.0.1:5000.

Access the web interface:

Open a web browser and navigate to http://127.0.0.1:5000.
Fill out the form with student details (age, gender, subject, family income level, nationality, study hours, and LMS usage).
Submit the form to receive a prediction.


View results:

The result page (result.html) displays the prediction ("Yes" or "No") with a confidence probability and a bar chart showing class probabilities.
If an error occurs (e.g., invalid input or missing model files), the error page (error.html) will be shown.



Example Input

Age: 15
Gender: M
Subject: Math
Family Income Level: Medium
Nationality: Jordan
Study Hours per Week: 10
LMS: Yes

Notes

The application assumes the model and preprocessing files are available in the models/ directory. If these files are missing, the app will display an error message in the console and fail to load.
The categorical input options (e.g., gender, subject) are hardcoded based on the dataset used for training.
The application uses Bootstrap 5.3.0-alpha1 and Chart.js for styling and visualization, loaded via CDN.
The error page includes Font Awesome icons for visual feedback, also loaded via CDN.

Troubleshooting

Model not found error: Ensure all .joblib files are present in the models/ directory. Run the training script to generate these files if necessary.
Invalid input error: Check that all form fields are filled correctly (e.g., age and study hours must be numeric).
Dependency issues: Verify that all required packages are installed using the specified versions in requirements.txt.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Built with Flask, scikit-learn, and Bootstrap.
Visualization powered by Chart.js.
Icons provided by Font Awesome.

