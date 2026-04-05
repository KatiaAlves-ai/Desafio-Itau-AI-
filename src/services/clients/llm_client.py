import httpx
import os
from tenacity import retry, stop_after_attempt, wait_exponential

class OpenRouterClient: 
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.url = "https://api.groq.com/openai/v1/chat/completions"
        
        self.model = "llama-3.3-70b-versatile"

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=6))
    async def get_completion(self, prompt: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, headers=headers, json=payload, timeout=30.0)
            
            if response.status_code != 200:
                print(f"--- ERRO GROQ ---")
                print(f"Status: {response.status_code}")
                print(f"Resposta: {response.text}")
                print(f"-----------------")
                response.raise_for_status()
                
            data = response.json()
            return {
                "text": data['choices'][0]['message']['content'],
                "model": data.get('model', self.model)
            }