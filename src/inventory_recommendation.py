import pandas as pd

# Read data
df = pd.read_csv("data/sales_data.csv")

# Open report file
report = open("reports/inventory_recommendation_report.txt", "w")

report.write("=" * 50 + "\n")
report.write("Inventory Recommendation Report\n")
report.write("=" * 50 + "\n\n")

products = df["Product"].unique()

for product in products:

    product_data = df[df["Product"] == product]

    total_units = product_data["Units_Sold"].sum()
    stock = product_data["Stock_Level"].iloc[-1]
    average_sales = product_data["Units_Sold"].mean()

    days_left = stock / average_sales

    if days_left < 7:
        recommendation = "Reorder immediately"
    elif days_left < 14:
        recommendation = "Monitor stock"
    else:
        recommendation = "Stock level is healthy"

    report.write(f"Product: {product}\n")
    report.write(f"Total Units Sold: {total_units}\n")
    report.write(f"Current Stock: {stock}\n")
    report.write(f"Average Daily Sales: {average_sales:.2f}\n")
    report.write(f"Estimated Days Left: {days_left:.1f}\n")
    report.write(f"Recommendation: {recommendation}\n")
    report.write("-" * 40 + "\n")

report.close()

print("Report saved successfully!")