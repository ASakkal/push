"""
Instructions to fulfil:

Take the features DataFrame.
Implement one simple, transparent rule (z-score mean-reversion or dual moving-average crossover).
Produce a signal series taking values in {+1, 0, -1} (or {+1, 0} if staying long-only/flat).
Convert the signal into a position series that is lagged by one bar (shift(1)). This is mandatory.
Return both the raw signal and the lagged position (or just the lagged position if you prefer a minimal interface).
Keep parameters (lookbacks, thresholds) clearly defined and easy to change.

How to assess success:

The position series is exactly one bar behind the signal (verify by inspecting a few rows).
Positions only change when the rule says they should.
No use of future information in the decision.
A plot of price with position overlays (or background colouring) makes intuitive sense for the chosen rule.
Changing a parameter (e.g. z-score threshold) visibly changes the positions as expected.
"""