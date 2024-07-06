# MuscleMagic

MuscleMagic is a project management tool for gym administrators. It provides functionalities for managing gym memberships, sending fee reminders, and viewing user activities through an admin interface.

## Features

- Admin login and authentication
- Manage users (add, edit, delete)
- Send fee reminders manually
- Display user activities
- Store and fetch data from Firestore

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Database: Firestore

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Jay-2808/MuscleMagic.git
   cd MuscleMagic

2. Set up a virtual environment and install dependencies:
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt

3. Set up Firestore:
    1.Obtain the Firebase Admin SDK JSON file.
    2.Place the JSON file in the project directory.
    3.Update the path in your GetUserInfo.py file.



#Usage

1. Start the Flask application
    python app.py

2. Open your web browser and go to http://localhost:5000


#Future Enhancements
    Implement Bootstrap or React.js for frontend improvements.
    Add AI/ML features for advanced user analytics.
    Deploy the project on Vercel or AWS.


#Contact
For any questions or feedback, please reach out at jayachandirank28@gmail.com
