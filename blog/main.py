from fastapi import FastAPI
from .database import Base, engine
from .routers import blog, user, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/", tags=["Root"])
def read_root():
    return{"message" :"Welcome to blog root"}

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)