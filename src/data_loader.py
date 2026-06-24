import pandas as pd


def load_data(uploaded_file=None):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("data/sales_data.csv")

    df["Date"] = pd.to_datetime(df["Date"])
    df["Revenue"] = df["Units_Sold"] * df["Price"]

    return df