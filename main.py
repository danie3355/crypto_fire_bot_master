import time
import pandas as pd
from utils.indicators import add_indicators
from utils.analyzer import analyze_market
from utils.telegram import send_telegram_alert
from utils.data_fetcher import fetch_price_data
from config import SYMBOLS, CHECK_INTERVAL

def analyze_and_alert(symbol):
   try:
    df = fetch_price_data(symbol)
    df = calculate_indicators(df)
    action, analysis, target = analyze_market(df)

    message = f"{action.upper()} {symbol} AGORA!"
    message += f"\n🎯 Alvo estimado: {target}"
    message += f"\n📊 Análise: {analysis}"

    send_telegram_alert(message)

except Exception as e:
    print(f"Erro ao analisar {symbol}: {e}")

if __name__ == "__main__":
    while True:
        for symbol in SYMBOLS:
            analyze_and_alert(symbol)
        time.sleep(CHECK_INTERVAL)
