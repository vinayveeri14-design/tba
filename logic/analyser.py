import pandas as pd

def summary_stats(df):
    return {
        "Total Calls": len(df),
        "Total Duration (mins)": round(df["duration"].sum() / 60, 2),
        "Total Cost": round(df["cost"].sum(), 2)
    }

def top_users(df, n=5):
    return df.groupby("user_id")["cost"].sum().sort_values(ascending=False).head(n)

def call_type_distribution(df):
    return df["call_type"].value_counts()
