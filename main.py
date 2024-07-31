# import uvicorn

# from configure.config import *
# from app.api.student import router
# from app.api.teacher.router import *
# from app.api.marklist.router import *

# app=FastAPI()

# app.include_router(student.router, prefix="/api")

# Base.metadata.create_all(bind=engine)

# if __name__=="__main__":
#     uvicorn.run("main:app",port=8000,reload=True) 


from fastapi import FastAPI
import uvicorn
from configure.config import engine, Base
from app.api.student.router import *  
from app.api.teacher.router import *
from app.api.marklist.router import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Include routers
app.include_router(router1)
app.include_router(router2)
app.include_router(router3)

# Create database tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Entry point
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
