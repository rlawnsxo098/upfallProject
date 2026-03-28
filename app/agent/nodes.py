from app.llm.llm import get_llm
from app.prompt.prompt import SYSTEM_PROMPT

llm = get_llm()

def retrieve_node(state, retriever):
    docs = retriever.get_relevant_documents(state["question"])
    context = "\n".join([doc.page_content for doc in docs])

    return {"context": context}

def answer_node(state):
    prompt = f"""
{SYSTEM_PROMPT}

[문서]
{state['context']}

[질문]
{state['question']}
"""

    response = llm.predict(prompt)

    return {"answer": response}