from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from src.presentation.api.dependencia import get_chat_service

router = APIRouter()

class ChatRequest(BaseModel):
    userId: str
    prompt: str
    

@router.post("/chat")
async def chat_endpoint(request: ChatRequest, service = Depends(get_chat_service)):
    try:
        result = await service.process_prompt(request.userId, request.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))