# backend/app/attendance/routes.py

from fastapi import APIRouter
from uuid import uuid4

from app.attendance.schemas import (
    StartSessionRequest,
    StartSessionResponse,
    PresenceReportRequest,
    PresenceReportResponse,
)
from app.attendance.evaluator import evaluate_presence

router = APIRouter()

# -------------------------
# In-memory demo storage
# -------------------------
ACTIVE_SESSIONS = {}
ATTENDANCE_RECORDS = {}


# -------------------------
# Start class session
# -------------------------
@router.post("/start-session", response_model=StartSessionResponse)
def start_session(request: StartSessionRequest):
    session_id = str(uuid4())

    ACTIVE_SESSIONS[session_id] = {
        "teacher_id": request.teacher_id,
        "subject": request.subject,
        "classroom": request.classroom,
    }

    ATTENDANCE_RECORDS[session_id] = []

    return StartSessionResponse(
        session_id=session_id,
        message="Session started successfully (demo)",
    )


# -------------------------
# Report student presence
# -------------------------
@router.post("/report-presence", response_model=PresenceReportResponse)
def report_presence(request: PresenceReportRequest):
    if request.session_id not in ACTIVE_SESSIONS:
        return PresenceReportResponse(
            status="error",
            message="Invalid or inactive session",
        )

    is_present = evaluate_presence(request.student_id)

    if is_present:
        if request.student_id not in ATTENDANCE_RECORDS[request.session_id]:
            ATTENDANCE_RECORDS[request.session_id].append(request.student_id)

        return PresenceReportResponse(
            status="present",
            message="Attendance marked (demo)",
        )

    return PresenceReportResponse(
        status="absent",
        message="Attendance not marked",
    )


# -------------------------
# Get attendance for session
# -------------------------
@router.get("/session/{session_id}")
def get_attendance(session_id: str):
    if session_id not in ATTENDANCE_RECORDS:
        return {"students": []}

    return {
        "students": ATTENDANCE_RECORDS[session_id]
    }


# -------------------------
# Ping (health check)
# -------------------------
@router.get("/ping")
def attendance_ping():
    return {"message": "Attendance router is working"}
