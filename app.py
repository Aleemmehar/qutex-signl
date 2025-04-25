import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="QuteX Signal Bot", layout="centered")

st.title("📈 QuteX 1-Minute Candle Signal Bot")
st.markdown("Signals based on strong candle patterns (Demo Version)")

# Simulate candle data (for demo purpose)
def get_fake_candle():
    open_price = random.uniform(1.0, 2.0)
    close_price = open_price + random.uniform(-0.05, 0.05)
    high = max(open_price, close_price) + random.uniform(0.01, 0.03)
    low = min(open_price, close_price) - random.uniform(0.01, 0.03)
    return {
        "open": round(open_price, 4),
        "close": round(close_price, 4),
        "high": round(high, 4),
        "low": round(low, 4)
    }

# Determine signal from candle pattern
def get_signal(candle):
    body = abs(candle['close'] - candle['open'])
    wick_upper = candle['high'] - max(candle['close'], candle['open'])
    wick_lower = min(candle['close'], candle['open']) - candle['low']

    if body > wick_upper and body > wick_lower:
        if candle['close'] > candle['open']:
            return "📘 BUY Signal"
        else:
            return "📕 SELL Signal"
    return "➖ No Strong Signal"

if st.button("🔁 Get Latest Signal"):
    candle = get_fake_candle()
    signal = get_signal(candle)

    st.subheader("🕐 Candle Data")
    st.json(candle)

    st.subheader("📊 Signal")
    st.success(signal) if "BUY" in signal else st.error(signal) if "SELL" in signal else st.info(signal)

st.markdown("---")
st.caption("Demo version. For real candles, integrate with QuteX data.")
