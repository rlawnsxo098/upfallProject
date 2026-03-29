from fastapi import FastAPI

from app.retriever.loader import load_pdf
from app.retriever.vectorstore import create_vectorstore
from app.retriever.embedding import get_embedding

from app.routers.routes import router as root_router
from app.routers.ask import router as ask_router
from app.routers.upload import router as upload_router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    try:
        create_vectorstore(load_pdf("app/data/sample.pdf"), get_embedding())
        print("Success Loding")
    except Exception as e:
        print(f"Startup Error: {str(e)}")

app.include_router(root_router)
app.include_router(ask_router)
app.include_router(upload_router)