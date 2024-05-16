from flask import render_template, redirect, url_for, request, flash, session, jsonify, Flask
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import os
from amadeus import Client, ResponseError
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)



amadeus = Client(
    client_id = os.getenv('API_KEY'),
    client_secret = os.getenv('API_SECRET')
)


@app.route('/', methods=['GET', 'POST'])
def index():
        db.create_all()
        return render_template('index.html')


@app.route('/search_flights', methods=['POST', 'GET'])
def search_flights():
    if 'username' in session:  
        origin_name = request.form.get('origin')
        destination_name = request.form.get('destination')
        departure_date = request.form.get('date')
        num_of_adults = 2 
        print(origin_name)

        if not origin_name or not destination_name:
            flash('Invalid origin or destination.', 'error')
            return redirect(url_for('index')) 

        #flight search using Amadeus API
        flights = amadeus.shopping.flight_offers_search.get(originLocationCode=origin_name,
            destinationLocationCode=destination_name,
            departureDate=departure_date,
            adults=num_of_adults,
            max=3)

        if not flights:
            flash('No flights found.', 'info')
            return redirect(url_for('index')) 

        return render_template('flight_results.html', flights=flights.data)
    else:
        flash('You need to login to search for flights')
        return redirect(url_for('login'))


@app.route('/book_flight', methods=['POST'])
def book_flight():
    # Extract booking details from form data
    flight_id = request.form.get('flight_id')
    name = request.form.get('name')

    # Perform booking process (this is just a placeholder)
    # You'll need to implement this based on your booking system
    # For example, you may need to call the Amadeus API to confirm the booking
    # Here, we'll just display a success message
    flash('Flight confirmed.', 'success')
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            flash('Login successful!', 'success')
            return render_template('index.html')
        else:
            flash('Invalid username or password. Please try again.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session variable
    session.pop('username', None)
    flash('Logout successful!', 'success')
    return render_template('index.html')

@app.route('/get_recent_flash_message')
def get_recent_flash_message():
    message = None
    if '_flashes' in session:
        message = session['_flashes'][-1][1]
    return jsonify({'message': message})