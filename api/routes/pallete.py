from flask import Blueprint

pallete_bp = Blueprint('pallete', __name__, url_prefix='/pallete')

@pallete_bp.route('/listup')
def pallete_listup():
    return "listup"

@pallete_bp.route('/create')
def pallete_create():
    return "create"

@pallete_bp.route('/delete')
def pallete_delete():
    return "delete"

@pallete_bp.route('/show')
def pallete_show():
    return "show"

@pallete_bp.route('/placeAdd')
def pallete_placeAdd():
    return "placeAdd"

@pallete_bp.route('/placeDelete')
def pallete_placeDelete():
    return "placeDelete"

@pallete_bp.route('/pathfindAdd')
def pallete_pathfindAdd():
    return "pathfindAdd"

@pallete_bp.route('/pathfindDelete')
def pallete_pathfindDelete():
    return "pathfindDelete"