from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

import crud  # Імпортуємо наш CRUD

app = FastAPI()

crud.create_table()

class User(BaseModel):
    id: int = None
    username: str
    email: str

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = crud.get_user_by_id(user_id)
    if user:
        return User(id=user[0], username=user[1], email=user[2])
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/users", response_model=List[User])
def read_users():
    users = crud.get_all_users()
    return [User(id=user[0], username=user[1], email=user[2]) for user in users]

@app.post("/create_user", response_model=User)
def create_user(user: User):
    crud.add_user(user.username, user.email)
    return user
