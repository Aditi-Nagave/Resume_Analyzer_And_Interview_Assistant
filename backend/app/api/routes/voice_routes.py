from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil

from app.services.speech_service import (
    speech_to_text
)

router = APIRouter()

@router.post("/speech-to-text")

async def convert_audio(
    file: UploadFile = File(...)
):

    path = f"app/uploads/{file.filename}"

    with open(path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    text = speech_to_text(path)

    return {
        "text": text
    }