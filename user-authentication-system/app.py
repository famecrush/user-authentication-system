from flask import Flask, render_template, request, redirect, url_for, flash, session
from passlib.hash import bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from forms import LoginForm  

import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key

# Define the User Registration Form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

# Define the User Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/')
def home():
    return render_template('login.html')

from flask import flash

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT username, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.verify(password, user[1]):
            session['username'] = username
            flash('Login successful', 'success')
            return redirect(url_for('profile'))  # Redirect to profile page
        else:
            flash('Login failed. Please check your username and password.', 'danger')

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Hash the password before storing it in the database
        hashed_password = bcrypt.using(rounds=12).hash(password)

        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/profile')
def profile():
    if 'username' in session:
        return f'Welcome, {session["username"]}! <a href="/logout" style="display: inline-block; padding: 10px 20px; background-color: #e74c3c; color: #fff; text-decoration: none; border: none; border-radius: 5px; cursor: pointer;">Logout</a>'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
