from langchain.prompts import PromptTemplate

from app.services.llm_service import llm

from app.core.prompts import (
    MOCK_INTERVIEW_PROMPT
)

def generate_mock_question(
    resume_text
):

    prompt = PromptTemplate(
        template=MOCK_INTERVIEW_PROMPT,
        input_variables=["resume"]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "resume": resume_text
        }
    )

    return response.content