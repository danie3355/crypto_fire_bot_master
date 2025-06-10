import pandas as pd
import ta

def calculate_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(close=df['close'], window=14).rsi()
    df['ema_fast'] = ta.trend.EMAIndicator(close=df['close'], window=9).ema_indicator()
    df['ema_slow'] = ta.trend.EMAIndicator(close=df['close'], window=21).ema_indicator()
    return df
