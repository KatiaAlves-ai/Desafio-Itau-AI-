import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from src.presentation.api.controller import router as chat_router
from src.infrastructure.database.model import engine, Base

load_dotenv()
app = FastAPI()

import os
load_dotenv()

minha_chave = os.getenv("OPENROUTER_API_KEY")
if minha_chave:
    print(f"DEBUG: Chave carregada! Começa com: {minha_chave[:6]} e termina com: {minha_chave[-4:]}")
else:
    print("DEBUG: ERRO! Nenhuma chave foi encontrada no .env")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(chat_router, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)