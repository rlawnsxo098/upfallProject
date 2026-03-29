from langgraph.graph import StateGraph, END
from app.agent.state import AgentState
from app.agent.nodes import analyze_node, retrieve_node, answer_node

def build_graph(retriever):

    builder = StateGraph(AgentState)

    builder.add_node("analyze", analyze_node)
    builder.add_node("retrieve", lambda state: retrieve_node(state, retriever))
    builder.add_node("answer", answer_node)

    builder.set_entry_point("analyze")
    builder.add_edge("analyze", "retrieve")
    builder.add_edge("retrieve", "answer")
    builder.add_edge("answer", END)

    return builder.compile()