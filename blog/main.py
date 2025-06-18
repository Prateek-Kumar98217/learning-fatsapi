from fastapi import FastAPI
from .schema import Blog
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return{"messade" :"Welcome to blog root"}

@app.post("/blog")
def create_blog(blog:Blog):
    pass