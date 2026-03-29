from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_docs_only(docs):
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        return splitter.split_documents(docs)
    except Exception as e:
        raise Exception(f"Split Error: {str(e)}")


def create_vectorstore(docs, embedding):
    try:
        if not docs:
            #빈 Object는 FAISS 생성이 불가.
            return FAISS.from_texts(["init document"], embedding)
        split_docs = split_docs_only(docs)
        return FAISS.from_documents(split_docs, embedding)
    except Exception as e:
        raise Exception(f"VectorStore Error: {str(e)}")