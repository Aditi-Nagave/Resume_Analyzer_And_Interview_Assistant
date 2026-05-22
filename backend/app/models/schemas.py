from pydantic import BaseModel

class JDRequest(BaseModel):

    resume_text: str
    jd_text: str