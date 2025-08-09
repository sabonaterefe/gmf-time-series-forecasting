from statsmodels.tsa.stattools import adfuller
import numpy as np

def adf_test(series):
    result = adfuller(series.dropna())
    return {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Stationary': result[1] < 0.05
    }

def calculate_var(returns, confidence=0.95):
    return returns.quantile(1 - confidence)

def calculate_sharpe_ratio(returns, risk_free_rate=0.01):
    excess_returns = returns.mean() - risk_free_rate / 252
    return excess_returns / returns.std()
