from sqlalchemy import Column,Integer,String
from configure.config import *



class class_marklist(Base):
    __tablename__="marklist"

    marklist_id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    marklist_subject=Column(String)
    marklist_mark=Column(Integer)
    marklist_teacher_id=Column(Integer)
    marklist_student_id=Column(Integer)
    marklist_exam=Column(String)


