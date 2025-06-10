import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        if not response.ok:
            print(f"[ERRO] Telegram falhou: {response.text}")
    except Exception as e:
        print(f"[ERRO] Falha no envio para Telegram: {e}")
