# utils/analyzer.py

from utils.indicators import calculate_ema, calculate_rsi, calculate_macd

def analyze_market(df):
    df['ema_fast'] = calculate_ema(df, period=9)
    df['ema_slow'] = calculate_ema(df, period=21)
    df['rsi'] = calculate_rsi(df)
    df['macd'], df['signal'], df['histogram'] = calculate_macd(df)

    latest = df.iloc[-1]

    # Condições de COMPRA
    if (
        latest['ema_fast'] > latest['ema_slow'] and
        latest['rsi'] < 70 and
        latest['macd'] > latest['signal']
    ):
        return "COMPRA AGORA", "Tendência de alta confirmada por EMA, RSI saudável e MACD positivo"

    # Condições de VENDA
    elif (
        latest['ema_fast'] < latest['ema_slow'] and
        latest['rsi'] > 30 and
        latest['macd'] < latest['signal']
    ):
        return "VENDE JÁ", "Tendência de queda confirmada por cruzamento de EMA, RSI e MACD negativo"

    return None, "Sem sinal claro no momento"
