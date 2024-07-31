
from sqlalchemy.orm import Session
from configure.config import *
from app.api.marklist.models import *
from app.api.marklist.schemas import *


from sqlalchemy import and_


    

def create_marklist_service(obj_marklist : create_marklist_schema,db:Session):

    check = db.query(class_marklist).filter(and_(class_marklist.marklist_student_id == obj_marklist.marklist_student_id,class_marklist.marklist_subject == obj_marklist.marklist_subject)).first()

    if check:
        return 1

    db_user=class_marklist(
                          marklist_subject = obj_marklist.marklist_subject,
                          marklist_mark = obj_marklist.marklist_mark,
                          marklist_teacher_id = obj_marklist.marklist_teacher_id,
                          marklist_student_id = obj_marklist.marklist_student_id,
                          marklist_exam = obj_marklist.marklist_exam)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"created marklist successfully for student : ",obj_marklist.marklist_student_id}

def get_marklist_service(obj_marklist_id : int ,db : Session):
    return db.query(class_marklist).filter(class_marklist.marklist_id == obj_marklist_id).all()

def update_marklist_service(marklist_update : update_marklist_schema,marklist_update_id : int, db:Session):

    db_user = db.query(class_marklist).filter(class_marklist.marklist_id == marklist_update_id).first()

    
    if db_user:

        db_user.marklist_mark = marklist_update.marklist_mark
        db_user.marklist_student_id = marklist_update.marklist_student_id
        db_user.marklist_teacher_id = marklist_update.marklist_teacher_id
        db_user.marklist_exam = marklist_update.marklist_exam
        db.commit()
        db.refresh(db_user)
    else:
        return None
    db_user = db.query(class_marklist).filter(class_marklist.marklist_id == marklist_update_id).first()
    return "updated marklist successfully for student : "+marklist_update.marklist_student_id

def delete_marklist_service(delete_marklist_id : int ,db: Session):
    db_user = db.query(class_marklist).filter(class_marklist.marklist_id == delete_marklist_id).first()
    if db_user :
        db.delete(db_user)
        db.commit()
        
    else:
        return None
    return "deleted marklist successfully marklist id : "+delete_marklist_id

def check_student_marklist(obj_student_id,db:Session):
    return db.query(class_marklist).filter(class_marklist.marklist_student_id == obj_student_id).first()



def student_marklist_by_id(student_id_obj,db:Session):
    return db.query(class_marklist).filter(class_marklist.marklist_student_id == student_id_obj).all()


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
  
