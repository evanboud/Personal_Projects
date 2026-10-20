import pandas as pd
import os
from datetime import date
#function calculating the next ression IF
today = date.today()



def get_next_session_ID(): 
   if os.path.exists("poker.csv"):
    csv_session_df = pd.read_csv("poker.csv")
    return int(max(csv_session_df["Session ID"] + 1)) 
   else:
    return int(1)

session_ID = get_next_session_ID()


def converter(conversion, text):
    while True:
        try:
            str_input = input(text)
            convert1= conversion(str_input)
            return convert1  

        except ValueError:
           print("Not a Valid Input")
           continue


def log_session():

    

    session_data = [{"Session ID": session_ID, "date": today, "Venue": input("Venue: "), "Stakes": input("Stakes: "), "Buy-in": converter(float, "Buy In: "), 
                    "Cashout": converter(float, "How much did you Cashout with? "), "Hours": converter(float, "Hours: "), "Hands Played": converter(int, "Hands Played "), "Decisions Priced": converter(int, "Decisions Priced "), 
                    "Decisions Total": converter(int, "Total Decisions "), "Tilt": input("Tilted Y/N "), "Tilt Trigger": input("Tilt Trigger "), "Planned Hours": input("Planned Hours "), 
                    "Notes": input("Additional Notes ")}]    

    session_data_frame = pd.DataFrame(session_data)
    session_data_frame.to_csv("poker.csv", header=False if os.path.exists("poker.csv") else True , mode="a", index=False)

    
def main():
   log_session()


if __name__ == "__main__":
   main()



#read the CSV File









    





