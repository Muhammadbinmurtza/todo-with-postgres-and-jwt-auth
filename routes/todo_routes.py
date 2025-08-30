from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from validations.validation import TodoCreate
from sqlalchemy.orm import Session
from models.todo_model import Todo
from utils.utils_helper import verify_token

todo_router = APIRouter()

@todo_router.post("/create")
def create_todo(todo:TodoCreate,user = Depends(verify_token),db:Session=Depends(get_db)):
    try:
        # user = verify_token(todo.token)
        # print("user from token:",user)
        # if not user:
        #     raise HTTPException(status_code=401, detail="Invalid token")
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        user_id = user.get("user_id")
        db_todo = Todo(title=todo.title,description= todo.description,completed= todo.completed,user_id=user_id)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return {
            "data" : db_todo,
            "message" : "TODO created successfully",
            "status" : "success"
        }
    except Exception as e:
        print(f"an exception occured, {e}")
        return{
            "data" : None,
            "message" : str(e)
        }
    
@todo_router.get("/")
def get_todos( db: Session = Depends(get_db)):
    try:
        todos =  db.query(Todo).all()
        return{
            "data" : todos,
            "message" : "Todos retrieved successfully",
            "status" : "success"
        }
    except Exception as e:
        print(f"an exception occured, {e}")
        return{
            "data" : None,
            "message" : str(e)
        }


@todo_router.get("/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        return{
            "data" : todo,
            "message" : "Todo retrieved successfully",
            "status" : "success"
        }
    except Exception as e:
        print(f"an exception occured, {e}")
        return{
            "data" : None,
            "message" : str(e)
        }