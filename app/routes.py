from flask import Blueprint, render_template, send_from_directory, jsonify
from .database import db

main = Blueprint('main', __name__)

@main.route('/api/login', methods=['POST'])
def api():
    return jsonify({}), 200, { 'Content-Type': 'application/json' }

@main.route('/<path:path>')
def home(path):
    return send_from_directory('templates', path)
