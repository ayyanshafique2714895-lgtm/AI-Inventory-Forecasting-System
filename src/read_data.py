import pandas as pd

# Read the CSV file
df = pd.read_csv("data/sales_data.csv")

print("=" * 50)
print("Sales Dataset")
print("=" * 50)

# Show the data
print(df)

print("\nDataset Information")
print(df.info())

print("\nFirst Five Rows")
print(df.head())

print("\nLast Five Rows")
print(df.tail())

print("\nSummary Statistics")
print(df.describe())