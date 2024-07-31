from sqlalchemy.orm import Session
# from app.api.student.controller import *
from app.api.student.models import *
from app.api.student.schemas import *

# from app.api.student.router import *

from sqlalchemy import and_,func
from app.api.teacher.service import find_teacher_name


def create_student_service(obj_student : create_student_schema,db:Session):
    db_val= db.query(class_student).filter(class_student.student_email == obj_student.student_email).first()

    if db_val:
        return 1
    db_user=class_student(
                          student_name = obj_student.student_name,
                          student_email = obj_student.student_email,
                          student_class = obj_student.student_class.upper(),
                          student_teacher_id=obj_student.student_teacher_id,
                          student_standard=obj_student.student_standard,
                          student_password=obj_student.student_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "created student successfully for student : "+obj_student.student_name

def get_student_service(obj_student_id : int ,db:Session):
   return db.query(class_student).filter(class_student.student_id == obj_student_id).all()

def update_student_service(student_update :update_student_schema,student_update_id : int ,db : Session):
    db_val= db.query(class_student).filter(class_student.student_email == student_update.student_email).first()

    if db_val:
        return 1
    db_user = db.query(class_student).filter(class_student.student_id == student_update_id).first()
    if db_user :
        if student_update.student_email != None:

            db_user.student_email=student_update.student_email
            db_user.student_class=student_update.student_class
            db_user.student_standard=student_update.student_standard
            db_user.student_password=student_update.student_password
        else:
            db_user.student_class=student_update.student_class
            db_user.student_standard=student_update.student_standard
            
        db.commit()
        db.refresh(db_user)
    else:
        return None
    db_user = db.query(class_student).filter(class_student.student_id == student_update_id).first()
    return "updated student successfully for student : "+student_update_id

def delete_student_service(student_delete_id : int,db : Session):
    db_user = db.query(class_student).filter(class_student.student_id == student_delete_id).first()
    if db_user :
        db.delete(db_user)
        db.commit()
        
        
    else:
        return None
    return "deleted student successfully for student : "+student_delete_id

def get_by_name_service(get_name,get_standard,get_class,db):
    return db.query(class_student).filter(and_(and_(class_student.student_name.like(f"%{get_name}%"),class_student.student_standard ==get_standard)),class_student.student_class == get_class.upper() ).all()

def paginate_student(page: int, page_size: int, db: Session):
   
    range_page = (page - 1) * page_size
    total_students = db.query(func.count(class_student.student_id)).scalar()

    students = db.query(class_student).\
        limit(page_size).\
        offset(range_page).\
        all()
    
    total_pages = (total_students + page_size - 1) // page_size

    return students, "Total students :", total_students, "total pages :",total_pages

def login_validate(email,pwd,db):
    return db.query(class_student).filter(and_(class_student.student_email == email,class_student.student_password == pwd)).first()

def student_check(name,db:Session):
    return db.query(class_student).filter(and_(class_student.student_name == name,class_student.is_deleted==False)).first() 

def student_get_by_email(student,db:Session):
    return db.query(class_student).filter(and_(class_student.student_email == student.student_email,class_student.is_deleted==False)).first()

def student_create_service(student:create_student_schema,accesstoken,db:Session):
    add = class_student(
        student_name = student.student_name,
        student_email = student.student_email,
        student_password = student.student_password,
        student_standard=student.student_standard,
        student_class=student.student_class,
        student_teacher_id=student.student_teacher_id,
        student_token=accesstoken
    )
    
    
    db.add(add)
    db.commit()
    db.refresh(add)
    return add

def check_student_id(teacher,db:Session):
    return db.query(class_student).filter(class_student.student_id == teacher).first()

 


def teacher_get_student_id_serviceStudent(teacher,db:Session):
    student= db.query(class_student).filter(class_student.student_id == teacher).first()
    student_teacher_name=find_teacher_name(student.student_teacher_id,db)
    return {"studentname":student.student_name,"studentclass":student.student_class,"studentemail":student.student_email,"studentstandard":student.student_standard,"teacherName":f"{student_teacher_name}"}


def student_name_check(db: Session, teacher):
    return db.query(class_student).filter(
        and_(
            class_student.teacher_name == teacher,
            class_student.is_deleted == False
        )
    ).first()

def student_get_email(db:Session,teacher):
    return db.query(class_student).filter(class_student.teacher_email == teacher.teacher_email).first()

def student_get_email(db:Session,student):
    return db.query(class_student).filter(class_student.student_email == student.student_email).first()

def student_token_validate(token,db:Session):
   print("entered validating")
   print(token)
   return db.query(class_student).filter(class_student.student_token == token).first()


def refresh_update_token(db:Session,token,refresh):
    # To  check re-login as an admin
    print(token)
    update = student_token_validate(token,db)
    print(update)
    if update:
        print("entered update")
        update.student_token = refresh
        update.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(update)
        return update
    

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
  
