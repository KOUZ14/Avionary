from flask import render_template, redirect, url_for, request, flash, session, jsonify
from app import app, db
from app.models import User
import requests
import json
import os
from amadeus import Client, ResponseError
from dotenv import load_dotenv

load_dotenv()

amadeus = Client(
    client_id = os.getenv('API_KEY'),
    client_secret = os.getenv('API_SECRET')
)


@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('index.html')


@app.route('/search_flights', methods=['POST', 'GET'])
def search_flights():
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
        # Handle form submission (process signup data)
        email = request.form['email']
        password = request.form['password']
        # Your signup logic goes here

        # Redirect to the appropriate page after signup (e.g., login page)
        return redirect(url_for('login'))

    # Render the signup form template for GET requests
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Your login implementation goes here
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session variable
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/get_recent_flash_message')
def get_recent_flash_message():
    message = None
    if '_flashes' in session:
        message = session['_flashes'][-1][1]
    return jsonify({'message': message})