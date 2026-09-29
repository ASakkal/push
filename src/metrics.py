"""
Instructions to fulfil:

- Take strategy returns (and optionally benchmark returns / equity curve).
- Calculate a standard, small set of metrics:
- Total return
- Annualised return
- Annualised volatility
- Sharpe ratio (assume risk-free rate = 0 for simplicity, or make it a parameter)
- Maximum drawdown
- Turnover or number of trades

Return results in a clear structure (dictionary or formatted print) that can be shown for both train and test periods.
Optionally produce a simple equity curve plot.

How to assess success:

- Metrics are numerically reasonable (e.g. Sharpe is not absurdly high after costs).
- Maximum drawdown is negative and matches what you see on the equity curve.
- Turnover/number of trades matches the number of position changes.
- Running the same returns twice produces identical metric values.
- Train vs test comparison is easy to read.
"""