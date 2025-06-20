from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.schema import UserCreate, UserResponse, UserResponseWithBlogs
from blog.repositories import user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["User"])
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get("/{user_id}", response_model=UserResponseWithBlogs, tags=["User"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user.get_user(user_id, db)