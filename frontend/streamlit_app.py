import streamlit as st
import requests

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="CareerPilot",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("📄 CareerPilot")

st.subheader(
    "AI Resume Analyzer & Interview Assistant"
)

# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

# -----------------------------------
# MAIN FLOW
# -----------------------------------

if uploaded_file:

    # -----------------------------------
    # Resume Upload & ATS Analysis
    # -----------------------------------

    with st.spinner(
        "Analyzing Resume..."
    ):

        response = requests.post(
            "http://127.0.0.1:8000/upload-resume",
            files={
                "file": uploaded_file
            }
        )

    data = response.json()

    st.success(
        "Resume Uploaded Successfully"
    )

    st.divider()

    # -----------------------------------
    # ATS ANALYSIS
    # -----------------------------------

    st.header("📊 ATS Analysis")

    st.markdown(
        data["ats_analysis"]
    )

    st.divider()

    # -----------------------------------
    # JD MATCHING
    # -----------------------------------

    st.header(
        "🎯 Job Description Matching"
    )

    jd = st.text_area(
        "Paste Job Description"
    )

    if st.button(
        "Match Resume"
    ):

        with st.spinner(
            "Matching Resume..."
        ):

            match_response = requests.post(
                "http://127.0.0.1:8000/jd-match",
                json={
                    "resume_text":
                    data["resume_text"],

                    "jd_text":
                    jd
                }
            )

        match_data = (
            match_response.json()
        )

        st.subheader(
            "📌 Match Analysis"
        )

        if "response" in match_data:

            st.markdown(
                match_data["response"]
            )

        else:

            st.write(match_data)

    st.divider()

    # -----------------------------------
    # INTERVIEW QUESTION GENERATOR
    # -----------------------------------

    st.header(
        "💡 AI Interview Questions"
    )

    if st.button(
        "Generate Interview Questions"
    ):

        with st.spinner(
            "Generating Questions..."
        ):

            question_response = requests.post(
                "http://127.0.0.1:8000/generate-questions",
                json={
                    "resume_text":
                    data["resume_text"]
                }
            )

        question_data = (
            question_response.json()
        )

        st.subheader(
            "🧠 Suggested Questions"
        )

        if "questions" in question_data:

            st.markdown(
                question_data["questions"]
            )

        else:

            st.write(question_data)

    st.divider()

    # -----------------------------------
    # AI MOCK INTERVIEW
    # -----------------------------------

    st.header(
        "🎤 AI Mock Interview"
    )

    # Generate Question

    if st.button(
        "Start Mock Interview"
    ):

        with st.spinner(
            "Generating Interview Question..."
        ):

            response = requests.post(
                "http://127.0.0.1:8000/mock-interview",
                json={
                    "resume_text":
                    data["resume_text"]
                }
            )

        question_data = response.json()

        # Save question in session state

        st.session_state[
            "mock_question"
        ] = question_data["question"]

    # Show Question

    if "mock_question" in st.session_state:

        st.subheader(
            "🗣 Interview Question"
        )

        st.markdown(
            st.session_state[
                "mock_question"
            ]
        )

        answer = st.text_area(
            "Write Your Answer",
            key="answer_box"
        )

        # Evaluate Answer

        if st.button(
            "Evaluate Answer"
        ):

            with st.spinner(
                "Evaluating Answer..."
            ):

                feedback_response = requests.post(
                    "http://127.0.0.1:8000/evaluate-answer",
                    json={
                        "question":
                        st.session_state[
                            "mock_question"
                        ],

                        "answer":
                        answer
                    }
                )

            feedback_data = (
                feedback_response.json()
            )

            st.subheader(
                "📈 AI Feedback"
            )

            if "feedback" in feedback_data:

                st.markdown(
                    feedback_data[
                        "feedback"
                    ]
                )

            else:

                st.write(
                    feedback_data
                )