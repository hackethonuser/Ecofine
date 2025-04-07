
import mysql.connector
import os

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'sql123'),  # Use environment variable for security
    )
    return connection


connection = get_db_connection()
cursor = connection.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS circular_economy""")
cursor.execute("""USE circular_economy""")
# Check if the user already exists before inserting
cursor.execute("SELECT * FROM users WHERE email = %s", ('lister@example.com',))
existing_user = cursor.fetchone()

if not existing_user:
    cursor.execute("SELECT * FROM users WHERE email = %s", ('lister@example.com',))
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO users (email, role) VALUES (%s, %s)", ('lister@example.com', 'lister'))
    print("User inserted")
else:
    print("User already exists")

# Create the items and orders tables if not already present
cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    quantity INT NOT NULL,
    image VARCHAR(255)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")

connection.commit()
connection.close()
