import pandas as pd

def compute_daily_returns(prices):
    return prices.pct_change().dropna()

def compute_rolling_volatility(returns, window=21):
    rolling_std = returns.rolling(window).std()
    rolling_mean = returns.rolling(window).mean()
    return rolling_mean, rolling_std

def detect_outliers(returns, threshold=0.05):
    outliers = {}
    for asset in returns.columns:
        high = returns[asset][returns[asset] > threshold]
        low = returns[asset][returns[asset] < -threshold]
        outliers[asset] = {'high': high, 'low': low}
    return outliers
