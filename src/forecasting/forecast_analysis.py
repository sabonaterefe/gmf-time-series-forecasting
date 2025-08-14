def analyze_trend(forecast):
    trend = "upward" if forecast[-1] > forecast[0] else "downward"
    volatility = max(forecast) - min(forecast)
    return trend, volatility

def interpret_confidence_intervals(intervals):
    widths = [hi - lo for lo, hi in intervals]
    widening = widths[-1] > widths[0]
    reliability = "decreasing" if widening else "stable"
    return reliability, widths
