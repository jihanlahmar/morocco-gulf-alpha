import yfinance as yf
import json
from datetime import datetime

tickers = {
    "MAD_USD": "MADUSD=X",
    "SAR_USD": "SARUSD=X",
    "AED_USD": "AEDUSD=X",
    "TASI_Saudi": "^TASI",
    "ADX_UAE": "ADX.AE",
    "Fertilizer_ETF_SOIL": "SOIL"
}

data = {}
for name, ticker in tickers.items():
    try:
        hist = yf.Ticker(ticker).history(period="5d")
        if len(hist) >= 2:
            price = round(hist['Close'][-1], 4)
            change = round((hist['Close'][-1] / hist['Close'][-2] - 1) * 100, 2)
            data[name] = {"price": price, "change_1d_pct": change}
        else:
            data[name] = {"error": "no_data"}
    except:
        data[name] = {"error": "fetch_failed"}

snapshot = {
    "date": datetime.utcnow().strftime("%Y-%m-%d"),
    "data": data
}

with open("/content/snapshot.json", "w") as f:
    json.dump(snapshot, f, indent=2)

print("✅ SUCCESS! Your snapshot.json is ready.")
print("Now click the folder icon on the left → find 'snapshot.json' → right-click → Download")