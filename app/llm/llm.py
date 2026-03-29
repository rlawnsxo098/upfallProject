# OpenAI API
# from langchain_openai import ChatOpenAI

# def get_llm():
#     try:
#         return ChatOpenAI(model="gpt-4o-mini", temperature=0)
#     except Exception as e:
#         raise Exception(f"LLM Init Error: {str(e)}")

#ollama
from langchain_ollama import OllamaLLM

def get_llm():
    try:
        return OllamaLLM(
            model="llama3",
            temperature=0
        )
    except Exception as e:
        raise Exception(f"LLM Init Error: {str(e)}")