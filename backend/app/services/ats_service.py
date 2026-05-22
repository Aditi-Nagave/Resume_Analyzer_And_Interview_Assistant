from app.services.rag_service import (
    create_rag_chain
)

from app.core.prompts import ATS_PROMPT

def analyze_resume(vectorstore):

    chain = create_rag_chain(
        vectorstore,
        ATS_PROMPT
    )

    response = chain.invoke(
        {
            "query": "Analyze this resume"
        }
    )

    return response["result"]