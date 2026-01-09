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
    st.session_state.session_id = None

if "session_id" in query_params:
    st.session_state.session_id = query_params["session_id"][0]



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
    BASE_STREAMLIT_URL = "https://attendance-for-demo.streamlit.app"
    join_url = f"{BASE_STREAMLIT_URL}/?session_id={st.session_state.session_id}"



    qr = qrcode.make(join_url)
    buf = BytesIO()
    qr.save(buf)

    st.image(buf.getvalue(), caption="📱 Scan to Join (Student)")

st.divider()

if st.session_state.session_id:
    st.info("Joined session automatically via QR")


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
