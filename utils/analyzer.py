 from utils.data_fetcher import fetch_ohlcv
from utils.indicators import apply_indicators

def analyze_market(symbol="SOLUSDT"):
    df = fetch_ohlcv(symbol)
    df = apply_indicators(df)

    last = df.iloc[-1]

    # Estratégia combinada para lucro (indicadores cruzados)
    ema_buy = last["ema20"] > last["ema50"]
    macd_buy = last["macd"] > last["macd_signal"]
    rsi_buy = last["rsi"] < 70 and last["rsi"] > 50

    ema_sell = last["ema20"] < last["ema50"]
    macd_sell = last["macd"] < last["macd_signal"]
    rsi_sell = last["rsi"] > 70

    if ema_buy and macd_buy and rsi_buy:
        return {
            "signal": "buy",
            "symbol": symbol,
            "trade_type": "swing trade",
            "target_price": last["close"] * 1.04,  # +4%
            "estimated_time": 12,
            "reason": "EMA 20 acima da 50, MACD positivo e RSI saudável",
            "current_price": last["close"]
        }

    elif ema_sell and macd_sell and rsi_sell:
        return {
            "signal": "sell",
            "symbol": symbol,
            "trade_type": "swing trade",
            "target_price": last["close"] * 0.96,  # -4%
            "estimated_time": 8,
            "reason": "EMA 20 abaixo da 50, MACD negativo e RSI alto",
            "current_price": last["close"]
        }

    return None
