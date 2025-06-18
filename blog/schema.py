from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str
    published: bool = False

class BlogUpdate(BaseModel):
    title: str| None = None
    content: str| None = None
    published: bool| None = None
