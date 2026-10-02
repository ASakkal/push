"""
Instructions to fulfil:

1- Take the cleaned price DataFrame from data.py.
2- Compute a small set of basic features only: 
    - Simple returns Rolling means (e.g. 10-day, 20-day, 30-day)
    - Rolling standard deviation / volatility
    - Z-score of price (or returns) versus a rolling mean
3- Return a DataFrame that contains the original prices plus the new feature columns, aligned on the same index.

# Do not generate trading signals here — only features.

How to assess success:

- Output DataFrame has the same index as the input prices.
- New columns exist and contain no obvious look-ahead (rolling calculations use only past data).
- Z-score (or equivalent) is centred around zero and has reasonable magnitude.
- Dropping NaNs caused by the rolling windows leaves a usable length of data.
- Features can be inspected visually (e.g. price vs rolling mean, z-score time series) and look correct.
"""

"""
FEATURE ENGINEERING FUNCTIONS
"""
def engineer_features():
    pass


"""
COMPUTATIONAL FUNCTIONS
"""
def compute_rolling_means():
    pass

def compute_rolling_sd():
    pass

def compute_z_score():
    pass