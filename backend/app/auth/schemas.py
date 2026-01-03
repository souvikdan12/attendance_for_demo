# backend/app/auth/schemas.py

from pydantic import BaseModel


class LoginRequest(BaseModel):
    user_id: str
    role: str  # "student" or "teacher"


class LoginResponse(BaseModel):
    token: str
    role: str
    message: str
