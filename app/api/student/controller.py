from fastapi import HTTPException
# from app.api.student.router import *
from app.api.student.service import *


from app.utils.validation import email_validate,password_check
from app.utils.auth_handler import *

def paginate_student_controller(page, page_size, db):
    
    try:
        data=paginate_student(page, page_size, db)
        if not data:
            raise HTTPException(status_code=404,detail="no data foundr")
        return data
    except Exception as x:
        raise HTTPException(status_code=400,detail=str(x)+ " ")
    


def student_login_controller(email,password,db):
    if not email_validate(email):
        raise HTTPException(status_code=400, detail={"please enter a valid email address"})
    if not password_check(password):
        raise HTTPException(status_code=400, detail={"please enter a valid password"})
    login = login_validate(email,password,db)
    if login :
        
        
        access_token = create_access_token(email)
        refresh_token = create_access_token(email)
        db_token = student_token(student_token_id=login.student_id,refresh_token=refresh_token)
        db.add(db_token)
        db.commit()
        

        return {"success": True,"message":"login Successfully","records": login,"access_token": access_token}
    else:
        raise HTTPException(status_code=404, detail={"message": "Account doesn't exist. Enter a different account or create new account","success":False})

    
    




def student_create_controller_jwt(student,db):
   
    if student_check(student.student_name,db):
        raise HTTPException(status_code=400, detail={"message":"name already exists","success":False})
    if not email_validate(student.student_email):
        raise HTTPException(status_code=400, detail={"message":"please enter a valid email address","success":False})
    email_check = student_get_by_email(student,db)
    if email_check:
        raise HTTPException(status_code=400,detail="Email already registered")
    if not password_check(student.student_password):
        raise HTTPException(status_code=400, detail={"message":"please enter a valid password","success":False})
   
    try:
        access_token = create_access_token(student.student_email)
        token = student_create_service(student,access_token,db)
    
        return {"success": True,"message":"Account created Successfully","records": token,"access_token": access_token}
    except:
        raise HTTPException(status_code=404, detail={"message": "cannot create new account","success":False})
    


def student_relogin_controller(token,db):
    
    try:
        check=student_token_validate(token,db)
        
        if check:
            print("entered")
            access=create_access_token(check.student_email)
            print("entered 1")
            print("access = ",access)
            refresh=create_refresh_token(check.student_email)
            print("refresh = ",refresh)
            print("entered 2")
            refresh_student=refresh_update_token(db,token,refresh)
            print("entered 3")
            return {"success": True,"message":"login Successfully","admin record": refresh_student,"access_token": access}
        else:
             raise HTTPException(status_code=404, detail={"message": "please enter a valid token","success":False})
        
    except Exception as e:
        print(e)





# def create_student_controller(student,db):
#     try:

        
#         data=create_student_service(student,db)
#         if data==1:
#             raise HTTPException(status_code=404,detail="already found email id")
#         if not data:
#             raise HTTPException(status_code=404,detail="not found to create teacher")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")

# def get_student_controller(student_id,db):
#     try:
#         data=get_student_service(student_id,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="not found searching teacher")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")

# def update_student_controller(student_update, student_update_id, db):
#     try:
#         data=update_student_service(student_update,student_update_id,db)
#         if data==1:
#             raise HTTPException(status_code=404,detail="already found email id")
#         if not data:
#             raise HTTPException(status_code=404,detail="id not found to update teacher")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")

# def delete_student_controller(delete_student_id,db):
#     try:
#         data = delete_student_service(delete_student_id,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="id not found to delete teacher")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")


# def get_by_name_controller(get_name,get_standard,get_class,db):
#     try:
#         data=get_by_name_service(get_name,get_standard,get_class,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="data not found by searching field: name, standard, class")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")








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
    
