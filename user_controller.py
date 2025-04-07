from flask import jsonify, request
from db import get_db_connection

def login():
    data = request.get_json()
    email = data['email']
    role = data['role']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND role = %s", (email, role))
    user = cursor.fetchone()

    if user:
        return jsonify({'success': True, 'user_id': user[0], 'role': user[2]})
    else:
        return jsonify({'success': False, 'message': 'Invalid email or role'}), 400
