# MFT Minimal Viable Pipeline

A clean, end-to-end research pipeline for medium-frequency trading ideas on liquid equities and ETFs.

**Purpose**: Demonstrate a correct research process from raw market data → features → simple strategy → cost-aware backtest → honest performance analysis.

This is **not** a production trading system and **not** a claim of alpha. It is a learning and evidence project focused on methodological correctness under realistic constraints.

---

## What this project does

1. Downloads daily price data for a small universe of liquid US ETFs/stocks
2. Constructs basic features (returns, moving averages, volatility, z-scores)
3. Generates a simple trading signal
4. Converts signals into lagged positions (no look-ahead bias)
5. Runs a vectorised backtest with transaction costs
6. Applies a chronological train/test split
7. Reports standard performance metrics and produces an equity curve
8. Documents results and limitations honestly

---

## What this project deliberately does *not* do

- No complex portfolio optimisation
- No machine learning
- No intraday data or high-frequency assumptions
- No leverage or short-selling complexity in the first version
- No claim that the strategy is profitable after costs in live trading

---

## Project structure

mft-pipeline/
├── README.md
├── requirements.txt
├── data/                  # Cached price data (not tracked if large)
├── src/
│   ├── data.py            # Download and clean market data
│   ├── features.py        # Feature engineering
│   ├── strategy.py        # Signal generation
│   ├── backtest.py        # Vectorised engine + costs
│   └── metrics.py         # Performance statistics
├── notebooks/             # Optional exploration only
└── run_backtest.py        # Main entry point


---

## Setup

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt