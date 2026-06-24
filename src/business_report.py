import pandas as pd

# Read the data
df = pd.read_csv("data/sales_data.csv")

print("=" * 50)
print("AI Inventory Business Report")
print("=" * 50)

# Total Units Sold
total_units = df["Units_Sold"].sum()
print(f"Total Units Sold: {total_units}")

# Total Revenue
df["Revenue"] = df["Units_Sold"] * df["Price"]
total_revenue = df["Revenue"].sum()
print(f"Total Revenue: ${total_revenue}")

# Best Selling Product
best_product = df.groupby("Product")["Units_Sold"].sum().idxmax()
print(f"Best Selling Product: {best_product}")

# Lowest Stock
lowest_stock = df.loc[df["Stock_Level"].idxmin()]

print(f"Lowest Stock Product: {lowest_stock['Product']}")
print(f"Stock Left: {lowest_stock['Stock_Level']}")

print("=" * 50)