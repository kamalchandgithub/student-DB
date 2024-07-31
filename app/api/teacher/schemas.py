from pydantic import BaseModel,EmailStr
from typing import Optional

class class_teacher_schema(BaseModel):
    teacher_id:int
    # teacher_name:str
    # teacher_email:Optional[EmailStr]=None
    # teacher_class:str

class create_teacher_schema(BaseModel):
    teacher_name:Optional[str]=None
    teacher_email:Optional[EmailStr]=None
    teacher_class:Optional[str]=None
    teacher_standard:Optional[int]=None
    teacher_password:Optional[str]=None
    class Config:
        json_schema_extra={
            "example":{
                "teacher_name":"User",
                "teacher_email":"user@gmail.com",
                "teacher_password":"User12@",
                "teacher_standard":"1",
                "teacher_class":"A"
            }
        }
    

class update_teacher_schema(BaseModel):
    teacher_email:Optional[EmailStr]=None
    teacher_class:Optional[str]=None
    teacher_standard:Optional[int]=None
    teacher_password:Optional[str]=None


class teacher_login_schema(BaseModel):
    teacher_email:Optional[str] = None 
    teacher_password:Optional[str] = None  
    class Config:
        json_schema_extra={
            "example":{
                "teacher_email":"user@gmail.com",
                "teacher_password":"User12@"
            }
        }

class teacherUserRefreshToken_schema(BaseModel): # admin user refresh token swagger class
    admin_id: int
    refresh_token : str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example":{
                "admin_id": 2,
                "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbF9pZCI6InRlc3Q0QGdtYWlsLmNvbSIsInR5cGUiOiJyZWZyZXNoIn0.Sbit9GbF7KQmETdDFp7MoliGVHl5M1hGEeniUJCrSgk"
            }
        }

