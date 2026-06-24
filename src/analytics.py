def calculate_kpis(df):
    total_units = df["Units_Sold"].sum()
    total_revenue = df["Revenue"].sum()
    lowest_stock = df["Stock_Level"].min()
    best_product = df.groupby("Product")["Units_Sold"].sum().idxmax()

    return total_units, total_revenue, lowest_stock, best_product