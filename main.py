from fastapi import FastAPI
from dotenv import load_dotenv
import os 
from routes import todo_routes,user_routes
load_dotenv()
#create tables in database
# Base.metadata.create_all(bind=engine)

app= FastAPI()



app.include_router(user_routes.user_router, prefix="/users", tags=["User"])

app.include_router(todo_routes.todo_router, prefix="/todos", tags=["Todo"])