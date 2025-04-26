from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)''')
conn.commit()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = c.fetchone()
    if user:
        return User(id=user[0], username=user[1], email=user[2])
    return {"message": "User not found"}

@app.get("/users")
def get_users():
    c.execute("SELECT *  FROM users")
    all_users = c.fetchall()
    return [{"id": user[0], "username": user[1], "email": user[2]} for user in all_users]

@app.post("/create_user")
def create_user(user: User):
    c.execute("INSERT INTO users (username, email) VALUES (?, ?)", (user.username, user.email))
    conn.commit()
    return user