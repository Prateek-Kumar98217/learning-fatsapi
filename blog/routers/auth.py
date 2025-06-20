from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.repositories import user
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from blog.authentication import create_access_token
from blog.schema import Token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
async def login(request:Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    print("Received login request:", request)
    user_data = user.authenticate_user(request.username, request.password, db)
    print("User data:", user_data)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"}
            )
    access_token = create_access_token(data={"sub": user_data.email})
    return Token(access_token=access_token, token_type="bearer")
    