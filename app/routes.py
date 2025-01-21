from flask import Blueprint, render_template, send_from_directory, jsonify, redirect
from .database import db

main = Blueprint('main', __name__)

# Läd die Login Seite (Funktioniert noch nicht)
@main.route('/api/login', methods=['POST'])
def api():
    return jsonify({}), 200, { 'Content-Type': 'application/json' }

# Automatischer Redirect zu index.html
@main.route('/')
def index():
    return redirect('/index.html')

# Läd die HTML Dateien aus dem templates Ordner
@main.route('/<path:path>')
def home(path):
    return send_from_directory('templates', path)
