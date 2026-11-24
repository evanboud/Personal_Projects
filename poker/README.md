# Poker Tracker

A Python tool I built to log my online no-limit hold'em sessions and hands, then measure the quality of my decisions instead of my results.

## Why

Win rate is noisy over small samples, so I track process instead: did I price the decision, how close was my equity estimate, and was the action correct. I treat it as a first version of a trading journal.

## How it works

- `session.py` logs a session (stakes, buy-in, cashout, hours, decisions priced vs. total, tilt) to `sessions.csv`.
- `hands.py` logs as many hands as you want from a session to `hands.csv`, linked by session ID. Pot odds are calculated automatically.
- `report.py` reads both files and prints the report.

## What the report shows

- **Pricing rate:** share of decisions where I calculated pot odds before acting, graphed per session
- **Equity error:** average absolute gap between my equity estimate and the actual equity
- **Decision accuracy:** share of hands where my action was correct

## Requirements

- Python 3.12+
- `pip install pandas matplotlib`

## How to run

1. `python session.py`: enter your session info
2. `python hands.py`: enter hands (press Enter at the session prompt to use the latest session)
3. `python report.py`: run whenever you want a report

## Future work

- Restrict inputs like tilt and error type to fixed choices so typos can't get into the data
- Filter the report by week
