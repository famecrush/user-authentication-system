# User Authentication System
This is a simple User Authentication System project built using Flask, SQLite, and Bcrypt for password hashing. It includes user registration, login, session management, and secure password hashing. The system is designed for educational purposes to demonstrate the fundamentals of user authentication.

## Technologies Used
* Programming Language: Python
* Web Framework: Flask
* Database: SQLite
* Password Hashing: Bcrypt
* HTML/CSS for Frontend

## Project Structure
* app.py: Main application file.
* templates/: HTML templates.
  * login.html: Login form.
  * register.html: Registration form.
  * logout.html: Logout form.
* static/: CSS and other static files.
  * style.css: CSS stylesheet for styling the HTML templates.
* db.sqlite: SQLite database.
* requirements.txt: List of project dependencies.

## Setup and Run
Clone the repository:
````
git clone https://github.com/famecrush/user-authentication-system.git
cd user-authentication-system
````
Create a virtual environment (optional but recommended):
````
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
````
Install project dependencies:
````
pip3 install -r requirement.txt
````
Create database:
````
python3 db_create.py
````
Run the application:
````
python3 app.py
````

Access the application in your web browser at http://localhost:5000/login.

## Usage
* Visit the home page and choose between "Login" and "Register."
* Register: Sign up with a username and password. Passwords are securely hashed before storing in the database.
* Login: Registered users can log in using their username and password. Session management keeps users logged in until they log out.
* Logout: To log out, click the "Logout" button.

## Accessing the Database
You can access the SQLite database used in this User Authentication System for debugging and analysis. Below are some commands to interact with the database using the SQLite command-line utility:

### Prerequisites
SQLite Command-Line Utility

### Steps to Access the Database

Open your terminal or command prompt.

Navigate to the directory where your SQLite database file (db.sqlite) is located.

To open the SQLite shell, run the following command:
````
sqlite3 db.sqlite
````
On some systems, you may need to provide the full path to the database file.

You will now be in the SQLite shell, where you can execute SQL commands to interact with the database. Here are some common commands:

To list all tables in the database:
````
.tables
````
To view the structure of a specific table, replace your_table_name with the table name:
````
.schema your_table_name
````
To execute SQL queries, use standard SQL commands. For example, to retrieve all records from the users table:
````
SELECT * FROM users;
````
To exit the SQLite shell, type ````.exit```` or press Ctrl + D.

These commands allow you to explore the database and retrieve information as needed. 

The password hashes in the password column are securely hashed using the Bcrypt hashing algorithm.

## Cracking Password Hashes with John the Ripper

### Requirements
John the Ripper

### Steps to Crack Password Hashes
You can use John the Ripper to crack the password hashes. If you haven't already obtained the password hashes you want to crack, you can find them in the db.sqlite database in the users table.

Use John the Ripper with the appropriate options to crack the hashes. For example, to crack the hashes stored in a file named bcrypt-hashes.txt using a wordlist file named passwords.txt, run the following command:
````
john --format=bcrypt --wordlist=passwords.txt bcrypt-hashes.txt
````
Replace bcrypt-hashes.txt with the file containing the password hashes and passwords.txt with your password list.

John the Ripper will attempt to crack the password hashes. If successful, it will display the cracked passwords.

When you try to crack the password for second time John the Ripper will not show cracked password directly it store it in a session.

John the Ripper uses a session file to keep track of its progress during password cracking. If the session file is still present from the previous run, John may think it has already completed the cracking process. To start a new cracking session, you can either delete the session file or use the --show option:
````
john --show bcrypt-hashes.txt
````
## Features Contributing
Contributions are welcome! Feel free to open issues and pull requests.

## Contact
My LinkedIn :- https://www.linkedin.com/in/mahipal-choudhary-b8181823a/

