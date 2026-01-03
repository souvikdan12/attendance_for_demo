# backend/app/verification/routes.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def verification_ping():
    return {"message": "Verification router is working"}
