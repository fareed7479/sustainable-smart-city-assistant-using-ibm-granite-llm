from fastapi import APIRouter, UploadFile, File, HTTPException
from document_embedder import document_embedder

router = APIRouter()

@router.post("/policy/upload")
async def upload_policy(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are supported.")
    content = await file.read()
    text = content.decode("utf-8")
    # Split text into chunks (e.g., paragraphs)
    chunks = [chunk.strip() for chunk in text.split("\\n\\n") if chunk.strip()]
    docs = [(str(i), chunk) for i, chunk in enumerate(chunks)]
    document_embedder.upsert_documents(docs)
    return {"status": f"Uploaded {len(docs)} document chunks."}

@router.get("/policy/search")
async def search_policy(query: str):
    results = document_embedder.query(query)
    hits = [{"id": match.id, "score": match.score} for match in results]
    return {"results": hits}
