import streamlit as st
import requests
from api_client import start_session
from components.attendance_table import render_attendance_table

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Smart Attendance Dashboard", layout="centered")
st.title("📋 Smart Attendance – Live Demo")

# ---------------- Teacher Panel ----------------
st.header("👩‍🏫 Teacher Panel")

teacher_id = st.text_input("Teacher ID")
subject = st.text_input("Subject")
classroom = st.text_input("Classroom")

if st.button("Start Session"):
    if teacher_id and subject and classroom:
        res = start_session(teacher_id, subject, classroom)
        st.session_state["session_id"] = res.get("session_id")
        st.session_state["marked_students"] = set()
        st.success(f"Session Started: {st.session_state['session_id']}")
    else:
        st.warning("Fill all fields")

session_id = st.session_state.get("session_id")
marked_students = st.session_state.get("marked_students", set())

# ---------------- Student Demo Panel ----------------
st.divider()
st.header("📱 Student Demo Panel")

students = ["student_01", "student_02", "student_03", "student_04"]
cols = st.columns(len(students))

for col, student in zip(cols, students):
    with col:
        disabled = student in marked_students
        if st.button(f"Mark {student}", disabled=disabled):
            if session_id:
                payload = {
                    "session_id": session_id,
                    "student_id": student
                }
                requests.post(
                    f"{BACKEND_URL}/attendance/report-presence",
                    json=payload
                )
                marked_students.add(student)
                st.session_state["marked_students"] = marked_students
                st.success(f"{student} marked present")
            else:
                st.error("Start session first")

# ---------------- Live Attendance ----------------
st.divider()
render_attendance_table(session_id)
