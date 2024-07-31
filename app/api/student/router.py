from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.student.schemas import *
from app.api.student.controller import *
# from app.api.task.service import *
from configure.config import *
from app.utils.auth_bearer import JWTBearer


router2=APIRouter(tags=["STUDENT"])
http_bearer = JWTBearer()


@router2.post("/login/student_jwt",tags=["using JWT "])
def student_login_router(student:login_student_schema,db:Session=Depends(get_db)):
    return student_login_controller(student.student_email,student.student_password,db)

@router2.post("/create_student",tags=["using JWT "])
async def student_create_router_jwt(student: create_student_schema, db: Session = Depends(get_db)):
    return student_create_controller_jwt(student,db)

@router2.post("/create/student_relogin",tags=["using JWT"])
def student_relogin_router(token :str,db:Session=Depends(get_db)):
    return student_relogin_controller(token,db)




# @router2.post("/create/student")
# def get_student(student:create_student_schema, db:Session=Depends(get_db)):
#     return create_student_controller(student,db)

# @router2.get("/get/student")
# def get_student(student_id:int,db:Session=Depends(get_db)):
#     return get_student_controller(student_id,db)

# @router2.put("/update/student")
# def update_student(student_update :update_student_schema, student_update_id : int, db:Session=Depends(get_db) ):
#     return update_student_controller(student_update, student_update_id, db)

# @router2.delete("/delete/student")
# def delete_student(delete_student_id : int,db:Session=Depends(get_db)):
#     return delete_student_controller(delete_student_id,db)

# @router2.get("/get/by/name")
# def get_by_name(get_name:str,get_standard:int,get_class:str,db:Session=Depends(get_db)):
#     return get_by_name_controller(get_name,get_standard,get_class,db)


# @router2.get("/get/student/paginated")
# def paginate_student(page: int, page_size: int, db: Session=Depends(get_db)):
#     return paginate_student_controller(page, page_size, db)




















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

