import requests
import pandas as pd

def fetch_data(symbol: str, interval: str = "1h", limit: int = 100) -> pd.DataFrame:
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"
    ])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    df = df[["open", "high", "low", "close", "volume"]].astype(float)
    return df
