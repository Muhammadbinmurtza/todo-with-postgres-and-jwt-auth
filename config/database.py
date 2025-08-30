from sqlalchemy import create_engine  # for making connection to the db
from sqlalchemy.orm import sessionmaker # creates the session in which it stores the data that is updated , deleted or anything or you can say it manages history
import os 
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

print(f"could not bind the engine and retrieve the db uri ")

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()