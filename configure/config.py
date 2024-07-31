from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from fastapi import FastAPI,APIRouter

Base=declarative_base()
DATABASE_URL="postgresql://postgres:12345@localhost/taskschool"


engine=create_engine(DATABASE_URL)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# app=FastAPI()

def get_db():
    
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()