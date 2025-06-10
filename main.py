import time
from utils.analyzer import analyze_market
from utils.telegram import send_telegram_message

def main():
    while True:
        signals = analyze_market()
        for signal in signals:
            send_telegram_message(signal)
        time.sleep(300)  # analisa a cada 5 minutos

if __name__ == "__main__":
    main()
