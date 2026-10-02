import src.data as data


# Establish relevant universes
UNIVERSE = ["SPY"]
# additional_tickers = ["AAPL", "MSFT", "GOOGL"]

# Download data
data.download_data()

# Clean data
data.clean_data