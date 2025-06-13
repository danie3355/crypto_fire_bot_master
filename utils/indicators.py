import pandas as pd
import pandas_ta as ta
from numpy import nan
def apply_indicators(df):
    # Garante que os dados estão em ordem cronológica
    df = df.copy()
    df.sort_index(inplace=True)

    # Calcula indicadores técnicos
    df['ema20'] = ta.ema(df['close'], length=20)
    df['ema50'] = ta.ema(df['close'], length=50)
    df['rsi'] = ta.rsi(df['close'], length=14)

    macd = ta.macd(df['close'])
    df['macd'] = macd['MACD_12_26_9']
    df['macd_signal'] = macd['MACDs_12_26_9']

    return df
