import sqlite3
from argon2.exceptions import VerifyMismatchError
db = sqlite3.connect('app.db')

def verify_user(username, password):
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return cursor.fetchone()
    except VerifyMismatchError:
        return False, "Invalid password"
# Create a table for users if it doesn't exist (Bei zweiteFremdsprache bitte nur 0 oder 1 eingeben (0 = Nein, 1 = Ja))
db.cursor().execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT,email TEXT, password TEXT)').close()
# Hier kann man einen SQLite Befehl ausführen.
db.cursor().execute("SELECT* FROM users").close()
# Commit the changes
db.commit()
