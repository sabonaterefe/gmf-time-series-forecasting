## GMF Time Series Forecasting
## This repository contains a modular, production-grade analytics pipeline developed for GMF Investments. It supports exploratory data analysis (EDA), statistical testing, and risk assessment for financial assets including TSLA, BND, and SPY. The system is designed for reliability, maintainability, and real-world investment decision support.

## Task 1: Data Exploration & Risk Analysis
Scope
Task 1 focuses on building a robust foundation for time series analysis. The pipeline includes:

Data acquisition and preprocessing using yfinance, with forward-fill handling for missing values.

Exploratory data analysis, including daily returns, rolling volatility, and outlier detection.

Statistical testing with Augmented Dickey-Fuller (ADF) for stationarity.

Risk metrics such as Value at Risk (VaR) and Sharpe Ratio.

Visualization tools for price trends, return distributions, and volatility patterns.

All components are modularized for reuse and extensibility.

## Implemented Modules
The following Python modules have been developed and committed:

config.py: Defines asset tickers and analysis date ranges.

data_utils.py: Handles data fetching, cleaning, and validation.

eda_utils.py: Computes returns, volatility, and flags anomalies.

stats_utils.py: Performs statistical tests and calculates risk metrics.

plot_utils.py: Generates visualizations for EDA and reporting.

analysis.py: Integrates all utilities into a cohesive analysis workflow.

## Notebook
The notebook 01_data_exploration.ipynb demonstrates the full pipeline in action:

Loads and cleans historical price data for TSLA, BND, and SPY.

Performs EDA and statistical analysis.

Visualizes asset behavior and volatility.

Interprets risk metrics in the context of portfolio modeling.

## Project Structure
gmf-time-series-forecasting/
├── config/                     # Configuration files
├── notebooks/                 # Jupyter notebooks
│   └── 01_data_exploration.ipynb
├── reports/                   # Output plots and summaries
├── src/                       # Core pipeline modules
│   ├── config.py
│   ├── data_utils.py
│   ├── eda_utils.py
│   ├── stats_utils.py
│   ├── plot_utils.py
│   └── analysis.py
├── requirements.txt           # Python dependencies
└── .gitignore                 # Excludes venv, cache, checkpoints
Assets Analyzed
TSLA: High-growth, high-volatility tech stock.

BND: Bond ETF with stable yield and low volatility.

SPY: Broad market ETF used as a benchmark.

## Next Steps
Implement Task 2: Time series forecasting using ARIMA and LSTM.

Add unit tests and logging for pipeline reliability.

Automate workflows with orchestration tools (e.g., Prefect, Airflow).

Deploy interactive dashboard for real-time analytics.

