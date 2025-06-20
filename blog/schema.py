from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str

class BlogUpdate(BaseModel):
    title: str| None = None
    content: str| None = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str  

class UserResponse(BaseModel):
    username: str
    email: str

class UserResponseWithBlogs(BaseModel):
    username: str
    email: str
    blogs: list[Blog] = []

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    creator: UserResponse
