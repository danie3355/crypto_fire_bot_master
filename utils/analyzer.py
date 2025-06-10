def analyze_market(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]

    signals = []

    # Exemplo: cruzamento de EMAs
    if prev['EMA_20'] < prev['EMA_50'] and last['EMA_20'] > last['EMA_50']:
        signals.append("cruzamento de alta (EMA20 > EMA50)")
        action = "COMPRA"
    elif prev['EMA_20'] > prev['EMA_50'] and last['EMA_20'] < last['EMA_50']:
        signals.append("cruzamento de baixa (EMA20 < EMA50)")
        action = "VENDA"
    else:
        return None, "Sem sinal claro", "-"

    # Confirmação com RSI
    if last['RSI'] < 30 and action == "COMPRA":
        signals.append("RSI em sobrevenda")
    elif last['RSI'] > 70 and action == "VENDA":
        signals.append("RSI em sobrecompra")
    else:
        return None, "Sinal não confirmado pelo RSI", "-"

    # Previsão de alvo simples
    if action == "COMPRA":
        price_target = round(last['close'] * 1.03, 4)
    else:
        price_target = round(last['close'] * 0.97, 4)

    analysis = " + ".join(signals)
    return action, analysis, price_target
