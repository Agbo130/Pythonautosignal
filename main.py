from fastapi import FastAPI
import uvicorn
from signal_sender import send_crypto_signal
import threading
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Bot is running!"}

def run_bot():
    while True:
        send_crypto_signal()
        time.sleep(900)  # 15 minutes

if __name__ == "__main__":
    # Start bot in a background thread
    threading.Thread(target=run_bot).start()
    uvicorn.run(app, host="0.0.0.0", port=8080)
