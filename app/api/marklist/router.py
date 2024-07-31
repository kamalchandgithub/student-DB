from app.api.marklist.controller import *
# from app.api.task.service import *
from fastapi import FastAPI,Depends,APIRouter



router1=APIRouter(tags=["MARKLIST"])

@router1.post("/create/marklist")
def create_marklist(marklist:create_marklist_schema,db:Session=Depends(get_db)):
    return create_marklist_controller(marklist,db)

@router1.get("/get/marklist")
def get_marklist(marklist_id:int,db:Session=Depends(get_db)):
    return get_marklist_controller(marklist_id,db)

@router1.put("/update/marklist")
def update_marklist(update_marklist : update_marklist_schema, update_marklist_id : int, db:Session=Depends(get_db) ):
    return update_marklist_controller(update_marklist,update_marklist_id,db)

@router1.delete("/delete/marklist")
def delete_marklist(delete_marklist_id : int,db:Session=Depends(get_db)):
    return delete_marklist_controller(delete_marklist_id,db)





# @app.get("/get/students_by_class")
# def get_students_by_class_router(fetch_by_class:str,fetch_by_standard : int, db:Session=Depends(get_db)):
#     return get_students_by_class_controller(fetch_by_class,fetch_by_standard,db)

# @app.get("/get/students_by_teacher_id")
# def get_students_by_teacher_id_router(fetch_by_teacher_id:int,db:Session=Depends(get_db)):
#     return get_students_by_teacher_id_controller(fetch_by_teacher_id,db)

# @app.get("/get/marklist_by_exam")
# def get_marklist_by_exam(fetch_by_exam:str,db:Session=Depends(get_db)):
#     return get_marklist_by_exam_controller(fetch_by_exam,db)

# @app.get("/get/marklist_by_exam/standard")
# def get_marklist_by_exam_standard(fetch_by_exam:str,fetch_by_standard:int,db:Session=Depends(get_db)):
#     return get_marklist_by_exam_standard_controller(fetch_by_exam,fetch_by_standard,db)

