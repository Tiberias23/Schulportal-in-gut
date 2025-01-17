from flask import Blueprint, render_template, send_from_directory, jsonify
from .database import db

main = Blueprint('main', __name__)

# Läd die Login Seite (Funktioniert noch nicht)
@main.route('/api/login', methods=['POST'])
def api():
    return jsonify({}), 200, { 'Content-Type': 'application/json' }

# Läd die HTML Dateien aus dem templates Ordner
@main.route('/<path:path>')
def home(path):
    return send_from_directory('templates', path)
