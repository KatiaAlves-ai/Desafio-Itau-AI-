from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class ChatPrompt:
    user_id: str
    prompt: str
    response: str = None
    model: str = None
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def update_response(self, response: str, model: str):
        self.response = response
        self.model = model