import time
from utils.indicators import get_ema_signals
from utils.analyzer import analyze_market
from utils.telegram import send_telegram_alert
from utils.data import fetch_price_data

symbols = ["BTCUSDT", "ETHUSDT", "DOGEUSDT", "SOLUSDT"]

def analyze_and_alert(symbol):
    try:
        df = fetch_price_data(symbol)
        df = get_ema_signals(df)

        action, analysis, target = analyze_market(df)

        if action:
            message = f"{action.upper()} {symbol} AGORA!\n🎯 Alvo estimado: {target}\n📊 Análise: {analysis}"
            send_telegram_alert(message)
        else:
            print(f"{symbol}: Sem sinal claro.")

    except Exception as e:
        print(f"Erro ao analisar {symbol}: {e}")

if __name__ == "__main__":
    while True:
        for symbol in symbols:
            analyze_and_alert(symbol)
        time.sleep(300)
