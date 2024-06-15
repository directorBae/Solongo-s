from flask import Blueprint

purchase_bp = Blueprint('purchase', __name__, url_prefix='/purchase')

@purchase_bp.route('/listup')
def purchase_listup():
    return "listup"

@purchase_bp.route('/charge')
def purchase_charge():
    return "charge"