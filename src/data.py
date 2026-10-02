from pathlib import Path
import yfinance as yf
from datetime import date

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
RAW_DIR = ROOT / "data" / "raw"
CLEAN_DIR = ROOT / "data" / "clean"

def download_data(ticker_symbol: str, start_date: date | str, end_date: date | str, filename: Path | str):
    """Retrieves yfinance data given a ticker symbol, a specified date and a filename to store 

    Args:
        ticker: 
        start_date:
        end_date:
        filename:
    """

    # Check if raw data already exists, if not, download and save it
    if not (RAW_DIR / filename).exists():
    
        print(f"Raw data not found at {RAW_DIR / filename}. Downloading from Yahoo Finance...")
        # RAW_DIR.mkdir(parents=True, exist_ok=True)
        SPY_data = yf.download(tickers=[ticker_symbol], start="2015-01-01", keepna=True)  # Retrieve SPY data from Yahoo Finance
        SPY_data.to_csv(RAW_DIR / filename, index=True) # Save to CSV in relevant directory
    else:
        print(f"Raw data already exists at {RAW_DIR / filename}. Skipping download.")

def clean_data(raw_dir: Path | str, clean_dir: Path | str):
    """Clean Blah Blah Blah. Stores the cleaned data in a specified directory.

    Args:
        raw_dir:
        clean_dir:
    """
    pass