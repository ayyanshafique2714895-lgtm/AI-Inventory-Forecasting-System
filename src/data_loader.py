import pandas as pd
import streamlit as st

COLUMN_MAPPING = {
    "product": "Product",
    "product name": "Product",
    "item": "Product",
    "item name": "Product",

    "category": "Category",

    "quantity": "Units_Sold",
    "qty": "Units_Sold",
    "qty sold": "Units_Sold",
    "units": "Units_Sold",
    "units sold": "Units_Sold",

    "price": "Price",
    "unit price": "Price",
    "selling price": "Price",

    "stock": "Stock_Level",
    "inventory": "Stock_Level",
    "inventory level": "Stock_Level",
    "stock level": "Stock_Level",

    "date": "Date",
    "sale date": "Date",
    "order date": "Date"
}

def rename_columns(df):

    new_columns = {}

    for col in df.columns:

        clean_col = col.strip().lower()

        if clean_col in COLUMN_MAPPING:
            new_columns[col] = COLUMN_MAPPING[clean_col]

    df = df.rename(columns=new_columns)

    return df

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
        df = rename_columns(df)
    else:
        df = pd.read_csv("data/sales_data.csv")
        df = rename_columns(df)

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