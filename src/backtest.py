"""
Instructions to fulfil:

- Take prices and the lagged position series.
- Compute strategy returns as: position * asset_returns.
- Subtract transaction costs based on position changes (turnover). Start with a fixed cost (e.g. 10 bps).
- Support a simple chronological train/test split.
- Produce:
    - Strategy returns (net of costs)
    - Equity curve
    - Optional benchmark (buy-and-hold) equity curve
- Keep the engine vectorised and free of look-ahead.

How to assess success:

- Removing the cost term increases the equity curve (as expected).
- Setting the position lag to zero (deliberately introducing look-ahead) materially improves results — proving the lag matters.
- Train and test periods are strictly sequential with no overlap.
-Equity curve starts at 1.0 (or initial capital) and compounds correctly.
- Turnover/cost impact is visible when you increase the cost parameter.
"""