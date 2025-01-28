from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import get_db 
import user.crud as crud
from pydantic import BaseModel
from fastapi import  Depends

router = APIRouter(
    prefix='/user',
    tags=['user']
)

class User(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    new_email: str 

@router.post("/")
def create_user(user:User, db: Session = Depends(get_db)):
    return crud.create_user(db, user.username, user.email, user.password)

@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@router.get("/username/{username}")
def read_user_by_username(username: str, db: Session = Depends(get_db)):
    return crud.get_user_by_username(db, username)

@router.put("/{user_id}")
def update_user_email(user_id:int,email:UserUpdate,db: Session = Depends(get_db)):
    print("update",db, user_id, email.new_email)
    return crud.update_user_email(db, user_id, email.new_email)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)