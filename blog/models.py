from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id= Column(Integer, primary_key = True, index = True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")

    def __repr__(self) -> str:
        return f"<BlogPost(id={self.id}, title='{self.title}', published={self.published})>"
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    blogs = relationship("BlogPost", back_populates="creator")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"