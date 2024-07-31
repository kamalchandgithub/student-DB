import re
from fastapi import HTTPException

def email_validate(email):
    reg = r'\b[A-Za-z0-9._%+-]+@gmail.com\b'
    
    if email and re.fullmatch(reg, email) :
        return True
    else:
        return False 






def password_check(passwd):  
    SpecialSym =['$', '@', '#', '%','!']
    val = True  
    if len(passwd) < 6:
        val == False
        raise HTTPException(status_code=422, detail='Password length should be at least 6')    
    if len(passwd) > 20:
        val = False
        raise HTTPException(status_code=422, detail='Password length should be not be greater than 8')      
    if not any(char.isdigit() for char in passwd):
        val = False
        raise HTTPException(status_code=422, detail='Password should have at least one numeral')      
    if not any(char.isupper() for char in passwd):
        val = False 
        raise HTTPException(status_code=422, detail='Password should have at least one uppercase letter')     
    if not any(char.islower() for char in passwd):
        val = False
        raise HTTPException(status_code=422, detail='Password should have at least one lowercase letter')
    if not any(char in SpecialSym for char in passwd):
        val = False
        raise HTTPException(status_code=422, detail='Password should have at least one of the symbols $@#!%')
    return val

