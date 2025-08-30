from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key= True, index= True)
    name = Column(String, nullable=False,index=True)
    email = Column(String, nullable=False,unique=True)
    password = Column(String,nullable=True)
    todos = relationship("Todo", back_populates="user", cascade="all, delete")
    todo = relationship("Todos", back_populates="user", cascade="all, delete")

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer,primary_key= True, index= True)
    title = Column(String, index= True)
    description = Column(String, nullable= True)
    status = Column(String, nullable= True)
    completed = Column(Boolean, default= False)
    # created_at = Column(String, default=datetime.datetime.now().strftime)
    user_id= Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    user = relationship("User", back_populates="todos")

class Todos(Base):
    __tablename__ = 'todo'

    id = Column(Integer,primary_key= True, index= True)
    title = Column(String, index= True,nullable=False)
    description = Column(String, nullable= True)
    status = Column(String, nullable= True)
    completed = Column(Boolean, default= False)
    user_id= Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="todo") 