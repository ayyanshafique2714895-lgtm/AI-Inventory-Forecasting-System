import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("data/sales_data.csv")

# Group by product and calculate total units sold
sales = df.groupby("Product")["Units_Sold"].sum()

# Create the chart
plt.figure(figsize=(8,5))
plt.bar(sales.index, sales.values)

plt.title("Total Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Total Units Sold")

plt.show()