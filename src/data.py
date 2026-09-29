"""
Phase A: Data layer

1- Write data.py that downloads daily OHLCV for SPY + 2 – 4 other liquid names (QQQ, IWM, XLF, etc.) from 2015 or 2018 to now using yfinance.
2- Force auto_adjust=True (or be explicit) and check for missing days / corporate actions.
3- Save to parquet or csv so you are not hitting Yahoo every run.
4- Basic sanity checks: plot price, check for gaps, confirm last available date.

Done when: You can call one function and get a clean multi-ticker DataFrame of adjusted closes (and volume if you want).
"""

