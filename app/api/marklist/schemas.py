from pydantic import BaseModel,EmailStr
from typing import Optional


class class_marklist_schema(BaseModel):
    marklist_id:int
    marklist_subject:str
    marklist_mark:int
    marklist_teacher_id:int
    marklist_student_id:int

class create_marklist_schema(BaseModel): 

    marklist_subject:str
    marklist_mark:int
    marklist_teacher_id:int
    marklist_student_id:int
    marklist_exam:str

class update_marklist_schema(BaseModel):
    marklist_mark:int
    marklist_teacher_id:int
    marklist_student_id:int
    marklist_exam:str