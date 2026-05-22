from pydantic import BaseModel

class JDRequest(BaseModel):

    resume_text: str
    jd_text: str

class InterviewRequest(
    BaseModel
):

    resume_text: str

class FeedbackRequest(
    BaseModel
):

    question: str
    answer: str