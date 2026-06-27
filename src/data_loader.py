import pandas as pd
import streamlit as st

REQUIRED_COLUMNS = [
    "Date",
    "Product",
    "Category",
    "Units_Sold",
    "Price",
    "Stock_Level"
]

def load_data(uploaded_file=None):

    # Load data
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("data/sales_data.csv")

    # Validate uploaded CSV
    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        st.error(
            f"Missing required columns: {', '.join(missing_columns)}"
        )
        st.stop()

    # Extra processing
    df["Date"] = pd.to_datetime(df["Date"])
    df["Revenue"] = df["Units_Sold"] * df["Price"]

    return df