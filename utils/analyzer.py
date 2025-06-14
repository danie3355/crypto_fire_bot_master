from utils.data_fetcher import fetch_data
from utils.indicators import calculate_indicators

def analyze_market():
    symbol = "BTCUSDT"
    df = fetch_data(symbol)
    indicators = calculate_indicators(df)
    price = df["close"].iloc[-1]

    if indicators["ema_trend"] == "bullish" and indicators["rsi"] < 70:
        return {
            "signal": "buy",
            "symbol": symbol,
            "trade_type": "swing trade",
            "target_price": price * 1.05,
            "estimated_time": 12,
            "reason": "Tendência de alta (EMA), RSI favorável e MACD positivo",
            "current_price": price
        }
    elif indicators["ema_trend"] == "bearish" and indicators["rsi"] > 30:
        return {
            "signal": "sell",
            "symbol": symbol,
            "trade_type": "swing trade",
            "target_price": price * 0.95,
            "estimated_time": 8,
            "reason": "Tendência de baixa (EMA), RSI elevado e MACD negativo",
            "current_price": price
        }
    else:
        return None
