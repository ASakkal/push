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

```
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
```

---

## Setup

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Requirements** (minimal):
- Python 3.11+
- yfinance
- pandas
- numpy
- matplotlib

---

## How to run

```bash
python run_backtest.py
```

This will:
- Load (or download) the data
- Generate features and signals
- Run the backtest with costs and a train/test split
- Print key metrics
- Save a simple equity curve plot

---

## Strategy (v1)

**Type**: Simple mean-reversion or dual moving-average rule on liquid ETFs (primarily SPY).

**Core logic**:
- Compute a z-score (or moving-average crossover) on daily closes
- Generate a signal (+1 / 0 / –1)
- **Lag the position by one bar** so the decision uses only information available at the previous close
- Apply a fixed transaction cost on every position change

Exact parameters and the precise rule are defined in `src/strategy.py` and documented in the results section below once the first complete run is finished.

---

## Methodological principles

These are non-negotiable in this project:

1. **No look-ahead bias**  
   Positions are always lagged (`shift(1)`). A signal generated on day *t* can only be acted on from day *t+1*.

2. **Transaction costs**  
   A realistic cost (starting point: 10 bps per turnover) is subtracted. High-turnover strategies are stress-tested against this friction.

3. **Train / test separation**  
   Parameters and rules are examined on an earlier period; final reported performance uses a later, unseen period.

4. **Honesty over optimisation**  
   The goal is a trustworthy process, not the highest possible backtest Sharpe.

---

## Results

*(To be completed after the first clean run)*

**Universe**:  
**Period**:  
**Train / Test split**:  

| Metric              | Train     | Test      |
|---------------------|-----------|-----------|
| Total Return        |           |           |
| Annualised Return   |           |           |
| Annualised Vol      |           |           |
| Sharpe Ratio        |           |           |
| Max Drawdown        |           |           |
| Turnover            |           |           |
| Number of Trades    |           |           |

**Key observations**:
- 
- 
- 

**What broke or degraded**:
- 

**What I would change next**:
- 

---

## Limitations (explicit)

- Uses free daily data (`yfinance`). Corporate actions and exact point-in-time accuracy are limited.
- Transaction cost model is a simple fixed percentage. No market impact, no variable spread, no borrow costs.
- Single-asset or very small universe focus in v1.
- No walk-forward optimisation or robust parameter stability testing yet.
- Equity curve assumes fills at the next bar’s close/open with the stated cost — a simplification.

These limitations are accepted deliberately so that the core research loop remains clear and correct.

---

## Future extensions (not in scope for this repo)

- Regime or volatility filters
- Multi-asset portfolio construction
- More realistic cost models
- Comparison against a simple machine-learning baseline
- Proper walk-forward analysis

These belong in subsequent projects once this foundation is solid.

---

## Author

Mature Year 1 BSc Mathematics student building practical medium-frequency research skills under a hard time constraint (≤ 8 hours/week). This repository is part of a deliberate, project-driven learning path.
