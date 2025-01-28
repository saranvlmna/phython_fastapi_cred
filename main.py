from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db 
import crud
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    new_email: str 

@app.post("/user/")
def create_user(user:User, db: Session = Depends(get_db)):
    return crud.create_user(db, user.username, user.email, user.password)

@app.get("/user/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.get("/user/username/{username}")
def read_user_by_username(username: str, db: Session = Depends(get_db)):
    return crud.get_user_by_username(db, username)

@app.put("/user/{user_id}")
def update_user_email(user_id:int,email:UserUpdate,db: Session = Depends(get_db)):
    print("update",db, user_id, email.new_email)
    return crud.update_user_email(db, user_id, email.new_email)

@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)
    


    

    
