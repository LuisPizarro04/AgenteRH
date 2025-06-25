from langgraph.graph import StateGraph
from nodes.retriever_node import retrieve_from_pdf
from nodes.answer_node import answer_question

class GraphState(TypedDict):
    question: str
    docs: list
    answer: str

# Construir el grafo
graph = StateGraph(GraphState)

graph.add_node("retrieve", retrieve_from_pdf)
graph.add_node("answer", answer_question)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "answer")
graph.set_finish_point("answer")

faq_graph = graph.compile()
