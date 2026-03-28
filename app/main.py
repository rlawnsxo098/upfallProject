from fastapi import FastAPI

import os
from dotenv import load_dotenv

load_dotenv()

from app.routers.routes import create_routes
from app.retriever.loader import load_pdf
from app.retriever.embedding import get_embedding
from app.retriever.vectorstore import create_vectorstore
from app.agent.graph import build_graph

app = FastAPI()

# 서버 시작 시 1회 실행
docs = load_pdf("app/data/sample.pdf")
print(docs[0])

embedding = get_embedding()
vectorstore = create_vectorstore(docs, embedding)
retriever = vectorstore.as_retriever()

graph = build_graph(retriever)

# 라우터 연결
# app.include_router(create_routes())
app.include_router(create_routes(graph))