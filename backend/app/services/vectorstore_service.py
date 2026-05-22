from langchain_community.vectorstores import Chroma

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_core.documents import Document

from app.services.embedding_service import (
    embedding_model
)

CHROMA_PATH = "app/vectorstore/chroma_db"

def create_vectorstore(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    docs = [
        Document(page_content=chunk)
        for chunk in chunks
    ]

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )

    return vectorstore