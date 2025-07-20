from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'femcare_secret'
app.permanent_session_lifetime = timedelta(days=7)

users = {}  # Simple user store (for demo)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user in users and users[user] == pwd:
            session['user'] = user
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        users[user] = pwd
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if "user" in session:
        return f"Welcome {session['user']} to FemCare Dashboard!"
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

from models.prediction import predict_next_period
import datetime

@app.route('/tracker', methods=['GET', 'POST'])
def tracker():
    prediction = None
    logged_symptoms = []
    if request.method == 'POST':
        last_period = request.form['last_period']
        cycle_length = int(request.form['cycle_length'])
        symptoms = request.form.getlist('symptoms')
        logged_symptoms = ", ".join(symptoms)

        # Predict next period date
        prediction = predict_next_period(last_period, cycle_length)

    return render_template('tracker.html', prediction=prediction, logged_symptoms=logged_symptoms)

from models.risk_calculator import calculate_pcos_risk

@app.route('/risk', methods=['GET', 'POST'])
def risk():
    risk_level = None
    if request.method == 'POST':
        answers = {
            "irregular_periods": request.form['irregular_periods'],
            "hirsutism": request.form['hirsutism'],
            "acne": request.form['acne'],
            "weight_gain": request.form['weight_gain'],
            "fatigue": request.form['fatigue']
        }
        risk_level = calculate_pcos_risk(answers)
    return render_template('risk.html', risk_level=risk_level)
