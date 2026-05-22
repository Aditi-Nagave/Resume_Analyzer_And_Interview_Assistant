from langchain.prompts import PromptTemplate

from app.services.llm_service import llm

from app.core.prompts import JD_PROMPT

def match_resume_jd(
    resume_text,
    jd_text
):

    prompt = PromptTemplate(
        template=JD_PROMPT,
        input_variables=[
            "resume",
            "jd"
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "resume": resume_text,
            "jd": jd_text
        }
    )

    return {
        "response": response.content
    }