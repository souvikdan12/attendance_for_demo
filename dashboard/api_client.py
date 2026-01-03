import requests

BASE_URL = "https://YOUR_BACKEND_URL"




def start_session(teacher_id, subject, classroom):
    url = f"{BASE_URL}/attendance/start-session"
    payload = {
        "teacher_id": teacher_id,
        "subject": subject,
        "classroom": classroom
    }
    response = requests.post(url, json=payload)
    return response.json()


def get_attendance(session_id):
    url = f"{BASE_URL}/attendance/session/{session_id}"
    response = requests.get(url)
    return response.json()
