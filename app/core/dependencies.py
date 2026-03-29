from functools import lru_cache

from app.core.config import load_config
load_config()

from app.retriever.embedding import get_embedding
from app.retriever.vectorstore import create_vectorstore
from langchain_community.vectorstores import FAISS
from app.agent.graph import build_graph


@lru_cache()
def get_vectorstore(docs=None):
    if docs is None:
        docs = []
    embedding = get_embedding()
    return create_vectorstore(docs, embedding)
@lru_cache()
def get_graph():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()
    return build_graph(retriever)