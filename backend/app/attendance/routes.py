from fastapi import APIRouter, HTTPException
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
ACTIVE_SESSIONS: dict = {}
ATTENDANCE_RECORDS: dict = {}


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
        raise HTTPException(status_code=400, detail="Invalid or inactive session")

    is_present = evaluate_presence(request.student_id)

    if is_present:
        if request.student_id not in ATTENDANCE_RECORDS.get(request.session_id, []):
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
    students = ATTENDANCE_RECORDS.get(session_id, [])
    return {"students": students}


# -------------------------
# Ping (health check)
# -------------------------
@router.get("/ping")
def attendance_ping():
    return {"message": "Attendance router is working"}
