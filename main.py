import time
from utils.telegram import send_telegram_message
from utils.analyzer import analyze_market
from config import CHECK_INTERVAL

def main():
    while True:
        try:
            result = analyze_market()
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
            send_telegram_message(f"❌ Erro no bot: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
