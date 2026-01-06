import streamlit as st
from api_client import get_attendance

def render_attendance_table(session_id):
    st.subheader("📊 Live Attendance")

    if not session_id:
        st.info("Start or join a session to view attendance")
        return

    if st.button("🔄 Refresh Attendance"):
        data = get_attendance(session_id)
        students = data.get("students", [])

        if students:
            st.table({"Present Students": students})
        else:
            st.warning("No attendance recorded yet")
