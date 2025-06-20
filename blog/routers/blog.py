from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.schema import Blog, BlogUpdate, BlogResponse
from blog.repositories import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.post("/",response_model=Blog, status_code=status.HTTP_201_CREATED, tags=["Blog"])
def create_blog(request:Blog, db: Session = Depends(get_db)):
    return blog.create_blog(request, db)

@router.get("/", response_model=list[BlogResponse], tags=["Blog"])
def get_blogs(db: Session = Depends(get_db)):
    return blog.get_blogs_all(db)

@router.get("/{blog_id}", response_model=BlogResponse, tags=["Blog"])
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return blog.get_blog(blog_id, db)

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
def delete_blog(blog_id:int, db: Session = Depends(get_db)):
    return blog.delete_blog(blog_id, db)

@router.put("/{blog_id}", response_model=BlogResponse, status_code=status.HTTP_202_ACCEPTED, tags=["Blog"])
def update_blog(blog_id:int, request: BlogUpdate, db: Session = Depends(get_db)):
    return blog.update_blog(blog_id, request, db)
