import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("data/sales_data.csv")

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

    plt.figure(figsize=(8, 5))
    plt.plot(product_data["Day"], product_data["Units_Sold"], marker="o", label="Actual Sales")
    plt.plot(future_days.flatten(), predictions, marker="o", label="Forecast Sales")

    plt.title(f"7-Day Sales Forecast - {product}")
    plt.xlabel("Day")
    plt.ylabel("Units Sold")
    plt.legend()
    plt.show()