
import pymysql
pymysql.install_as_MySQLdb()  # This line is needed for PyMySQL to work with Flask-SQLAlchemy

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import os

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:sql123@localhost/circular_economy'  # Use mysql-connector
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Use environment variable for security

# Initialize SQLAlchemy and JWT
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Create a user model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

# Create Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=True)

# User login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    role = data['role']

    user = User.query.filter_by(email=email).first()

    if user and user.role == role:
        access_token = create_access_token(identity=email)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Invalid credentials"}), 401

# Add item endpoint
@app.route('/api/add_item', methods=['POST'])
@jwt_required()
def add_item():
    data = request.get_json()
    name = data['name']
    description = data['description']
    quantity = data['quantity']
    image = data['image']

    new_item = Item(name=name, description=description, quantity=quantity, image=image)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added successfully!"}), 200

# View items endpoint
@app.route('/api/view_items', methods=['GET'])
@jwt_required()
def view_items():
    items = Item.query.all()
    items_list = [{"id": item.id, "name": item.name, "description": item.description, "quantity": item.quantity, "image": item.image} for item in items]
    return jsonify(items_list), 200

# Initialize the database (run this once)
# @app.before_first_request  # Commented out temporarily for debugging
def create_tables():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return "Welcome to the Circular Economy Marketplace API!"

@app.route('/')
def index():
    return "Welcome to the Circular Economy Marketplace API!"
