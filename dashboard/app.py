import streamlit as st
import qrcode
from io import BytesIO
from api_client import start_session, mark_attendance
from components.attendance_table import render_attendance_table

st.caption("Build verified: fresh repo deployment")

st.set_page_config(
    page_title="BLE Smart Attendance (Demo)",
    layout="centered"
)

# -------------------------------
# Read session_id from URL (PHONE)
# -------------------------------
query_params = st.query_params
if "session_id" not in st.session_state:
    sid = query_params.get("session_id")
    if sid:
        st.session_state.session_id = sid[0]
    else:
        st.session_state.session_id = None

st.title("📡 BLE Smart Attendance (Demo)")

# ===============================
# TEACHER PANEL (Laptop)
# ===============================
st.header("👨‍🏫 Teacher Panel")

teacher_id = st.text_input("Teacher ID", "teacher_01")
subject = st.text_input("Subject", "DSA")
classroom = st.text_input("Classroom", "Room-101")

if st.button("Start Session"):
    response = start_session(teacher_id, subject, classroom)
    st.session_state.session_id = response["session_id"]

    st.success(f"Session Started!")
    st.code(st.session_state.session_id)

    # QR code for students
    join_url = (
        "https://attendance-for-demo.streamlit.app/"
        f"?session_id={st.session_state.session_id}"
    )

    qr = qrcode.make(join_url)
    buf = BytesIO()
    qr.save(buf)

    st.image(buf.getvalue(), caption="📱 Scan to Join (Student)")

st.divider()

# ===============================
# STUDENT PANEL (Phone)
# ===============================
st.header("🎓 Student Panel")

student_id = st.text_input("Student ID", "student_01")

if st.button("Mark Attendance"):
    if not st.session_state.session_id:
        st.error("Session not joined yet. Scan QR first.")
    else:
        mark_attendance(st.session_state.session_id, student_id)
        st.success(f"{student_id} marked present")

st.divider()

# ===============================
# LIVE ATTENDANCE (Laptop)
# ===============================
render_attendance_table(st.session_state.session_id)
