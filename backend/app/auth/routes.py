# backend/app/auth/routes.py

from fastapi import APIRouter, HTTPException
from app.auth.schemas import LoginRequest, LoginResponse
from app.auth.utils import generate_demo_token

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """
    Demo login endpoint.
    Accepts user_id and role.
    """

    if request.role not in ["student", "teacher"]:
        raise HTTPException(status_code=400, detail="Invalid role")

    token = generate_demo_token(request.user_id)

    return LoginResponse(
        token=token,
        role=request.role,
        message="Login successful (demo)",
    )


@router.get("/ping")
def auth_ping():
    return {"message": "Auth router is working"}
