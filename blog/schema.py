from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str
    published: bool = False

class BlogUpdate(BaseModel):
    title: str| None = None
    content: str| None = None
    published: bool| None = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str  

class UserResponse(BaseModel):
    username: str
    email: str