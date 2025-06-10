def analyze_market(df):
    last = df.iloc[-1]
    previous = df.iloc[-2]

    buy_signal = last['ema_fast'] > last['ema_slow'] and previous['ema_fast'] <= previous['ema_slow']
    sell_signal = last['ema_fast'] < last['ema_slow'] and previous['ema_fast'] >= previous['ema_slow']

    if buy_signal:
        return "COMPRA AGORA", "📈 Expectativa de alta com alvo entre 5% a 15% acima.", "5–15% acima"
    elif sell_signal:
        return "VENDE JÁ", "⚠️ Expectativa de queda com possível correção de 5% a 12%.", "5–12% abaixo"
    else:
        return None, "⏸ Mercado neutro. Sem oportunidade clara agora.", "-"
