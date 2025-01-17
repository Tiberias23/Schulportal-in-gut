import sqlite3

db = sqlite3.connect('app.db')

# Create a table for users if it doesn't exist (Bei zweiteFremdsprache bitte nur 0 oder 1 eingeben (0 = Nein, 1 = Ja))
db.cursor().execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT,email TEXT, password TEXT)').close()
# Hier kann man einen SQLite Befehl ausführen.
db.cursor().execute("").close()
# Commit the changes
db.commit()
