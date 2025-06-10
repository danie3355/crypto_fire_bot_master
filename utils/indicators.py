import pandas as pd

def get_ema_signals(df, fast=9, slow=21):
    df['ema_fast'] = df['close'].ewm(span=fast, adjust=False).mean()
    df['ema_slow'] = df['close'].ewm(span=slow, adjust=False).mean()
    return df
