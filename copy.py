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

def session_retriever(x):
    session_number = int_converter(input(x))
    session_pulled = session_data_frame.loc(session_number)
    print(session_pulled)
                          

def int_converter(x):
    while True:
        try:
            str_input = input(x)
            convert1= int(str_input)
            return convert1  
        except ValueError:
           print("Not a Integer")
           continue

def float_converter(x):
    while True:
        try:
            str_input = input(x)
            convert2= float(str_input)
            return convert2  
        except ValueError:
           print("Not a Float")
           continue
#creates the data fram that appends the CSV with session ID information 

session_data = [{"Session ID": get_next_session_ID(), "date": today, "Venue": input("Venue: "), "Stakes": input("Stakes: "), "Buy-in": float_converter("Buy In: "), 
                "Cashout": float_converter("How much did you Cashout with? "), "Hours": int_converter("Hours: "), "Hands Played": int_converter("Hands Played "), "Decisions Priced": int_converter("Decisions Priced "), 
                "Decisions Total": int_converter("Total Decisions "), "Tilt": input("Tilted Y/N "), "Tilt Trigger": input("Tilt Trigger "), "Planned Hours": input("Planned Hours "), 
                "Notes": input("Additional Notes ")}]
    
  

session_data_frame = pd.DataFrame(session_data)
session_data_frame.to_csv("poker.csv", header=False if os.path.exists("poker.csv") else True , mode="a", index=False)


#read the CSV File









    





