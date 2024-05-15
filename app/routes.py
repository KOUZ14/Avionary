from flask import render_template, redirect, url_for, jsonify
from app import app, db
from app.models import User
import requests
from flask import render_template, redirect, url_for, request, flash
import json

# Loads the JSON object containing airport data
with open('app\IATA.json', 'r') as f:
    airports_data = json.load(f)

# function to search for airport codes
def search_airport_code(location_name):
    for airport in airports_data:
        print(airports_data[1])
        print(airports_data[airport])
        if airport['name'].lower() == location_name.lower():
            return airport['code']
    return None  




@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# flight search route
@app.route('/search_flights', methods=['POST','GET'])
def search_flights():
    origin_name = request.form.get('origin')
    destination_name = request.form.get('destination')
    depature_date = request.form.get('date')
    num_of_adults = 2
    print(origin_name)
    
    # Search for airport codes for origin and destination
    origin_code = search_airport_code(origin_name)
    destination_code = search_airport_code(destination_name)
    
    if origin_code and destination_code:
        # request to Amadeus API using the found airport codes
        api_key = 'your_amadeus_api_key'
        url = f'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={origin_code}&destinationLocationCode={destination_code}&departureDate={depature_date}&adults={num_of_adults}&apikey={api_key}'
        response = requests.get(url)
        
        if response.status_code == 200:
            flights = response.json()
            return render_template('flight_results.html', flights=flights)
        else:
            flash('Failed to retrieve flight information. Please try again later.', 'error')
            return redirect(url_for('search_flights'))
    else:
        flash('Invalid origin or destination location.', 'error')
        return redirect(url_for('search_flights'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Implementation of user registration
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implementation of user login
    pass

@app.route('/logout')
def logout():
    # Implementation of user logout
    pass
