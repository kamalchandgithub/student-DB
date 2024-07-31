from sqlalchemy import Column,Integer,String,DateTime,func,Boolean,ForeignKey
from configure.config import *
from datetime import datetime


class class_student(Base):
    __tablename__="student"

    student_id=Column(Integer,autoincrement=True,primary_key=True,index=True)
    student_name=Column(String(length=20))
    student_email=Column(String,unique=True)
    student_class=Column(String(length=1))
    student_teacher_id=Column(Integer)
    student_standard=Column(Integer)
    student_password=Column(String)
    student_token=Column(String)

    create_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    # is_active = Column(Boolean, default=True)
    # is_deleted
    # created_at = Column(Time)
    # updated_at = Column


class student_token(Base):
    __tablename__="student_Token"
    id=Column(Integer,primary_key=True,index=True)
    student_token_id=Column(Integer,ForeignKey("student.student_id"))
    refresh_token=Column(String,nullable=False)


