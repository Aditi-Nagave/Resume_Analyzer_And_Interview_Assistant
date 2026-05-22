from langchain.chains import RetrievalQA

from langchain.prompts import PromptTemplate

from app.core.memory import memory

from app.services.llm_service import llm

def create_rag_chain(
    vectorstore,
    prompt_template
):

    retriever = vectorstore.as_retriever()

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context"]
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        memory=memory,
        chain_type_kwargs={
            "prompt": prompt
        }
    )

    return chain