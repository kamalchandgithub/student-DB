from datetime import datetime, timedelta
from typing import Optional
import time
import jwt 

ACCESS_SECRET_KEY = "ACCESS_SECRET"
API_ALGORITHM = "HS256"
API_ACCESS_TOKEN_EXPIRE_MINUTES =  1440
API_REFRESH_TOKEN_EXPIRE_MINUTES = 1440
REFRESH_SECRET_KEY = "SECRET_KEY"

def access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, ACCESS_SECRET_KEY, algorithm=API_ALGORITHM)
    return encoded_jwt



def decodeJWT(token: str) -> dict:
    decode_token = jwt.decode(token,ACCESS_SECRET_KEY, algorithms=[API_ALGORITHM])
    expires = decode_token.get("exp")
    if expires >= time.time():
        return decode_token
    
def create_access_token(email,role = 'student'):
    access_token_expires = timedelta(minutes=API_ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {'username': email, 'role': role}
    token = access_token(data=payload, expires_delta=access_token_expires)
    return token
    
def create_refresh_token(email,role = 'student'):
    payload = {'username': email, 'role': role}
    expires = timedelta(minutes=API_REFRESH_TOKEN_EXPIRE_MINUTES)
    return refresh_token(payload, expires_delta=expires)

def refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, REFRESH_SECRET_KEY, algorithm=API_ALGORITHM)
    return encoded_jwt