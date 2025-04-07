from flask import Blueprint
from controllers.order_controller import place_order, view_orders

order_routes = Blueprint('order_routes', __name__)

order_routes.route('/api/place_order', methods=['POST'])(place_order)
order_routes.route('/api/view_orders/<int:collector_id>', methods=['GET'])(view_orders)
