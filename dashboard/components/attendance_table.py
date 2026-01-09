import streamlit as st
from api_client import get_attendance
import time


def render_attendance_table(session_id):
    st.subheader("📊 Live Attendance")

    if not session_id:
        st.info("Start or join a session to view attendance")
        return

    # Fetch attendance from backend
    try:
        data = get_attendance(session_id)
        students = data.get("students", [])
    except Exception as e:
        st.error("Failed to fetch attendance")
        return

    # Display attendance
    if students:
        st.table({"Present Students": students})
    else:
        st.warning("No attendance recorded yet")

    # 🔄 AUTO-REFRESH every 2 seconds
    time.sleep(2)
    st.rerun()
