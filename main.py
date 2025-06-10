import time
import pandas as pd
from utils.telegram import send_telegram_alert
from utils.analyzer import analyze_market
from utils.indicators import fetch_price_data, calculate_indicators
from config import SYMBOLS
for symbol in SYMBOLS:
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
