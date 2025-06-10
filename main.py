import time
from utils.indicators import fetch_price_data, calculate_indicators
from utils.analyzer import analyze_market
from utils.telegram import send_telegram_alert

SYMBOLS = ["BTCUSDT", "ETHUSDT", "DOGEUSDT", "SOLUSDT"]
INTERVAL = "15m"
LIMIT = 100
SLEEP_TIME = 300  # 5 minutos entre análises

def analyze_and_alert(symbol):
    try:
        df = fetch_price_data(symbol, INTERVAL, LIMIT)
        df = calculate_indicators(df)
        action, analysis, target = analyze_market(df)
        message = f"{action.upper()} {symbol} AGORA!\n🎯 Alvo estimado: {target}\n📊 Análise: {analysis}"
        send_telegram_alert(message)
    except Exception as e:
        print(f"Erro ao analisar {symbol}: {e}")

if __name__ == "__main__":
    while True:
        for symbol in SYMBOLS:
            analyze_and_alert(symbol)
        time.sleep(SLEEP_TIME)
