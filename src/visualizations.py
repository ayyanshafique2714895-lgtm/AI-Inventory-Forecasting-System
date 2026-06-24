def get_sales_by_product(df):
    return df.groupby("Product")["Units_Sold"].sum()


def get_revenue_by_product(df):
    return df.groupby("Product")["Revenue"].sum()


def get_stock_by_product(df):
    return df.groupby("Product")["Stock_Level"].min()


def get_daily_sales(df):
    return df.groupby("Date")["Units_Sold"].sum()