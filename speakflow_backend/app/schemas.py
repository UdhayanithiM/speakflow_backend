from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    total_xp: int
    
    class Config:
        from_attributes = True


class SpeakingProgressRequest(BaseModel):
    user_id: int
    lesson_id: int
    dialogue_id: int
    score: int        