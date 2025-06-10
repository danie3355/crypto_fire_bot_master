import pandas as pd
import requests
from utils.indicators import calculate_indicators
from utils.telegram import send_telegram_alert

def fetch_price_data(symbol):
    try:
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=5m&limit=100"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"[ERRO] Binance API para {symbol}: {e}")
        return None

    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close',
        'volume', 'close_time', 'quote_asset_volume',
        'number_of_trades', 'taker_buy_base_volume',
        'taker_buy_quote_volume', 'ignore'
    ])
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    df.dropna(inplace=True)
    return df

def analyze_and_alert(symbol):
    df = fetch_price_data(symbol)
    if df is None or df.empty:
        print(f"[ERRO] Dados inválidos para {symbol}")
        return

    df = calculate_indicators(df)
    last = df.iloc[-1]

    action = None
    if last['EMA_20'] > last['EMA_50'] and last['RSI'] < 70:
        action = 'compra'
    elif last['EMA_20'] < last['EMA_50'] and last['RSI'] > 30:
        action = 'venda'

    if action:
        message = f"{action.upper()} {symbol} AGORA!\n🎯 Alvo estimado: {last['close']:.4f}\n📊 RSI: {last['RSI']:.2f}"
        send_telegram_alert(message)
