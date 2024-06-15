from flask import Blueprint

pathfind_bp = Blueprint('pathfind', __name__, url_prefix='/pathfind')

@pathfind_bp.route('/find')
def pathfind_find():
    return "find"

@pathfind_bp.route('/show')
def pathfind_show():
    return "show"