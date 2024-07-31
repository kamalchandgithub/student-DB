from fastapi import Depends
from sqlalchemy.orm import Session
from app.api.teacher.controller import *
from configure.config import *

from app.utils.auth_bearer import JWTBearer

http_bearer = JWTBearer()
router3=APIRouter(tags=["TEACHER"])

# @router3.post("/create/teacher")
# def create_teacher(teacher:create_teacher_schema,db:Session=Depends(get_db)):
#     return create_teacher_controller(teacher,db)

# @router3.get("/get/teacher")
# def get_teacher(teacher_id:int,db:Session=Depends(get_db)):
#     return get_teacher_controller(teacher_id,db)

# @router3.put("/update/teacher")
# def update_teacher(teacher_update : update_teacher_schema,teacher_id : int,db:Session=Depends(get_db)):
#     return update_teacher_controller(teacher_update,teacher_id,db)

# @router3.delete("/delete/teacher")
# def delete_teacher(delete_teacher_id : int,db:Session=Depends(get_db)):
#     return delete_teacher_controller(delete_teacher_id,db)

# @router3.get("/get/teacher/name")
# def get_by_name(get_name:str,get_standard:int,get_class:str,db:Session=Depends(get_db)):
#     return get_by_name_controller(get_name,get_standard,get_class,db)

# @router3.get("/students/")
# def get_students(start:int,end:int,db:Session=Depends(get_db)):
    
#     students_between_indices = db.query(class_teacher).slice(start, end + 1).all()
#     return students_between_indices

# @router3.get("/get/teachers")
# def paginate_teachers(page: int, page_size: int, db: Session=Depends(get_db)):
#     return paginate_teachers_controller(page, page_size, db)



# user and admin login
@router3.post("/user-login",tags=["teacher JWT"])
async def teacher_login(teacher:teacher_login_schema,db: Session = Depends(get_db)):
    return teacher_login_controller(db,teacher.teacher_email,teacher.teacher_password)

@router3.post("/teacher",tags=["teacher JWT"])
async def teacher_create_router(teacher:create_teacher_schema,db: Session = Depends(get_db)):
    
    return teacher_create_controller(teacher,db)

@router3.get("/teacher/student_by_id/{id}")
async def teacher_get_student_id(teacher:int,db:Session=Depends(get_db),token: str = Depends(http_bearer)):
    return teacher_get_student_id_controller(teacher,token,db)


@router3.post("/re-login",tags=["teacher JWT"])
async def student_refresh_router(token: str, database: Session = Depends(get_db)):
    return teacher_refresh_controller(database, token)





# @router3.get('/users')
# def get_users(db: Session = Depends(get_db)) -> Page[UserOut]:
#     return paginate(db, select(class_teacher).order_by(User.created_at))


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

