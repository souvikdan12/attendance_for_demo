import requests

BASE_URL = "https://attendance-for-demo.onrender.com"


def start_session(teacher_id, subject, classroom):
    url = f"{BASE_URL}/attendance/start-session"
    payload = {
        "teacher_id": teacher_id,
        "subject": subject,
        "classroom": classroom
    }
    return requests.post(url, json=payload).json()


def mark_attendance(session_id, student_id):
    url = f"{BASE_URL}/attendance/report-presence"
    payload = {
        "session_id": session_id,
        "student_id": student_id
    }
    return requests.post(url, json=payload).json()


def get_attendance(session_id):
    url = f"{BASE_URL}/attendance/session/{session_id}"
    return requests.get(url).json()
