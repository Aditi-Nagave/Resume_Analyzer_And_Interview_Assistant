from app.services.rag_service import (
    create_rag_chain
)

from app.core.prompts import (
    INTERVIEW_PROMPT
)

def generate_interview_questions(
    vectorstore
):

    chain = create_rag_chain(
        vectorstore,
        INTERVIEW_PROMPT
    )

    response = chain.invoke(
        {
            "query":
            "Generate interview questions"
        }
    )

    return response["result"]