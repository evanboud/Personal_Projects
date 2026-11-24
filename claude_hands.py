"""Log hands for a poker session to hands.csv.

Reference version for comparison with Hands.py. Same behavior, with the
cleanup items applied.
"""

import os

import pandas as pd

from Poker import converter

SESSIONS_FILE = "poker.csv"
HANDS_FILE = "hands.csv"

POSITIONS = ["btn", "sb", "bb", "ep", "lp"]
STREETS = ["preflop", "flop", "turn", "river"]
ACTIONS = ["fold", "call", "raise"]
ERROR_TYPES = ["sizing", "range read", "pot odds", "discipline", "none"]


def next_id(path, column):
    """Return the column's max + 1, or 1 if the file doesn't exist yet."""
    if not os.path.exists(path):
        return 1
    df = pd.read_csv(path)
    return int(df[column].max()) + 1


def choose(prompt, options):
    """Ask until the answer is one of options; return it lowercased."""
    while True:
        answer = input(f"{prompt} ({'/'.join(options)}): ").strip().lower()
        if answer in options:
            return answer
        print("Pick one of:", ", ".join(options))


def yes_no(prompt):
    """Ask a y/n question. Return True for y, False for n."""
    return choose(prompt, ["y", "n"]) == "y"


def get_session_id():
    """Ask which session these hands belong to. Enter = most recent session."""
    if not os.path.exists(SESSIONS_FILE):
        raise SystemExit("No sessions logged yet. Run Poker.py first.")
    sessions = pd.read_csv(SESSIONS_FILE)

    while True:
        text = input("Session ID (Enter for last session): ").strip()
        if text == "":
            return int(sessions["Session ID"].max())
        try:
            session_id = int(text)
        except ValueError:
            print("Enter a whole number.")
            continue
        if (sessions["Session ID"] == session_id).any():
            return session_id
        print("No session with that ID.")


def pot_odds(my_bet, pot_before_bet, bet_faced):
    """Return the equity needed to continue, as a fraction (0 to 1).

    pot_before_bet is the pot BEFORE the villain bet.
    Final pot = pot_before_bet + bet_faced + my_bet.
    Example: pot 10, villain bets 5, I call 5 -> 5 / 20 = 0.25.
    """
    return my_bet / (pot_before_bet + bet_faced + my_bet)


def log_hand(session_id):
    """Prompt for one hand and append it to hands.csv."""
    hand_id = next_id(HANDS_FILE, "hand_id")

    position = choose("Position", POSITIONS)
    hole_cards = input("Hole cards (e.g. AhKd): ").strip()
    board = input("Board: ").strip()
    street = choose("Street of the hard decision", STREETS)
    pot_size = converter(float, "Pot before villain's bet: ")
    bet_faced = converter(float, "Bet faced: ")
    my_bet = converter(float, "My bet: ")

    row = {
        "session_id": session_id,
        "hand_id": hand_id,
        "position": position,
        "hole_cards": hole_cards,
        "board": board,
        "street": street,
        "pot_size": pot_size,
        "bet_faced": bet_faced,
        "my_bet": my_bet,
        "pot_odds": round(pot_odds(my_bet, pot_size, bet_faced), 3),
        "equity_estimate": converter(float, "Equity estimate (0 to 1): "),
        "equity_actual": converter(float, "Actual equity (0 to 1): "),
        "action_taken": choose("Action taken", ACTIONS),
        "action_correct": yes_no("Action correct?"),
        "error_type": choose("Error type", ERROR_TYPES),
        "lesson": input("Lesson (one sentence): ").strip(),
    }

    pd.DataFrame([row]).to_csv(
        HANDS_FILE,
        mode="a",
        index=False,
        header=not os.path.exists(HANDS_FILE),
    )
    print(f"Logged hand {hand_id} for session {session_id}.")


def main():
    session_id = get_session_id()
    while True:
        log_hand(session_id)
        if not yes_no("Log another hand?"):
            break


if __name__ == "__main__":
    main()