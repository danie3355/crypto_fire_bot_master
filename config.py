import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Criptomoedas a monitorizar (podes mudar ou adicionar mais)
SYMBOLS = ["BTCUSDT", "DOGEUSDT", "ETHUSDT", "SOLUSDT"]

# Verificar a cada X segundos (podes mudar, 60 = 1 min)
CHECK_INTERVAL = 60
