# backend/app/attendance/schemas.py

from pydantic import BaseModel
from typing import Optional


class StartSessionRequest(BaseModel):
    teacher_id: str
    subject: str
    classroom: str


class StartSessionResponse(BaseModel):
    session_id: str
    message: str


class PresenceReportRequest(BaseModel):
    session_id: str
    student_id: str


class PresenceReportResponse(BaseModel):
    status: str
    message: str
