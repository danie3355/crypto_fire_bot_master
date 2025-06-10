import pandas as pd
import requests

def fetch_price_data(symbol: str, interval: str = "1h", limit: int = 100) -> pd.DataFrame:
    """
    Busca dados históricos de preço da Binance para o símbolo dado.

    :param symbol: Ex: 'BTCUSDT'
    :param interval: Intervalo de tempo (Ex: '1h', '4h', '1d')
    :param limit: Quantidade de velas (candles) a buscar
    :return: DataFrame com colunas: open_time, open, high, low, close, volume
    """
    url = f"https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])

    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df["close_time"] = pd.to_datetime(df["close_time"], unit="ms")
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df[["open_time", "open", "high", "low", "close", "volume"]]
