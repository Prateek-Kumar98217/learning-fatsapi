from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schema import Blog
from ..models import BlogPost

def create_blog(request: Blog, db: Session):
    new_blog = BlogPost(title = request.title, content = request.content, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blogs_all(db: Session):
    blogs = db.query(BlogPost).all()
    return blogs

def get_blog(blog_id: int, db: Session):
    blog = db.query(BlogPost).get(blog_id)
    if blog:
        return blog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

def update_blog(blog_id: int, request: Blog, db: Session):
    blog = db.query(BlogPost).get(blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    data = request.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(blog, key, value)
    
    db.commit()
    db.refresh(blog)
    return blog

def delete_blog(blog_id: int, db: Session):
    blog = db.query(BlogPost).get(blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    db.delete(blog)
    db.commit()
    return None