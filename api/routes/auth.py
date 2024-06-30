from flask import Blueprint, jsonify, request
import sqlite3
from api.db import get_db
from auth import generate_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def auth_register():
    data = request.get_json()
    uid = data['uid']
    nickname = data['nickname']
    upw = data['upw']
    country = data['country']
    
    db = get_db('userDB.db')
    try:
        db.execute('INSERT INTO user (uid, upw, nickname, country) VALUES (?, ?, ?, ?)', (uid, upw, nickname, country))
        db.commit()
    except sqlite3.IntegrityError:
        return jsonify(message='User ID already exists'), 400
    return jsonify(message='User registered successfully'), 201

@auth_bp.route('/login', methods=['POST'])
def auth_login():
    data = request.get_json()
    username = data['uid']
    password = data['upw']
    
    db = get_db('userDB.db')
    user = db.execute('SELECT * FROM user WHERE uid = ? AND upw = ?', (username, password)).fetchone()
    print("login")
    if user is None:
        return jsonify(message='Login failed'), 401
    token = generate_token(user[0])
    return jsonify(message='Login successful', token=token)

@auth_bp.route('/logout', methods=['GET'])
def auth_logout():
    print("logged out!")
    return jsonify(message='Logout successful')

@auth_bp.route('/edit', methods=['GET'])
def auth_edit():
    return "Edit"