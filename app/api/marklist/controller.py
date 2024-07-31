from app.api.marklist.service import *
from fastapi import HTTPException
import traceback



def  create_marklist_controller(marklist,db):
    try:
        data=create_marklist_service(marklist,db)
        if data==1:
            raise HTTPException(status_code=404,detail="already created")

        if not data:
            raise HTTPException(status_code=404,detail="not found to create marklist")
        return data
    except Exception as x:
        traceback.print_exc()
        raise HTTPException(status_code=400,detail=str(x)+ " ")

def get_marklist_controller(marklist_id,db):
    try:
        data=get_marklist_service(marklist_id,db)
        if not data:
            raise HTTPException(status_code=404,detail="id not found to get marklist")
        return data
    except Exception as x:
        raise HTTPException(status_code=400,detail=str(x)+ " ")


def update_marklist_controller(update_marklist,update_marklist_id,db):
    try:
        data=update_marklist_service(update_marklist, update_marklist_id, db)
        if not data:
            raise HTTPException(status_code=404,detail="id not found to update marklist")
        return data
    except Exception as x:
        raise HTTPException(status_code=400,detail=str(x)+ " ")


def delete_marklist_controller(delete_marklist_id,db):
    try:
        data = delete_marklist_service(delete_marklist_id,db)
        if not data:
            raise HTTPException(status_code=404,detail="id not found to delete marklist")
        return data
    except Exception as x:
        raise HTTPException(status_code=400,detail=str(x)+ " ")



# def get_students_by_class_controller(fetch_by_class,fetch_by_standard,db):
#     try:
#         data =  get_students_by_class_service(fetch_by_class,fetch_by_standard,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="not found student by class,standard")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")




# def get_students_by_teacher_id_controller(fetch_by_teacher_id,db):
#     try:
#         data = get_students_by_teacher_id_service(fetch_by_teacher_id,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="not found student by teacher id")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")
    
# def get_marklist_by_exam_controller(fetch_by_exam,db):
#     try:
#         data = get_by_exam_service(fetch_by_exam,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="not found student by exam")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")


# def get_marklist_by_exam_standard_controller(fetch_by_exam,fetch_by_standard,db):
#     try:
#         data = get_by_exam_standard_service(fetch_by_exam,fetch_by_standard,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="not found student by exam")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")
    
