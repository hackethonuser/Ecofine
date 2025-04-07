from flask import Blueprint
from controllers.item_controller import add_item, view_items, browse_items

item_routes = Blueprint('item_routes', __name__)

item_routes.route('/api/add_item', methods=['POST'])(add_item)
item_routes.route('/api/view_items/<int:lister_id>', methods=['GET'])(view_items)
item_routes.route('/api/browse_items', methods=['GET'])(browse_items)
