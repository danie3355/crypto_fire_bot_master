import pandas as pd
import requests
from utils.indicators import generate_signal

def get_price_data(symbol):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=100'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    df['close'] = df['close'].astype(float)
    return df[['close']]

def analyze_market(symbol):
    try:
        df = get_price_data(symbol)
        signal, target, strategy = generate_signal(df)

        if signal:
            return {
                "symbol": symbol,
                "action": signal,
                "price_now": df['close'].iloc[-1],
                "target_price": round(target, 4),
                "strategy": strategy,
                "timeframe": "1h"
            }
        else:
            return None
    except Exception as e:
        return {"error": str(e)}
