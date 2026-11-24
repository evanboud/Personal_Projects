import pandas as pd
import os
from datetime import date
from session import converter

today = date.today()


def session_id_generator(): 
     while True:
      session_id_input = input("Input Session ID (Press Enter for Last Session): ")
      if session_id_input == '':
         if os.path.exists("poker.csv"):
             csv_session_df = pd.read_csv("poker.csv")
             return int(max(csv_session_df["Session ID"])) 
      else:
            try:
               session_id_input =  int(session_id_input)
               poker_session_df = pd.read_csv("poker.csv")
               if poker_session_df[poker_session_df["Session ID"] == session_id_input].empty:
                   print("Session Doesn't Exist")
                   continue
               else:
                   return session_id_input
            except ValueError:
                  print("Input Not a Integer")
                  continue
                
def hand_id_generator():
    if os.path.exists("hands.csv"):
      hands_session_df = pd.read_csv("hands.csv")
      return int(max(hands_session_df["hand_id"] + 1))
    return int(1)

def position_func():
   while True:
         position = input("Positons? (BTN/SB/BB/EP/LP): ").lower().strip()
         if position in ["btn","sb","bb","ep","lp"]:
            return position
         print("Not Valid Position")
         continue

def yes_no(text):
    while True:
      x = input(text).lower().strip()
      if x in ["y","n"]:
         return x 
      continue
    
    
    

def pot_odds_calculator(bet, bet_faced, pot_size):
   return bet / (bet + bet_faced + pot_size)
         


def log_hand(log_function_session_id):
    hand_id = hand_id_generator()
    bet = converter(float, "My Bet: ")
    bet_faced = converter(float, "Bet Faced: ")
    pot_size = converter(float, "Pot Size: ")
    position = position_func()
    pot_odds = pot_odds_calculator(bet, bet_faced, pot_size)
    
    hand_data = [{"session_id": log_function_session_id, "hand_id": hand_id, "position": position, "hole_cards": input("Hole Cards: "), "board": input("Board: " ),
                  "street": input("Street (Where Was the difficult decison made ?): "), "pot_size": pot_size, "bet_faced": bet_faced, "my_bet": bet, "pot_odds": pot_odds,
                  "equity_estimate": converter(float, "Equity Estimate: " ), "equity_actual": converter(float, "Actual Equity: "), "action_taken": input("Action Taken (Fold/Call/Raise/Sizing): "),
                  "action_correct": yes_no("Action Correct (y/n) ") , "error_type": input("Error Type:" ), "lesson": input("Lesson Learned: ")}]    

    hand_data_frame = pd.DataFrame(hand_data)
    hand_data_frame.to_csv("hands.csv", header=False if os.path.exists("hands.csv") else True , mode="a", index=False)   



def main():
   log_function_session_id = session_id_generator()
   while True:
      log_hand(log_function_session_id)
      p = input("Continue (y/n?): ")
      if  p == "y":
          continue
      break
   


if __name__ == "__main__":
   main()

