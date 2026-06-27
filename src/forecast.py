import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def generate_forecast(df, product, days=7):
    forecast_data = df[df["Product"] == product].copy()

    forecast_data = forecast_data.sort_values("Date")

    forecast_data["Day"] = range(1, len(forecast_data) + 1)

    forecast_data["Previous_Sales"] = forecast_data["Units_Sold"].shift(1)

    forecast_data = forecast_data.dropna()

    X = forecast_data[["Day", "Previous_Sales"]]
    y = forecast_data["Units_Sold"]

    model = LinearRegression()
    model.fit(X, y)

    predictions = []
    last_previous_sales = forecast_data["Units_Sold"].iloc[-1]
    last_day = forecast_data["Day"].iloc[-1]

    for i in range(1, days + 1):
        next_day = last_day + i

        input_data = pd.DataFrame({
            "Day": [next_day],
            "Previous_Sales": [last_previous_sales]
        })

        predicted_sales = model.predict(input_data)[0]
        predicted_sales = max(0, predicted_sales)

        predictions.append(round(predicted_sales, 2))

        last_previous_sales = predicted_sales

    forecast_df = pd.DataFrame({
        "Day": [f"Day {i}" for i in range(1, days + 1)],
        "Predicted Units Sold": predictions
    })

    return forecast_df