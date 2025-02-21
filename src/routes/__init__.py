from flask import Blueprint

from controllers import get_items, update_item

api_routes = Blueprint('api', __name__)

api_routes.add_url_rule('/items', view_func=get_items, methods=['GET'])
api_routes.add_url_rule('/item/<string:item_id>', view_func=update_item, methods=['PUT'])