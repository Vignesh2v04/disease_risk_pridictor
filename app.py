from flask import Flask, render_template, request, redirect, url_for, session,flash
from database import init_db, register_user, validate_user
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
import sqlite3
import os,secrets
import pandas as pd
#from flask_frozen import Freezer






app = Flask(__name__)
#freezer = Freezer(app)
app.secret_key = secrets.token_hex(16)  
app.secret_key = os.getenv("SECRET_KEY", secrets.token_hex(16))


init_db()
users = {}


@app.route('/')
def index():
    """Home page route."""
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration: Allows new users to register."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))

        users[username] = password
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login: Validates credentials and starts a session."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')




@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))



@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

try:
    diabetes_model = joblib.load('diabetes_model.pkl')
    cvd_model = joblib.load('cvd_model.pkl')
    print("✅ Models loaded successfully!")
except Exception as e:
    print(f"❌ Error loading models: {str(e)}")
    diabetes_model = None
    cvd_model = None




@app.route('/cvd_form')
def cvd_form():
    return render_template('cvd_form.html')

@app.route('/diabetes_form')
def diabetes_form():
    return render_template('diabetes_form.html')


@app.route('/predict_cvd', methods=['POST'])
def predict_cvd():
    if not cvd_model:
        return render_template('result.html', prediction="Error: CVD model not loaded", model_type="CVD")
    
    try:
        
        patient_data = {
            'age': float(request.form['age']),
            'gender': int(request.form['gender']), 
            'ap_hi': float(request.form['ap_hi']),
            'ap_lo': float(request.form['ap_lo']),
            'cholesterol': float(request.form['cholesterol']),
            'smoke': int(request.form['smoke']),   
            'weight': float(request.form['weight'])
        }

        
        input_df = pd.DataFrame([patient_data])[cvd_model['features']['cvd']]
        scaled_data = cvd_model['scaler_cvd'].transform(input_df)
        risk_prob = cvd_model['cvd_model'].predict_proba(scaled_data)[0][1]

       
        risk_level = "🚨 High Risk" if risk_prob > 0.7 else "✅ Low Risk"
        result = f"""
        <h3>CVD Risk: <strong>{risk_prob:.1%}</strong></h3>
        <p class="risk-level { 'high-risk' if risk_prob > 0.7 else 'low-risk' }">{risk_level}</p>
        <h4>Recommendations:</h4>
        <ul>
            <li>{"Consult a cardiologist immediately" if risk_prob > 0.7 else "Maintain healthy lifestyle"}</li>
            <li>{"Get an ECG test" if risk_prob > 0.7 else "Regular BP monitoring"}</li>
        </ul>
        """
        return render_template('result.html', prediction=result, model_type="CVD")

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}", model_type="CVD")


@app.route('/predict', methods=['POST'])
def predict():
    if diabetes_model is None:
        return render_template('error.html', 
                            message="Diabetes model not loaded. Please try again later.")
    
    try:
       
        patient_data = {
            'Pregnancies': float(request.form['Pregnancies']),
            'Glucose': float(request.form['Glucose']),
            'BloodPressure': float(request.form['BloodPressure']),
            'SkinThickness': float(request.form['SkinThickness']),
            'Insulin': float(request.form['Insulin']),
            'BMI': float(request.form['BMI']),
            'DiabetesPedigreeFunction': float(request.form['DiabetesPedigreeFunction']),
            'Age': float(request.form['Age'])
        }

        features = pd.DataFrame([patient_data])[diabetes_model['features']['diabetes']]
        scaled_features = diabetes_model['scaler_diabetes'].transform(features)
        
        
        probability = diabetes_model['diabetes_model'].predict_proba(scaled_features)[0][1]
        prediction = "Diabetic" if probability > 0.5 else "Not Diabetic"
        
        
        if probability > 0.7:
            risk_level = "High"
            recommendations = [
                "Immediate HbA1c test recommended",
                "Consult an endocrinologist",
                "Start lifestyle intervention",
                "Monitor glucose levels daily"
            ]
        elif probability > 0.4:
            risk_level = "Moderate"
            recommendations = [
                "Schedule glucose tolerance test",
                "Improve diet and exercise",
                "Monitor symptoms"
            ]
        else:
            risk_level = "Low"
            recommendations = [
                "Maintain healthy lifestyle",
                "Annual checkup recommended"
            ]

        
        result = {
            'probability': f"{probability:.1%}",
            'prediction': prediction,
            'risk_level': risk_level,
            'key_indicators': {
                'Glucose': patient_data['Glucose'],
                'BMI': patient_data['BMI'],
                'Age': patient_data['Age']
            },
            'recommendations': recommendations,
            'all_data': patient_data
        }

        return render_template('dibatic_result.html', result=result)

    except KeyError as e:
        return render_template('error.html',
                            message=f"Missing required field: {str(e)}")
    except ValueError as e:
        return render_template('error.html',
                            message=f"Invalid input value: {str(e)}")
    except Exception as e:
        return render_template('error.html',
                            message=f"Prediction error: {str(e)}")



if __name__ == '__main__':
   # freezer.freeze()
    app.run(debug=True)
    
