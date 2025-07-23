import requests

TELEGRAM_BOT_TOKEN = "7970786658:AAEsc2pTqZBnVvxjMh3oAWarEhdOFIfDPW4"
TELEGRAM_CHAT_ID = "-1002813054305"  # Group chat ID

def get_crypto_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["bitcoin"]["usd"]
        return price
    except Exception as e:
        print(f"❌ Error fetching price: {e}")
        return None

def send_crypto_signal(price):
    message = (
        f"🚀 *Crypto Signal*\n"
        f"🪙 Bitcoin\n"
        f"💰 Entry: ${price}\n"
        f"🎯 Take Profit: ${round(price * 1.01, 2)}\n"
        f"🛑 Stop Loss: ${round(price * 0.99, 2)}\n"
        f"📅 Time: Now\n"
        f"#BTC #Crypto #Signal"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Telegram group signal sent!")
        else:
            print(f"❌ Failed to send: {response.status_code}")
    except Exception as e:
        print(f"❌ Telegram error: {e}")
