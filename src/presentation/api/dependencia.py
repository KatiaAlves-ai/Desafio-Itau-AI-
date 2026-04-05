from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database.model import get_db, SQLAlchemyChatRepository
from src.services.clients.llm_client import OpenRouterClient
from src.services.chat_service import ChatService

def get_chat_service(db: AsyncSession = Depends(get_db)):
    repo = SQLAlchemyChatRepository(db)
    
    llm_client = OpenRouterClient()
    
    return ChatService(repo, llm_client)