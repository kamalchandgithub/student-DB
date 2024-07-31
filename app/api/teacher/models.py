from sqlalchemy import Column,Integer,String,DateTime,func,Boolean,ForeignKey
from configure.config import *
from datetime import datetime

class class_teacher(Base):

    __tablename__="teacher"

    teacher_id=Column(Integer,autoincrement=True, primary_key=True, index=True)
    teacher_name=Column(String)
    teacher_email=Column(String)
    teacher_class=Column(String)
    teacher_standard=Column(Integer)

    teacher_password = Column(String)
    teacher_token=Column(String)
    create_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

class teacher_token(Base):
    __tablename__ = "teacher_token"
    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer, ForeignKey("teacher.teacher_id"))
    refresh_token = Column(String, nullable=False)