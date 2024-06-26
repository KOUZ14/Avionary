## Functional Requirements
1. Users must be able to create an account and sign in using email and password.
2. Users must be able to log out of their accounts.
3. Users should be able to search for flights based on origin, destination, and date.
4. Users should receive a confirmation of their booking via email.
5. Users should be able to book a flight from the search results.
6. Users should be able to book a hotel from the search results
7. Users are able to cancel their hotel booking
8. Users are able to check their flight status
9. Users should be able to view their past bookings.
10. Users should be able to cancel their booking


## Non-functional Requirements
1. The website should load quickly and respond to user actions within 2 seconds.


## Use Cases 
1. **Create Account with Email and Password** [Iskandar Daoud] (Login Page)
- **Summary:** Users can create a new account within the application by providing a valid email address and password.
- **Actors:** New Users, Application
- **Pre-conditions:** User is not currently registered in the application.
- **Trigger:** User clicks "Create New Account."
- **Primary Sequence:**
- 1. User enters their email address in "Email:" field.
- 2. User enters a password with at least one uppercase character and at least one special symbol in the "Password:" field.
- 3. User re-enters same password in "Confirm Password:" field.
- 4. User clicks "Create Account".
- 5. The application returns the user to the login screen.
- **Primary Postcondition:** The user account is successfully created, and the user is now registered in the application.
- **Alternate Sequence**
- 5. The provided email address is already associated with an existing account.
- 6. The application informs the user that the email address is already in use and prompts them to use a different one.
     
2. **User logout** [Iskandar Daoud]
- **Summary:** Users can securely log out of the application to protect their account and data.
- **Actors:** Registered Users and Application
- **Pre-conditions**: User has an account and is logged into the application.
- **Trigger**: User decides to log out of the application.
- **Primary Sequence**:
- 1. User navigates to the logout option within the application.
- 2. User clicks on the “logout” button.
- 3. User confirms the logout action.
- 4. The application invalidates the user's session, logging them out.
- 5. The application returns the user to the login screen
- **Primary Postcondition:** The user is successfully logged out, and their session is terminated.
- **Alternative Sequence:**
- 3. User cancels logout option.
- 4. User remains logged in and stays on the current screen.


3. Flight Search (Home Page) [Kousik]
- **Pre-condition:** User has logged into their account.
- **Trigger:** Search Button
- **Primary Sequence:**
1. User enters the origin, destination, and date in the search form.
2. User submits the search form.
3. System retrieves matching flights.
4. User views the list of matching flights.
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. User doesn't enter all or one of the following: origin, destination, and date in the search form.
2. User submits the search form.
3. System fails to retrieve matching flights.
4. User views an error message telling them what they forgot to enter.

4. Flight Booking Confirmation [Kousik]
- **Pre-condition:** User has logged into their account and booked a flight.
- **Trigger:** Book Button
- **Primary Sequence:**
1. System sends a confirmation email to the user.
2. User receives the confirmation email.
3. User verifies the booking details in the email.

3. Flight Booking (Flight_Results) [Kousik]
- **Pre-condition:** User has logged into their account and searched for flights.
- **Trigger:** Book Button
- **Primary Sequence:**
1. User selects a flight from the search results.
2. User confirms the flight details.
3. User completes the payment process.
4. System books the flight for the user.
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. User selects a flight from the search results.
2. User confirms the flight details.
3. User fails to complete the payment process.
4. User is met with a failed to process payment error.


6. Users should be able to book a hotel from the search results
- **Pre-Condition:** User is logged in 
- **Trigger:** User clicks on book hotel on notes menu bar
- **Primary Sequence:**
1.User is selects from different options of hotels
2.User confirms which hotel they want
3.User confirms the hotel they wish to stay in
4.User is prompted they have succfesully booked a hotel
- **Primary Postconditions:**
1. User has successfully booked a hotel

7. Users are able to cancel their hotel booking
- **Pre-Condition:** User is logged and has booked a hotel
- **Trigger:** User clicks on hotel status from menu bar
- **Primary Sequence:**
1.User selects hotel status
2.User is prompted with options on hotel status or cancel
3.User selects cancel hotel booking
4.User is prompted with hotel booking is succesufllly canceled
- **Primary Postconditions:**
1. User has canceled their hotel booking

8. Users are able to check their flight status
- **Pre-Condition:** User has booked a flight
- **Trigger:** User clicks flight status on notes menu bar
- **Primary Sequence:**
1.The user clicks on button “Check Flight Status”
2.User is prompted to enter their flight number
- **Primary Postconditions:**
  - Flight status is showed

 **Alternate Sequence:** The provided flight number is wrong
	1. User is prompted error, please input a correct flight number
     2. Returns them back to prompt of inputting flight number

9. Users are able to see their booking history
- **Pre-Condition:** User has booked a flight
- **Trigger:** Booking history button
- **Primary Sequence:**
1. User navigates to the booking history page.
2. System retrieves the user’s past bookings.
3. User views their past bookings.

10. Users are able to cancel their flights
- **Pre-Condition:** User has booked a flight
- **Trigger:** Flight cancel button
- **Primary Sequence:**
1. User selects a booking from their booking history.
2. User requests to cancel the booking.
3. System cancels the booking.
4. User receives a cancellation confirmation.
