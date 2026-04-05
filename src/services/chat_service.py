from src.domain.entities.chat import ChatPrompt

class ChatService:
    def __init__(self, repo, llm_client):
        self.repo = repo
        self.llm_client = llm_client

    async def process_prompt(self, user_id: str, prompt_text: str):
        chat = ChatPrompt(user_id=user_id, prompt=prompt_text)
        llm_data = await self.llm_client.get_completion(prompt_text)
        chat.update_response(llm_data["text"], llm_data["model"])
        await self.repo.save(chat)
        return chat