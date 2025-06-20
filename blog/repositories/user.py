from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import User
from ..schema import UserCreate
from ..utils import hash_password
from ..utils import verify_password
from fastapi import Depends
from ..database import get_db

def create_user(request: UserCreate, db: Session):
    hashed_password = hash_password(request.password)
    new_user = User(username=request.username, email=request.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(user_id: int, db: Session):
    user = db.query(User).get(user_id)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

def get_user_by_username(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_username(email, db)
    print("Authenticating user:", user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    return user