from flask import Blueprint

place_bp = Blueprint('place', __name__, url_prefix='/place')

@place_bp.route('/listup')
def place_listup():
    return "listup"

@place_bp.route('/getAddress')
def place_getAddress():
    return "getAddress"

@place_bp.route('/detail')
def place_detail():
    return "detail"