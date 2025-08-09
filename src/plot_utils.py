import matplotlib.pyplot as plt

def plot_price_trends(prices, assets):
    plt.figure(figsize=(14, 8))
    for asset in assets:
        plt.plot(prices.index, prices[asset]/prices[asset].iloc[0], label=asset)
    plt.title('Normalized Price Trends')
    plt.ylabel('Normalized Price')
    plt.xlabel('Date')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_daily_returns(returns, assets):
    plt.figure(figsize=(14, 8))
    for asset in assets:
        plt.plot(returns.index, returns[asset], label=asset)
    plt.title("Daily Percentage Change")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_volatility(rolling_std, assets):
    plt.figure(figsize=(14, 8))
    for asset in assets:
        plt.plot(rolling_std.index, rolling_std[asset], label=f"{asset} Volatility")
    plt.title("Rolling Volatility (21-day)")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.tight_layout()
    plt.show()
