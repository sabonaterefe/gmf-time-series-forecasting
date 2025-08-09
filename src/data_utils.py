import yfinance as yf
import pandas as pd

def fetch_and_clean_data(assets, start_date, end_date):
    print(f"🔄 Fetching data for: {assets}")
    data = yf.download(assets, start=start_date, end=end_date, auto_adjust=True)

    if data.empty or not isinstance(data.columns, pd.MultiIndex) or 'Close' not in data.columns.levels[0]:
        print("🚫 No usable 'Close' data found.")
        return None

    prices = data['Close'].copy()
    prices = prices.ffill().dropna()
    return prices
