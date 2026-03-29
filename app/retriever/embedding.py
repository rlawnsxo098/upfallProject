# OpenAi API 사용 시 
# from langchain_openai import OpenAIEmbeddings

# def get_embedding():
#     return OpenAIEmbeddings()

# ollama 사용 시 
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )