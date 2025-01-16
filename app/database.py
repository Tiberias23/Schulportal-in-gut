import sqlite3

db = sqlite3.connect('app.db')

db.cursor().execute('CREATE TABLE IF NOT EXISTS users ()')