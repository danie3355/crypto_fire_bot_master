import time
from utils.telegram import send_telegram_alert
from utils.analyzer import analyze_market
from config import SYMBOLS, CHECK_INTERVAL

def run_bot():
    while True:
        for symbol in SYMBOLS:
            try:
                action, analysis, price_target = analyze_market(symbol)
                if action:
                    message = f"{action.upper()} {symbol} AGORA!\n🎯 Alvo estimado: {price_target}\n📊 Análise: {analysis}"
                    send_telegram_alert(message)
            except Exception as e:
                print(f"Erro ao analisar {symbol}: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run_bot()
