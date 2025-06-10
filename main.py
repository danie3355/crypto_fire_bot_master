# main.py

import requests
import pandas as pd
import time
from config import SYMBOLS
from utils.analyzer import analyze_market
from utils.telegram import send_telegram_message

def get_klines(symbol, interval='15m', limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
        ])
        df['close'] = pd.to_numeric(df['close'])
        return df
    except Exception as e:
        print(f"Erro ao obter dados para {symbol}: {e}")
        return None

def main_loop():
    while True:
        for symbol in SYMBOLS:
            df = get_klines(symbol)
            if df is not None:
                decisao, explicacao = analyze_market(df)
                if decisao:
                    preco_atual = df['close'].iloc[-1]
                    mensagem = f"{decisao} ({symbol})\nPreço atual: {preco_atual:.4f}\n📊 {explicacao}"
                    send_telegram_message(mensagem)
        time.sleep(900)  # Espera 15 minutos

if __name__ == "__main__":
    main_loop()
