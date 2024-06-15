from flask import Blueprint

chatlog_bp = Blueprint('chatlog', __name__, url_prefix='/chatlog')

@chatlog_bp.route('/listup')
def chatlog_listup():
    return "listup"

@chatlog_bp.route('/show')
def chatlog_show():
    return "show"

@chatlog_bp.route('/addInPallete')
def chatlog_addInPallete():
    return "addInPallete"

@chatlog_bp.route('/delete')
def chatlog_delete():
    return "delete"