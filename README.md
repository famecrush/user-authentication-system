# User Authentication System
This is a simple User Authentication System project built using Flask, SQLite, and Bcrypt for password hashing. It includes user registration, login, session management, and secure password hashing. The system is designed for educational purposes to demonstrate the fundamentals of user authentication.

## Technologies Used
Programming Language: Python
Web Framework: Flask
Database: SQLite
Password Hashing: Bcrypt
HTML/CSS for Frontend

## Project Structure
app.py: Main application file.
templates/: HTML templates.
login.html: Login form.
register.html: Registration form.
static/: CSS and other static files.
style.css: CSS stylesheet for styling the HTML templates.
db.sqlite: SQLite database.
requirements.txt: List of project dependencies.
## Setup and Run
Clone the repository:
'''
git clone https://github.com/yourusername/user-authentication-system.git
cd user-authentication-system
'''
Create a virtual environment (optional but recommended):
''''
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
''''
Install project dependencies:
''''
pip install -r requirements.txt
''''
Run the application:
''''
python app.py
''''

Access the application in your web browser at http://localhost:5000.

## Usage
Visit the home page and choose between "Login" and "Register."
Register: Sign up with a username and password. Passwords are securely hashed before storing in the database.
Login: Registered users can log in using their username and password. Session management keeps users logged in until they log out.
Logout: To log out, click the "Logout" link.
