from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from granite_llm import granite_llm

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

import logging

@router.post("/chat/ask", response_model=ChatResponse)
async def chat_ask(request: ChatRequest):
    logging.debug(f"Received chat query: {request.query}")
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    response = granite_llm.ask(request.query)
    logging.debug(f"LLM response: {response}")
    return ChatResponse(response=response)
