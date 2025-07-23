# main.py
from fastapi import FastAPI
import asyncio
from signal_sender import send_crypto_signal

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "✅ Crypto Signal Bot is Running"}

@app.on_event("startup")
async def start_bot():
    asyncio.create_task(send_crypto_signal())
