import pandas as pd
import statistics
import matplotlib.pyplot as plt
from matplotlib import ticker as mtick


def pricing_rate_func(sessions_df_new):
    return sessions_df_new[" Decisions Priced"] / sessions_df_new[" Decisions Total"]

def equity_error_func(hands_df_new):
    return statistics.mean(abs(hands_df_new["equity_estimate"] - hands_df_new["equity_actual"]))

def decision_accuracy_func(hands_df_new):
    while True:
            if hands_df_new[hands_df_new["action_correct"] == "y"].empty:
                 print("No Actions Were Correct")
                 break
            x = f"{hands_df_new["action_correct"].value_counts(normalize=True, dropna=False).loc["y"]:.0%}"
            print(x)
            return x



def main():
    hands_df_new = pd.read_csv("hands.csv").set_index("session_id")
    sessions_df_new = pd.read_csv("sessions.csv").set_index("Session ID")
    decision_accuracy_func(hands_df_new)
    equity_error_func(hands_df_new)
    pricing_rate_ser = pricing_rate_func(sessions_df_new)
    z = pricing_rate_ser.plot(marker="*", markersize=10, linewidth=3, markerfacecolor="red", color="blue")
    plt.title("Pricing Rate", fontsize=18, family="Arial", fontweight="bold")
    plt.xlabel("Session ID")
    plt.ylabel("Decisions Priced")
    z.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    z.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=10, symbol=None, decimals=0))
    plt.show()
       
    
    



if __name__ == "__main__":
   main()
   


