import numpy as np

def compute_returns(prices):
    return prices.pct_change().dropna()

def compute_summary_stats(returns):
    stats = returns.describe().T
    stats['annualized_return'] = returns.mean() * 252
    stats['annualized_volatility'] = returns.std() * np.sqrt(252)
    stats['sharpe_ratio'] = stats['annualized_return'] / stats['annualized_volatility']
    return stats[['annualized_return', 'annualized_volatility', 'sharpe_ratio']]
