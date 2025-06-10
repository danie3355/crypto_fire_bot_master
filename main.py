import time
import schedule
from utils.indicators import fetch_price_data, calculate_indicators
from utils.analyzer import analyze_market
from utils.telegram import send_telegram_alert
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

symbols = ["BTCUSDT", "ETHUSDT", "DOGEUSDT", "SOLUSDT"]
interval = "15m"
limit = 100

def analyze_and_alert(symbol):
    try:
        df = fetch_price_data(symbol, interval, limit)
        df = calculate_indicators(df)
        action, analysis, target = analyze_market(df)
        if action:
            message = f"{action.upper()} {symbol} AGORA!\n🎯 Alvo estimado: {target}\n📊 Análise: {analysis}"
            send_telegram_alert(message)
    except Exception as e:
        print(f"Erro ao analisar {symbol}: {e}")

def job():
    for symbol in symbols:
        analyze_and_alert(symbol)

# Executar a cada 5 minutos
schedule.every(5).minutes.do(job)

if __name__ == "__main__":
    job()  # executa no início
    while True:
        schedule.run_pending()
        time.sleep(1)
