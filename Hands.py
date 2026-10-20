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
                


      
print(session_id_generator())
   



def log_hand():

    hand_data = [{"Session ID": "filler", "hand ID": "filler"}]    

    hand_data_frame = pd.DataFrame(hand_data)
    hand_data_frame.to_csv("hands.csv", header=False if os.path.exists("hands.csv") else True , mode="a", index=False)   



def main():
   log_hand()
   ...


if __name__ == "__main__":
   main()

