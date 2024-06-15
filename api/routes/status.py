from flask import Blueprint

status_bp = Blueprint('status', __name__)

@status_bp.route('/')
def home():
    return "Working!"