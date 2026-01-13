# server/routes.py
from flask import Blueprint, jsonify
from models import User, Recipe

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify(message="Hello, world!")

@bp.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([u.username for u in users])
