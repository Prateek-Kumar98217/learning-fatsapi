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