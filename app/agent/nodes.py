from app.llm.llm import get_llm
from app.prompt.prompt import SYSTEM_PROMPT

llm = get_llm()


def analyze_node(state):
    try:
        prompt = f"""
    질문을 더 명확하게 재작성하라:
    {state['question']}
    """
        refined = llm.invoke(prompt)
        return {"refined_question": refined}

    except Exception as e:
        return {"refined_question": state["question"]}


def retrieve_node(state, retriever):
    try:
        docs = retriever.get_relevant_documents(state["refined_question"])

        context = "\n".join([
            f"[page {doc.metadata.get('page', 'unknown')}] {doc.page_content}"
            for doc in docs
        ])

        return {"context": context}

    except Exception as e:
        return {"context": ""}


def answer_node(state):
    try:
        prompt = f"""
{SYSTEM_PROMPT}

[문서]
{state['context']}

[질문]
{state['question']}
"""
        #answer = llm.predict(prompt)
        answer = llm.invoke(prompt)
        return {"answer": answer}

    except Exception as e:
        return {"answer": "답변 생성 중 오류가 발생했습니다."}

def validate_node(state):
    try:
        answer = state["answer"]

        if "모르" in answer or len(answer) < 20:
            return {
                "answer": "문서에서 충분한 정보를 찾지 못했습니다. 질문을 구체화해 주세요."
            }

        return {"answer": answer}

    except Exception as e:
        return {"answer": "검증 단계에서 오류가 발생했습니다."}