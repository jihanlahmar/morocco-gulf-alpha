import yfinance as yf
import investpy as iv
import pandas as pd
import json
from datetime import datetime

# Gulf & Morocco tickers
tickers = {
    "MAD_USD": "MADUSD=X",
    "SAR_USD": "SARUSD=X",
    "AED_USD": "AEDUSD=X",
    "TASI": "^TASI",
    "ADX": "ADX.AE",
    "OCP": "OCP.MA"  # Verify symbol; if not on yfinance, skip for now
}

data = {}
today = datetime.utcnow().strftime("%Y-%m-%d")

for name, ticker in tickers.items():
    try:
        hist = yf.Ticker(ticker).history(period="5d")
        if not hist.empty:
            data[name] = {
                "price": round(hist['Close'][-1], 4),
                "change_1d_pct": round((hist['Close'][-1] / hist['Close'][-2] - 1) * 100, 2)
            }
    except Exception as e:
        data[name] = {"error": str(e)}

# Commodity: Phosphate (proxy via fertilizer ETF or tradingeconomics later)
# For now, use placeholder or skip

# Save as JSON
with open("snapshot.json", "w") as f:
    json.dump({"date": today, "data": data}, f, indent=2)

print(f"Snapshot saved for {today}")
