import streamlit as st
import requests

st.title("AI Resume GenAI System")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    response = requests.post(
        "http://127.0.0.1:8000/upload-resume",
        files={
            "file": uploaded_file
        }
    )

    data = response.json()

    st.subheader("ATS Analysis")
    st.write(data["ats_analysis"])

    jd = st.text_area(
        "Paste Job Description"
    )

    if st.button("Match Resume"):

        match_response = requests.post(
            "http://127.0.0.1:8000/jd-match",
            json={
                "resume_text":
                data["resume_text"],

                "jd_text":
                jd
            }
        )

        st.write(match_response.json())

    if st.button(
        "Generate Interview Questions"
    ):

        question_response = requests.post(
            "http://127.0.0.1:8000/generate-questions",
            json={
                "resume_text":
                data["resume_text"]
            }
        )

        st.write(
            question_response.json()
        )