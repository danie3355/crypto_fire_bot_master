from utils.indicators import apply_indicators
from utils.data_fetcher import fetch_market_data

def analyze_market(symbol="DOGE/USDT"):
    df = fetch_market_data(symbol)
    df = apply_indicators(df)

    current_price = df['close'].iloc[-1]
    ema20 = df['ema20'].iloc[-1]
    ema50 = df['ema50'].iloc[-1]
    rsi = df['rsi'].iloc[-1]
    macd = df['macd'].iloc[-1]
    macd_signal = df['macd_signal'].iloc[-1]
    upper_band = df['bb_upper'].iloc[-1]
    lower_band = df['bb_lower'].iloc[-1]
    stoch_k = df['stoch_k'].iloc[-1]
    stoch_d = df['stoch_d'].iloc[-1]

    signal = None
    reason = ""
    target_price = current_price
    trade_type = "swing" if abs(macd - macd_signal) > 0.05 else "day"
    estimated_time = 4 if trade_type == "day" else 24

    if ema20 > ema50 and rsi > 50 and macd > macd_signal and current_price < upper_band:
        signal = "buy"
        reason = "Tendência de alta confirmada com RSI e MACD favoráveis"
        target_price = upper_band

    elif ema20 < ema50 and rsi < 50 and macd < macd_signal and current_price > lower_band:
        signal = "sell"
        reason = "Tendência de baixa confirmada com RSI e MACD desfavoráveis"
        target_price = lower_band

    if signal:
        return {
            "symbol": symbol,
            "signal": signal,
            "reason": reason,
            "target_price": target_price,
            "current_price": current_price,
            "trade_type": trade_type,
            "estimated_time": estimated_time,
            "rsi": rsi
        }
    return None
