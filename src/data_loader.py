import pandas as pd
import streamlit as st

COLUMN_MAPPING = {
    "date": "Date",
    "sale date": "Date",
    "order date": "Date",
    "created at": "Date",
    "order created": "Date",
    "transaction date": "Date",
    "purchase date": "Date",

    "product": "Product",
    "product name": "Product",
    "item": "Product",
    "item name": "Product",
    "sku": "Product",
    "sku name": "Product",
    "variant": "Product",
    "variant name": "Product",
    "title": "Product",
    "name": "Product",

    "category": "Category",
    "product type": "Category",
    "collection": "Category",
    "department": "Category",
    "item category": "Category",

    "quantity": "Units_Sold",
    "qty": "Units_Sold",
    "qty sold": "Units_Sold",
    "units": "Units_Sold",
    "units sold": "Units_Sold",
    "qty ordered": "Units_Sold",
    "quantity sold": "Units_Sold",
    "sales quantity": "Units_Sold",
    "sold quantity": "Units_Sold",
    "items sold": "Units_Sold",
    "net quantity": "Units_Sold",
    "ordered quantity": "Units_Sold",

    "price": "Price",
    "unit price": "Price",
    "selling price": "Price",
    "retail price": "Price",
    "sale price": "Price",
    "item price": "Price",
    "amount": "Price",

    "stock": "Stock_Level",
    "inventory": "Stock_Level",
    "inventory level": "Stock_Level",
    "stock level": "Stock_Level",
    "available": "Stock_Level",
    "available stock": "Stock_Level",
    "current stock": "Stock_Level",
    "current inventory": "Stock_Level",
    "inventory quantity": "Stock_Level",
    "stock quantity": "Stock_Level",
    "on hand": "Stock_Level",
    "quantity on hand": "Stock_Level",
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