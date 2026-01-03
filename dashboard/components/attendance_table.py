import streamlit as st
import time
from api_client import get_attendance


def render_attendance_table(session_id: str):
    st.subheader("Live Attendance")

    if not session_id:
        st.info("Start a session to view attendance.")
        return

    # Initialize refresh timer
    if "last_refresh" not in st.session_state:
        st.session_state["last_refresh"] = 0

    current_time = time.time()

    # Refresh every 2 seconds (SAFE METHOD)
    if current_time - st.session_state["last_refresh"] >= 2:
        st.session_state["attendance_data"] = get_attendance(session_id)
        st.session_state["last_refresh"] = current_time

    data = st.session_state.get("attendance_data", {})
    students = data.get("students", [])

    if students:
        table = []
        for i, student in enumerate(students, start=1):
            table.append({
                "S.No": i,
                "Student ID": student,
                "Status": "Present"
            })
        st.table(table)
    else:
        st.warning("No attendance recorded yet.")
