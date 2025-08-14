import numpy as np
import pandas as pd

def simulate_portfolio(returns_df, weights):
    weighted_returns = returns_df.dot(weights)
    cumulative_returns = (1 + weighted_returns).cumprod()
    return cumulative_returns

def calculate_sharpe_ratio(returns, risk_free_rate=0.01):
    excess_returns = returns - risk_free_rate / 252
    return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

def backtest_strategy(returns_df, strategy_weights, benchmark_weights):
    strategy_cum = simulate_portfolio(returns_df, strategy_weights)
    benchmark_cum = simulate_portfolio(returns_df, benchmark_weights)

    strategy_daily = strategy_cum.pct_change().dropna()
    benchmark_daily = benchmark_cum.pct_change().dropna()

    strategy_sharpe = calculate_sharpe_ratio(strategy_daily)
    benchmark_sharpe = calculate_sharpe_ratio(benchmark_daily)

    return {
        "strategy": {
            "cumulative": strategy_cum,
            "sharpe": strategy_sharpe,
            "total_return": strategy_cum.iloc[-1] - 1
        },
        "benchmark": {
            "cumulative": benchmark_cum,
            "sharpe": benchmark_sharpe,
            "total_return": benchmark_cum.iloc[-1] - 1
        }
    }

if __name__ == "__main__":
    # Dummy returns for testing — replace with real data
    dates = pd.date_range(start="2022-01-01", periods=252, freq="B")
    np.random.seed(42)
    returns_df = pd.DataFrame(np.random.normal(0.0005, 0.01, size=(252, 3)), columns=["TSLA", "SPY", "BND"], index=dates)

    # Example weights
    strategy_weights = np.array([0.8, 0.2, 0.0])   # Max Sharpe
    benchmark_weights = np.array([0.33, 0.33, 0.34])  # Equal-weight benchmark

    results = backtest_strategy(returns_df, strategy_weights, benchmark_weights)

    print("\n📊 Strategy Performance:")
    print(f"Total Return: {results['strategy']['total_return']:.4f}")
    print(f"Sharpe Ratio: {results['strategy']['sharpe']:.4f}")

    print("\n📈 Benchmark Performance:")
    print(f"Total Return: {results['benchmark']['total_return']:.4f}")
    print(f"Sharpe Ratio: {results['benchmark']['sharpe']:.4f}")
