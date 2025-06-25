from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langgraph.graph import tool

@tool
def answer_question(state: PDFQuestionState) -> dict:
    llm = ChatOpenAI(temperature=0)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=FAISS.load_local("embeddings/faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True).as_retriever()
    )
    response = chain.invoke({"question": state["question"], "chat_history": []})
    return {"answer": response["answer"]}
