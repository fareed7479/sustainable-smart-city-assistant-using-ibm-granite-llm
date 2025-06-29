from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Feedback(BaseModel):
    name: str
    category: str
    message: str

@router.post("/feedback")
async def submit_feedback(feedback: Feedback):
    # Placeholder: store feedback or send notification
    return {"status": "Feedback received"}
