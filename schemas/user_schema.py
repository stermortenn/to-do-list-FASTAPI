from pydantic import BaseModel, EmailStr

class BaseResponse(BaseModel):
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    user_name: str 
    user_email: EmailStr
    user_password: str

class UserResponse(BaseResponse):
    user_id: int
    user_name: str
    user_email: EmailStr

class UserLogin(BaseModel):
    user_email: EmailStr
    user_password: str
