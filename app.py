'''
from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",  # Replace with your MySQL host
        user="root",       # Replace with your MySQL username
        password="sql123",       # Replace with your MySQL password
        database="circular_marketplace" # Replace with your database name
    )

# Home page (Login form)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check login credentials in MySQL database
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        # If user exists and password matches
        if user and user[2] == password:  # Assuming the password is stored in user[2]
            return redirect(url_for('lister_dashboard'))
        else:
            return "Invalid credentials, please try again."

    return render_template('login.html')

# Lister dashboard (after successful login)
@app.route('/lister_dashboard')
def lister_dashboard():
    return "Welcome to Lister Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
'''