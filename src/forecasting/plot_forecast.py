import matplotlib.pyplot as plt

def plot_forecasts(series, forecasts: dict, title: str = "Forecast Comparison"):
    plt.figure(figsize=(12, 6))
    plt.plot(series.index, series.values, label="Actual", color="black", linewidth=2)

    for model_name, forecast_values in forecasts.items():
        forecast_len = len(forecast_values)
        forecast_index = series.index[-forecast_len:]
        plt.plot(forecast_index, forecast_values, label=f"{model_name} Forecast")

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
