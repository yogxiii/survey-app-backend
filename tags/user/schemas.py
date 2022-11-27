from pydantic import BaseModel
from typing import Union

class UserBase(BaseModel):
    user_name : str

class UserCreate(UserBase):
    password : str 

class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str

class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
