from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langgraph.graph import StateGraph, tool
from typing import TypedDict

class PDFQuestionState(TypedDict):
    question: str
    docs: list

@tool
def retrieve_from_pdf(state: PDFQuestionState) -> PDFQuestionState:
    vectorstore = FAISS.load_local("embeddings/faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(state["question"])
    return {"question": state["question"], "docs": docs}
