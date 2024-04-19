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
1. non-functional
2. non-functional

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
1. **Create Account with Email and Password** [Iskandar Daoud]
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
