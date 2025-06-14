import time
from utils.telegram import send_telegram_message
from utils.analyzer import analyze_market
from config import CHECK_INTERVAL

# Lista de símbolos a analisar (podes adicionar mais se quiseres)
SYMBOLS = ["BTCUSDT", "DOGEUSDT", "SOLUSDT", "ETHUSDT"]

def main():
    while True:
        for symbol in SYMBOLS:
            try:
                result = analyze_market(symbol)

                if result and result.get("signal") in ["buy", "sell"]:
                    action = "COMPRA AGORA" if result["signal"] == "buy" else "VENDE JÁ"
                    message = (
                        f"🚨 {action}\n\n"
                        f"💰 Cripto: {result['symbol']}\n"
                        f"📊 Tipo: {result['trade_type']}\n"
                        f"🎯 Alvo estimado: {result['target_price']:.4f}\n"
                        f"⏱️ Tempo estimado: {result['estimated_time']} horas\n"
                        f"💡 Justificativa: {result['reason']}\n"
                        f"📈 Preço atual: {result['current_price']:.4f}"
                    )
                    send_telegram_message(message)

            except Exception as e:
                send_telegram_message(f"❌ Erro no bot com {symbol}: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
