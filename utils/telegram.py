# utils/telegram.py

import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_alert(message: str) -> None:
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except Exception as e:
        print(f"Erro ao enviar mensagem para o Telegram: {e}")
