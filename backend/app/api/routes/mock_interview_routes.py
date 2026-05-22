from fastapi import APIRouter

from app.models.schemas import (
    InterviewRequest,
    FeedbackRequest
)

from app.services.mock_interview_service import (
    generate_mock_question
)

from app.services.feedback_service import (
    evaluate_answer
)

router = APIRouter()

@router.post("/mock-interview")

def mock_interview(
    request: InterviewRequest
):

    response = generate_mock_question(
        request.resume_text
    )

    return {
        "question": response
    }

@router.post("/evaluate-answer")

def evaluate(
    request: FeedbackRequest
):

    response = evaluate_answer(
        request.question,
        request.answer
    )

    return {
        "feedback": response
    }