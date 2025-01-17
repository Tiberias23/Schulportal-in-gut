import sqlite3

db = sqlite3.connect('app.db')

# Create a table for users if it doesn't exist
db.cursor().execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)').close()
# Hier kann man einen SQLite Befehl ausführen.
db.cursor().execute("SELECT * FROM users").close()
# Commit the changes
db.commit()
