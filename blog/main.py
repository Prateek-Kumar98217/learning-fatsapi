from fastapi import FastAPI, Depends, status, Response, HTTPException
from .schema import Blog, BlogUpdate
from .database import engine, SessionLocal
from .models import Base, BlogPost
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return{"message" :"Welcome to blog root"}

@app.post("/blog",response_model=Blog, status_code=status.HTTP_201_CREATED)
def create_blog(request:Blog, db: Session = Depends(get_db)):
    new_blog = BlogPost(title = request.title, content = request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", response_model=list[Blog])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(BlogPost).all()
    return blogs

@app.get("/blog/{blog_id}", response_model=Blog)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogPost).get(blog_id)
    if blog:
        return blog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

@app.delete("/blog/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id:int, db: Session = Depends(get_db)):
    blog = db.query(BlogPost).get(blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return
    

@app.put("/blog/{blog_id}", response_model=Blog, status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id:int, request: BlogUpdate, db: Session = Depends(get_db)):
    blog = db.query(BlogPost).get(blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    data = request.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(blog, key, value)
    db.commit()
    db.refresh(blog)
    return blog
    