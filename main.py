import schedule
import time
from utils.analyzer import analyze_and_alert

symbols = ['BTCUSDT', 'ETHUSDT', 'DOGEUSDT', 'SOLUSDT']

def job():
    for symbol in symbols:
        try:
            analyze_and_alert(symbol)
        except Exception as e:
            print(f"Erro ao analisar {symbol}: {e}")

schedule.every(5).minutes.do(job)

if __name__ == "__main__":
    print("🔥 Bot de Alertas Iniciado (24/7)...")
    job()  # executa na inicialização
    while True:
        schedule.run_pending()
        time.sleep(1)
