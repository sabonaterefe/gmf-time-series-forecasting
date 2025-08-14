## GMF Forecasting & Portfolio Optimization Pipeline
## Overview
# This repository implements a modular, extensible pipeline for financial time series forecasting, portfolio construction, and strategy backtesting. It is designed for production-grade deployment in quantitative research environments and supports both classical statistical models and deep learning architectures. The pipeline centers on Tesla (TSLA) as the primary forecasted asset, with SPY and BND serving as benchmark and stabilizing components for portfolio optimization.

The system is built for reliability, interpretability, and scalability, with explicit handling of API inconsistencies, shape mismatches, and model evaluation across multiple metrics.

# Objectives
Forecast TSLA stock prices using ARIMA, SARIMA, and LSTM models.

Quantify model performance using RMSE, MAE, and MAPE.

Generate forward-looking forecasts to inform asset allocation.

Construct optimal portfolios using Modern Portfolio Theory.

Backtest strategy performance against SPY, BND, and equal-weight benchmarks.

Validate pipeline reliability and prepare for production deployment.

# Task 1: Time Series Forecasting
Methodology
Data Source: Daily adjusted close prices for TSLA via yfinance.

# Models:

ARIMA: Auto-tuned via AIC minimization.

SARIMA: Seasonal parameters selected via autocorrelation and decomposition.

LSTM: Scaled inputs, supervised reshaping, single-layer architecture.

Evaluation:

Chronological train/test split (2015–2023 train, 2024–2025 test).

Metrics: RMSE, MAE, MAPE.

# Results
ARIMA and SARIMA provided stable, interpretable forecasts.

LSTM captured nonlinear dynamics and outperformed in RMSE and MAE.

Trade-offs observed between smoothness (ARIMA) and responsiveness (LSTM).

# Task 2: Forecast Generation
Methodology
Forecast Horizon: 6–12 months.

# Techniques:

ARIMA/SARIMA: Direct multi-step forecasts with confidence intervals.

LSTM: Recursive prediction using last known sequence.

Visualization: Historical overlay with forecast trajectories and uncertainty bounds.

# Results
ARIMA forecasts were conservative and stable.

LSTM forecasts showed sharper inflection points and higher volatility.

Forecasts used to guide asset weighting in portfolio construction.

# Task 3: Portfolio Optimization
Methodology
Assets: TSLA, SPY, BND.

Returns: Log returns computed for numerical stability.

# Optimization:

Monte Carlo simulation of random portfolios.

Metrics: Expected return, volatility, Sharpe ratio.

Targets: Max Sharpe, Min Volatility, Custom return thresholds.

Efficient Frontier: Visualized trade-offs and extracted optimal weights.

# Results
Max Sharpe portfolio favored TSLA with moderate SPY exposure.

Min Volatility portfolio leaned on BND and SPY.

Efficient Frontier confirmed diversification benefits and risk-adjusted performance.

# Task 4: Strategy Backtesting
Methodology
Framework: Monthly rebalancing with fixed weights.

# Metrics:

Cumulative returns

Annualized volatility

Sharpe ratio

Max drawdown

Benchmarks: SPY, BND, Equal-weight portfolio.

Visualization: Return curves, rolling Sharpe ratios, drawdown plots.

# Results
Max Sharpe portfolio outperformed SPY and BND in risk-adjusted terms.

Min Volatility portfolio showed resilience during macro shocks.

Backtest confirmed superiority of model-driven allocations.

# Task 5: Pipeline Validation & Deployment Readiness
Methodology
Validation:

Shape alignment across modules

Explicit error handling for API changes

Consistent metric computation

Reliability Enhancements:

Fallback logic for missing data

Logging and exception tracking

Unit tests for core functions

## Deployment:

Docker containerization

Config-driven model selection

Scheduled retraining via cron or Airflow

## Results
Pipeline validated end-to-end.

Supports iterative experimentation and scalable deployment.

Ready for integration into production-grade investment workflows.

## Repository Structure
data/ – Raw and processed datasets

models/ – ARIMA, SARIMA, and LSTM implementations

optimization/ – Portfolio construction and efficient frontier analysis

backtesting/ – Strategy simulation and benchmark comparison

utils/ – Preprocessing, evaluation, and visualization helpers

config/ – Model and portfolio parameters

main.py – Pipeline entry point

## Installation
git clone https://github.com/your-org/gmf-pipeline.git
cd gmf-pipeline
pip install -r requirements.txt
Requirements
Python 3.8+

pandas

numpy

scikit-learn

statsmodels

keras

matplotlib

yfinance

# Author
## Sabona Financial Data Analyst & Pipeline Engineer Specializing in modular time series forecasting, portfolio optimization, and production-grade analytics for investment decisions.
