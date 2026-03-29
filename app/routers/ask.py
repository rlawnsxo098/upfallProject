from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.core.dependencies import get_graph

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
def ask(
    req: QuestionRequest,
    graph = Depends(get_graph)
):
    try:
        result = graph.invoke({
            "question": req.question,
            "refined_question": "",
            "context": "",
            "answer": ""
        })

        return {"answer": result["answer"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))