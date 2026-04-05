from abc import ABC, abstractmethod
from src.domain.entities.chat import ChatPrompt

class IChatRepository(ABC):
    @abstractmethod
    async def save(self, chat: ChatPrompt) -> None:
        pass