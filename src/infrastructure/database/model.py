from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = "sqlite+aiosqlite:///./storage.db"
engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class ChatModel(Base):
    __tablename__ = "chats"
    id = Column(String, primary_key=True)
    user_id = Column(String)
    prompt = Column(Text)
    response = Column(Text)
    model = Column(String)
    timestamp = Column(DateTime)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


from src.domain.repository.chat_repo import IChatRepository
from src.domain.entities.chat import ChatPrompt

class SQLAlchemyChatRepository(IChatRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, chat: ChatPrompt) -> None:
        db_chat = ChatModel(
            id=chat.id, user_id=chat.user_id, prompt=chat.prompt,
            response=chat.response, model=chat.model, timestamp=chat.timestamp
        )
        self.session.add(db_chat)
        await self.session.commit()