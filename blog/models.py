from sqlalchemy import Column, Integer, String
from .database import Base

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id= Column(Integer, primary_key = True, index = True)
    title = Column(String)
    content = Column(String)
    published = Column(Integer, default = 0)

    def __repr__(self) -> str:
        return f"<BlogPost(id={self.id}, title='{self.title}', published={self.published})>"
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"