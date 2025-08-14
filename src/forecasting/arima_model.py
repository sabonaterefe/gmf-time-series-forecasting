import numpy as np
import pmdarima as pm
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error

def train_arima(train_series):
    model = pm.auto_arima(train_series, seasonal=False, stepwise=True, suppress_warnings=True)
    return model

def forecast_arima(model, steps):
    return model.predict(n_periods=steps)

def evaluate_arima(test, forecast):
    test = np.asarray(test).flatten()
    forecast = np.asarray(forecast).flatten()
    return {
        "RMSE": np.sqrt(mean_squared_error(test, forecast)),
        "MAE": mean_absolute_error(test, forecast),
        "MAPE": mean_absolute_percentage_error(test, forecast)
    }
