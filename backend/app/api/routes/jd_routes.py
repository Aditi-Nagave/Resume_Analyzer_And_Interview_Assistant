from fastapi import APIRouter

from app.models.schemas import JDRequest

from app.services.jd_service import (
    match_resume_jd
)

router = APIRouter()

@router.post("/jd-match")
def jd_match(
    request: JDRequest
):

    return match_resume_jd(
        request.resume_text,
        request.jd_text
    )