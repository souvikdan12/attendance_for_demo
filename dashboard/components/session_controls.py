# dashboard/components/session_controls.py

import streamlit as st
from api_client import start_session




def render_session_controls():
    st.subheader("Start Class Session")

    teacher_id = st.text_input("Teacher ID", value="teacher_01")
    subject = st.text_input("Subject", value="DSA")
    classroom = st.text_input("Classroom", value="Room-101")

    if st.button("Start Session"):
        response = start_session(teacher_id, subject, classroom)
        st.session_state["session_id"] = response["session_id"]
        st.success("Session started!")
        st.write("Session ID:", response["session_id"])
