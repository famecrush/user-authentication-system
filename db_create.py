# db_create.py

import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
