from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import User
import requests
import json

# Loads the JSON object containing airport data
with open('app/IATA.json', 'r') as f:
    airports_data = json.load(f)

# Function to search for airport codes
def search_airport_code(location_name):
    for airport in airports_data:
        if airport['name'].lower() == location_name.lower():
            return airport['code']
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process flight search form data here
        origin_name = request.form.get('origin')
        destination_name = request.form.get('destination')
        departure_date = request.form.get('date')
        num_of_adults = 2

        # Search for airport codes for origin and destination
        origin_code = search_airport_code(origin_name)
        destination_code = search_airport_code(destination_name)

        if origin_code and destination_code:
            # Request to Amadeus API using the found airport codes
            api_key = 'your_amadeus_api_key'
            url = f'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={origin_code}&destinationLocationCode={destination_code}&departureDate={departure_date}&adults={num_of_adults}&apikey={api_key}'
            response = requests.get(url)

            if response.status_code == 200:
                flights = response.json()
                return render_template('flight_results.html', flights=flights)
            else:
                flash('Failed to retrieve flight information. Please try again later.', 'error')
                return redirect(url_for('index'))
        else:
            flash('Invalid origin or destination location.', 'error')
            return redirect(url_for('index'))
    else:
        return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle form submission (process signup data)
        email = request.form['email']
        password = request.form['password']
        # Your signup logic goes here

        # Redirect to the index route after successful signup
        return redirect(url_for('index'))

    # Render the signup form template for GET requests
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Your login implementation goes here
    # Assuming login is successful, redirect the user to the index route
    return redirect(url_for('index'))
