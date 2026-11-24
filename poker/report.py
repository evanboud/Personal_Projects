import pandas as pd

hands_df = pd.read_csv("hands.csv")
sessions_df = pd.read_csv("sessions.csv")
hands_df_new = hands_df.set_index("session_id")
sessions_df_new = sessions_df.set_index("Session ID")

def pricing_rate_func():
    return sessions_df_new[" Decisions Priced"] / sessions_df_new[" Decisions Total"]

def equity_error_func():
    return hands_df_new["equity_estimate"] - hands_df_new["equity_actual"]

def decision_accuracy_func():
    while True:
        if hands_df_new[hands_df_new["action_correct"] == "y"].empty:
             print("No Actions Were Correct")
             break
        x = f"{hands_df_new["action_correct"].value_counts(normalize=True, dropna=False).loc["y"]:.0%}"
        print(x)
        return x

    



def main():
    hands_df = pd.read_csv("hands.csv")
    sessions_df = pd.read_csv("sessions.csv")
    hands_df_new = hands_df.set_index("session_id")
    sessions_df_new = sessions_df.set_index("Session ID")
    decision_accuracy_func()
    



if __name__ == "__main__":
   main()
   
   


