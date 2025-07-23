import requests
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID")

def fetch_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        return data['bitcoin']['usd']
    except Exception as e:
        print("❌ Error fetching price:", e)
        return None

def send_crypto_signal():
    price = fetch_price()
    if price:
        entry = price
        sl = round(price * 0.98, 2)
        tp = round(price * 1.02, 2)
        message = f"🚀 *Crypto Signal*

*Entry:* ${entry}
*SL:* ${sl}
*TP:* ${tp}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        r = requests.post(url, data=data)
        return r.status_code == 200
    return False
