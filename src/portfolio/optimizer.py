import numpy as np
from scipy.optimize import minimize

def annualize_returns(daily_returns):
    return daily_returns.mean() * 252

def portfolio_performance(weights, mean_returns, cov_matrix):
    """
    Returns expected portfolio return and volatility.
    """
    returns = np.dot(weights, mean_returns)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, volatility

def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.01):
    """
    Objective function to maximize Sharpe Ratio (by minimizing negative).
    """
    returns, volatility = portfolio_performance(weights, mean_returns, cov_matrix)
    return -(returns - risk_free_rate) / volatility

def minimize_volatility(weights, mean_returns, cov_matrix):
    """
    Objective function to minimize portfolio volatility.
    """
    _, volatility = portfolio_performance(weights, mean_returns, cov_matrix)
    return volatility

def optimize_portfolio(mean_returns, cov_matrix, risk_free_rate=0.01):
    """
    Runs optimization for:
    - Maximum Sharpe Ratio Portfolio
    - Minimum Volatility Portfolio
    """
    num_assets = len(mean_returns)
    bounds = tuple((0, 1) for _ in range(num_assets))
    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    initial_guess = num_assets * [1. / num_assets]

    # Max Sharpe Ratio
    max_sharpe = minimize(negative_sharpe_ratio, initial_guess,
                          args=(mean_returns, cov_matrix, risk_free_rate),
                          method='SLSQP', bounds=bounds, constraints=constraints)

    # Min Volatility
    min_vol = minimize(minimize_volatility, initial_guess,
                       args=(mean_returns, cov_matrix),
                       method='SLSQP', bounds=bounds, constraints=constraints)

    return {
        "max_sharpe": {
            "weights": max_sharpe.x,
            "performance": portfolio_performance(max_sharpe.x, mean_returns, cov_matrix)
        },
        "min_volatility": {
            "weights": min_vol.x,
            "performance": portfolio_performance(min_vol.x, mean_returns, cov_matrix)
        }
    }

# 🧪 Example usage block
if __name__ == "__main__":
    # Sample expected returns: TSLA, SPY, BND
    expected_returns = np.array([0.15, 0.08, 0.04])  # Annualized
    cov_matrix = np.array([
        [0.05, 0.02, 0.01],
        [0.02, 0.03, 0.015],
        [0.01, 0.015, 0.02]
    ])  # Annualized covariance

    results = optimize_portfolio(expected_returns, cov_matrix)

    print("\n📊 Max Sharpe Ratio Portfolio:")
    weights = results["max_sharpe"]["weights"]
    ret, vol = results["max_sharpe"]["performance"]
    print(f"Weights: {weights.round(4)}")
    print(f"Expected Return: {ret:.4f}")
    print(f"Volatility: {vol:.4f}")
    print(f"Sharpe Ratio: {(ret - 0.01) / vol:.4f}")

    print("\n🛡️ Min Volatility Portfolio:")
    weights = results["min_volatility"]["weights"]
    ret, vol = results["min_volatility"]["performance"]
    print(f"Weights: {weights.round(4)}")
    print(f"Expected Return: {ret:.4f}")
    print(f"Volatility: {vol:.4f}")
    print(f"Sharpe Ratio: {(ret - 0.01) / vol:.4f}")
