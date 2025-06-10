import pandas as pd
import ta

def apply_indicators(df):
    df['ema20'] = ta.trend.ema_indicator(df['close'], window=20).ema_indicator()
    df['ema50'] = ta.trend.ema_indicator(df['close'], window=50).ema_indicator()
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    macd = ta.trend.macd(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    return df
