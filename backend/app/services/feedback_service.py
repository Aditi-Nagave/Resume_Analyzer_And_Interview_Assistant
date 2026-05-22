from langchain.prompts import PromptTemplate

from app.services.llm_service import llm

from app.core.prompts import (
    FEEDBACK_PROMPT
)

def evaluate_answer(
    question,
    answer
):

    prompt = PromptTemplate(
        template=FEEDBACK_PROMPT,
        input_variables=[
            "question",
            "answer"
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question,
            "answer": answer
        }
    )

    return response.content