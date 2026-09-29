"""
Instructions to fulfil:

1- Download daily OHLCV data for a small universe (SPY + 2–4 other liquid ETFs/stocks) using yfinance.
2- Use adjusted prices (auto_adjust=True or equivalent).
3- Clean the data: handle missing values, ensure a proper DatetimeIndex, drop rows with insufficient data.
4- Cache the cleaned data (parquet or csv) so repeated runs do not hit Yahoo every time.
5- Provide a simple function that returns a clean DataFrame (or dict of DataFrames) ready for feature engineering.
6- Keep the universe and date range configurable at the top of the file or via function arguments.

How to assess success:

- Calling the main load function returns a DataFrame with a DatetimeIndex and columns such as Open, High, Low, Close, Volume (or at least Close).
- No major gaps in the date index for the chosen liquid instruments.
- Data can be re-loaded from cache without a network call.
- A quick plot of the Close price looks sensible (no obvious errors or inverted series).
- The function is deterministic: same inputs produce the same cleaned output.

"""
