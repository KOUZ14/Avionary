## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. Users must be able to create an account and sign in using email and password.
2. Users must be able to log out of their accounts.
3. Users should be able to search for flights based on origin, destination, and date.
4. Users should receive a confirmation of their booking via email.
5. Users should be able to book a flight from the search results.
6. requirement
7. requirement
8. requirement
9. requirement
10. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. The website should load quickly and respond to user actions within 2 seconds.

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
1. Ut enim ad minim veniam, quis nostrum e
2. Et sequi incidunt
3. Quis aute iure reprehenderit
4. ...
5. ...
6. ...
7. ...
8. ...
9. ...
10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>

1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...

3. Flight Search
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

4. Flight Booking Confirmation
- **Pre-condition:** User has logged into their account and booked a flight.
- **Trigger:** Book Button
- **Primary Sequence:**
1. System sends a confirmation email to the user.
2. User receives the confirmation email.
3. User verifies the booking details in the email.

3. Flight Booking
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
