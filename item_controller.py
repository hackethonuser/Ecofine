from flask import jsonify, request
from db import get_db_connection

def add_item():
    data = request.get_json()
    name = data['name']
    description = data['description']
    quantity = data['quantity']
    image = data['image']  # Assume image is a URL or path to the file

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items (name, description, quantity, image) VALUES (%s, %s, %s, %s)",
                   (name, description, quantity, image))
    connection.commit()

    return jsonify({'success': True})

def view_items(lister_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items WHERE user_id = %s", (lister_id,))
    items = cursor.fetchall()

    return jsonify({'items': items})

def browse_items():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    return jsonify({'items': items})
