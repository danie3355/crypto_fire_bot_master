import time
from config import SYMBOLS, CHECK_INTERVAL
from utils.telegram import send_telegram_message
from utils.analyzer import analyze_price
import requests

def fetch_price_data(symbol):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m&limit=10"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    data = response.json()
    return [{"close": float(candle[4])} for candle in data]

def main():
    while True:
        for symbol in SYMBOLS:
            price_data = fetch_price_data(symbol)
            if not price_data:
                continue

            decision, target, indicators = analyze_price(price_data)
            if decision:
                msg = f"{decision} {symbol}\n🎯 Alvo: {round(target, 5)}\n📊 Indicadores: {indicators}"
                send_telegram_message(msg)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
