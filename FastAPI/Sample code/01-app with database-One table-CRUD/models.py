from database import Base
from sqlalchemy import Column, Integer, String, Boolean
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email =  Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=False)
 

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title =  Column(String)
    description = Column(String)