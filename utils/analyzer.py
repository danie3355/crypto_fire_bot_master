import ccxt
import pandas as pd
from datetime import datetime, timedelta
from utils.indicators import apply_indicators

exchange = ccxt.binance()

symbols = {
    "BTC/USDT": "Bitcoin",
    "ETH/USDT": "Ethereum",
    "DOGE/USDT": "Dogecoin",
    "SOL/USDT": "Solana"
}

def fetch_data(symbol, timeframe='5m', limit=200):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def analyze_market():
    results = []
    for symbol, name in symbols.items():
        df = fetch_data(symbol)
        df = apply_indicators(df)

        last = df.iloc[-1]

        buy_signal = (
            last['rsi'] < 30 and
            last['ema20'] > last['ema50'] and
            last['macd'] > last['macd_signal']
        )
        sell_signal = (
            last['rsi'] > 70 and
            last['ema20'] < last['ema50'] and
            last['macd'] < last['macd_signal']
        )

        if buy_signal:
            entry = round(last['close'], 4)
            target = round(entry * 1.04, 4)
            tempo = "em 2-12h"
            tipo = "💥 Day Trade"
            results.append(f"📈 COMPRA AGORA {name}\n🎯 Alvo: {target} USD\n💰 Entrada: {entry} USD\n⏱️ Estimativa: {tempo}\n📊 Tipo: {tipo}")
        elif sell_signal:
            entry = round(last['close'], 4)
            target = round(entry * 0.96, 4)
            tempo = "em 1-8h"
            tipo = "⚠️ Swing Trade"
            results.append(f"🔻 VENDE JÁ {name}\n🎯 Alvo: {target} USD\n💰 Preço atual: {entry} USD\n⏱️ Estimativa: {tempo}\n📊 Tipo: {tipo}")
    return results
