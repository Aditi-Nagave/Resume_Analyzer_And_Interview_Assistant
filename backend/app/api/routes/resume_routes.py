from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import os

from app.services.parser_service import (
    parse_pdf,
    parse_docx
)

from app.services.vectorstore_service import (
    create_vectorstore
)

from app.services.ats_service import (
    analyze_resume
)

router = APIRouter()

UPLOAD_DIR = "app/uploads"

@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    if file.filename.endswith(".pdf"):

        resume_text = parse_pdf(file_path)

    else:

        resume_text = parse_docx(file_path)

    vectorstore = create_vectorstore(
        resume_text
    )

    ats_analysis = analyze_resume(
        vectorstore
    )

    return {
        "resume_text": resume_text,
        "ats_analysis": ats_analysis
    }