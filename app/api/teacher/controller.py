

from app.api.teacher.service import *
from app.api.marklist.service import *

from app.utils.auth_handler import *
from app.utils.validation import *
from fastapi import HTTPException

from app.api.student.service import *



# def create_teacher_controller(teacher,db,):
#     try:
#         data=create_teacher_service(teacher,db)
   
#         if data==1:
#             raise HTTPException(status_code=404,detail="already found email id")
    
#         if not data:
#             raise HTTPException(status_code=404,detail="not found to create teacher")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")


# def get_teacher_controller(teacher_id,db):
#     try:
#         data=get_teacher_service(teacher_id,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="id not found to get teacher")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")

# def update_teacher_controller(teacher_id,update_teacher_id,db):
#     try:
#         data=update_teacher_service(teacher_id,update_teacher_id,db)

#         if not data:
#             raise HTTPException(status_code=404,detail="id not found to update teacher")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ "   exception")

# def delete_teacher_controller(teacher_id,db):
#     try:
#         data=delete_teacher_service(teacher_id,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="id not found to delete teacher")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")

# def get_by_name_controller(get_name,get_standard,get_class,db):
#     try:
#         data=get_by_name_service(get_name,get_standard,get_class,db)
#         if not data:
#             raise HTTPException(status_code=404,detail="no data found by searching :name, standard, class")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")

# def paginate_teachers_controller(page, page_size, db):
    
#     try:
#         data=paginate_teachers(page, page_size, db)
#         if not data:
#             raise HTTPException(status_code=404,detail="no data found")
#         return data
#     except Exception as x:
#         raise HTTPException(status_code=400,detail=str(x)+ " ")
    


def teacher_login_controller(db,email,password):
    
    # if not email_validate(email):
    #     raise HTTPException(status_code=400, detail={"message":"please enter a valid email address","success":False})
    if not password_check(password):
        raise HTTPException(status_code=400, detail={"message":"please enter a valid password","success":False})
    
    login = login_validate_teacher(email,password,db)
    
    if login:
        
        access_token = create_access_token(email,"teacher")
        refresh_token = create_access_token(email,"teacher")
        db_token = teacher_token(refresh_token=refresh_token,admin_id=login.teacher_id)
        db.add(db_token)
        db.commit()
        return {"success": True,"message":"login Successfully","records": login,"access_token": access_token, "refresh_token": refresh_token}
    else:
        raise HTTPException(status_code=404, detail={"message": "Account doesn't exist. Enter a different account or create new account","success":False})


def teacher_create_controller(teacher,db):
    
    if teacher_name_check(db,teacher.teacher_name):
        raise HTTPException(status_code=400, detail={"message":"name already exists","success":False})
    if not email_validate(teacher.teacher_email):
        raise HTTPException(status_code=400, detail={"message":"please enter a valid email address","success":False})
    email_check = teacher_get_email(db,teacher)
    if email_check:
        raise HTTPException(status_code=400,detail="Email already registered")
    if not password_check(teacher.teacher_password):
        raise HTTPException(status_code=400, detail={"message":"please enter a valid password","success":False})
  
    try:
        
        access_token = create_access_token(teacher.teacher_email,"teacher")
        data = teacher_create_service(db,teacher,access_token)
        return {"success": True,"message":"Account created Successfully","records": data,"token":access_token}
    except:
        raise HTTPException(status_code=404, detail={"message": "cannot create new account","success":False})
    

def teacher_get_student_id_controller(id,token,db):
    try:
        check = decodeJWT(token)
        admin = check.get("role")
        
        if admin == 'teacher':
            if not check_student_id(id,db):
                raise HTTPException(status_code=400, detail={"message":"student not found","success":False})
            studentdata=  teacher_get_student_id_serviceStudent(id,db)
            if not check_student_marklist(id,db):
                raise HTTPException(status_code=400, detail={"message":"student not found","success":False})

            marklist = student_marklist_by_id(id,db)
            marklistRec=[{"marklist":marklist}]
            response = {
            "success": True,
            "message": "Fetched API",
            "records": studentdata,  # Ensure studentdata is defined earlier
            "marklist": marklistRec
            }
        
            return response
        else:
            raise HTTPException(status_code=400, detail={"message":"not authorised","success":False})
    except Exception as x:
        raise HTTPException(status_code=400,detail=str(x)+ " ")


def teacher_refresh_controller(db,token):
    # login admin detail validation
    login = teacher_token_validate(db,token)
    
    if login:
        # Create new access token
        access_token = create_access_token(login.teacher_email,"teacher")
        # To create new refresh token
        refresh_token = create_refresh_token(login.teacher_email,"teacher")
        # To update refresh token
        refresh_admin = refresh_update_token(db,token,refresh_token)
        return {"success": True,"message":"login Successfully","admin record": refresh_admin,"access_token": access_token}
    else:
        raise HTTPException(status_code=404, detail={"message": "please enter a valid token","success":False})
    




# def teacher_create_controller(teacher,db):
#     if teacher_name_check(db,teacher.teacher_name):
#         raise HTTPException(status_code=400, detail={"message":"name already exists","success":False})
#     if not email_validate(teacher.teacher_email):
#         raise HTTPException(status_code=400, detail={"message":"please enter a valid email address","success":False})
#     email_check = teacher_get_email(db,teacher)
#     if email_check:
#         raise HTTPException(status_code=400,detail="Email already registered")
#     if not password_check(teacher.password):
#         raise HTTPException(status_code=400, detail={"message":"please enter a valid password","success":False})
   
#     try:
#         data = user_create_service(db,teacher)
#         access_token = create_access_token(teacher.teacher_email)
#         return {"success": True,"message":"Account created Successfully","records": data,"token":access_token}
#     except:
#         raise HTTPException(status_code=404, detail={"message": "cannot create new account","success":False})


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
    
