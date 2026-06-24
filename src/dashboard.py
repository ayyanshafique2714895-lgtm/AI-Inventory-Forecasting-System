import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("data/sales_data.csv")

# Create Revenue column
df["Revenue"] = df["Units_Sold"] * df["Price"]

# Group data
sales = df.groupby("Product")["Units_Sold"].sum()
stock = df.groupby("Product")["Stock_Level"].min()
revenue = df.groupby("Product")["Revenue"].sum()

# ---------------- Chart 1 ----------------
plt.figure(figsize=(6,4))
plt.bar(sales.index, sales.values)
plt.title("Total Units Sold")
plt.xlabel("Product")
plt.ylabel("Units Sold")

# ---------------- Chart 2 ----------------
plt.figure(figsize=(6,4))
plt.bar(stock.index, stock.values)
plt.title("Current Stock Level")
plt.xlabel("Product")
plt.ylabel("Stock")

# ---------------- Chart 3 ----------------
plt.figure(figsize=(6,4))
plt.bar(revenue.index, revenue.values)
plt.title("Total Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")

# Display all charts
plt.show()