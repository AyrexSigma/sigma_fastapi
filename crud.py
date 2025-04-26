import sqlite3
from typing import List, Optional

conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()

def add_user(username: str, email: str):
    c.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
    conn.commit()

def get_user_by_id(user_id: int) -> Optional[tuple]:
    c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    return c.fetchone()

def get_all_users() -> List[tuple]:
    c.execute('SELECT * FROM users')
    return c.fetchall()
