from flask import Blueprint
from controllers.user_controller import login

user_routes = Blueprint('user_routes', __name__)

user_routes.route('/api/login', methods=['POST'])(login)
