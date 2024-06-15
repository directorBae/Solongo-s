from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register')
def auth_register():
    return "Register"

@auth_bp.route('/login')
def auth_login():
    return "Login"

@auth_bp.route('/logout')
def auth_logout():
    return "Logout"

@auth_bp.route('/edit')
def auth_edit():
    return "Edit"