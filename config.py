# config.py

# Tempo em segundos entre análises (ex: 900 = 15 minutos)
CHECK_INTERVAL = 900  

# Token e Chat ID do teu Bot Telegram
TELEGRAM_BOT_TOKEN = '7783305563:AAGZ5fkdH662e9ISSx-Tthtw2vLYYxn1VBQ'
TELEGRAM_CHAT_ID = '1466428936'

# Lista de criptomoedas para monitorar
SYMBOLS = [
    "BTC/USDT",
    "ETH/USDT",
    "SOL/USDT",
    "DOGE/USDT"
]

# Configurações dos indicadores
INDICATOR_SETTINGS = {
    "ema_fast": 9,
    "ema_slow": 21,
    "rsi_period": 14,
    "rsi_buy_threshold": 30,
    "rsi_sell_threshold": 70,
    "macd_fast": 12,
    "macd_slow": 26,
    "macd_signal": 9
}
