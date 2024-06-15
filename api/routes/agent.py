from flask import Blueprint

agent_bp = Blueprint('agent', __name__, url_prefix='/agent')

@agent_bp.route('/stt')
def agent_stt():
    return "stt"

@agent_bp.route('query')
def agent_query():
    return "query"

@agent_bp.route('addInPallete')
def agent_addInPallete():
    return "addInPallete"