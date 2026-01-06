import requests
from config import API_BASE_URL

def start_session(teacher_id, subject, classroom):
    url = f"{API_BASE_URL}/attendance/start-session"
    r = requests.post(url, json={
        "teacher_id": teacher_id,
        "subject": subject,
        "classroom": classroom
    })
    return r.json()

def mark_attendance(session_id, student_id):
    url = f"{API_BASE_URL}/attendance/report-presence"
    requests.post(url, json={
        "session_id": session_id,
        "student_id": student_id
    })

def get_attendance(session_id):
    url = f"{API_BASE_URL}/attendance/session/{session_id}"
    return requests.get(url).json()
