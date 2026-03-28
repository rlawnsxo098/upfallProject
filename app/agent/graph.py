from langgraph.graph import StateGraph, END
from app.agent.state import AgentState
from app.agent.nodes import retrieve_node, answer_node

def build_graph(retriever):

    builder = StateGraph(AgentState)

    # 노드 추가
    builder.add_node("retrieve", lambda state: retrieve_node(state, retriever))
    builder.add_node("answer", answer_node)

    # 흐름 정의
    builder.set_entry_point("retrieve")
    builder.add_edge("retrieve", "answer")
    builder.add_edge("answer", END)

    return builder.compile()