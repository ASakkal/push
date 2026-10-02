from pathlib import Path
import yfinance as yf

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

# Define the root directory and target directory for saving raw data
ROOT = Path(__file__).resolve().parents[1]
TARGET_DIR = ROOT / "data" / "raw"

# Define the relevant raw data file names
SPY_file = "SPY_raw.csv"
# additional_file = "additional_raw.csv"

# Optional expansion of 2-4 highly liquid ETFs/stocks
# additional_tickers = ["AAPL", "MSFT", "GOOGL"]

# Check if raw data already exists, if not, download and save it
if not (TARGET_DIR / SPY_file).exists():
    
    print(f"Raw data not found at {TARGET_DIR / SPY_file}. Downloading from Yahoo Finance...")
    # TARGET_DIR.mkdir(parents=True, exist_ok=True)
    SPY_data = yf.download(tickers=["SPY"], start="2015-01-01", keepna=True)  # Retrieve SPY data from Yahoo Finance
    SPY_data.to_csv(TARGET_DIR / SPY_file, index=True) # Save to CSV in relevant directory
else:
    print(f"Raw data already exists at {TARGET_DIR / SPY_file}. Skipping download.")