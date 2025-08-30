from fastapi import Depends, APIRouter, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from config.database import get_db
from models.todo_model import User
from validations.validation import UserCreate
from utils.utils_helper import create_access_token
from validations.validation import LoginUser

user_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

def verify_password(plain_password: str, hashed_password: str) :
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@user_router.post("/register")
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    try:
        user_hash_password = hash_password(user.password)
        print("user plain password :", user.password)
        print("user hash password :", user_hash_password)
        db_user = User(name=user.name,email= user.email,password= user_hash_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        valid_user = db.query(User).filter(User.email == user.email).first()
        token = create_access_token(data={"email": db_user.email, "name":db_user.name,"user_id": valid_user.id})
        return {
            "data" : {
                "name": db_user.name,
                "email": db_user.email,
                "token": token
            },
            "message" :"user registered and logged in successfully",
            "status" : "success"
        }
    except Exception as e:
        print(f"an exception occured, {e}")
        return{
            "data" : None,
            "message" : str(e)
        }



@user_router.post("/login")
def login_user(user : LoginUser, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.email == user.email).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="User not found")
        is_valid_password = verify_password(user.password, db_user.password)
        if not is_valid_password:
            raise HTTPException(status_code=400, detail="Invalid  password")
        # if db_user.email != user.email:
        #     raise HTTPException(status_code=400, detail="Invalid email")
        token = create_access_token(data={"email": db_user.email, "name":db_user.name," user_id": db_user.id})
        user_data = {
            "email": db_user.email,
            "name": db_user.name,
            "token": token
        }
        return{
            "data": user_data,
            "message" : "user logged in successfully",
            "status" : "success"
        }
    except Exception as e:
        print(f"an exception occured, {e}")
        return {
        "data": None,
        "message": str(e),
        "status": "error"
    }
