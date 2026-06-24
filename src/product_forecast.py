import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("data/sales_data.csv")

print("=" * 50)
print("7-Day Product Sales Forecast")
print("=" * 50)

products = df["Product"].unique()

for product in products:
    product_data = df[df["Product"] == product].copy()
    product_data["Day"] = range(1, len(product_data) + 1)

    X = product_data[["Day"]]
    y = product_data["Units_Sold"]

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.array(range(len(product_data) + 1, len(product_data) + 8)).reshape(-1, 1)
    predictions = model.predict(future_days)

    print(f"\nProduct: {product}")
    for day, prediction in zip(future_days.flatten(), predictions):
        print(f"Day {day}: {prediction:.2f} units")