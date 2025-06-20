from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import User
from ..schema import UserCreate
from ..utils import hash_password

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