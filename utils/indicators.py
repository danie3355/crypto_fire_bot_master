import pandas as pd

def calculate_ema(data, period):
    return data['close'].ewm(span=period, adjust=False).mean()

def calculate_rsi(data, period=14):
    delta = data['close'].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def calculate_macd(data):
    ema12 = calculate_ema(data, 12)
    ema26 = calculate_ema(data, 26)
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

def generate_signal(data):
    ema20 = calculate_ema(data, 20)
    ema50 = calculate_ema(data, 50)
    rsi = calculate_rsi(data)
    macd, signal = calculate_macd(data)

    last_price = data['close'].iloc[-1]
    last_rsi = rsi.iloc[-1]
    last_macd = macd.iloc[-1]
    last_signal = signal.iloc[-1]

    if last_rsi < 30 and last_macd > last_signal and ema20.iloc[-1] > ema50.iloc[-1]:
        return "COMPRA AGORA", last_price * 1.05, "swing trade"
    elif last_rsi > 70 and last_macd < last_signal and ema20.iloc[-1] < ema50.iloc[-1]:
        return "VENDE JÁ", last_price * 0.95, "swing trade"
    else:
        return None, None, None
