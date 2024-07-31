from pydantic import BaseModel,EmailStr
from typing import Optional


class class_student_schema(BaseModel):
    
    student_id:int

class create_student_schema(BaseModel):
    student_name:Optional[str]=None
    student_email:Optional[EmailStr]=None
    student_class:Optional[str]=None
    student_standard:Optional[int]=None
    student_teacher_id:Optional[int]=None
    student_password:Optional[str]=None

class update_student_schema(BaseModel):
    student_email:Optional[EmailStr]=None
    student_class:Optional[str]=None
    student_standard:Optional[int]=None
    student_password:Optional[str]=None

class login_student_schema(BaseModel):
    student_email:Optional[EmailStr]=None
    student_password:Optional[str]=None
     
class Config:
    json_schema_extra={
        "example":{
             "student_email":"admin@gmail.com",
             "student_password":"Admin12@"
            }
        }
class student_token_schema(BaseModel): # admin user refresh token swagger class
    student_token_id: int
    refresh_token : str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example":{
                "student_token_id": 2,
                "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbF9pZCI6InRlc3Q0QGdtYWlsLmNvbSIsInR5cGUiOiJyZWZyZXNoIn0.Sbit9GbF7KQmETdDFp7MoliGVHl5M1hGEeniUJCrSgk"
            }
        }
