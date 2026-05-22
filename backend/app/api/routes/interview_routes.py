from fastapi import APIRouter
from pydantic import BaseModel

from app.services.vectorstore_service import (
    create_vectorstore
)

from app.services.interview_service import (
    generate_interview_questions
)

router = APIRouter()

class QuestionRequest(BaseModel):
    resume_text: str

@router.post("/generate-questions")
def generate_questions(
    request: QuestionRequest
):

    vectorstore = create_vectorstore(
        request.resume_text
    )

    questions = generate_interview_questions(
        vectorstore
    )

    return {
        "questions": questions
    }