# Student Internet Access Prediction App

A Flask web application that predicts whether a student has internet access at home based on demographic and academic factors using a K-Nearest Neighbors (KNN) machine learning model.

## 🎯 Overview

This application uses machine learning to predict internet access availability for students based on:
- Personal demographics (age, gender, nationality)
- Academic information (subject, study hours)
- Family background (income level)
- Learning management system usage

## 🚀 Features

- **Interactive Web Interface**: User-friendly form for inputting student information
- **Real-time Predictions**: Instant predictions with confidence scores
- **Visual Analytics**: Interactive charts showing prediction probabilities
- **Responsive Design**: Mobile-friendly Bootstrap interface
- **Error Handling**: Comprehensive error management and user feedback

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the trained models in the `models/` directory:**
   - `knn_model.joblib` - Trained KNN classifier
   - `scaler.joblib` - Feature scaler
   - `label_encoders.joblib` - Categorical variable encoders
   - `numeric_cols.joblib` - List of numeric columns
   - `target_encoder.joblib` - Target variable encoder
   - `feature_names.joblib` - Feature names for model input

## 📁 Project Structure

```
project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── models/               # Trained ML models and preprocessors
│   ├── knn_model.joblib
│   ├── scaler.joblib
│   ├── label_encoders.joblib
│   ├── numeric_cols.joblib
│   ├── target_encoder.joblib
│   └── feature_names.joblib
└── templates/            # HTML templates
    ├── index.html        # Main input form
    ├── result.html       # Prediction results page
    └── error.html        # Error handling page
```

## 🚀 Running the Application

1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Fill out the student information form with:**
   - Age (numeric)
   - Gender (Male/Female)
   - Subject area
   - Family income level
   - Nationality
   - Study hours per week
   - LMS usage (Yes/No)

4. **Click "Predict" to get the internet access prediction**

## 🎯 How It Works

### Input Features
- **Age**: Student's age in years
- **Gender**: Male (M) or Female (F)
- **Subject**: Academic subject area (Math, English, Science, etc.)
- **Family Income Level**: Low, Medium, or High
- **Nationality**: Student's country of origin
- **Study Hours per Week**: Number of hours spent studying weekly
- **LMS Usage**: Whether the student uses a Learning Management System

### Prediction Process
1. **Data Collection**: User inputs are collected via the web form
2. **Preprocessing**: Categorical variables are encoded and numeric features are scaled
3. **Model Prediction**: The trained KNN model generates predictions
4. **Results Display**: Prediction results are shown with confidence scores and visualizations

### Supported Options

**Subjects:**
- Math, English, Science, Arabic, CS, Quran, Spanish, French, History, Geography, Biology, Chemistry, Geology

**Nationalities:**
- KW, Jordan, Palestine, Iraq, Lebanon, Egypt, USA, Venezuela, Iran, Saudi Arabia, Syria, Morocco, Tunisia

**Income Levels:**
- Low, Medium, High

## 📊 Model Information

- **Algorithm**: K-Nearest Neighbors (KNN)
- **Target Variable**: Internet access at home (Yes/No)
- **Feature Engineering**: Label encoding for categorical variables, standard scaling for numeric features
- **Output**: Binary classification with probability scores

## 🔧 Technical Details

### Dependencies
- **Flask 3.0.0+**: Web framework
- **pandas 2.0.0+**: Data manipulation
- **numpy 1.26.0+**: Numerical computing
- **scikit-learn 1.5.0+**: Machine learning
- **joblib 1.4.0+**: Model serialization
- **Bootstrap 5.3**: Frontend styling
- **Chart.js**: Data visualization

### API Endpoints
- `GET /`: Main page with input form
- `POST /predict`: Prediction endpoint that processes form data

## 🎨 User Interface

The application features a modern, responsive design with:
- Clean Bootstrap-based styling
- Interactive probability visualizations
- Mobile-friendly responsive layout
- Clear error messaging
- Intuitive navigation

## 🛡️ Error Handling

The application includes comprehensive error handling for:
- Missing or invalid input data
- Model loading failures
- Unseen categorical values
- Missing model files

## 🚀 Deployment

For production deployment:

1. **Set Flask environment variables:**
   ```bash
   export FLASK_ENV=production
   ```

2. **Use a production WSGI server like Gunicorn:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 app:app
   ```

3. **Consider using a reverse proxy like Nginx**

## 🔍 Troubleshooting

**Common Issues:**

1. **"Model not found" error:**
   - Ensure all model files are present in the `models/` directory
   - Check that model files were generated by running the training script

2. **Import errors:**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Prediction errors:**
   - Ensure input values match the expected format
   - Check for any unseen categorical values

## 🤝 Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is available for educational and research purposes.

## 📞 Support

For support or questions about this application, please check the error messages displayed in the web interface or review the console output for detailed debugging information.
