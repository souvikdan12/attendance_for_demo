import requests

# 🔗 PUBLIC BACKEND URL (Render)
API_BASE_URL = "https://attendance-for-demo.onrender.com"


def start_session(teacher_id, subject, classroom):
    url = f"{API_BASE_URL}/attendance/start-session"
    response = requests.post(
        url,
        json={
            "teacher_id": teacher_id,
            "subject": subject,
            "classroom": classroom
        },
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def mark_attendance(session_id, student_id):
    url = f"{API_BASE_URL}/attendance/report-presence"
    response = requests.post(
        url,
        json={
            "session_id": session_id,
            "student_id": student_id
        },
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def get_attendance(session_id):
    url = f"{API_BASE_URL}/attendance/session/{session_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
