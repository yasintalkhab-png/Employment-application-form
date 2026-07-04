import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    national_id TEXT,
    birthdate TEXT,
    gender TEXT,
    email TEXT,
    phone TEXT,
    website TEXT,
    degree TEXT,
    newsletter INTEGER,
    description TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")
