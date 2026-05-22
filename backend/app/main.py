from fastapi import FastAPI

from app.api.routes.resume_routes import (
    router as resume_router
)

from app.api.routes.jd_routes import (
    router as jd_router
)

from app.api.routes.interview_routes import (
    router as interview_router
)

from app.api.routes.mock_interview_routes import (
    router as mock_router
)

from app.api.routes.voice_routes import (
    router as voice_router
)

app = FastAPI(
    title="AI Resume GenAI System"
)

app.include_router(resume_router)
app.include_router(jd_router)
app.include_router(interview_router)
app.include_router(mock_router)
app.include_router(voice_router)

@app.get("/")
def home():

    return {
        "message":
        "AI Resume GenAI System Running"
    }