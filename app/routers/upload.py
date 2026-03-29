from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
import os

from app.core.dependencies import get_vectorstore
from app.retriever.loader import load_pdf
from app.retriever.vectorstore import split_docs_only

router = APIRouter()

UPLOAD_DIR = os.getenv("DOWN_LOAD_URL")

@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...),
    vectorstore = Depends(get_vectorstore)
):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        docs = load_pdf(file_path)
        split_docs = split_docs_only(docs)

        vectorstore.add_documents(split_docs)
        return {"message": f"{file.filename} Success Upload"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))