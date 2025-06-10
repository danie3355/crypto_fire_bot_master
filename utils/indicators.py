import pandas as pd

def calculate_indicators(df):
    df['ema_fast'] = df['close'].ewm(span=9, adjust=False).mean()
    df['ema_slow'] = df['close'].ewm(span=21, adjust=False).mean()
    return df

def fetch_price_data(symbol):
    import requests

    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=100'
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'num_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])

    df['close'] = df['close'].astype(float)
    return df
