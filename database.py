import sqlite3

def get_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    conn = get_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        major TEXT NOT NULL,
        gpa REAL NOT NULL,
        enrollment_year INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
def dict_from_row(row):
    """Convert sqlite3.Row to dictionary."""
    return dict(row) if row else None