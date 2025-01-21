import sqlite3
import argon2

db = sqlite3.connect('app.db')

def verify_user(username, password):
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return cursor.fetchone()
    except argon2.VerifyMismatchError:
        return False, "Invalid password"


# Create a table for users if it doesn't exist (Bei zweiteFremdsprache bitte nur 0 oder 1 eingeben (0 = Nein, 1 = Ja))
db.cursor().execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT,email TEXT, password TEXT)').close()
# Modify the stuff in quotes to us SQL commands 
# if you want to drop the table you have to run the program tow times and befor the second time you have to delete the "drop table" command orherewise it will delete the new generatet table
db.cursor().execute("SELECT* FROM users").close()
# Commit the changes
db.commit()
