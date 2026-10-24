import pandas as pd
import os
from sys import argv
from datetime import date
from Poker import converter, session_ID

today = date.today()
last_session_ID = int(session_ID) - 1

def session_id_generator(): 
     while True:
      session_id_input = input("Input Session ID (Press Enter for Last Session): ")
      if session_id_input == '':
         return last_session_ID
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
      hands_session_df = pd.read_csv("hands.csv)")
      return int(max(hands_session_df["Session ID"] + 1))
    return int(1)

def position_func():
   while True:
         position = input("Posiitons? (BTN/SB/BB/EP/LP): ")
         if position in ["BTN","SB","BB","EP","LP"]:
            return position
         print("Not Valid Position")
         continue

def my_bet():
    return converter(float, "My Bet: ")
def bet_faced_func():
    return converter(float, "Bet Faced ")
def pot_size_func():
    return converter(float, "Pot Size: ")
def pot_odds_calculator(bet, bet_faced, pot_size):
   return bet / (bet_faced + pot_size)
    
    
    

        
log_function_session_id = session_id_generator()
position = position_func()

def log_hand():
    hand_id = hand_id_generator()
    bet = my_bet()
    bet_faced = bet_faced_func()
    pot_size = pot_size_func()
    pot_odds = pot_odds_calculator()
    
    hand_data = [{"session_id": log_function_session_id, "hand_id": hand_id, "position": position, "hole_cards": input("Hole Cards: "), "board": input("Board: " ),
                  "street": input("Street (Where Was the difficult decison made ?): "), "pot_size": pot_size, "bet_faced": bet_faced, "my_bet": bet, "pot_odds": pot_odds,
                  "equity_estimate": converter(float, "Equity Estimate: " ), "equity_actual": converter(float, "Actual Equity: "), "action_taken": input("Action Taken (Fold/Call/Raise/Sizing): "),
                  "action_correct": converter(bool, )}]    

    hand_data_frame = pd.DataFrame(hand_data)
    hand_data_frame.to_csv("hands.csv", header=False if os.path.exists("hands.csv") else True , mode="a", index=False)   



def main():
   log_hand()
   ...


if __name__ == "__main__":
   main()

