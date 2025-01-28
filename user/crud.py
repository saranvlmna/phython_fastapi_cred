from sqlalchemy.orm import Session
from model.user import User

# Create a new user
def create_user(db: Session, username: str, email: str, password: str):
    db_user = User(username=username, email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Read a user by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Read a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Update a user's email
def update_user_email(db: Session, user_id: int, new_email: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.email = new_email
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete a user by ID
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user