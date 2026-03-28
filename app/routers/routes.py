from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

def create_routes(graph):
    @router.get("/ask")
    def getAsk():
        return {"answer": "answer"}
    
    @router.post("/ask")
    def ask(req: QuestionRequest):
        result = graph.invoke({
            "question": req.question,
            "context": "",
            "answer": ""
        })
        return {"answer": result["answer"]}
    
    return router