from fastapi import FastAPI
from signal_sender import send_crypto_signal

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Crypto Signal Bot is Running."}

@app.get("/send-signal")
def send_signal():
    success = send_crypto_signal()
    return {"status": "sent" if success else "failed"}
