# utils/data.py

import requests
import pandas as pd

def fetch_price_data(symbol: str, interval: str = "1h", limit: int = 100) -> pd.DataFrame:
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        df = pd.DataFrame(data, columns=[
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "number_of_trades",
            "taker_buy_base", "taker_buy_quote", "ignore"
        ])

        df["close"] = pd.to_numeric(df["close"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df[["timestamp", "close"]]

    except Exception as e:
        print(f"Erro ao buscar dados para {symbol}: {e}")
        return pd.DataFrame()
