from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text  # Import text to wrap raw SQL queries
from database import get_db  # Import the get_db dependency
import crud

app = FastAPI()

@app.post("/users/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return crud.create_user(db, username, email, password)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.get("/users/username/{username}")
def read_user_by_username(username: str, db: Session = Depends(get_db)):
    return crud.get_user_by_username(db, username)

@app.put("/users/{user_id}")
def update_user_email(user_id: int, new_email: str, db: Session = Depends(get_db)):
    return crud.update_user_email(db, user_id, new_email)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)
    


    

    
