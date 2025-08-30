from pydantic import BaseModel, Field
from typing import Annotated

class TodoCreate(BaseModel):
    title : str
    description : str = None
    completed : bool = False
    



class LoginUser(BaseModel):
    email: str 
    password: str

class UserCreate(BaseModel):
    name : str
    email : Annotated[str, Field(pattern=r'^\S+@\S+$')] 
    password : Annotated[str, Field(min_length=6,max_length=17)] 

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class TodoResponse(TodoCreate):
    id : int 
    class Config:
        orm_mode = True