from sqlalchemy.orm import Session
# from app.api.teacher.controller import *
from app.api.teacher.models import *
from app.api.teacher.schemas import *
from sqlalchemy import and_,func





# def create_teacher_service(obj_teacher : create_teacher_schema,db:Session):
#     db_val= db.query(class_teacher.teacher_name, class_teacher.teacher_email, class_teacher.teacher_class).filter(class_teacher.teacher_email == obj_teacher.teacher_email).first()

#     if db_val:
#         return 1
#     else:
    
#         db_user=class_teacher(
#                           teacher_name = obj_teacher.teacher_name,
#                           teacher_email = obj_teacher.teacher_email,
#                           teacher_class = obj_teacher.teacher_class.upper(),
#                           teacher_standard = obj_teacher.teacher_standard)
                          
#     # db_val= db.query(class_teacher).filter(class_teacher.teacher_email == obj_teacher.teacher_email).first()
#     # if not db_val:
#     #     return HTTPException(status_code=404,detail="email repetation error")
    
#         db.add(db_user)
#         db.commit()
#         db.refresh(db_user)
#         return "created teacher successfully for teacher : "+obj_teacher.teacher_name
   

# def get_teacher_service(obj_teacher_id:int ,db:Session):
#     return  db.query(class_teacher).filter(class_teacher.teacher_id == obj_teacher_id).all()


# def update_teacher_service(teacher :update_teacher_schema,update_teacher_id:int ,db:Session):
#     db_user=db.query(class_teacher).filter(class_teacher.teacher_id == update_teacher_id).first()
   
#     if db_user :

#         if teacher.teacher_email != None:
        
#             db_user.teacher_email = teacher.teacher_email
#             db_user.teacher_class = teacher.teacher_class.upper()
#             db_user.teacher_standard=teacher.teacher_standard
#         else:
#             db_user.teacher_class = teacher.teacher_class.upper()
#             db_user.teacher_standard=teacher.teacher_standard

#         db.commit()
#         db.refresh(db_user)
#     else:
#         return None
#     db_user=db.query(class_teacher).filter(class_teacher.teacher_id == update_teacher_id).first()
#     # db.commit()
#     return "updated teacher successfully to : "+teacher.teacher_class

# def delete_teacher_service(obj_teacher_id:int ,db:Session):
#     db_user=  db.query(class_teacher).filter(class_teacher.teacher_id == obj_teacher_id).first()  
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#     # db_user=  db.query(class_teacher).filter(class_teacher.teacher_id == obj_teacher_id).first()   
#     return "deleted teacher successfully for teacher : "+obj_teacher_id

# def get_by_name_service(get_name,get_standard,get_class,db):
#     return db.query(class_teacher).filter(and_(and_(class_teacher.teacher_name.like(f"%{get_name}%"),class_teacher.teacher_standard ==get_standard)),class_teacher.teacher_class == get_class.upper() ).all()


# def paginate_teachers(page: int, page_size: int, db: Session):
   
#     range_page = (page - 1) * page_size
#     total_teacher = db.query(func.count(class_teacher.teacher_id)).scalar()

#     teacher = db.query(class_teacher).\
#         limit(page_size).\
#         offset(range_page).\
#         all()
    
#     total_pages = (total_teacher + page_size - 1) // page_size

#     return teacher, "Total teacher :", total_teacher, "total pages :",total_pages



# def login_validate(email, pwd, db: Session):
#     try:
#         print("email = " + email)
#         result = db.query(class_teacher).filter(
#             class_teacher.teacher_email == email,
#             class_teacher.teacher_password == pwd
#         ).first()
#         if result:
#             print("User found")
#         else:
#             print("User not found")
#         return result
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None


# def teacher_name_check(db:Session,teacher):
#     return db.query(class_teacher).filter(and_(class_teacher.teacher_name == teacher.teacher_name,class_teacher.is_deleted==False)).first()


def teacher_name_check(db: Session, teacher):
    return db.query(class_teacher).filter(
        and_(
            class_teacher.teacher_name == teacher,
            class_teacher.is_deleted == False
        )
    ).first()

def teacher_get_email(db:Session,teacher):
    return db.query(class_teacher).filter(class_teacher.teacher_email == teacher.teacher_email).first()

def teacher_create_service(db:Session,teacher:create_teacher_schema,access_token):
    add = class_teacher(
            teacher_name = teacher.teacher_name,
            teacher_email = teacher.teacher_email,
            teacher_password = teacher.teacher_password,
            teacher_class=teacher.teacher_class,
            teacher_standard=teacher.teacher_standard,
            teacher_token=access_token
        )
    
    db.add(add)
    db.commit()
    db.refresh(add)
    return add



def find_teacher_name(student_teacher_id,db:Session):
    try:
        name=db.query(class_teacher).filter(class_teacher.teacher_id == student_teacher_id).first()
    # tname=name.teacher_name
    # print(tname)
        
        return {name.teacher_name}
    except Exception as e:
        print(e)

def teacher_token_validate(db:Session,token):
    
    return db.query(class_teacher).filter(class_teacher.teacher_token == token).first()

    
def refresh_update_token(db:Session,token,refresh):
    # To  check re-login as an admin
    update = teacher_token_validate(db,token)
    if update:
        update.refresh_token = refresh
        update.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(update)
        return update
    
def login_validate_teacher(email,pwd,db:Session):
    print("email = "+email)
    return db.query(class_teacher).filter(class_teacher.teacher_email == email,class_teacher.teacher_password == pwd).first()
 


# def get_students_by_class_service(fetch_by_class: str,fecth_by_standard:int,db:Session):
#     return db.query(class_student).\
#         join(class_teacher, class_teacher.teacher_class == class_student.student_class).\
#         filter(and_(class_teacher.teacher_class == fetch_by_class,class_student.student_standard == fecth_by_standard)).\
#         all()
#     # return db.query(class_student,class_teacher).join(class_teacher,class_teacher.teacher_class == class_student.student_class).\
#     # filter(class_teacher.teacher_class == fetch_by_class).all()
   
# def get_students_by_teacher_id_service(fetch_by_teacher_id : int,db:Session):
#     return db.query(class_student).join(class_teacher,class_teacher.teacher_id == class_student.student_teacher_id).\
#     filter(class_student.student_teacher_id == fetch_by_teacher_id).all()


# def get_by_exam_service(fetch_by_exam,db:Session):
#     return db.query(class_student).\
#     filter(class_marklist.marklist_exam == fetch_by_exam).all()


# def get_by_exam_standard_service(fetch_by_exam: str,fecth_by_standard:int,db:Session):
#     return db.query(class_student).\
#        join(class_marklist,class_marklist.marklist_student_id == class_student.student_id).\
#        filter(and_(class_marklist.marklist_exam == fetch_by_exam,class_student.student_standard == fecth_by_standard)).all()
  
# def validate_email(email):
#     # Regular expression for basic email validation
#     pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     if re.match(pattern, email):
#         return True
#     else:
#         return False