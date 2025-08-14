import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_tsla_data():
    tsla = yf.download("TSLA", start="2015-01-01", end="2025-08-01", auto_adjust=False)
    tsla = tsla["Adj Close"] if "Adj Close" in tsla.columns else tsla["Close"]
    tsla = tsla.dropna()
    train = tsla[:'2023']
    test = tsla['2024':]
    return tsla, train, test

def scale_data(train, test):
    scaler = MinMaxScaler()
    train_scaled = scaler.fit_transform(train.values.reshape(-1, 1))
    test_scaled = scaler.transform(test.values.reshape(-1, 1))
    return scaler, train_scaled, test_scaled
