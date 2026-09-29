"""
Phase B:Features + signals

1- Compute returns, rolling mean, rolling std, z-score.
2- Generate a position series (+1 / 0 / –1) from the rule.
3- Critical: shift the position by 1 day so you do not trade on the same bar the signal appears (no look-ahead).
4- Visualise signals on a price chart for a couple of years.

Done when: You have a clean positions Series aligned to the price index and you can see the signals make intuitive sense."""