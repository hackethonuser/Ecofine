from flask import jsonify, request
from db import get_db_connection

def place_order():
    data = request.get_json()
    item_id = data['item_id']
    collector_id = data['collector_id']
    quantity = data['quantity']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO orders (item_id, collector_id, quantity) VALUES (%s, %s, %s)",
                   (item_id, collector_id, quantity))
    connection.commit()

    return jsonify({'success': True, 'message': 'Order placed successfully'})

def view_orders(collector_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT o.id, i.name, o.quantity, o.order_date, o.status
        FROM orders o
        JOIN items i ON o.item_id = i.id
        WHERE o.collector_id = %s
    """, (collector_id,))
    orders = cursor.fetchall()

    return jsonify({'orders': orders})
