
import pandas as pd
import ta

def apply_indicators(df):
    df['ema20'] = ta.trend.ema_indicator(df['close'], window=20).ema_indicator()
    df['ema50'] = ta.trend.ema_indicator(df['close'], window=50).ema_indicator()
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
    df['macd'] = ta.trend.macd_diff(df['close'])
    bb = ta.volatility.BollingerBands(df['close'], window=20, window_dev=2)
    df['bb_bbm'] = bb.bollinger_mavg()
    df['bb_bbh'] = bb.bollinger_hband()
    df['bb_bbl'] = bb.bollinger_lband()
    stoch = ta.momentum.StochasticOscillator(df['high'], df['low'], df['close'], window=14, smooth_window=3)
    df['stoch_k'] = stoch.stoch()
    df['stoch_d'] = stoch.stoch_signal()
    df['adx'] = ta.trend.ADXIndicator(df['high'], df['low'], df['close'], window=14).adx()
    vwap = (df['volume'] * (df['high'] + df['low'] + df['close']) / 3).cumsum() / df['volume'].cumsum()
    df['vwap'] = vwap
    return df

  
