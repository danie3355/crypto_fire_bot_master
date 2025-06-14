import pandas as pd

def calculate_indicators(df: pd.DataFrame) -> dict:
    df["EMA20"] = df["close"].ewm(span=20).mean()
    df["EMA50"] = df["close"].ewm(span=50).mean()
    df["RSI"] = compute_rsi(df["close"], 14)
    df["MACD"] = df["close"].ewm(span=12).mean() - df["close"].ewm(span=26).mean()

    latest = df.iloc[-1]
    return {
        "ema_trend": "bullish" if latest["EMA20"] > latest["EMA50"] else "bearish",
        "rsi": latest["RSI"],
        "macd": latest["MACD"]
    }

def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
