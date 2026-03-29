from langchain_community.document_loaders import PyPDFLoader

def load_pdf(path):
    try:
        loader = PyPDFLoader(path)
        return loader.load()
    except Exception as e:
        raise Exception(f"PDF Load Error: {str(e)}")